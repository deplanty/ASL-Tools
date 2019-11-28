from PySide2.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QTreeWidget,
    QTreeWidgetItem
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


def iter_tree(qt_tree:QTreeWidget) -> QTreeWidgetItem:
    """
    Generator to iterate through the toplevel items in a Qt tree widget

    Args:
        qt_tree (QTreeWidget): the Qt tree to process

    Returns:
        QTreeWidgetItem: Qt tree toplevel item
    """

    for row in range(qt_tree.topLevelItemCount()):
        yield qt_tree.topLevelItem(row)


def iter_treeitem(qt_item:QTreeWidgetItem) -> QTreeWidgetItem:
    """
    Generator to iterate through the children of an item in a Qt tree widget

    Args:
        qt_item (QTreeWidgetItem): the Qt tree item

    Returns:
        QTreeWidgetItem: Qt tree child item
    """

    for row in range(qt_item.childCount()):
        yield qt_item.child(row)
