import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, '../../db')
DB_PATH = os.path.join(DB_DIR, 'real_estate.db')

def get_connection():
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    c = conn.cursor()

    # Create Agents table
    c.execute('''CREATE TABLE IF NOT EXISTS Agents (
                 agent_id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 number TEXT NOT NULL,
                 email TEXT NOT NULL,
                 phone_number TEXT NOT NULL
                 )''')

    # Create Properties table
    c.execute('''CREATE TABLE IF NOT EXISTS Properties (
                 property_id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 status TEXT NOT NULL,
                 agent_id INTEGER,
                 FOREIGN KEY (agent_id) REFERENCES Agents(agent_id)
                 )''')

    # Create Clients table
    c.execute('''CREATE TABLE IF NOT EXISTS Clients (
                 client_id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 email TEXT NOT NULL,
                 phone_number TEXT NOT NULL,
                 agent_id INTEGER,
                 property_id INTEGER,
                 FOREIGN KEY (agent_id) REFERENCES Agents(agent_id),
                 FOREIGN KEY (property_id) REFERENCES Properties(property_id)
                 )''')

    conn.commit()
    conn.close()

def add_agent(name, number, email, phone):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO Agents (name, number, email, phone_number) VALUES (?, ?, ?, ?)", (name, number, email, phone))
    conn.commit()
    conn.close()

def add_property(name, status, agent_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO Properties (name, status, agent_id) VALUES (?, ?, ?)", (name, status, agent_id))
    conn.commit()
    conn.close()

def add_client(name, email, phone, agent_id, property_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO Clients (name, email, phone_number, agent_id, property_id) VALUES (?, ?, ?, ?, ?)", (name, email, phone, agent_id, property_id))
    conn.commit()
    conn.close()

def get_properties():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT Properties.name, Properties.status, Agents.name FROM Properties JOIN Agents ON Properties.agent_id = Agents.agent_id")
    properties = c.fetchall()
    conn.close()
    return properties

def get_clients():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT Clients.name, Clients.email, Clients.phone_number, Agents.name, Properties.name FROM Clients JOIN Agents ON Clients.agent_id = Agents.agent_id JOIN Properties ON Clients.property_id = Properties.property_id")
    clients = c.fetchall()
    conn.close()
    return clients
