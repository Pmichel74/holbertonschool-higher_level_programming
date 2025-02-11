# 🔄 Python Serialization Project

## 📋 Table of Contents
- [🔄 Python Serialization Project](#-python-serialization-project)
  - [📋 Table of Contents](#-table-of-contents)
  - [📋 Description](#-description)
  - [🛠️ Project Files](#️-project-files)
  - [🔧 Requirements](#-requirements)
  - [💻 Usage](#-usage)
  - [📚 Features Implemented](#-features-implemented)
    - [JSON Serialization](#json-serialization)
    - [Pickle Serialization](#pickle-serialization)
    - [CSV to JSON Conversion](#csv-to-json-conversion)
    - [XML Data Handling](#xml-data-handling)
  - [📝 Learning Goals](#-learning-goals)
  - [👤 Author](#-author)

## 📋 Description
This repository demonstrates different serialization methods in Python, including JSON, Pickle, XML and CSV conversions.

## 🛠️ Project Files
- `task_00_basic_serialization.py`: JSON serialization examples
- `task_01_pickle.py`: Object serialization with Pickle
- `task_02_csv.py`: CSV to JSON conversion utilities  
- `task_03_xml.py`: XML data handling and conversion

## 🔧 Requirements
- Python 3.x
- Standard library modules:
  - json
  - pickle
  - csv
  - xml.etree.ElementTree
- Unix-like operating system
- Text editor or IDE

## 💻 Usage
1. Clone the repository:
```bash
git clone [repository-url]
cd python-serialization
```

2. Run individual tasks:
```bash
python3 task_00_basic_serialization.py
python3 task_01_pickle.py
python3 task_02_csv.py
python3 task_03_xml.py
```

3. Check generated files:
```bash
ls *.json *.pkl *.xml
```

## 📚 Features Implemented

### JSON Serialization
```python
# Save dictionary to JSON
data = {"name": "Alice", "age": 25}
serialize_and_save_to_file(data, "output.json")
```

### Pickle Serialization
```python
# Create and serialize object
person = CustomObject("Bob", 30, True)
person.serialize("person.pkl")

# Deserialize object
loaded_person = CustomObject.deserialize("person.pkl")
```

### CSV to JSON Conversion
```python
# Convert CSV to JSON
convert_csv_to_json("input.csv")
```

### XML Data Handling
```python
# Dictionary to XML
data = {"name": "Charlie", "age": 35}
serialize_to_xml(data, "output.xml")

# XML back to dictionary
result = deserialize_from_xml("output.xml")
```

## 📝 Learning Goals
- Understanding different serialization formats:
  - JSON for web data exchange
  - Pickle for Python object serialization
  - CSV for tabular data handling
  - XML for structured data representation
- Implementing error handling and data validation
- Working with file I/O operations
- Converting between different data formats
- Handling complex data structures

## 👤 Author
- Name: Patrick MICHEL
- GitHub: [@PatrickMICHEL](https://github.com/Pmichel74)

---
⭐ Made with Python serialization magic ⭐