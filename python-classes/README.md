# Python - Classes and Objects 🐍 

## Overview 📚
This project explores Object-Oriented Programming (OOP) in Python, focusing on classes, objects, and data encapsulation.

## Project Information ℹ️
- Language: Python 3.8.5
- Style guide: PEP 8
- Project Structure: Individual task files

## Files and Descriptions 📂
| File | Description |
|------|-------------|
| `0-square.py` | Empty class `Square` definition |
| `1-square.py` | `Square` class with size attribute |
| `2-square.py` | Size validation for `Square` class |
| `3-square.py` | Area calculation method |
| `4-square.py` | Getter/setter implementation |
| `5-square.py` | Square printing method |
| `6-square.py` | Position attribute addition |

## Learning Objectives 🎯
- Understanding Object-Oriented Programming
- Working with classes and objects
- Managing attributes (public, private)
- Properties and methods implementation
- Data encapsulation and information hiding

## Requirements ⚠️
- Python 3.8.5
- pycodestyle 2.8.*
- All files must be executable
- Documentation is mandatory

## Usage Example 💻
```python
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
```

## Testing 🧪
```python
python3 -m doctest ./tests/*
```

### Author
```
Patrick MICHEL
```