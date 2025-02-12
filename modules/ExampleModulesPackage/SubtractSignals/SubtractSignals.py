"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    SubtractSignals
    TODO CLASS DESCRIPTION
"""
import numpy as np
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

class SubtractSignals(SciNode):
    """
    TODO CLASS DESCRIPTION

    Parameters
    ----------
        main_signal: TODO TYPE
            TODO DESCRIPTION
        signal_to_subtract: TODO TYPE
            TODO DESCRIPTION
        

    Returns
    -------
        signal: TODO TYPE
            TODO DESCRIPTION
        
    """
    def __init__(self, **kwargs):
        """ Initialize module SubtractSignals """
        super().__init__(**kwargs)
        if DEBUG: print('SubtractSignals.__init__')

        # Input plugs
        InputPlug('main_signal',self)
        InputPlug('signal_to_subtract',self)
        

        # Output plugs
        OutputPlug('signal',self)
        

        # Init module variables
        self.this_is_an_example_you_can_delete_it = 0

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, main_signal,signal_to_substract):
        # Make appropriate checks to input values
        if not isinstance(main_signal, dict):
                raise NodeInputException(self.identifier, "main_signal", "main_signal must be a dictionary")
        if not isinstance(signal_to_substract, dict):
                raise NodeInputException(self.identifier, "signal_to_substract", "signal_to_substract must be a dictionary")

        if 'samples' not in main_signal or 'samples' not in signal_to_substract:
                raise NodeInputException(self.identifier, "samples", "main_signal and signal_to_substract must contain 'samples' key")

        if 'sample_rate' not in main_signal or 'sample_rate' not in signal_to_substract:
                raise NodeInputException(self.identifier, "sample_rate", "main_signal and signal_to_substract must contain 'sample_rate' key")

        if main_signal['sample_rate'] != signal_to_substract['sample_rate']:
                raise NodeInputException(self.identifier, "sample_rate", "Sample rates of both signals must be the same.")

        # Determine the lengths of the signal samples
        len_main_signal = len(main_signal['samples'])
        len_signal_to_substract = len(signal_to_substract['samples'])

        # Extend the shorter signal with zeros
        if len_main_signal < len_signal_to_substract:
                main_signal['samples'] = np.pad(main_signal['samples'], (0, len_signal_to_substract - len_main_signal), 'constant')
        elif len_signal_to_substract < len_main_signal:
                signal_to_substract['samples'] = np.pad(signal_to_substract['samples'], (0, len_main_signal - len_signal_to_substract), 'constant')

        # Perform the addition of the signals
        result_samples = main_signal['samples'] - signal_to_substract['samples']

        # Create the output signal dictionary
        output_signal = {
                'samples': result_samples,
                "sample_rate":main_signal['sample_rate']
        }

        return {'signal': output_signal}

