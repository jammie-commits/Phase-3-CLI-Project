
from connection import conn, cursor


class Property:

    def __init__(
        self, name, id=None, address=None, price=None, sold=None, agent_id=None
    ):
        self.id = id
        self.name = name
        self.price = price
        self.address = address
        self.sold = sold
        self.agent_id = agent_id

    def __repr__(self):
        return f"<Property {self.id} {self.name} {self.price} {self.address} {self.sold} {self.agent_id}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE properties (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price TEXT NOT NULL,
            address TEXT NOT NULL,
            sold INTEGER NOT NULL,
            agent_id INTEGER NOT NULL,
            )
        """

        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS properties;
        """

        cursor.execute(sql)
        conn.commit()

    def save(self):
        sql = """
            INSERT INTO properties (
            name, price, address, sold, agent_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            sql,
            (
                self.name,
                self.price,
                self.address,
                self.sold,
                self.agent_id,
            ),
        )
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, name, price, address, sold, agent_id):
        Property = cls(name, price, address, sold, agent_id)

        Property.save()

        return Property

    def update(self):
        sql = """
            UPDATE properties SET name = ?, phone = ?, email = ?
            WHERE id = ?
        """

        cursor.execute(
            sql,
            (
                self.name,
                self.address,
                self.price,
                self.sold,
                self.agent_id,
                self.id,
            ),
        )

        conn.commit()

    def delete(self):
        sql = """
            DELETE FROM properties
            WHERE id = ?
        """

        cursor.execute(sql, (self.id,))
        conn.commit()
