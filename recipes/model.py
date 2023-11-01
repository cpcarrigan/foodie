# -*- coding: utf-8 -*-
# recipes/model.py

"""This module provides a model to manage the recipe table."""

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class ContactsModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        """Create and set up the model."""
        tableModel = QSqlTableModel()
        tableModel.setTable("recipes")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID", "Name", "Author", "Date", "Ingredients", "Directions","Source")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel