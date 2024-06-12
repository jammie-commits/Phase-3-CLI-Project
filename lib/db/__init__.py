import sqlite3

def connect_db():
  
  conn = sqlite3.connect('manager.db')
  return conn, conn.cursor()

def close_db(conn):

  conn.commit()
  conn.close()
