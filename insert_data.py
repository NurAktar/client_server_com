import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database.db')

# Create a cursor object
cursor = conn.cursor()

# SQL command to insert data
sql_command = """
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    percentage REAL,
    locality TEXT,
    roll_no INTEGER);
"""
# Execute the SQL command
cursor.execute(sql_command)
sql_command = """
INSERT INTO students (name, percentage, locality, roll_no) VALUES
    ('John Doe', 85.5, 'City1', 101),
    ('Jane Smith', 92.3, 'City2', 102),
    ('Bob Johnson', 78.9, 'City3', 103);
"""
cursor.execute(sql_command)
# Commit the changes
conn.commit()

# Close the connection
conn.close()
