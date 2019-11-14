from PySide2.QtWidgets import (
    QMessageBox
)


def done(parent, title:str=None, message:str=None):
    """
    Show a popup window to notify the end of an operation

    Args:
        parent (QWidget): qt parent widget
        title (str, optional): title of the window
        message (str, optional): information message
    """

    if not title:
        title = "Terminé"
    if not message:
        message = "L'opération s'est correctement terminée"

    QMessageBox.information(
        parent,
        title,
        message,
        QMessageBox.Ok
    )
