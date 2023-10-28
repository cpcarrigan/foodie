# -*- coding: utf-8 -*-
# recipes/main.py

"""This module provides Foodie recipes application."""

import sys

from PyQt5.QtWidgets import QApplication

from .database import createConnection
from .views import Window

def main():
    """ Recipes main function."""
    # Create the application
    app = QApplication(sys.argv)
    # Connect to the database before creating any window
    if not createConnection("recipes.sqlite"):
        sys.exit(1)
    # Create the main window if the connection succeeded
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec())
