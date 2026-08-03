"""
Lesson 01: Instructor Solutions
solutions.py

These are reference solutions to assignment.md.
Do not read this until you have genuinely attempted every task yourself.
"""

import numpy as np


# ============================================================
# Task 1: Build an Array from Scratch
# ============================================================

daily_steps = np.array([6000, 8500, 9200, 3000, 11000, 7600, 4300])

print("Task 1")
print("daily_steps:", daily_steps)
print("shape:", daily_steps.shape)
print("dtype:", daily_steps.dtype)
print()


# ============================================================
# Task 2: Basic Statistics
# ============================================================

print("Task 2")
print("Total steps this week:", daily_steps.sum())
print("Average steps per day:", daily_steps.mean())
print("Highest single day:", daily_steps.max())
print("Lowest single day:", daily_steps.min())
print()


# ============================================================
# Task 3: Filtering with a Boolean Mask
# ============================================================

print("Task 3")
goal_mask = daily_steps > 8000
days_meeting_goal = daily_steps[goal_mask]
print("Boolean mask:", goal_mask)
print("Days meeting goal:", days_meeting_goal)
print("Number of days meeting goal:", goal_mask.sum())
print()


# ============================================================
# Task 4: 2D Array Practice
# ============================================================

weekly_scores = np.array([
    [88, 92, 79, 85],
    [70, 65, 74, 68],
    [95, 91, 89, 97],
])

print("Task 4")
print("Shape:", weekly_scores.shape)
print("Second student's scores:", weekly_scores[1, :])
print("Average score on first quiz:", weekly_scores[:, 0].mean())
print("Scores >= 70:", weekly_scores[weekly_scores >= 70])
print()


# ============================================================
# Task 5: Explanation (reference answer)
# ============================================================

explanation = """
Task 5 (reference answer -- yours should be in your own words):

A NumPy array is faster than a Python list because it stores all of its
values as a single, uniform data type in one continuous block of memory,
instead of storing separate Python objects scattered across memory the
way a list does. Because of this, when you perform an operation like
multiplying every element by 2, NumPy can hand the entire operation off
to fast, pre-compiled C code that processes all the numbers in one pass,
instead of Python having to loop through each element one at a time and
check its type at every step. This is called vectorization, and it is
the core reason NumPy -- and everything built on top of it, like
Pandas -- can handle large datasets efficiently.
"""

print(explanation)
