# -*- coding: utf-8 -*-

"""This module provides views to manage the recipes table."""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from .model import RecipeModel


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Recipes")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.recipeModel = RecipeModel()

        self.setupUI()

    def setupUI(self):
        """Setup the main window's GUI."""
        # Create the table view widget
        self.table = QTableView()
        self.table.setModel(self.recipeModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        # Create buttons
        self.addButton = QPushButton("Add...")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete")
        self.deleteButton.clicked.connect(self.deleteRecipe)
        self.viewButton = QPushButton("View")
        self.clearAllButton = QPushButton("Clear All")
        self.clearAllButton.clicked.connect(self.clearRecipes)
        # Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def clearRecipes(self):
        """Remove all recipes from the database."""
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove all your recipes?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.recipeModel.clearRecipes()

    def deleteRecipe(self):
        """Delete the selected contact from the database."""
        row = self.table.currentIndex().row()
        if row < 0:
            return

        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove the selected recipe?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.recipeModel.deleteRecipe(row)

    def openAddDialog(self):
        """Open the Add Recipe dialog."""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.recipeModel.addRecipe(dialog.data)
            self.table.resizeColumnsToContents()

class AddDialog(QDialog):
    """Add Recipe dialog."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent=parent)
        self.setWindowTitle("Add Recipe")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        """Setup the Add Recipe dialog's GUI."""
        # Create line edits for data fields
        # headers = ("ID", "Name", "Author", "Date", "Ingredients", "Directions","Source")
        self.nameField = QLineEdit()
        self.nameField.setObjectName("Name")
        self.authorField = QLineEdit()
        self.authorField.setObjectName("author")
        self.dateField = QLineEdit()
        self.dateField.setObjectName("Date")
        self.ingredientsField = QLineEdit()
        self.ingredientsField.setObjectName("Ingredients")
        self.directionsField = QLineEdit()
        self.directionsField.setObjectName("Directions")
        self.sourceField = QLineEdit()
        self.sourceField.setObjectName("Source")
        # Lay out the data fields
        layout = QFormLayout()
        layout.addRow("Name:", self.nameField)
        layout.addRow("Author:", self.authorField)
        layout.addRow("Date:", self.dateField)
        layout.addRow("Ingredients:", self.ingredientsField)
        layout.addRow("Directions:", self.directionsField)
        layout.addRow("Source:", self.sourceField)
        self.layout.addLayout(layout)
        # Add standard buttons to the dialog and connect them
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)
    
    def accept(self):
        """Accept the data provided through the dialog."""
        self.data = []
        for field in (self.nameField, self.authorField, self.dateField, self.ingredientsField, self.directionsField, self.sourceField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a recipes's {field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            self.data.append(field.text())

        super().accept()
    
    def openAddDialog(self):
        """Open the Add Recipe dialog."""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.recipeModel.addRecipe(dialog.data)
            self.table.resizeColumnsToContents()