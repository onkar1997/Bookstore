# importing database module
import sqlite3

# creating function to connect with database
def connect():
    conn= sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mystore(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

# function to insert data into database
def insert(title, author, year, isbn):
    conn= sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("INSERT INTO mystore VALUES(NULL,?,?,?,?)",(title, author, year, isbn))
    conn.commit()
    conn.close()

# function to delete data from database
def delete(id):
    conn= sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("DELETE FROM mystore WHERE id=?",(id,))
    conn.commit()
    conn.close()

# function to search particular data from database
def search(title="", author="", year="", isbn=""):
    conn= sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM mystore WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn))
    rows= cur.fetchall()
    conn.close()
    return rows

# function to update the data in database
def update(id, title, author, year, isbn):
    conn= sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("UPDATE mystore SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
    conn.commit()
    conn.close()

# function to view the data
def view():
    conn= sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM mystore")
    rows=cur.fetchall()
    conn.close()
    return rows

# function to clear all the data
def clearall():
    conn= sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("")
    conn.commit()
    conn.close()

# function to clear particular data
def clear():
    conn= sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("")
    conn.commit()
    conn.close()


connect()
