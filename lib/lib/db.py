import sqlite3

def connect_db():
  """Connects to the SQLite database."""
  conn = sqlite3.connect('manager.db')
  return conn, conn.cursor()

def close_db(conn):
  """Closes the connection to the database."""
  conn.commit()
  conn.close()