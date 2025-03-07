🐍 Python Object-Relational Mapping (ORM) Project 🗄️
<div align="center"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL"> <img src="https://img.shields.io/badge/SQLAlchemy-FF4500?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy"> </div>
📋 Table of Contents
🔍 Project Overview
🛠️ Prerequisites
💻 Installation
📁 Project Structure
📊 Exercise Reviews
Direct MySQL Scripts
SQLAlchemy ORM Scripts
🚀 Usage Examples
📚 Learning Objectives
🔗 Resources
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
1. Clone the repository:
```bash
git clone https://github.com/your-username/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/python-object_relational_mapping
```
2. Set up a virtual environment:
```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
3. Install the required packages:
```bash
pip install mysqlclient SQLAlchemy
```
4. Set up the database:
```sql
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

📊 Exercise Reviews
Direct MySQL Scripts
0️⃣ 0-select_states.py
Description: This script connects to a MySQL database and lists all states in the states table ordered by ID.
Skills demonstrated: Basic database connection, cursor handling, query execution.
Usage: ./0-select_states.py username password database
1️⃣ 1-filter_states.py
Description: Lists all states whose name starts with 'N' (case sensitive).
Skills demonstrated: SQL filtering with LIKE clause, result processing.
Usage: ./1-filter_states.py username password database
2️⃣ 2-my_filter_states.py
Description: Takes a state name as argument and displays all matching states.
Skills demonstrated: User input handling, string formatting in SQL queries.
Usage: ./2-my_filter_states.py username password database state_name
Security issue: ⚠️ Vulnerable to SQL injection.
3️⃣ 3-my_safe_filter_states.py
Description: Same as script 2 but safe from SQL injection.
Skills demonstrated: Parameterized queries, secure database access.
Usage: ./3-my_safe_filter_states.py username password database state_name
4️⃣ 4-cities_by_state.py
Description: Lists all cities from the cities table with their corresponding state names using JOIN.
Skills demonstrated: JOIN operations, working with multiple tables.
Usage: ./4-cities_by_state.py username password database
5️⃣ 5-filter_cities.py
Description: Lists all cities of a given state using SQL JOIN and safe parameterized queries.
Skills demonstrated: JOIN operations, result formatting, parameterized queries.
Usage: ./5-filter_cities.py username password database state_name
SQLAlchemy ORM Scripts
🗃️ model_state.py
Description: Defines the State class that maps to the states table using SQLAlchemy ORM.
Skills demonstrated: ORM class definition, table mapping, SQLAlchemy declarative base.
🏙️ model_city.py
Description: Defines the City class that maps to the cities table using SQLAlchemy ORM.
Skills demonstrated: ORM class definition, foreign key relationships.
7️⃣ 7-model_state_fetch_all.py
Description: Lists all State objects from the database using SQLAlchemy ORM.
Skills demonstrated: SQLAlchemy engine and session creation, basic queries.
Usage: ./7-model_state_fetch_all.py username password database
8️⃣ 8-model_state_fetch_first.py
Description: Prints the first State object from the database.
Skills demonstrated: SQLAlchemy query filtering and limit.
Usage: ./8-model_state_fetch_first.py username password database
9️⃣ 9-model_state_filter_a.py
Description: Lists all State objects that contain the letter 'a'.
Skills demonstrated: SQLAlchemy filtering with like operator.
Usage: ./9-model_state_filter_a.py username password database
🔟 10-model_state_my_get.py
Description: Prints the ID of a State object with a name passed as argument.
Skills demonstrated: Exact match filtering in SQLAlchemy.
Usage: ./10-model_state_my_get.py username password database state_name
1️⃣1️⃣ 11-model_state_insert.py
Description: Adds a new State object "Louisiana" to the database.
Skills demonstrated: Creating and adding objects with SQLAlchemy ORM.
Usage: ./11-model_state_insert.py username password database
1️⃣2️⃣ 12-model_state_update_id_2.py
Description: Changes the name of the State object with id=2 to "New Mexico".
Skills demonstrated: Updating objects with SQLAlchemy ORM.
Usage: ./12-model_state_update_id_2.py username password database
1️⃣3️⃣ 13-model_state_delete_a.py
Description: Deletes all State objects with a name containing the letter 'a'.
Skills demonstrated: Deleting objects with SQLAlchemy ORM.
Usage: ./13-model_state_delete_a.py username password database
1️⃣4️⃣ 14-model_city_fetch_by_state.py
Description: Lists all City objects by state using SQLAlchemy relationships.
Skills demonstrated: Working with relationship queries in SQLAlchemy.
Usage: ./14-model_city_fetch_by_state.py username password database
🚀 Usage Examples
Using MySQLdb
```
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
Using SQLAlchemy ORM
```
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
Understand the difference between raw SQL and ORM approaches
```
# 🐍 Python Object-Relational Mapping (ORM) Project 🗄️

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/SQLAlchemy-FF4500?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
</div>

## 📋 Table of Contents
- 🔍 Project Overview
- 🛠️ Prerequisites
- 💻 Installation
- 📁 Project Structure
- 📊 Exercise Reviews
  - Direct MySQL Scripts
  - SQLAlchemy ORM Scripts
- 🚀 Usage Examples
- 📚 Learning Objectives
- 🔗 Resources

## 🔍 Project Overview

**This project bridges the gap between Python programming and database operations through Object-Relational Mapping.** It demonstrates two ways to interact with a MySQL database:

1. **Direct Database Access**: Using the MySQLdb module to connect to MySQL and execute raw SQL queries
2. **ORM Approach**: Using SQLAlchemy ORM to abstract database operations into Python objects

ORM allows developers to interact with databases using object-oriented paradigms, making the code more maintainable and database-agnostic.

## 🛠️ Prerequisites

* **Python 3.8+**
* **MySQL 5.7+**
* **MySQLdb module**
* **SQLAlchemy**
* **A MySQL server running with appropriate permissions**

## 💻 Installation

**1. Clone the repository:**
```bash
git clone https://github.com/your-username/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/python-object_relational_mapping
```

**2. Set up a virtual environment:**
```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

**3. Install the required packages:**
```bash
pip install mysqlclient SQLAlchemy
```

**4. Set up the database:**
```sql
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
-- Add sample data as needed
```

## 📁 Project Structure

```
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

## 📊 Exercise Reviews

### Direct MySQL Scripts

#### 0️⃣ **0-select_states.py**
* **Description**: This script connects to a MySQL database and lists all states in the `states` table ordered by ID.
* **Skills demonstrated**: Basic database connection, cursor handling, query execution.
* **Usage**: `./0-select_states.py username password database`

#### 1️⃣ **1-filter_states.py**
* **Description**: Lists all states whose name starts with 'N' (case sensitive).
* **Skills demonstrated**: SQL filtering with LIKE clause, result processing.
* **Usage**: `./1-filter_states.py username password database`

#### 2️⃣ **2-my_filter_states.py**
* **Description**: Takes a state name as argument and displays all matching states.
* **Skills demonstrated**: User input handling, string formatting in SQL queries.
* **Usage**: `./2-my_filter_states.py username password database state_name`
* **Security issue**: ⚠️ Vulnerable to SQL injection.

#### 3️⃣ **3-my_safe_filter_states.py**
* **Description**: Same as script 2 but safe from SQL injection.
* **Skills demonstrated**: Parameterized queries, secure database access.
* **Usage**: `./3-my_safe_filter_states.py username password database state_name`

#### 4️⃣ **4-cities_by_state.py**
* **Description**: Lists all cities from the `cities` table with their corresponding state names using JOIN.
* **Skills demonstrated**: JOIN operations, working with multiple tables.
* **Usage**: `./4-cities_by_state.py username password database`

#### 5️⃣ **5-filter_cities.py**
* **Description**: Lists all cities of a given state using SQL JOIN and safe parameterized queries.
* **Skills demonstrated**: JOIN operations, result formatting, parameterized queries.
* **Usage**: `./5-filter_cities.py username password database state_name`

### SQLAlchemy ORM Scripts

#### 🗃️ **model_state.py**
* **Description**: Defines the State class that maps to the `states` table using SQLAlchemy ORM.
* **Skills demonstrated**: ORM class definition, table mapping, SQLAlchemy declarative base.

#### 🏙️ **model_city.py**
* **Description**: Defines the City class that maps to the `cities` table using SQLAlchemy ORM.
* **Skills demonstrated**: ORM class definition, foreign key relationships.

#### 7️⃣ **7-model_state_fetch_all.py**
* **Description**: Lists all State objects from the database using SQLAlchemy ORM.
* **Skills demonstrated**: SQLAlchemy engine and session creation, basic queries.
* **Usage**: `./7-model_state_fetch_all.py username password database`

#### 8️⃣ **8-model_state_fetch_first.py**
* **Description**: Prints the first State object from the database.
* **Skills demonstrated**: SQLAlchemy query filtering and limit.
* **Usage**: `./8-model_state_fetch_first.py username password database`

#### 9️⃣ **9-model_state_filter_a.py**
* **Description**: Lists all State objects that contain the letter 'a'.
* **Skills demonstrated**: SQLAlchemy filtering with like operator.
* **Usage**: `./9-model_state_filter_a.py username password database`

#### 🔟 **10-model_state_my_get.py**
* **Description**: Prints the ID of a State object with a name passed as argument.
* **Skills demonstrated**: Exact match filtering in SQLAlchemy.
* **Usage**: `./10-model_state_my_get.py username password database state_name`

#### 1️⃣1️⃣ **11-model_state_insert.py**
* **Description**: Adds a new State object "Louisiana" to the database.
* **Skills demonstrated**: Creating and adding objects with SQLAlchemy ORM.
* **Usage**: `./11-model_state_insert.py username password database`

#### 1️⃣2️⃣ **12-model_state_update_id_2.py**
* **Description**: Changes the name of the State object with id=2 to "New Mexico".
* **Skills demonstrated**: Updating objects with SQLAlchemy ORM.
* **Usage**: `./12-model_state_update_id_2.py username password database`

#### 1️⃣3️⃣ **13-model_state_delete_a.py**
* **Description**: Deletes all State objects with a name containing the letter 'a'.
* **Skills demonstrated**: Deleting objects with SQLAlchemy ORM.
* **Usage**: `./13-model_state_delete_a.py username password database`

#### 1️⃣4️⃣ **14-model_city_fetch_by_state.py**
* **Description**: Lists all City objects by state using SQLAlchemy relationships.
* **Skills demonstrated**: Working with relationship queries in SQLAlchemy.
* **Usage**: `./14-model_city_fetch_by_state.py username password database`

## 🚀 Usage Examples

### **Using MySQLdb**

```python
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

### **Using SQLAlchemy ORM**

```python
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

## 📚 Learning Objectives

* **Connect to a MySQL database from a Python script**
* **Execute SELECT queries on a MySQL database from Python**
* **Understand SQL injection and implement secure queries**
* **Create and utilize a SQLAlchemy ORM**
* **Map Python classes to MySQL tables using SQLAlchemy**
* **Perform CRUD operations using SQLAlchemy**
* **Understand the difference between raw SQL and ORM approaches**

## 🔗 Resources

* [**Object-Relational Mapping**](https://en.wikipedia.org/wiki/Object-relational_mapping)
* [**SQLAlchemy Documentation**](https://docs.sqlalchemy.org/)
* [**Python MySQLdb Documentation**](https://mysqlclient.readthedocs.io/)
* [**MySQL Tutorial**](https://dev.mysql.com/doc/refman/8.0/en/tutorial.html)
* [**SQL Injection Prevention**](https://owasp.org/www-community/attacks/SQL_Injection)
* [**Python Database Access**](https://www.python.org/dev/peps/pep-0249/)

---

***This project is part of the Holberton School Higher Level Programming curriculum. It focuses on connecting Python applications to databases using both direct SQL queries and ORM techniques.***
