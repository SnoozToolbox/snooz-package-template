"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    Yasa
    TODO CLASS DESCRIPTION
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
    TODO CLASS DESCRIPTION

    Parameters
    ----------
        raw: TODO TYPE
            TODO DESCRIPTION
        hpy: TODO TYPE
            TODO DESCRIPTION
        additional: TODO TYPE
            TODO DESCRIPTION
        

    Returns
    -------
        Accuracy: TODO TYPE
            TODO DESCRIPTION
        additional: TODO TYPE
            TODO DESCRIPTION
        
    """
    def __init__(self, **kwargs):
        """ Initialize module Yasa """
        super().__init__(**kwargs)
        if DEBUG: print('Yasa.__init__')

        # Input plugs
        InputPlug('raw',self)
        InputPlug('hpy',self)
        InputPlug('additional',self)
        

        # Output plugs
        OutputPlug('Accuracy',self)
        OutputPlug('additional',self)
        
        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self.is_done = False
        self._is_master = False

    
    def compute(self, raw,hpy,additional):
        """
        TODO DESCRIPTION

        Parameters
        ----------
            raw: TODO TYPE
                TODO DESCRIPTION
            hpy: TODO TYPE
                TODO DESCRIPTION
            additional: TODO TYPE
                TODO DESCRIPTION
 a           

        Returns
        -------
            Accuracy: TODO TYPE
                TODO DESCRIPTION
            additional: TODO TYPE
                TODO DESCRIPTION
            

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """


        # Mapping of numerical stages to string labels
        stage_mapping = {
            '0': 'WAKE',
            '1': 'N1',
            '2': 'N2',
            '3': 'N3',
            '4': 'N3',
            '5': 'REM',
            '9': 'UNS'
        }
        labels = hpy['name'].values
        labels = [stage_mapping.get(stage, 'UNKNOWN') for stage in labels]
        #labels = list(filter(lambda x: x != "UNS" and "ART", labels))
        labels = yasa.Hypnogram(labels, freq="30s")

        rawa = mne.io.read_raw_fif('sub-02_mne_raw.fif', preload=True, verbose=False)
        hyp = np.loadtxt('sub-02_hypno_30s.txt', dtype=str)
        hyp = yasa.Hypnogram(hyp, freq="30s")

        '''if len(raw) == 3:
            # Extract the names of the channels
            ch_names = [raw[0].channel, raw[1].channel, raw[2].channel]  # List of channel names
            ch_type = ['eeg', 'emg', 'eog']  # List of channel types
            sfreq = raw[0].sample_rate  # EEG sample rate
            # check if all the channels have the same sample rate!
            if raw[1].sample_rate != sfreq:
                num_samples = int(len(raw[1].samples) * sfreq / raw[1].sample_rate)
                raw[1].samples = resample(raw[1].samples, num_samples)  # Resample the other signals to the EEG sample rate
            elif raw[2].sample_rate != sfreq:
                num_samples = int(len(raw[2].samples) * sfreq / raw[2].sample_rate)
                raw[2].samples = resample(raw[2].samples, num_samples)  # Resample the other signals to the EEG sample rate
            
            data = np.array([raw[0].samples, raw[1].samples, raw[2].samples])  # Convert signals to NumPy array
            # Create MNE Info structure
            info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_type)
            # Create MNE RawArray object
            raw = mne.io.RawArray(data, info)
            # Apply YASA SleepStaging with the available channels
            sls = yasa.SleepStaging(raw, eeg_name = ch_names[0], emg_name = ch_names[1], eog_name = ch_names[2])
        
        elif len(raw) == 2:
            # Extract the names of the channels
            ch_type = []  # List of channel types
            ch_type.append('eeg')
            if "EMG" in raw[1].channel:
                ch_type.append('emg')
            elif "EOG" in raw[1].channel:
                ch_type.append('eog')
            ch_names = [raw[0].channel, raw[1].channel]  # List of channel names

            sfreq = raw[0].sample_rate  # EEG sample rate
            # check if all the channels have the same sample rate!
            if raw[1].sample_rate != sfreq:
                num_samples = int(len(raw[1].samples) * sfreq / raw[1].sample_rate)
                raw[1].samples = resample(raw[1].samples, num_samples)  # Resample the other signals to the EEG sample rate
            
            data = np.array([raw[0].samples, raw[1].samples])  # Convert signals to NumPy array
            # Create MNE Info structure
            info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_type)        
            # Create MNE RawArray object
            raw = mne.io.RawArray(data, info)
            # Apply YASA SleepStaging with the available channels
            sls = yasa.SleepStaging(raw, eeg_name = ch_names[0], emg_name = ch_names[1] if ch_type[1] == 'emg' else None, 
                                    eog_name = ch_names[1] if ch_type[1] == 'eog' else None)
            
        elif len(raw) == 1:
            # Extract the names of the channels
            ch_names = [raw[0].channel]  # List of channel names === raw.ch_names[3]
            ch_type = ['eeg']  # List of channel types
            sfreq = raw[0].sample_rate  # EEG sample rate === raw.info['sfreq']
            data = np.array([raw[0].samples])  # Convert signals to NumPy array === raw._data[3]
            # Create MNE Info structure
            info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_type)        
            # Create MNE RawArray object
            raw = mne.io.RawArray(data, info)
            # Apply YASA SleepStaging with the available channels
            sls = yasa.SleepStaging(raw, eeg_name = ch_names[0])
        else:
            raise NodeInputException(self.identifier, "raw", "The number of channels is not supported.")'''

        ch_names = [rawa.ch_names[3], rawa.ch_names[6], rawa.ch_names[8]]  # List of channel names
        ch_type = ['eeg', 'emg', 'eog']  # List of channel types
        sfreq = rawa.info['sfreq']  # EEG sample rate
        # check if all the channels have the same sample rate!
        '''if raw[1].sample_rate != sfreq:
            num_samples = int(len(raw[1].samples) * sfreq / raw[1].sample_rate)
            raw[1].samples = resample(raw[1].samples, num_samples)  # Resample the other signals to the EEG sample rate
        elif raw[2].sample_rate != sfreq:
            num_samples = int(len(raw[2].samples) * sfreq / raw[2].sample_rate)
            raw[2].samples = resample(raw[2].samples, num_samples)  # Resample the other signals to the EEG sample rate'''
        
        data = np.array([rawa._data[3], rawa._data[6], rawa._data[8]])  # Convert signals to NumPy array
        # Create MNE Info structure
        info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_type)
        # Create MNE RawArray object
        raw1 = mne.io.RawArray(data, info)
        # Apply YASA SleepStaging with the available channels
        sls = yasa.SleepStaging(raw1, eeg_name = ch_names[0], emg_name = ch_names[1], eog_name = ch_names[2])

                    # Extract the names of the channels
        '''ch_names = [rawa.ch_names[3]]  # List of channel names === raw.ch_names[3]
        ch_type = ['eeg']  # List of channel types
        sfreq = rawa.info['sfreq']  # EEG sample rate === raw.info['sfreq']
        data = np.array([rawa._data[3]])  # Convert signals to NumPy array === raw._data[3]
        # Create MNE Info structure
        info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_type)        
        # Create MNE RawArray object
        rawa = mne.io.RawArray(data, info)
        # Apply YASA SleepStaging with the available channels
        sls = yasa.SleepStaging(rawa, eeg_name = ch_names[0])'''
        
        y_pred = sls.predict()
        y_pred = yasa.Hypnogram(y_pred, freq="30s")

        '''#NOTE creating the new dataframe for the predicted labels
        # decode the lables names to the numerical values
                # Mapping of numerical stages to string labels
        stage_mapping = {
            'WAKE': '0',
            'N1': '1',
            'N2': '2',
            'N3': '3',
            'REM': '5',
            'UNS': '9'
        }
        y_pred_decod = list(y_pred.hypno)
        y_pred_decod = [stage_mapping.get(stage, '9') for stage in y_pred_decod]
        # Update the 'stage' column values in the dictionary
        j = -1
        for i, stage in enumerate(additional['group']):
            if stage == 'stage':
                j += 1
                additional['name'][i] = y_pred_decod[j]  # Change 'new_value' to the desired value
        New_additional = additional'''

        
        # Masking the values before the first wake and after the last wake 
        # NOTE: Always labels should be the first argument then y_pred
        labels_new, first_wake, last_wake = self.mask_list(list(hyp.hypno), mask_value='UNS', first_wake=None, last_wake=None, flag=True)
        y_pred_new, first_wake, last_wake = self.mask_list(list(y_pred.hypno), mask_value='UNS', first_wake=first_wake, last_wake=last_wake, flag=False)
    
        # Remove "UNS" labels and corresponding values in y_pred_new
        labels_new_filtered = []
        y_pred_new_filtered = []
        for label, pred in zip(labels_new, y_pred_new):
            if label != "UNS":
                labels_new_filtered.append(label)
                y_pred_new_filtered.append(pred)
        
        labels_new = labels_new_filtered
        y_pred_new = y_pred_new_filtered
        # Compute the agreement between the two scores
        accuracy = 100 * (pd.Series(labels_new) == pd.Series(y_pred_new)).mean()
        # Extract information from the classification report
        target_names = sorted(list(set(labels_new + y_pred_new)))
        report_dict = classification_report(labels_new, y_pred_new, target_names=target_names, output_dict=True)

        F1_WAKE = report_dict['WAKE']['f1-score']*100 if 'WAKE' in report_dict else None
        F1_N1 = report_dict['N1']['f1-score']*100 if 'N1' in report_dict else None
        F1_N2 = report_dict['N2']['f1-score']*100 if 'N2' in report_dict else None
        F1_N3 = report_dict['N3']['f1-score']*100 if 'N3' in report_dict else None
        F1_REM = report_dict['REM']['f1-score']*100 if 'REM' in report_dict else None
        
        print(f"The overall agreement is {accuracy:.2f}%")
        # Make it ready for hypnogram
        labels_new = yasa.Hypnogram(labels_new, freq="30s")
        y_pred_new = yasa.Hypnogram(y_pred_new, freq="30s")
        ###### Add confusion matrix
        #confusion_matrix = yasa.hypno_to_unique_states(hpy.hypno, y_pred.hypno)
        #print(confusion_matrix)
        # Code examples

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        # raise NodeInputException(self.identifier, "my_input", \
        #        f"Yasa this input is wrong.")

        # Raise NodeRuntimeException if there is a critical error during runtime. 
        # This will usually be a user error, a file that can't be read due to security reason,
        # a parameter that is out of bound, etc. This exception will stop and skip the current
        # process but will not stop the followin iterations if a master node is not done.
        # Once the master node is completed, a dialog will appear to show all NodeRuntimeException
        # to the user.
        #
        # Set the iteration_identifier if this module is a master node.
        # This will be used to identify the problematic iteration if a runtime exception occurs
        # in any module during this process. For example, a master node that reads one file at a 
        # could set the identifier to the name of the file.
        # self.iteration_identifier = current_filename
        #
        # Iteration count and counter are used to show a progress bar in percent.
        # Update these when creating a master node to properly show the progress 
        # for each iteration. This is optional and can be ignored but it's a good practice
        # to do for your users.
        #self.iteration_count = the total amout of iteration to make
        #self.iteration_counter = the current iteration number

        #
        # Raise the runtime exception
        # raise NodeRuntimeException(self.identifier, "files", \
        #        f"Some file could not be open.")

        #
        #

        # Write to the cache to use the data in the resultTab
        # cache = {}
        # cache['this_is_a_key'] = 42
        # self._cache_manager.write_mem_cache(self.identifier, cache)

        # Cache the results
        self.cache_signal(labels_new, y_pred_new, accuracy, sls, first_wake, last_wake)

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "Hypnogram computed.")
        self._log_manager.log(self.identifier, f"The overall agreement is {accuracy:.2f}%")
        # Create a DataFrame to store the accuracy
        df_Classification_report = pd.DataFrame({'Accuracy': [accuracy], 'F1-N1': [F1_N1], 'F1-N2': [F1_N2], 'F1-N3': [F1_N3], 'F1-REM': [F1_REM], 'F1-WAKE': [F1_WAKE]})

        return {
            'Accuracy': df_Classification_report,
            'additional': None # Replace it with New_additional
        }
    
    def cache_signal(self, labels_new, y_pred_new, accuracy, sls, first_wake, last_wake):
        """
        Cache the hypnogram.

        Parameters
        ----------
            hpy : Hypnogram
                The hypnogram to cache.
        """
        cache = {}
        cache['labels_new'] = labels_new
        cache['y_pred_new'] = y_pred_new
        cache['accuracy'] = accuracy
        cache['sls'] = sls
        cache['first_wake'] = first_wake
        cache['last_wake'] = last_wake
        self._cache_manager.write_mem_cache(self.identifier, cache)

    # Mask_list function masks elements outside the range of first and last "WAKE"
    def mask_list(self, lst, mask_value=None, first_wake=None, last_wake=None, flag=False):
        try:
            if flag:
                first_wake = lst.index("WAKE")  # Find first occurrence of "WAKE"
                last_wake = len(lst) - 1 - lst[::-1].index("WAKE")  # Find last occurrence of "WAKE"
            else:
                pass
            # Mask elements outside the range of first and last "WAKE"
            masked_list = [mask_value if i < first_wake or i > last_wake else lst[i] for i in range(len(lst))]
            return masked_list, first_wake, last_wake
    
        except ValueError:  # If "WAKE" is not in the list
            return [mask_value] * len(lst)  # Mask entire list
