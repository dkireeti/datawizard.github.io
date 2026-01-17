# Python Basics

This page covers minimal, hands-on Python essentials for ML. It's designed to be short intutibe and executable in the accompanying notebook `notebooks/python_basics.ipynb`.

## Resources
- [Python3/tutorial](https://docs.python.org/3/tutorial/introduction.html)

## Goal

- To understand variables and basic data types (numbers, strings, booleans)
- Work with lists and dictionaries
- Use NumPy for vectorized operations
- Create a tiny Pandas DataFrame


## What is python ?
Python is a high-level, general-purpose programming language known for its simple, readable syntax that emphasizes code clarity and allows developers to express concepts in fewer lines of code than many other languages

### Key Features
- Versatility: It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
- Interpreted: Python is an interpreted language, meaning code can be executed line-by-line immediately, which speeds up the prototyping and debugging process.
- Large Standard Library & Ecosystem: Python comes with an extensive standard library and a vast collection of third-party modules and frameworks (e.g., NumPy, Pandas, Django, Flask, TensorFlow) that simplify complex tasks in various fields.
- Dynamically Typed: Programmers do not need to declare variable types explicitly, as Python determines them at runtime, leading to faster development speed.
- Open Source & Community: Python is free to use and distribute, supported by a large, active, and helpful global community

### Common Applications
- Python's flexibility makes it a popular choice for a wide range of applications: 
- Web Development: Used for server-side web development with frameworks like Django and Flask.
- Data Science and Machine Learning: The de facto choice for data analysis, visualization, and building AI models using libraries such as Pandas, NumPy, and TensorFlow.
- Automation & Scripting: Widely used for writing scripts to automate repetitive tasks due to its simple syntax.
- Software Development: Used for various software development tasks, including building prototypes and desktop applications. 

with this, lets begins from variables,

## Variables
variables are very basic elements and simple placeholders to hold some value(reference aswell) in python code or file. As the term says,the value can be changed by all possible programming logic or by direct assignment to the variable while running code.

In the below example, X holds the value 10, while fruits holds the reference of the List of fruits names.

```python

# Variables Examples
x = 10 #Interger
pi = 3.14159 #Float
name = 'DataWizard' #String
is_working = True # Boolean
i = None # None type.
# List
fruits = ['apple', 'banana', 'cherry']

print(x, pi, name)
```
## Data Types
- Well Data Types for variables to specify what type of data that variable holds and the operations that can be performed on it, telling the computer how to store and process the data efficiently.

### Numeric Types
These types are used to store numeric values. 
- int (Integers): Whole numbers, positive or negative, without a decimal point (e.g., 10, -25). There is no limit to their length in Python 3.
- float (Floating-point numbers): Real numbers that have a decimal point (e.g., 3.14, -0.001).
- complex (Complex numbers): Numbers with a real and an imaginary part, written as x + yj (e.g., 2 + 3j). 

```python

# Examples
x = 10 #Interger
pi = 3.14159 #Float
a = 2+3j # Complex Number

print(x, pi, name)
```

### Sequence Types
These are ordered collections of items, where each item can be accessed by an index. 
- str (Strings): An immutable sequence of Unicode characters used to represent text (e.g., "Hello, world!"). They can be enclosed in single, double, or triple quotes.
- list (Lists): A mutable, ordered collection of items enclosed in square brackets (e.g., [1, "apple", True]). They are very flexible and can contain elements of different data types.
- tuple (Tuples): An immutable, ordered collection of items enclosed in parentheses (e.g., (10, 20, 30)). Once created, elements cannot be changed.
- range: An immutable sequence of numbers, often used for looping a specific number of times.

```python

#  Examples
s = "Hello World"

# List
fruits = ['apple', 'banana', 'cherry']
# tuple
t = (1,2)
print(s,s[0])
```

### Mapping Type
- dict (Dictionaries): An unordered collection that stores data in key-value pairs, enclosed in curly braces (e.g., {"name": "John", "age": 36}). Each key must be unique and immutable.
```python

# Examples
m = {'a':1,'b':2}
print(m['a'])
```
### Set Types
- Python includes set types for unordered collections of unique elements: set (mutable) and frozenset (immutable).

### Boolean Type
- The bool type represents logical values True or False. 
### Binary Types
- Binary types handle binary data and include bytes (immutable), bytearray (mutable), and memoryview for efficient data access. 
### None Type
- The NoneType represents a null value with the single value None.

## Small NumPy demo

We'll use NumPy for basic vector math. See the notebook for live execution.

```python
import numpy as np
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)  # elementwise addition
```

## Tiny Pandas example

```python
import pandas as pd
df = pd.DataFrame({'feature': [1,2,3], 'target':[0,1,0]})
df
```

## Where to run

Open `notebooks/python_basics.ipynb` locally or [python data types](/python-data-types). We'll add Binder/Thebe badges later for live execution if you want that interactive route.
