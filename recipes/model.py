# -*- coding: utf-8 -*-
# recipes/model.py

"""This module provides a model to manage the recipe table."""

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class RecipeModel:
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

    def addRecipe(self, data):
        """Add a recipe to the database."""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column + 1), field)
        self.model.submitAll()
        self.model.select()
    
    def viewRecipe(self, row):
        """View a recipe from the database."""
        self.model.fetchMore(row)
        self.model.submitAll()
        self.model.select()
    
    def deleteRecipe(self, row):
        """Remove a recipe from the database."""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()
    
    def clearRecipes(self):
        """Remove all recipes in the database."""
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()