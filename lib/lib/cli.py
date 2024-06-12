"""CLI for interacting with the database."""
import sqlite3
from db import connect_db, close_db
from models import Agent, Property
from helpers import get_user_input, get_integer_input, get_yes_no_confirmation, is_valid_name, is_valid_price, is_valid_commission_rate

# Function definitions for CRUD operations
def create_agent():
  """Creates a new agent."""
  while True:
    name = get_user_input("Enter agent name: ")
    if is_valid_name(name):
      break
    else:
      print("Error: Name can only contain letters, numbers, and spaces.")
  conn, cursor = connect_db()
  try:
    new_agent = Agent.create_agent(conn, name)
    print(f"Agent '{name}' created successfully (ID: {new_agent.id})!")
  except sqlite3.IntegrityError:
    print(f"Error: Agent with name '{name}' already exists!")
  finally:
    close_db(conn)

def delete_agent():
  """Deletes an agent."""
  agent_id = get_integer_input("Enter agent ID to delete: ")
  conn, cursor = connect_db()
  try:
    agent = Agent.get_agent_by_id(conn, agent_id)
    if not agent:
      print(f"Error: Agent with id {agent_id} not found!")
      return
    if get_yes_no_confirmation(f"Are you sure you want to delete agent '{agent.name}'?"):
      Agent.delete_agent(conn, agent_id)
      print(f"Agent (ID: {agent_id}) deleted successfully!")
  except sqlite3.Error as e:
    print(f"Error deleting agent: {e}")
  finally:
    close_db(conn)

def get_all_agents():
  """Fetches all agents."""
  conn, cursor = connect_db()
  agents = Agent.get_all_agents(conn)
  if not agents:
    print("No agents found!")
    return
  for agent in agents:
    print(f"ID: {agent.id}  Name: {agent.name}")
  close_db(conn)

def get_agent_by_id():
  """Fetches an agent by ID."""
  agent_id = get_integer_input("Enter agent ID: ")
  conn, cursor = connect_db()
  agent = Agent.get_agent_by_id(conn, agent_id)
  if not agent:
    print(f"Error: Agent with id {agent_id} not found!")
    return
  print(f"ID: {agent.id}  Name: {agent.name}")
  close_db(conn)

def create_property():
  """Creates a new property."""
  conn, cursor = connect_db()
  while True:
    address = get_user_input("Enter property address: ")
    if address:
      break
    else:
      print("Error: Please enter a valid address.")
  while True:
    try:
      price = get_integer_input("Enter property price: ", min_value=1)
      if is_valid_price(price):
        break
      else:
        print("Error: Price must be a positive integer.")
    except ValueError:
      print("Error: Please enter a valid integer.")
  while True:
    try:
      commission_rate = get_integer_input("Enter commission rate (as a percentage): ", min_value=1, max_value=100)
      if is_valid_commission_rate(commission_rate):
        break
      else:
        print("Error: Commission rate must be an integer between 1 and 100.")
    except ValueError:
      print("Error: Please enter a valid integer.")
  agent_id = get_integer_input("Enter agent ID for the property (or 0 if none): ")
  try:
    new_property = Property.create_property(conn, address, price, commission_rate, agent_id)
    print(f"Property created successfully (ID: {new_property.id})!")
  except sqlite3.IntegrityError:
    print(f"Error: Property with address '{address}' already exists!")
