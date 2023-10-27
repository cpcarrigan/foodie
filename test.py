import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# Create the connection
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("recipe.sqlite3")

# Open the connection
if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)

# Create a query and execute it right away using .exec()
createTableQuery = QSqlQuery()
createTableQuery.exec(
    """
    CREATE TABLE recipe (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        title VARCHAR(40) NOT NULL,
        ingredients VARCHAR(50),
        instructions VARCHAR(50),
        author VARCHAR(50),
        source VARCHAR(40) NOT NULL
    )
    """
)

print(con.tables())
