"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    ResultSummary
    TODO CLASS DESCRIPTION
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import pandas as pd
import os

DEBUG = False

class ResultSummary(SciNode):
    """
    TODO CLASS DESCRIPTION

    Parameters
    ----------
        ResultsDataframe: TODO TYPE
            TODO DESCRIPTION
        Additional: TODO TYPE
            TODO DESCRIPTION

    Returns
    -------
        ExportResults: TODO TYPE
            TODO DESCRIPTION
    """
    def __init__(self, **kwargs):
        """ Initialize module ResultSummary """
        super().__init__(**kwargs)
        if DEBUG: print('ResultSummary.__init__')

        # Input plugs
        InputPlug('ResultsDataframe', self)
        InputPlug('Additional', self)

        # Output plugs
        OutputPlug('ExportResults', self)

        # A master module allows the process to be reexcuted multiple times.
        # For example, this is useful when the process must be repeated over multiple
        # files. When the master module is done, i.e., when all the files were processed,
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False
        self.AccuracyList = []

    def compute(self, ResultsDataframe, Additional):
        """
        TODO DESCRIPTION

        Parameters
        ----------
            ResultsDataframe: TODO TYPE
                TODO DESCRIPTION
            Additional: TODO TYPE
                TODO DESCRIPTION

        Returns
        -------
            ExportResults: TODO TYPE
                TODO DESCRIPTION

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        # Define file path
        export_results_file_path = 'D:/CEAMS/snooz_workspace/ExportResults.xlsx' # You need to change this path to your own path

        # Check if file exists, if not create it with headers
        if not os.path.exists(export_results_file_path):
            pd.DataFrame().to_excel(export_results_file_path, index=False)

        # Load existing data
        try:
            export_results_df = pd.read_excel(export_results_file_path)
        except pd.errors.EmptyDataError:
            export_results_df = pd.DataFrame()

        # Append new data
        export_results_df = pd.concat([export_results_df, ResultsDataframe], ignore_index=True)

        # Save updated data back to excel file
        export_results_df.to_excel(export_results_file_path, index=False)

        # Return the path to the updated Excel file
        return {
            'ExportResults': export_results_file_path
        }
