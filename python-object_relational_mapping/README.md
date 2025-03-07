🐍 Python Object-Relational Mapping (ORM) Project 🗄️
<div align="center"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL"> <img src="https://img.shields.io/badge/SQLAlchemy-FF4500?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy"> </div>
📋 Table of Contents
Project Overview
Prerequisites
Installation
Project Structure
File Descriptions
Usage Examples
Learning Objectives
Resources
🔍 Project Overview
This project bridges the gap between Python programming and database operations through Object-Relational Mapping. It demonstrates two ways to interact with a MySQL database:

Direct Database Access: Using the MySQLdb module to connect to MySQL and execute raw SQL queries
ORM Approach: Using SQLAlchemy ORM to abstract database operations into Python objects
ORM allows developers to interact with databases using object-oriented paradigms, making the code more maintainable and database-agnostic.

🛠️ Prerequisites
Python 3.8+
MySQL 5.7+
MySQLdb module
SQLAlchemy
A MySQL server running with appropriate permissions
💻 Installation
Clone the repository:
```markdown
git clone https://github.com/your-username/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/python-object_relational_mapping
```
Set up a virtual environment:
```markdown
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
Install the required packages:
```markdown
pip install mysqlclient SQLAlchemy
```
Set up the database:
```markdown
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
-- Add sample data as needed
```
📁 Project Structure
```markdown
python-object_relational_mapping/
├── 0-select_states.py           # Lists all states from database
├── 1-filter_states.py           # Lists states starting with 'N'
├── 2-my_filter_states.py        # Filter states by user input
├── 3-my_safe_filter_states.py   # SQL Injection-safe filtering
├── 4-cities_by_state.py         # Lists all cities by state
├── 5-filter_cities.py           # Filter cities by state name
├── 7-model_state_fetch_all.py   # Lists all State objects
├── 8-model_state_fetch_first.py # Prints the first State object
├── 9-model_state_filter_a.py    # Lists all State objects with letter 'a'
├── 10-model_state_my_get.py     # Gets a State object by name
├── 11-model_state_insert.py     # Adds a new State object
├── 12-model_state_update_id_2.py # Updates a State object
├── 13-model_state_delete_a.py   # Deletes State objects with letter 'a'
├── 14-model_city_fetch_by_state.py # Lists all City objects by State
├── model_state.py               # State class definition
├── model_city.py                # City class definition
├── README.md                    # Project documentation
└── env/                         # Virtual environment directory
```

📝 File Descriptions
Direct MySQL Scripts
0-select_states.py: Lists all states from the database
1-filter_states.py: Lists states starting with 'N'
2-my_filter_states.py: Filters states based on user input
3-my_safe_filter_states.py: Prevents SQL injection
4-cities_by_state.py: Lists all cities with their state names
5-filter_cities.py: Lists all cities of a specified state
SQLAlchemy ORM Scripts
model_state.py: Defines the State class mapping to states table
model_city.py: Defines the City class mapping to cities table
7-model_state_fetch_all.py: Lists all State objects
8-model_state_fetch_first.py: Prints the first State object
9-model_state_filter_a.py: Lists State objects containing letter 'a'
10-model_state_my_get.py: Prints State ID by name
11-model_state_insert.py: Adds a new State object
12-model_state_update_id_2.py: Updates a State object
13-model_state_delete_a.py: Deletes States containing letter 'a'
14-model_city_fetch_by_state.py: Lists all City objects by State
🚀 Usage Examples
Using MySQLdb
```markdown
# Example from 0-select_states.py
#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
```
Using SQLAlchemy
```markdown
# Example from 7-model_state_fetch_all.py
#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    
    session.close()
```
📚 Learning Objectives
Connect to a MySQL database from a Python script
Execute SELECT queries on a MySQL database from Python
Understand SQL injection and implement secure queries
Create and utilize a SQLAlchemy ORM
Map Python classes to MySQL tables using SQLAlchemy
Perform CRUD operations using SQLAlchemy
