# ALX Backend Python - Variable Annotations

This repository contains solutions for the ALX Backend Python tasks related to variable annotations.

## Task 0: Basic annotations - add

**Mandatory**

Write a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float.

## Task 1: Basic annotations - concat

**Mandatory**

Write a type-annotated function `concat` that takes a string `str1` and a string `str2` as arguments and returns a concatenated string.

## Task 2: Basic annotations - floor

**Mandatory**

Write a type-annotated function `floor` which takes a float `n` as argument and returns the floor of the float.

## Task 3: Basic annotations - to string

**Mandatory**

Write a type-annotated function `to_str` that takes a float `n` as argument and returns the string representation of the float.

## Task 4: Define variables

**Mandatory**

Define and annotate the following variables with the specified values:

- `a`, an integer with a value of 1
- `pi`, a float with a value of 3.14
- `i_understand_annotations`, a boolean with a value of True
- `school`, a string with a value of “Holberton”

## Task 5: Complex types - list of floats

**Mandatory**

Write a type-annotated function `sum_list` which takes a list `input_list` of floats as argument and returns their sum as a float.

## Task 6: Complex types - mixed list

**Mandatory**

Write a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float.

## Task 7: Complex types - string and int/float to tuple

**Mandatory**

Write a type-annotated function `to_kv` that takes a string `k` and an int OR float `v` as arguments and returns a tuple. The first element of the tuple is the string `k`. The second element is the square of the int/float `v` and should be annotated as a float.

## Task 8: Complex types - functions

**Mandatory**

Write a type-annotated function `make_multiplier` that takes a float `multiplier` as argument and returns a function that multiplies a float by `multiplier`.

## Task 9: Let's duck type an iterable object

**Mandatory**

Annotate the below function’s parameters and return values with the appropriate types

## Task 10: Duck typing - first element of a sequence

**Advanced**

Augment the following code with the correct duck-typed annotations:

```python
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
```

## Task 11: More involved type annotations

**Advanced**

Given the parameters and the return values, add type annotations to the function

```python
def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
```

## Task 12: Type Checking

**Advanced**

Use mypy to validate the following piece of code and apply any necessary changes.

```python
def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
```
