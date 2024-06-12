
from connection import conn, cursor


class Agent:

    def __init__(
        self, name, phone, email, id=None
    ):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"<Student {self.id} {self.name} {self.phone} {self.email}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE agents (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
          
            phone TEXT NOT NULL,
            
            email TEXT
            )
        """

        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS agents;
        """

        cursor.execute(sql)
        conn.commit()

    def save(self):
        sql = """
            INSERT INTO agents (
            name, phone, email
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            sql,
            (
                self.name,
                
                self.phone,
                
                self.email,
            ),
        )
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, name, phone, email):
        agent = cls(name, phone, email)

        agent.save()

        return agent

    def update(self):
        sql = """
            UPDATE agents SET name = ?, phone = ?, email = ?
            WHERE id = ?
        """

        cursor.execute(
            sql,
            (
                self.name,
                
                self.phone,
                
                self.email,
                self.id,
            ),
        )

        conn.commit()

    def delete(self):
        sql = """
            DELETE FROM agents
            WHERE id = ?
        """

        cursor.execute(sql, (self.id,))
        conn.commit()
