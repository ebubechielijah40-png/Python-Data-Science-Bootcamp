# Lesson 01: NumPy Fundamentals

## Lesson Overview

NumPy (Numerical Python) is the foundation almost every other data science
library in Python is built on top of. Pandas uses it internally. Matplotlib
plots NumPy arrays(An array means an orderly arrangement, a large group or collection of things, or a specific structure in math and computer science). Scikit-learn expects NumPy arrays as input. Before you
can use any of those tools well, you need to understand what a NumPy array
actually is and why it exists.

In this lesson you will learn what problem NumPy solves, how to create
arrays, how to inspect them, how to select data out of them, and why
NumPy code runs much faster than plain Python loops.

---

## Learning Objectives

By the end of this lesson you will be able to:

- Explain the difference between a Python list and a NumPy array
- Create 1D and 2D NumPy arrays
- Read an array's shape, size, dimensions, and data type
- Select single values, rows, columns, and slices from an array
- Filter array data using boolean masks
- Explain, in your own words, why NumPy is faster than a Python loop
- Read and understand a `ValueError` and an `IndexError` produced by NumPy

---

## Prerequisites

Before this lesson you should already be comfortable with:

- Python variables and data types (int, float, string, boolean)
- Python lists and list indexing (`my_list[0]`)
- Basic `for` loops
- Reading a Python traceback

If any of those feel shaky, stop here and revisit them first. Everything
in this lesson builds directly on top of lists and loops.

---

## Real World Motivation

Imagine you have exam scores for 1,000 students and you need to add 5
bonus points to every single score. With a plain Python list, you would
need to write a loop that visits every single number one at a time.

With a spreadsheet of a million rows — which is a normal size in real
data science work — a loop like that becomes slow. Not "a little slow."
Slow enough that a task that should take a fraction of a second takes
several seconds or minutes, and if you repeat that operation thousands
of times while cleaning or exploring data, it adds up to real wasted
time every single day.

NumPy solves this by letting you say "add 5 to this entire collection of
numbers" as a single instruction, instead of writing a loop yourself.
Under the hood, NumPy does the looping in fast, compiled C code instead
of slow, interpreted Python code. This is the single most important idea
in this lesson. Everything else builds on it.

---

## Theory

A Python list is a general-purpose container. It can hold any mix of
types — numbers, strings, other lists, anything — and Python has to check
the type of every single item every time it does something with it. That
flexibility is useful, but it is also slow when you're doing math on
thousands or millions of numbers.

A NumPy array is different. It is:

1. **Homogeneous** — every element must be the same data type (all
   integers, or all floats, but not mixed).
2. **Fixed in structure** — the array knows its shape (how many rows,
   how many columns) up front.
3. **Stored in one continuous block of memory** — instead of scattered
   Python objects, the numbers sit next to each other in memory, which
   is much faster for a computer to process.

Because of these three properties, NumPy can hand off math operations to
highly optimized, pre-compiled code instead of interpreting instructions
one Python line at a time. This is called **vectorization**: applying an
operation to an entire array at once, instead of writing a loop.

---

## Internal Explanation

When you write:

```python
numpy_array * 2
```

Python does NOT loop through the array one number at a time the way it
would with a list. Instead, NumPy recognizes this as a vectorized
operation and passes the entire array down to compiled C code that
performs the multiplication on all elements simultaneously (or in tight,
optimized loops written in C, not Python).

This is why the "Advanced Example" below shows NumPy being several times
faster than a plain Python loop performing the identical task.

---

## Syntax

```python
import numpy as np

# Creating arrays
array_1d = np.array([1, 2, 3])
array_2d = np.array([[1, 2], [3, 4]])

# Inspecting arrays
array.shape   # dimensions, as a tuple
array.ndim    # number of dimensions
array.size    # total number of elements
array.dtype   # data type of the elements

# Indexing and slicing
array[0]        # first element (1D)
array[0, 1]     # row 0, column 1 (2D)
array[:, 0]     # all rows, column 0
array[1, :]     # row 1, all columns

# Boolean masking
mask = array >= 80
filtered = array[mask]
```

`np` is the standard, universally used alias for `numpy`. You will see
`import numpy as np` at the top of nearly every data science file you
ever read. Always use it — it is a strong convention, and deviating from
it will confuse anyone reading your code.

---

## Code Anatomy

```python
grades = np.array([
    [85, 90, 78],
    [92, 88, 95],
])
```

- `np` — the NumPy module, imported earlier
- `.array(...)` — a function that converts a Python list (or list of
  lists) into a NumPy array
- `[[85, 90, 78], [92, 88, 95]]` — a Python list containing two inner
  lists; each inner list becomes one row of the resulting 2D array
- `grades` — the variable now holding a NumPy array object, not a plain
  list

---

## Execution Flow

1. Python evaluates the list literal `[[85, 90, 78], [92, 88, 95]]` first,
   the same as it would for any list.
2. `np.array()` receives that list and inspects its structure — how many
   inner lists, how long each one is, what type the numbers are.
3. NumPy allocates a single contiguous block of memory sized to hold all
   the numbers.
4. NumPy copies the numbers into that memory block in a specific,
   predictable layout.
5. The variable `grades` is bound to this new NumPy array object, which
   knows its own shape, size, and data type from this point forward.

---

## Beginner Example

See `examples.py`, section `BEGINNER EXAMPLE`.

This example creates a Python list and a NumPy array holding the same
numbers, and shows that you can multiply the NumPy array directly, while
doing the same to a plain list would raise a `TypeError` (multiplying a
list by an integer repeats the list instead of doing math on it).

---

## Intermediate Example

See `examples.py`, section `INTERMEDIATE EXAMPLE`.

This example builds a 2D array representing student grades, inspects its
shape and data type, indexes into specific rows and columns, and uses a
boolean mask to pull out only the passing grades.

---

## Advanced Example

See `examples.py`, section `ADVANCED EXAMPLE`.

This example times a Python loop against an equivalent NumPy vectorized
operation on one million numbers, and normalizes a small dataset to a
0–1 range — a real technique used before feeding data into many machine
learning models.

---

## Line-by-Line Explanation

```python
passing_mask = grades >= 80
```

- `grades >= 80` — NumPy compares **every element** in `grades` against
  80 and returns a brand new array of the same shape, filled with
  `True` and `False` values. This is another example of vectorization:
  no loop was written, but every element was checked.
- `passing_mask` — this variable now holds that array of `True`/`False`
  values, not the grades themselves.

```python
grades[passing_mask]
```

- When you index an array using another array of `True`/`False` values
  (the same shape), NumPy returns only the elements where the mask is
  `True`, flattened into a 1D array. This is called **boolean masking**
  and it is one of the most common patterns in all of data science —
  you will use this exact idea constantly in Pandas.

```python
normalized = (raw_scores - raw_scores.min()) / (raw_scores.max() - raw_scores.min())
```

- `raw_scores.min()` and `raw_scores.max()` — methods that scan the
  array and return its smallest and largest values.
- `raw_scores - raw_scores.min()` — subtracts the minimum from every
  element (vectorized), shifting the smallest value to 0.
- Dividing by `(max - min)` scales everything into a 0–1 range.
- This single line replaces what would otherwise be a multi-line loop
  with an if-check and a running min/max tracker.

---

## Common Errors

### ValueError: shape mismatch

```python
a = np.array([1, 2, 3])
b = np.array([1, 2])
a + b
```

Produces:

```
ValueError: operands could not be broadcast together with shapes (3,) (2,)
```

**Why it breaks:** NumPy needs to know, for every position, which
element in `a` pairs with which element in `b`. With 3 elements in one
array and 2 in the other, there's no way to pair them up evenly.

**The fix:** make sure both arrays are the same shape, or intentionally
use a shape that NumPy knows how to "broadcast" (a topic for a later
lesson). For now, the practical fix is simple — check `.shape` on both
arrays before combining them.

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)   # [11 22 33]  -- works, because shapes match
```

### IndexError: index out of range

```python
small_array = np.array([10, 20, 30])
small_array[5]
```

Produces:

```
IndexError: index 5 is out of bounds for axis 0 with size 3
```

**Why it breaks:** `small_array` only has 3 elements, at positions 0, 1,
and 2. Position 5 does not exist.

**The fix:** check `.shape` or `.size` before indexing, or use Python's
`len()`, which also works on NumPy arrays.

```python
print(small_array.shape)   # (3,)
print(small_array[2])      # 30 -- the last valid index
```

---

## Debugging

When a NumPy line throws an error, work through these steps in order:

1. **Read the error type first** — `ValueError` almost always means a
   shape or value mismatch. `IndexError` means you asked for a position
   that doesn't exist. `TypeError` usually means you mixed incompatible
   types.
2. **Print `.shape` on every array involved** before the line that
   failed. Shape mismatches are the single most common NumPy bug for
   beginners, and printing shapes makes the problem visible immediately.
3. **Print the array itself** to confirm it contains what you think it
   contains — a common mistake is assuming an array is 1D when it's
   actually 2D, or vice versa.
4. **Use VS Code's hover feature** — hovering over a variable that holds
   a NumPy array will often show you its shape and dtype directly,
   without needing to add a print statement.

---

## Best Practices

- Always `import numpy as np`. Never import it under a different alias.
- Prefer vectorized operations (`array * 2`) over Python loops whenever
  you're working with NumPy arrays. If you find yourself writing
  `for i in range(len(array)):`, stop and ask whether a vectorized
  operation could do the same thing.
- Check `.shape` early and often, especially before combining two
  arrays. Most NumPy bugs are shape bugs.
- Don't mix Python lists and NumPy arrays carelessly in the same
  expression — convert lists to arrays with `np.array()` first.

---

## Performance Notes

The measured results in `examples.py` on this machine were:

- Python loop over 1,000,000 numbers: **~0.52 seconds**
- NumPy vectorized operation over the same 1,000,000 numbers: **~0.10
  seconds**
- NumPy was roughly **5x faster**

Your own numbers will differ depending on your machine, but NumPy will
consistently outperform a plain Python loop, and the gap grows as the
data gets larger. This is not a minor convenience — it's the reason
NumPy exists, and the reason every other data science library is built
on top of it instead of on plain Python lists.

--

A NumPy array is a fixed-type, fixed-shape, memory-efficient alternative
to a Python list, built specifically so that math operations can run on
entire collections of numbers at once instead of one at a time. This
speed advantage — vectorization — is the foundation that Pandas,
Matplotlib, and scikit-learn are all built on top of.

---

## Key Takeaways

- NumPy arrays must hold a single, consistent data type.
- Vectorized operations replace explicit loops and are significantly
  faster.
- `.shape`, `.ndim`, `.size`, and `.dtype` are your primary tools for
  inspecting an array.
- Boolean masking (`array[array >= 80]`) is a core pattern you will use
  constantly in Pandas.
- `ValueError` from NumPy almost always means a shape mismatch — check
  `.shape` first when debugging.

---

## Preview of Next Lesson

Lesson 02 goes deeper into NumPy: multi-dimensional array manipulation,
reshaping arrays, broadcasting (how NumPy handles arrays of different
shapes), and the aggregate functions (`sum`, `mean`, `std`) you will use
constantly once you move into Pandas in Lesson 03.
