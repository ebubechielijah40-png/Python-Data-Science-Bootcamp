"""
Lesson 01: NumPy Fundamentals
examples.py

This file contains ONLY executable code examples.
Explanations live in README.md.
Run this file top to bottom with:

    python examples.py
"""

import numpy as np


# ============================================================
# BEGINNER EXAMPLE
# Creating arrays and comparing them to Python lists
# ============================================================

print("=== BEGINNER EXAMPLE ===")

python_list = [1, 2, 3, 4, 5]
numpy_array = np.array([1, 2, 3, 4, 5])

print("Python list:", python_list)
print("NumPy array:", numpy_array)
print("Type of python_list:", type(python_list))
print("Type of numpy_array:", type(numpy_array))

# A Python list cannot do math on all its elements at once.
# This next line is commented out because it would raise TypeError:
# python_list * 2 + 1

# A NumPy array CAN do math on all elements at once. This is called
# "vectorization."
doubled = numpy_array * 2
print("Array doubled:", doubled)

print()


# ============================================================
# INTERMEDIATE EXAMPLE
# Array shapes, indexing, and slicing
# ============================================================

print("=== INTERMEDIATE EXAMPLE ===")

grades = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [70, 65, 80],
])

print("Grades array:\n", grades)
print("Shape (rows, cols):", grades.shape)
print("Number of dimensions:", grades.ndim)
print("Total number of elements:", grades.size)
print("Data type of elements:", grades.dtype)

# Indexing: [row, column]
first_student_first_score = grades[0, 0]
print("First student, first score:", first_student_first_score)

# Slicing: grab an entire row
second_student_all_scores = grades[1, :]
print("Second student, all scores:", second_student_all_scores)

# Slicing: grab an entire column
first_test_all_students = grades[:, 0]
print("First test, all students:", first_test_all_students)

# Boolean masking: filter values based on a condition
passing_mask = grades >= 80
print("Boolean mask (True where grade >= 80):\n", passing_mask)
print("Only the passing grades:", grades[passing_mask])

print()


# ============================================================
# ADVANCED EXAMPLE
# Vectorized operations vs manual loops, and why speed matters
# ============================================================

print("=== ADVANCED EXAMPLE ===")

import time

size = 1_000_000
list_a = list(range(size))
array_a = np.arange(size)

# Method 1: Python loop (slow)
start = time.time()
result_loop = [x * 2 for x in list_a]
loop_time = time.time() - start

# Method 2: NumPy vectorized operation (fast)
start = time.time()
result_vectorized = array_a * 2
vector_time = time.time() - start

print(f"Python loop time:      {loop_time:.5f} seconds")
print(f"NumPy vectorized time: {vector_time:.5f} seconds")
print(f"NumPy was roughly {loop_time / vector_time:.1f}x faster")

# Real-world style example: normalizing a dataset
# (rescaling values to a 0-1 range, common in data science)
raw_scores = np.array([55, 70, 90, 60, 100, 45])

normalized = (raw_scores - raw_scores.min()) / (raw_scores.max() - raw_scores.min())
print("Raw scores:       ", raw_scores)
print("Normalized scores:", np.round(normalized, 2))

print()


# ============================================================
# BROKEN EXAMPLE 1: ValueError from mismatched shapes
# ============================================================

print("=== BROKEN EXAMPLE 1 ===")

try:
    a = np.array([1, 2, 3])
    b = np.array([1, 2])
    result = a + b
except ValueError as e:
    print("Caught an error on purpose:")
    print("ValueError:", e)

print()


# ============================================================
# BROKEN EXAMPLE 2: IndexError from out-of-range index
# ============================================================

print("=== BROKEN EXAMPLE 2 ===")

try:
    small_array = np.array([10, 20, 30])
    print(small_array[5])
except IndexError as e:
    print("Caught an error on purpose:")
    print("IndexError:", e)
