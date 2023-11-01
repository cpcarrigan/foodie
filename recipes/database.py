# -*- coding: utf-8 -*-
# recipes/database.py

"""This module provides a database connection."""

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def _createRecipesTable():
    """Create the recipes table in the database."""
    createTableQuery = QSqlQuery()
    # other tables to create?
    # tags / tag_recipe_mapping / source table
    # https://stackoverflow.com/questions/51128832/what-is-the-best-way-to-design-a-tag-based-data-table-with-sqlite

    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            author VARCHAR(50),
            date VARCHAR(50),
            ingredients VARCHAR(50),
            directions VARCHAR(50),
            source VARCHAR(50)
        )
        """
    )
def _createTagTable():
    """Create the tag table in the database."""
    createTagQuery = QSqlQuery()

    return createTagQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS tag_table (id INTEGER PRIMARY KEY, tag_name)
        """
    )

def _createRecipeTagTable():
    """Create the join table between recipe and tags in the database."""
    createRecipeTagQuery = QSqlQuery()

    return createRecipeTagQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS recipe_tag_mapping (recipe_reference INTEGER, tag_reference INTEGER);
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
    _createTagTable()
    _createRecipeTagTable()
    return True
