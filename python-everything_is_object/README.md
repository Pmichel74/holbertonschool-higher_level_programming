# 🐍 Python - Everything is Object

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Object-Oriented](https://img.shields.io/badge/Paradigm-Object--Oriented-orange)
![Memory Management](https://img.shields.io/badge/Topic-Memory%20Management-brightgreen)

This project explores the fundamental concept in Python that **everything is an object**. Through a series of questions and examples, we'll dive deep into object types, memory allocation, variable references, and Python's specific behaviors related to object handling.

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [🧠 Learning Objectives](#-learning-objectives)
- [📚 Concepts Covered](#-concepts-covered)
- [📂 File Structure](#-file-structure)
- [🔄 Object References and Assignment](#-object-references-and-assignment)
- [🆔 Identity and Equality](#-identity-and-equality)
- [🧩 Mutable vs Immutable Types](#-mutable-vs-immutable-types)
- [❓ Common Questions](#-common-questions)
- [📊 Memory Visualization](#-memory-visualization)
- [📝 Requirements](#-requirements)
- [📖 Resources](#-resources)
- [👤 Author](#-author)

## 🎯 Project Overview

In Python, understanding that "everything is an object" is crucial for writing effective code. This project aims to explore the nuances of Python's object model through a series of questions and exercises that will test your knowledge and deepen your understanding of:

- How Python allocates and manages memory
- The difference between mutable and immutable objects
- How variables store references rather than values
- Object identity versus equality
- How assignment and aliasing work

## 🧠 Learning Objectives

By the end of this project, you should be able to:

- Explain why Python is an object-oriented programming language
- Define what an object is and how it's represented in memory
- Differentiate between a class, an object, and an instance
- Understand the distinction between immutable and mutable objects
- Explain concepts like reference, assignment, and aliasing
- Determine if two variables are identical or linked to the same object
- Display the memory address of an object
- Identify built-in mutable and immutable types
- Understand how Python passes variables to functions

## 📚 Concepts Covered

- **Object Types**: Integers, strings, lists, dictionaries, etc., and their behaviors
- **Memory Allocation**: How Python manages memory for different object types
- **Object Identity**: Using `id()` function and the `is` operator
- **Equality vs. Identity**: Understanding the difference between `==` and `is`
- **Mutability**: Differences between mutable and immutable types
- **Variable Assignment**: How variables reference objects rather than contain them
- **Shallow vs. Deep Copying**: Creating independent copies of objects

## 📂 File Structure

Files in this project typically contain answers to specific questions about Python's object model. Most of these are simple text files with just a number or string representing the answer to a question (e.g., "True", "False", "[1, 2, 3]").

## 🔄 Object References and Assignment

In Python, variables don't contain values; they reference objects:

```python
a = 89      # 'a' references an int object with value 89
b = a       # 'b' now references the same object as 'a'
a = 100     # 'a' now references a NEW int object with value 100
# 'b' still references the original int object (89)
```

For mutable objects, modifying the object affects all variables referencing it:

```python
a = [1, 2, 3]  # 'a' references a list object
b = a          # 'b' references the SAME list object
b.append(4)    # Modifies the object that both 'a' and 'b' reference
# Now both a and b are [1, 2, 3, 4]
```

## 🆔 Identity and Equality

- **Identity (`is`)**: Checks if two variables reference the same object in memory
- **Equality (`==`)**: Checks if the values of two objects are equivalent

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (same values)
print(a is b)  # False (different objects in memory)
print(a is c)  # True (same object in memory)
```

## 🧩 Mutable vs Immutable Types

### Immutable Types
- Integers
- Floats
- Strings
- Tuples
- Frozen sets

### Mutable Types
- Lists
- Dictionaries
- Sets
- Custom classes (typically)

## ❓ Common Questions

1. **Why doesn't modifying a string change the original?**
   - Strings are immutable, so operations create new string objects

2. **Why does modifying a list in a function affect the caller's list?**
   - Lists are mutable and passed by reference

3. **What's the difference between `==` and `is`?**
   - `==` compares values, `is` compares identity (memory location)

4. **Why are some small integers shared?**
   - Python pre-allocates small integers (-5 to 256) for efficiency

## 📊 Memory Visualization

Understanding Python's memory model:

```
Memory:
+-------------------+      +-------------------+
| int object: 42    | <--- | Variable 'a'      |
+-------------------+      +-------------------+
         ^
         |
         |            +-------------------+
         +----------- | Variable 'b'      |
                      +-------------------+
```

## 📝 Requirements

- Python 3.8.5 or higher
- pycodestyle 2.8.* (for code style checking)
- All files should end with a new line
- All answer files must be only one line, with no shebang
- All answer files must have the correct answers

## 📖 Resources

- [Python Documentation: Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Immutable vs Mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
- [Python Tutor - Visualize Python code execution](http://www.pythontutor.com/)
- [Object-Oriented Programming](https://python.swaroopch.com/oop.html)

## 👤 Author

- **[Patrick MICHEL]** - [GitHub Profile](https://github.com/Pmichel74)