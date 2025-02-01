# Python - More Classes and Objects 🐍

## Overview 📚
Advanced exploration of Object-Oriented Programming (OOP) in Python, focusing on class methods, static methods, and class attributes.

## Project Information ℹ️
- Language: Python 3.8.5
- Style guide: PEP 8
- Project Structure: Progressive Rectangle class implementation

## Files and Descriptions 📂
| File | Description |
|------|-------------|
| `0-rectangle.py` | Empty Rectangle class |
| `1-rectangle.py` | Rectangle with width and height attributes |
| `2-rectangle.py` | Area and perimeter methods |
| `3-rectangle.py` | String representation |
| `4-rectangle.py` | Repr method implementation |
| `5-rectangle.py` | Deletion message |
| `6-rectangle.py` | Number of instances |
| `7-rectangle.py` | Class symbol customization |
| `8-rectangle.py` | Rectangle comparison |
| `9-rectangle.py` | Square implementation |

## Learning Objectives 🎯
- Class methods and static methods
- Special methods (`__str__`, `__repr__`)
- Class attributes vs instance attributes
- Property decorators
- Object lifecycle

## Requirements ⚠️
- Python 3.8.5
- pycodestyle 2.8.*
- All files must be executable
- Module and function documentation required

## Usage Example 💻
```python
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)
```

## Testing 🧪
```python
python3 -m doctest ./tests/*
```
### Author ✍️
```bash
Patrick MICHEL
```
