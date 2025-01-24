# 📘 Python Exception Handling

## 📄 Description
This repository contains Python scripts demonstrating various exception handling techniques and list manipulation exercises. Each script is designed to handle specific types of errors and perform operations safely.

## 📂 Project Structure
- `0-safe_print_list.py`: 📝 Function that prints `x` elements of a list.
- `1-safe_print_integer.py`: 🔢 Function that prints an integer.
- `2-safe_print_list_integers.py`: 🔢 Function that prints the first `x` integers of a list.
- `3-safe_print_division.py`: ➗ Function that divides 2 integers and prints the result.
- `4-list_division.py`: ➗ Function that divides element by element 2 lists.
- `5-raise_exception.py`: ⚠️ Function that raises a type exception.
- `6-raise_exception_msg.py`: ⚠️ Function that raises a name exception with a message.

## 📋 Requirements
- 🐍 Python 3.8.5
- 🐧 Ubuntu 20.04 LTS
- 🧹 pycodestyle 2.8.*

## 💾 Installation
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/yourusername/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/python-exceptions
```

## 📜 Example Usage
```python
from 3-safe_print_division import safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
```
## 📝 Examples
```bash
>>> list_division([10, 8, 4], [2, 4, 4], 3)
[5.0, 2.0, 1.0]
>>> safe_print_division(10, 2)
Inside result: 5.0
5.0
```

### 👤 Author
Patrick MICHEL
