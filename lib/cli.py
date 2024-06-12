import click
from db import connect_db, close_db
from models import Agent, Property

# Helper functions for CRUD operations
def create_agent(name):
  conn, cursor = connect_db()
  try:
    new_agent = Agent.create_agent(conn, name)
    close_db(conn)
    return new_agent    