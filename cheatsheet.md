# Lesson 01: Cheatsheet — NumPy Fundamentals

## Import

```python
import numpy as np
```

## Creating Arrays

```python
np.array([1, 2, 3])              # 1D array
np.array([[1, 2], [3, 4]])       # 2D array
np.zeros(5)                      # array of 5 zeros
np.ones((2, 3))                  # 2x3 array of ones
np.arange(0, 10, 2)              # [0, 2, 4, 6, 8]
```

## Inspecting Arrays

```python
arr.shape      # dimensions, e.g. (3, 4)
arr.ndim       # number of dimensions
arr.size       # total number of elements
arr.dtype      # data type of elements
```

## Indexing and Slicing

```python
arr[0]         # first element (1D)
arr[-1]        # last element
arr[0, 1]      # row 0, column 1 (2D)
arr[:, 0]      # all rows, column 0
arr[1, :]      # row 1, all columns
arr[1:3]       # slice, elements at index 1 and 2
```

## Boolean Masking

```python
mask = arr > 10
arr[mask]              # elements where mask is True
arr[arr > 10]          # same thing, one line
mask.sum()             # count of True values
```

## Math Operations (all vectorized)

```python
arr + 5
arr - 5
arr * 2
arr / 2
arr ** 2
```

## Aggregate Functions

```python
arr.sum()
arr.mean()
arr.max()
arr.min()
arr.std()
```

## Common Errors — Quick Reference

| Error | Usual Cause | First thing to check |
|---|---|---|
| `ValueError: broadcast` | Two arrays have incompatible shapes | `.shape` on both arrays |
| `IndexError` | Index doesn't exist in the array | `.shape` or `len()` |
| `TypeError` | Mixed incompatible types | `.dtype` |
