# 🐍 Python - Test-Driven Development

## 📄 Description
This repository contains Python scripts demonstrating various techniques for test-driven development (TDD). Each script is designed to showcase different functionalities and best practices in Python, with a focus on writing tests first and then implementing the code.

## 🎯 Learning Objectives
What’s an interactive test
Why tests are important
How to write Docstrings to create tests
How to write documentation for each module and function
What are the basic option flags to create tests
How to find edge cases

## 📂 Project Structure
- `0-add_integer.py`: ➕ Adds two integers and returns the result.
- `2-matrix_divided.py`: ➗ Divides all elements of a matrix by a given divisor.
- `3-say_my_name.py`: 🗣️ Prints a full name in the format: "My name is <first_name> <last_name>".
- `6-max_integer.py`: 🔢 Finds the maximum integer in a list.

## 🖥️ Requirements
- 🐍 Python 3.8 or later
- 🐧 Ubuntu 20.04 LTS or equivalent
- 🧹 pycodestyle 2.8.* (for style checking)

## 💾 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Pmichel74/holbertonschool_higher_level_programming.git
   cd holbertonschool_higher_level_programming/python-test_driven_development
   ```

2. Run each script directly
```bash
python3 0-add_integer.py
```
## 🚀 Usage
You can also import these scripts into your own Python files and call the functions they contain.
Example:
```bash
from 0-add_integer import add_integer

result = add_integer(1, 2)
print(result)  # Output: 3
```
## 🧪 Running Tests
To run the tests for each script, use the following command:
```bash
python3 -m unittest discover tests
```
### 👤 Author
Patrick MICHEL
