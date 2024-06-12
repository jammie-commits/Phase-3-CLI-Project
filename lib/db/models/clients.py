from connection import conn, cursor

class Client:
  def __init__(self, id, name, email, phone, property):
    self.id = id
    self.name = name
    self.email = email
    self.phone = phone
    self.property = property

@classmethod
def create_client(cls, conn, name, email, phone, property):
  """Creates a new client in the database."""
  cursor = conn.cursor()
  cursor.execute("INSERT INTO clients (name, email, phone, property) VALUES (?, ?, ?, ?)", (name, email, phone, property))
  conn.commit()
  return cls(cursor.lastrowid, name, email, phone, property)

@classmethod
def get_all_clients(cls, conn):
  """Fetches all clients from the database."""
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM clients")
  return [cls(*row) for row in cursor.fetchall()]

@classmethod
def get_client_by_id(cls, conn, client_id):
  """Fetches a client by their ID."""
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
  return cls(*cursor.fetchone()) if cursor.fetchone() else None

@classmethod
def delete_client(cls, conn, client_id):
  """Deletes a client from the database."""
  cursor = conn.cursor()
  cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
  conn.commit()