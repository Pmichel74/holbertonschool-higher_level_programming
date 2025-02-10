# 🐍 Python ABC Learning Project

## 📋 Description
This repository contains exercises and examples for learning Python fundamentals through Abstract Base Classes (ABC). The project focuses on implementing abstract classes and interfaces following Python's object-oriented programming principles.

## 🎯 Learning Objectives
- Understanding Abstract Base Classes in Python
- Working with interfaces and implementations
- Learning good practices for OOP in Python
- Implementing abstract methods and properties
- Creating robust and reusable class hierarchies
- Enforcing interface contracts through ABC
- Using decorators like `@abstractmethod`
- Understanding metaclasses in Python

## 🛠️ Technologies Used
- Python 3.x
- ABC module from Python's standard library
- unittest for testing
- Type hints and annotations
- Visual Studio Code with Python extension

## 📝 Project Structure
python-abc/
├── examples/
│   ├── basic_abc.py
│   ├── complex_abc.py
│   └── metaclass_demo.py
├── exercises/
│   ├── shape.py
│   ├── animal.py
│   └── vehicle.py
├── tests/
│   ├── test_shape.py
│   ├── test_animal.py
│   └── test_vehicle.py
└── README.md

## 🚀 Getting Started
1. Clone this repository
```bash
git clone [repository-url]
```
2. Navigate to the project directory
```bash
cd python-abc
```
3. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

## 💻 Usage Example
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape"""
        pass
```

## ✅ Testing
Run the test suite:
```bash
python3 -m unittest discover tests
```

## 📚 Additional Resources
- [Python ABC Documentation](https://docs.python.org/3/library/abc.html)
- [Real Python - Abstract Base Classes](https://realpython.com/python-interface/)
- [Python OOP Tutorial](https://docs.python.org/3/tutorial/classes.html)

## 🔍 Project Tasks
1. Implement the Shape ABC
2. Create concrete classes (Circle, Rectangle, Triangle)
3. Add unit tests for each shape
4. Implement the Animal ABC
5. Create concrete animal classes
6. Add vehicle hierarchy implementation

## 👥 Author
- Patrick

---
⭐ Happy Coding with Python ABC! ⭐