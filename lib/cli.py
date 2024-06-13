import click
from models.model_1 import init_db, add_agent, add_property, add_client, get_properties, get_clients

@click.group()
def cli():
    pass

@cli.command()
def initdb():
    """Initialize the SQLite database."""
    init_db()
    click.echo("Database initialized successfully!")

@cli.command()
@click.option('--name', prompt='Agent Name')
@click.option('--number', prompt='Agent Number')
@click.option('--email', prompt='Agent Email')
@click.option('--phone', prompt='Agent Phone Number')
def addagent(name, number, email, phone):
    """Add a new agent to the database."""
    add_agent(name, number, email, phone)
    click.echo("Agent added successfully!")

@cli.command()
@click.option('--name', prompt='Property Name')
@click.option('--status', prompt='Property Status (sold or not sold)')
@click.option('--agent_id', prompt='Agent ID')
def addproperty(name, status, agent_id):
    """Add a new property listing to the database."""
    add_property(name, status, agent_id)
    click.echo("Property added successfully!")

@cli.command()
@click.option('--name', prompt='Client Name')
@click.option('--email', prompt='Client Email')
@click.option('--phone', prompt='Client Phone Number')
@click.option('--agent_id', prompt='Agent ID')
@click.option('--property_id', prompt='Property ID')
def addclient(name, email, phone, agent_id, property_id):
    """Add a new client to the database."""
    add_client(name, email, phone, agent_id, property_id)
    click.echo("Client added successfully!")

@cli.command()
def viewproperties():
    """View all properties with their assigned agents."""
    properties = get_properties()
    click.echo("Properties:")
    for property in properties:
        click.echo(f"Name: {property[0]}, Status: {property[1]}, Agent: {property[2]}")

@cli.command()
def viewclients():
    """View all clients with their assigned agents and properties."""
    clients = get_clients()
    click.echo("Clients:")
    for client in clients:
        click.echo(f"Name: {client[0]}, Email: {client[1]}, Phone: {client[2]}, Agent: {client[3]}, Property: {client[4]}")

if __name__ == '__main__':
    cli()
