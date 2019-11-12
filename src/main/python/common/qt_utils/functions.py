from PySide2.QtWidgets import (
    QListWidget, QListWidgetItem
)


def iter_list(qt_list:QListWidget) -> QListWidgetItem:
    """
    Generator to iterate through a Qt list

    Args:
        qt_list (QListWidget): the Qt list to process

    Returns:
        QListWidgetItem: Qt list item
    """

    for row in range(qt_list.count()):
        yield qt_list.item(row)


def enumer_list(qt_list:QListWidget, start:int=0) -> QListWidgetItem:
    """
    Generator to enumerate through a Qt list

    Args:
        qt_list (QListWidget): the Qt list to process
        start (int): the starting value to enumerate

    Returns:
        int: the corresponding row
        QListWidgetItem: Qt list item
    """

    for row in range(qt_list.count()):
        yield row+start, qt_list.item(row)
