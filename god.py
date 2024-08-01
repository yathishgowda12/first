import sqlite3

# Connect to the database
conn = sqlite3.connect ('example.db')

# Create a cursor object
cursor = conn.cursor()

# Execute SQL commands
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
cursor.execute("INSERT INTO users (name, email) VALUES ('John Doe', 'john.doe@example.com')")
cursor.execute("SELECT * FROM users")

# Fetch the results
results = cursor.fetchall()
for row in results:
    print(row)

# Commit the changes and close the connection
conn.commit()
conn.close()
