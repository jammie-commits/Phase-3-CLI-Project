# Real_Estate_Management
### Project By James Mbugua
### Date 13 June 2024

## Introduction
This project is a command-line interface (CLI) tool designed for managing real estate data. It utilizes SQLite as its database backend and provides functionalities to add agents, properties, and clients, as well as view existing properties and clients with their associated details.
## Key Features
Database Management: Initialize and maintain a SQLite database (real_estate.db) that stores information about agents, properties, and clients.
Agent Management: Add new agents to the database with details such as name, contact number, email, and phone number.
Property Management: Add new property listings with status (sold or not sold) and assign them to specific agents.
Client Management: Register clients who have bought or booked properties, linking them to both the agent responsible and the property involved.
View Operations: Retrieve and display all properties along with their assigned agents, as well as list all clients with their associated agents and properties.
## Project Structure
phase-3-project/ 
├── Pipfile 
├── Pipfile.lock 
├── README.md 
└── lib 
├── models │ 
├── __init__.py │ 
└── model_1.py 
├── cli.py 
├── config.py 
├── debug.py 
└── helpers.py 
├── db # Database directory (will be created)

## Installation and Usage
Installation: Clone the repository, install dependencies using Pipenv, and initialize the database.
Usage: Utilize the CLI commands provided (addagent, addproperty, addclient, viewproperties, viewclients) to manage agents, properties, and clients efficiently from the command line.

## Commands
Add agent: pipenv run python lib/cli.py addagent
Add property: pipenv run python lib/cli.py addagent
Add client: pipenv run python lib/cli.py addclient
View properties: pipenv run python lib/cli.py viewproperties
View clients: pipenv run python lib/cli.py viewclients

## Purpose
This tool simplifies real estate management tasks by providing a streamlined interface to handle agent details, property listings, client registrations, and data retrieval, all within a SQLite database environment. It is suitable for real estate agencies or professionals looking for a straightforward solution to manage their operations digitally.
##Technologies used
-Python
-Sql-lite
