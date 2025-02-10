# 🐍 Python Inheritance Project

## 📚 Project Overview
This project demonstrates Object-Oriented Programming concepts in Python, specifically focusing on inheritance. It implements geometric shapes (Rectangle and Square) inheriting from a base geometry class.

## 🎯 Learning Objectives
- Understand inheritance in Python
- Work with parent and child classes 
- Implement class methods and properties
- Handle exceptions and validation

## 📚 Tasks

### 0. Lookup 🔍
- File: `0-lookup.py`
- Returns list of available attributes/methods
```python
def lookup(obj):
    """Returns list of attributes and methods"""
    return dir(obj)
```

### 1. My List 📋
- File: `1-my_list.py`
- Class MyList inherits from list
- Prints sorted list
```python
class MyList(list):
    """Extends list class"""
    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
```

### 2. Is Same Class 🧐
- File: `2-is_same_class.py`
- Checks if object is exactly an instance of class
```python
def is_same_class(obj, a_class):
    """Checks if object is exactly an instance of class"""
    return type(obj) is a_class
```

### 3. Is Kind of Class 🧐
- File: `3-is_kind_of_class.py`
- Checks if object is instance or inherited
```python
def is_kind_of_class(obj, a_class):
    """Checks if object is instance or inherited"""
    return isinstance(obj, a_class)
```

### 4. Inherits From 🧐
- File: `4-inherits_from.py`
- Checks if object inherits from class
```python
def inherits_from(obj, a_class):
    """Checks if object inherits from class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
```

### 5. Base Geometry 📐
- File: `5-base_geometry.py`
- Base geometry class
```python
class BaseGeometry:
    """Base geometry class"""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")
```

### 6. Improve Geometry ✨
- File: `6-base_geometry.py`
- Adds area() method

### 7. Integer Validator ✅
- File: `7-base_geometry.py`
- Validates integers
```python
def integer_validator(self, name, value):
    """Validates integer values"""
    if type(value) is not int:
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be greater than 0")
```

### 8. Rectangle 🟦
- File: `8-rectangle.py`
- Rectangle class with width/height
```python
class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """Initialize a new Rectangle."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height
    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
```

### 9. Full Rectangle 📊
- File: `9-rectangle.py`
- Implements area() and str()

### 10. Square #1 🟥
- File: `10-square.py`
- Square class inherits Rectangle
```python
class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size):
        """Initialize a new square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
```

11. Square #2 🔲
File: 11-square.py
Square with str() method

🚀 Installation & Testing

# Clone repository
git clone https://github.com/Pmichel74/python-inheritance.git
cd python-inheritance

# Run tests
python3 -m doctest -v ./tests/*.txt

# Check style
pycodestyle *.py

📁 File Structure
```markdown
python-inheritance/
├── 0-lookup.py
├── 1-my_list.py
├── 2-is_same_class.py
├── 3-is_kind_of_class.py
├── 4-inherits_from.py
├── 5-base_geometry.py
├── 6-base_geometry.py
├── 7-base_geometry.py
├── 8-rectangle.py
├── 9-rectangle.py
├── 10-square.py
├── 11-square.py
└── tests/
    ├── 1-my_list.txt
    └── 7-base_geometry.txt
```
👤 Author
Your Name
GitHub: Pmichel74
