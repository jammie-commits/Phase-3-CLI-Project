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