from PySide2.QtWidgets import (
    QListWidgetItem
)

class ListWidgetItem(QListWidgetItem):
    def __init__(self, text="", data=None):
        QListWidgetItem.__init__(self, text=text)
        self.setText(text)
        self.d = data

    def set_data(self, data):
        """
        Set the attached data to the item

        Args:
            data (Any): the data to attach
        """

        self.d = data

    def get_data(self):
        """
        Return the attached data

        Returns:
            Any: the attached data
        """

        return self.d
