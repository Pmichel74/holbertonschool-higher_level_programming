# 🚀 Python Server-Side Rendering Project

A Flask-based web application demonstrating progressive implementations of server-side rendering with multiple data sources, showcasing different data retrieval and display methods.

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
- [API Endpoints](#-api-endpoints)
- [Data Sources](#-data-sources)
- [Database Setup](#-database-setup)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)

## 📋 Project Overview

This project demonstrates the implementation of a Flask web application with server-side rendering capabilities. It progressively evolves from basic routing to handling multiple data sources including JSON files, CSV files, and SQLite databases.

The application showcases:
- Server-side rendering with Jinja2 templates
- Dynamic content generation based on data sources
- Error handling and data validation
- URL parameter processing for filtering content
- Progressive enhancement of features across multiple iterations

## 💻 Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager
- Basic understanding of Flask and web applications

### Setup Steps

1. Clone the repository:
```bash
git clone [repository-url]
cd python-server-side-rendering
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install flask
pip install sqlite3  # Usually included with Python
```

4. Prepare the data files:
   - Ensure `products.json` and `products.csv` are in the root directory
   - Sample formats are provided in the project structure section

5. Initialize the database (for Task 4):
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
│   ├── index.html        # Home page template
│   ├── about.html        # About page template
│   ├── contact.html      # Contact page template
│   ├── items.html        # Items listing template
│   └── product_display.html  # Product details template
├── products.json         # Sample product data in JSON format
├── products.csv          # Sample product data in CSV format
└── products.db           # SQLite database (created by newdb.py)
```

### Key Files Explained
- **task_02_logic.py**: Entry-level implementation with basic routing and template rendering
- **task_03_files.py**: Intermediate implementation with file-based data sources and parameter handling
- **task_04_db.py**: Advanced implementation integrating SQLite with comprehensive error handling
- **newdb.py**: Utility script to initialize and populate the SQLite database
- **templates/**: Directory containing all Jinja2 HTML templates for rendering views

### Data File Formats

**products.json**:
```json
{
  "products": [
    {
      "id": 1,
      "name": "Laptop",
      "category": "Electronics",
      "price": 799.99
    },
    {
      "id": 2,
      "name": "Coffee Mug",
      "category": "Home Goods",
      "price": 15.99
    }
  ]
}
```

**products.csv**:
```csv
id,name,category,price
1,Laptop,Electronics,799.99
2,Coffee Mug,Home Goods,15.99
```

## 📌 Tasks

### Task 2: Basic Routing and Logic
- Implementation of a Flask application with basic routing mechanisms
- Routes for home, about, contact pages with template-based rendering
- JSON file reading functionality for items display using error handling
- Template context injection for dynamic content generation
- Implementation showcases fundamental Flask application structure

### Task 3: File-based Data Sources
- Extended Flask application handling both JSON and CSV data sources
- Implementation of dedicated parsers for each data format
- Query parameter support for filtering by source (`source=json` or `source=csv`)
- Product ID filtering via URL parameters (`id=1`)
- Comprehensive error handling for file operations, data parsing, and validation
- User-friendly error messages displayed in templates

### Task 4: Database Integration
- Complete Flask application with SQLite database integration
- Support for three data sources (JSON, CSV, SQLite) via the `source` parameter
- Direct database querying with parameterized queries for security
- Transaction management for database operations
- Advanced error handling and detailed error reporting
- Data type validation and conversion for consistent display

## 🔧 Technologies Used

- **Python**: Core programming language chosen for its readability and powerful web libraries
  - Version 3.6+ recommended for f-string support and modern features

- **Flask**: Lightweight WSGI web application framework that simplifies web development
  - Provides routing, template rendering, and request handling
  - Minimalist approach allows for focused learning of core concepts

- **SQLite**: Self-contained, serverless, zero-configuration database engine
  - Perfect for smaller applications and development environments
  - Native Python support through the sqlite3 module
  - File-based storage makes deployment and testing simple

- **Jinja2**: Modern and designer-friendly templating engine for Python
  - Included with Flask and tightly integrated
  - Supports template inheritance, filters, and macros
  - Allows for clean separation of logic and presentation

- **JSON/CSV**: Common data formats for storing and retrieving structured information
  - Standard libraries in Python for parsing and generation
  - Represent two different approaches to data storage
  - Demonstrates flexibility in data source handling

## 🏃‍♂️ Running the Application

### Starting the Server

To run any of the application versions:

```bash
# For the basic version (Task 2)
python task_02_logic.py

# For the file-based version (Task 3)
python task_03_files.py

# For the database-integrated version (Task 4)
python task_04_db.py
```

By default, the application runs in debug mode, which provides detailed error messages and automatic server reloading when code changes are detected.

### Accessing the Application

Base URL: http://localhost:5000

Main pages:
- Home: http://localhost:5000/
- About: http://localhost:5000/about
- Contact: http://localhost:5000/contact
- Items list: http://localhost:5000/items

Product views:
- All products (JSON): http://localhost:5000/products?source=json
- All products (CSV): http://localhost:5000/products?source=csv
- All products (DB): http://localhost:5000/products?source=sql
- Specific product: http://localhost:5000/products?source=json&id=1

## 📡 API Endpoints

| Endpoint | Method | Description | Query Parameters |
|----------|--------|-------------|------------------|
| `/` | GET | Home page | None |
| `/about` | GET | About page | None |
| `/contact` | GET | Contact page | None |
| `/items` | GET | Display items from items.json | None |
| `/products` | GET | Display products from specified source | `source`: 'json', 'csv', or 'sql'<br>`id`: Optional product ID |

## 🗃️ Data Sources

The application demonstrates working with three different data sources:

1. **JSON Files**: Structured data in JavaScript Object Notation
   - Supports nested data structures
   - Human-readable format
   - Native parsing in modern browsers and Python

2. **CSV Files**: Comma-Separated Values for tabular data
   - Simple format widely supported by spreadsheet applications
   - Efficient for large datasets
   - Requires type conversion for non-string values

3. **SQLite Database**: Relational database in a single file
   - SQL query support for complex data operations
   - ACID compliance for data integrity
   - Efficient indexing and querying capabilities

## 🗄️ Database Setup

The database structure is defined and populated by the `newdb.py` script:

```bash
python newdb.py
```

### Schema

```sql
CREATE TABLE Products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
)
```

### Sample Data

The database is initialized with two sample products:
1. Laptop (Electronics) - $799.99
2. Coffee Mug (Home Goods) - $15.99

You can add more products by modifying the `newdb.py` script or using direct SQLite commands:

```bash
sqlite3 products.db
```

```sql
INSERT INTO Products (id, name, category, price) VALUES (3, 'Headphones', 'Electronics', 99.99);
```

## 🔍 Troubleshooting

### Common Issues

1. **FileNotFoundError**: 
   - Ensure products.json and products.csv exist in the root directory
   - Check file permissions

2. **Database Connection Error**:
   - Confirm products.db was created with newdb.py
   - Verify SQLite is installed and functioning

3. **Template Not Found**:
   - Ensure the templates directory contains all required HTML files
   - Check template names match those referenced in the code

### Debugging

For detailed error information:
- Check the terminal output where Flask is running
- Review the logs in debug mode
- Use the built-in Python debugger: `python -m pdb task_04_db.py`

## 🤝 Contributing

Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request



