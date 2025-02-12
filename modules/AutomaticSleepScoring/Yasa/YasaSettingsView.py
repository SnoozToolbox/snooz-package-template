"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    Settings viewer of the Yasa plugin
"""

from qtpy import QtWidgets

from AutomaticSleepScoring.Yasa.Ui_YasaSettingsView import Ui_YasaSettingsView
from commons.BaseSettingsView import BaseSettingsView

class YasaSettingsView(BaseSettingsView, Ui_YasaSettingsView, QtWidgets.QWidget):
    """
        YasaView set the Yasa settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._raw_topic = f'{self._parent_node.identifier}.raw'
        self._pub_sub_manager.subscribe(self, self._raw_topic)
        self._hpy_topic = f'{self._parent_node.identifier}.hpy'
        self._pub_sub_manager.subscribe(self, self._hpy_topic)
        self._additional_topic = f'{self._parent_node.identifier}.additional'
        self._pub_sub_manager.subscribe(self, self._additional_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._raw_topic, 'ping')
        self._pub_sub_manager.publish(self, self._hpy_topic, 'ping')
        self._pub_sub_manager.publish(self, self._additional_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to Yasa
        self._pub_sub_manager.publish(self, self._raw_topic, str(self.raw_lineedit.text()))
        self._pub_sub_manager.publish(self, self._hpy_topic, str(self.hpy_lineedit.text()))
        self._pub_sub_manager.publish(self, self._additional_topic, str(self.additional_lineedit.text()))
        


    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._raw_topic:
            self.raw_lineedit.setText(message)
        if topic == self._hpy_topic:
            self.hpy_lineedit.setText(message)
        if topic == self._additional_topic:
            self.additional_lineedit.setText(message)
        


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._raw_topic)
            self._pub_sub_manager.unsubscribe(self, self._hpy_topic)
            self._pub_sub_manager.unsubscribe(self, self._additional_topic)
            