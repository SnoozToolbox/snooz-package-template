"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    Yasa
    This class performs automatic sleep scoring using the YASA package.
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

import mne
import yasa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import resample
from sklearn.metrics import classification_report, confusion_matrix

DEBUG = False

class Yasa(SciNode):
    """
    This class performs automatic sleep scoring using the YASA package.

    Parameters
    ----------
    raw: list
        List of raw signal objects.
    hpy: DataFrame
        Hypnogram data.
    additional: dict
        Additional parameters.

    Returns
    -------
    dict
        Dictionary containing accuracy and additional information.
    """
    def __init__(self, **kwargs):
        """ Initialize module Yasa """
        super().__init__(**kwargs)
        if DEBUG: print('Yasa.__init__')

        # Input plugs
        InputPlug('raw', self)
        InputPlug('hpy', self)
        InputPlug('additional', self)

        # Output plugs
        OutputPlug('Accuracy', self)
        OutputPlug('additional', self)

        self.is_done = False
        self._is_master = False

    def compute(self, raw, hpy, additional):
        """
        Perform sleep scoring.

        Parameters
        ----------
        raw: list
            List of raw signal objects.
        hpy: DataFrame
            Hypnogram data.
        additional: dict
            Additional parameters.

        Returns
        -------
        dict
            Dictionary containing accuracy and additional information.

        Raises
        ------
        NodeInputException
            If any of the input parameters have invalid types or missing keys.
        NodeRuntimeException
            If an error occurs during the execution of the function.
        """
        # Mapping of sleep stages
        stage_mapping = {
            '0': 'WAKE',
            '1': 'N1',
            '2': 'N2',
            '3': 'N3',
            '4': 'N3',
            '5': 'REM',
            '9': 'UNS'
        }
        # Map stages to be compatible with Snooz staging
        labels = hpy['name'].values
        labels = [stage_mapping.get(stage, 'UNKNOWN') for stage in labels]
        labels = yasa.Hypnogram(labels, freq="30s")

        # Prepare raw data for sleep staging
        raw = self.prepare_raw_data(raw)
        # Apply sleep staging
        sls = self.apply_sleep_staging(raw)

        # Predict sleep stages
        y_pred = sls.predict()
        y_pred = yasa.Hypnogram(y_pred, freq="30s")

        # Mask unwanted stages
        labels_new, first_wake, last_wake = self.mask_list(list(labels.hypno), mask_value='UNS', flag=True)
        y_pred_new, _, _ = self.mask_list(list(y_pred.hypno), mask_value='UNS', first_wake=first_wake, last_wake=last_wake, flag=False)

        # Filter out "UNS" stages
        labels_new, y_pred_new = self.filter_uns(labels_new, y_pred_new)

        # Calculate accuracy
        accuracy = 100 * (pd.Series(labels_new) == pd.Series(y_pred_new)).mean()
        report_dict = classification_report(labels_new, y_pred_new, output_dict=True)

        # Calculate F1 scores for each stage
        F1_scores = {stage: report_dict[stage]['f1-score']*100 if stage in report_dict else None for stage in ['WAKE', 'N1', 'N2', 'N3', 'REM']}

        print(f"The overall agreement is {accuracy:.2f}%")

        # Convert lists back to Hypnogram objects
        labels_new = yasa.Hypnogram(labels_new, freq="30s")
        y_pred_new = yasa.Hypnogram(y_pred_new, freq="30s")

        # Cache the results
        self.cache_signal(labels_new, y_pred_new, accuracy, sls, first_wake, last_wake)

        # Log the results
        self._log_manager.log(self.identifier, "Hypnogram computed.")
        self._log_manager.log(self.identifier, f"The overall agreement is {accuracy:.2f}%")

        # Create a DataFrame for the classification report
        df_Classification_report = pd.DataFrame({'Accuracy': [accuracy], **{f'F1-{stage}': [F1_scores[stage]] for stage in F1_scores}})

        return {
            'Accuracy': df_Classification_report,
            'additional': None
        }

    def prepare_raw_data(self, raw):
        """
        Prepare raw data for sleep staging.

        Parameters
        ----------
        raw: list
            List of raw signal objects.

        Returns
        -------
        RawArray
            Prepared raw data.
        """
        # Check the number of channels as input
        if len(raw) == 3:
            raw = self.sort_and_resample(raw, ['EEG', 'EOG', 'EMG'])
            ch_names = [raw[0].channel, raw[1].channel, raw[2].channel]
            ch_type = ['eeg', 'eog', 'emg']
        elif len(raw) == 2:
            raw = self.sort_and_resample(raw, ['EEG', 'EOG', 'EMG'])
            ch_names = [raw[0].channel, raw[1].channel]
            ch_type = ['eeg', 'emg' if 'EMG' in raw[1].channel else 'eog']
        elif len(raw) == 1:
            ch_names = [raw[0].channel]
            ch_type = ['eeg']
        else:
            raise NodeInputException(self.identifier, "raw", "The number of channels is not supported.")

        # Create MNE RawArray object
        sfreq = raw[0].sample_rate
        data = np.array([r.samples for r in raw])
        info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_type)
        return mne.io.RawArray(data, info)

    def sort_and_resample(self, raw, channel_order):
        """
        Sort and resample raw data.

        Parameters
        ----------
        raw: list
            List of raw signal objects.
        channel_order: list
            List of channel types in order.

        Returns
        -------
        list
            Sorted and resampled raw data.
        """
        # Order the channels from EEG, EOG, EMG
        channel_order = {ch: i for i, ch in enumerate(channel_order)}
        raw = sorted(raw, key=lambda x: channel_order.get(x.channel[:3].upper(), len(channel_order)))
        # Resample the signals if the sampling frequency is different
        sfreq = raw[0].sample_rate
        for r in raw[1:]:
            if r.sample_rate != sfreq:
                num_samples = int(len(r.samples) * sfreq / r.sample_rate)
                r.samples = resample(r.samples, num_samples)
        return raw

    def apply_sleep_staging(self, raw):
        """
        Apply sleep staging using YASA.

        Parameters
        ----------
        raw: RawArray
            Prepared raw data.

        Returns
        -------
        SleepStaging
            YASA SleepStaging object.
        """
        ch_names = raw.ch_names
        ch_types = raw.get_channel_types()
        if len(ch_names) == 3:
            return yasa.SleepStaging(raw, eeg_name=ch_names[0], eog_name=ch_names[1], emg_name=ch_names[2])
        else:
            return yasa.SleepStaging(raw, eeg_name=ch_names[0], eog_name=ch_names[1] if 'eog' in ch_types else None, emg_name=ch_names[1] if 'emg' in ch_types else None)

    def cache_signal(self, labels_new, y_pred_new, accuracy, sls, first_wake, last_wake):
        """
        Cache the hypnogram.

        Parameters
        ----------
        labels_new : Hypnogram
            The new labels hypnogram.
        y_pred_new : Hypnogram
            The predicted labels hypnogram.
        accuracy : float
            The accuracy of the prediction.
        sls : SleepStaging
            The YASA SleepStaging object.
        first_wake : int
            Index of the first wake.
        last_wake : int
            Index of the last wake.
        """
        cache = {
            'labels_new': labels_new,
            'y_pred_new': y_pred_new,
            'accuracy': accuracy,
            'sls': sls,
            'first_wake': first_wake,
            'last_wake': last_wake
        }
        self._cache_manager.write_mem_cache(self.identifier, cache)

    def mask_list(self, lst, mask_value=None, first_wake=None, last_wake=None, flag=False):
        """
        Mask elements outside the range of first and last "WAKE".

        Parameters
        ----------
        lst : list
            List to be masked.
        mask_value : any
            Value to mask with.
        first_wake : int
            Index of the first wake.
        last_wake : int
            Index of the last wake.
        flag : bool
            Flag to indicate if first and last wake should be found.

        Returns
        -------
        tuple
            Masked list, first wake index, last wake index.
        """
        try:
            if flag:
                first_wake = lst.index("WAKE")
                last_wake = len(lst) - 1 - lst[::-1].index("WAKE")
            masked_list = [mask_value if i < first_wake or i > last_wake else lst[i] for i in range(len(lst))]
            return masked_list, first_wake, last_wake
        except ValueError:
            return [mask_value] * len(lst), None, None

    def filter_uns(self, labels, preds):
        """
        Filter out "UNS" labels and corresponding predictions.

        Parameters
        ----------
        labels : list
            List of labels.
        preds : list
            List of predictions.

        Returns
        -------
        tuple
            Filtered labels and predictions.
        """
        filtered_labels = []
        filtered_preds = []
        for label, pred in zip(labels, preds):
            if label != "UNS":
                filtered_labels.append(label)
                filtered_preds.append(pred)
        return filtered_labels, filtered_preds
