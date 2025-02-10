# 🐍 Python - Import Modules

## 📄 Description
This repository contains Python scripts demonstrating various techniques for importing modules and handling exceptions. Each script is designed to showcase different functionalities and best practices in Python.

## 📂 Project Structure
- [`0-add.py`](./0-add.py): ➕ Adds two numbers and prints the result.
- [`1-calculation.py`](./1-calculation.py): 🔢 Performs basic arithmetic operations using functions from a module.
- [`2-args.py`](./2-args.py): 📝 Prints the number of arguments and their values.
- [`3-infinite_add.py`](./3-infinite_add.py): ➕ Adds all arguments passed to the script and prints the result.
- [`4-hidden_discovery.py`](./4-hidden_discovery.py): 🔍 Prints all names defined by the compiled module `hidden_4.pyc`.
- [`5-variable_load.py`](./5-variable_load.py): 📥 Imports a variable from a module and prints its value.

## 🖥️ Requirements
- 🐍 Python 3.8 or later
- 🐧 Ubuntu 20.04 LTS or equivalent
- 🧹 pycodestyle 2.8.* (for style checking)

## 💾 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Pmichel74/holbertonschool_higher_level_programming.git
   cd holbertonschool_higher_level_programming/python-import_modules
   ```
2. Run each script directly:
   ```bash
   python3 0-add.py
   ```

## 🚀 Usage
You can also import these scripts into your own Python files and call the functions they contain.
Example:
```python
from 3-infinite_add import infinite_add

result = infinite_add(1, 2, 3, 4)
print(result)  # Output: 10
```

### 👤 Author
Patrick MICHEL - [GitHub Profile](https://github.com/Pmichel74)
