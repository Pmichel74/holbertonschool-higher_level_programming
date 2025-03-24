# 🚀 Python Server-Side Rendering Project

A Flask-based web application demonstrating progressive implementations of server-side rendering with multiple data sources.

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Tasks](#-tasks)
  - [Task 2: Basic Routing and Logic](#task-2-basic-routing-and-logic)
  - [Task 3: File-based Data Sources](#task-3-file-based-data-sources)
  - [Task 4: Database Integration](#task-4-database-integration)
- [Technologies Used](#-technologies-used)
- [Running the Application](#-running-the-application)
- [Database Setup](#-database-setup)

## 📋 Project Overview

This project demonstrates the implementation of a Flask web application with server-side rendering capabilities. It progressively evolves from basic routing to handling multiple data sources including JSON files, CSV files, and SQLite databases.

## 💻 Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd python-server-side-rendering
```

2. Install the required dependencies:
```bash
pip install flask
```

3. Initialize the database (optional, for Task 4):
```bash
python newdb.py
```

## 📁 Project Structure

```
python-server-side-rendering/
├── task_02_logic.py      # Basic Flask application with routing
├── task_03_files.py      # Flask application with JSON/CSV data support
├── task_04_db.py         # Flask application with database integration
├── newdb.py              # Database initialization script
├── templates/            # HTML templates for rendering
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── items.html
│   └── product_display.html
├── products.json         # Sample product data in JSON format
├── products.csv          # Sample product data in CSV format
└── products.db           # SQLite database (created by newdb.py)
```

## 📌 Tasks

### Task 2: Basic Routing and Logic
- Implementation of a Flask application with basic routing
- Routes for home, about, contact pages
- JSON file reading functionality for items display

### Task 3: File-based Data Sources
- Extended Flask application handling both JSON and CSV data sources
- Query parameter support for filtering by source and product ID
- Error handling for various file operations

### Task 4: Database Integration
- Complete Flask application with SQLite database integration
- Support for multiple data sources (JSON, CSV, SQLite)
- Advanced error handling and data validation

## 🔧 Technologies Used

- **Python**: Core programming language
- **Flask**: Web framework for building the application
- **SQLite**: Lightweight database for storing product information
- **Jinja2**: Templating engine for rendering HTML (included with Flask)
- **JSON/CSV**: Data formats for storing and retrieving product information

## 🏃‍♂️ Running the Application

To run any of the application versions:

```bash
# For the basic version
python task_02_logic.py

# For the file-based version
python task_03_files.py

# For the database-integrated version
python task_04_db.py
```

Access the application at http://localhost:5000

## 🗄️ Database Setup

Initialize the database with sample data:

```bash
python newdb.py
```

This script creates a SQLite database with a Products table containing sample product entries.

