#2. Connecting to SQLite in Python
#SQLite is a lightweight database stored in a single file. Python includes the sqlite3 library, so no separate installation is normally needed.
import sqlite3

# Connect to a database file (creates it if it does not exist)
connection = sqlite3.connect("company.db")

# Create a cursor to execute SQL commands
cursor = connection.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
""")

# Save the changes permanently
connection.commit()

# Close the connection
connection.close()

#Key steps:
#- sqlite3.connect("company.db"): Opens a connection to the database. If the database file does not exist, SQLite creates it.
#- connection.cursor(): Creates a cursor object, which is used to execute SQL commands such as CREATE, INSERT, SELECT, and DELETE.
#- cursor.execute(): Runs an SQL statement.
#- connection.commit(): Permanently saves changes made to the database. It is especially important after inserting, updating, or deleting records.
#- connection.close(): Closes the database safely when the program is finished.

