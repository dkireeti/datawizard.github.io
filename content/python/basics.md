# Python Basics

This page covers minimal, hands-on Python essentials we'll use throughout the course. It's designed to be short and executable in the accompanying notebook `notebooks/python_basics.ipynb`.

## Goals

- Understand variables and basic data types (numbers, strings, booleans)
- Work with lists and dictionaries
- Use NumPy for vectorized operations
- Create a tiny Pandas DataFrame

## Quick examples

Inline code and short blocks are supported. For example, simple arithmetic: $1 + 1 = 2$.

```python
# Variables
x = 10
pi = 3.14159
name = 'DataWizard'

# List
fruits = ['apple', 'banana', 'cherry']

print(x, pi, name)
```

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

Open `notebooks/python_basics.ipynb` locally or view the built HTML via the Jupyter Book site. We'll add Binder/Thebe badges later for live execution if you want that interactive route.
# Python basics

This page covers minimal, hands-on Python essentials we'll use throughout the course. It's designed to be short and executable in the accompanying notebook `notebooks/python_basics.ipynb`.

## Goals

- Understand variables and basic data types (numbers, strings, booleans)
- Work with lists and dictionaries
- Use NumPy for vectorized operations
- Create a tiny Pandas DataFrame

## Quick examples

Inline code and short blocks are supported. For example, simple arithmetic: $1 + 1 = 2$.

```python
# Variables
x = 10
pi = 3.14159
name = 'DataWizard'

# List
fruits = ['apple', 'banana', 'cherry']

print(x, pi, name)
```

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

Open `notebooks/python_basics.ipynb` locally or view the built HTML via the Jupyter Book site. We'll add Binder/Thebe badges later for live execution if you want that interactive route.
