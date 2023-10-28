# -*- coding: utf-8 -*-
# recipes/database.py

"""This module provides a database connection."""

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuerq


def _createRecipesTable():
    """Create the recipes table in the database."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            author VARCHAR(50),
            quantity VARCHAR(50),
            source VARCHAR(50),
            instructions VARCHAR(50)
        )
        """
    )


def createConnection(databaseName):
    """Create and open a database connection."""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "Foodie Recipes",
            f"Database Error: {connection.lastError().text()}",
        )
        return False

    _createRecipesTable()
    return True
