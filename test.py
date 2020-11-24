import sqlite3 

parts_table = sqlite3.connect('final_parts_table.db')

# Create a cursor 
c = parts_table.cursor() 

#c.execute("SELECT rowid, * FROM data")

# Get the columns name
c.execute("SELECT name FROM PRAGMA_TABLE_INFO('data')")
items = c.fetchall()
print(items)