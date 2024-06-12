class Agent:
  def __init__(self, id, name):
    self.id = id
    self.name = name

  @classmethod
  def create_agent(cls, conn, name):
    """Creates a new agent in the database."""
    cursor = conn.cursor()
    cursor.execute("INSERT INTO agents (name) VALUES (?)", (name,))
    conn.commit()
    return cls(cursor.lastrowid, name)

  @classmethod
  def get_all_agents(cls, conn):
    """Fetches all agents from the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agents")
    return [cls(*row) for row in cursor.fetchall()]

  @classmethod
  def get_agent_by_id(cls, conn, agent_id):
    """Fetches an agent by their ID."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agents WHERE id = ?", (agent_id,))
    return cls(*cursor.fetchone()) if cursor.fetchone() else None

  @classmethod
  def delete_agent(cls, conn, agent_id):
    """Deletes an agent from the database."""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM agents WHERE id = ?", (agent_id,))
    conn.commit()

class Property:
  def __init__(self, id, address, price, commission_rate, sold, agent_id):
    self.id = id
    self.address = address
    self.price = price
    self.commission_rate = commission_rate
    self.sold = sold
    self.agent_id = agent_id

  @classmethod
  def create_property(cls, conn, address, price, commission_rate, sold, agent_id):
    """Creates a new property in the database."""
    cursor = conn.cursor()
    cursor.execute("INSERT INTO properties (address, price, commission_rate, sold, agent_id) VALUES (?, ?, ?, ?, ?)", 
                  (address, price, commission_rate, sold, agent_id))
    conn.commit()
    return cls(cursor.lastrowid, address, price, commission_rate, sold, agent_id)

  @classmethod
  def get_all_properties(cls, conn):
    """Fetches all properties from the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM properties")
    return [cls(*row) for row in cursor.fetchall()]

  @classmethod
  def get_property_by_id(cls, conn, property_id):
    """Fetches a property by its ID."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM properties WHERE id = ?", (property_id,))
    return cls(*cursor.fetchone()) if cursor.fetchone() else None

  @classmethod
  def delete_property(cls, conn, property_id):
    """Deletes a property from the database."""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM properties WHERE id = ?", (property_id,))
    conn.commit()
