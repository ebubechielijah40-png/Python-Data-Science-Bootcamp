# Lesson 01: Assignment

Complete this on your own, after the lesson. Do not look at
`solutions.py` until you've genuinely attempted every task — copying the
solution without struggling first is the fastest way to stay dependent
on AI, which is the exact opposite of this bootcamp's goal.

---

## Task 1: Build an Array from Scratch

Create a NumPy array called `daily_steps` representing the number of
steps you (hypothetically) walked over 7 days. Use any 7 numbers you
like, each between 2,000 and 12,000.

Print:
- The array itself
- Its shape
- Its data type

---

## Task 2: Basic Statistics

Using `daily_steps` from Task 1, calculate and print:

- The total steps for the week (`.sum()`)
- The average steps per day (`.mean()`)
- The highest single day (`.max()`)
- The lowest single day (`.min()`)

You have not been taught `.sum()`, `.mean()`, `.max()`, or `.min()`
explicitly in the README — this is intentional. Use Python's built-in
`help(np.ndarray.mean)` or your editor's hover documentation to figure
out the syntax. Learning to read documentation is part of the
assignment.

---

## Task 3: Filtering with a Boolean Mask

Using `daily_steps` again:

1. Create a boolean mask for days where you walked more than 8,000 steps
2. Use that mask to print only the days that met the 8,000-step goal
3. Print how many days met the goal (hint: a boolean array can be
   summed — `True` counts as 1 and `False` counts as 0)

---

## Task 4: 2D Array Practice

Create a 2D array called `weekly_scores` representing 3 students' scores
across 4 quizzes (3 rows, 4 columns — make up any reasonable numbers).

1. Print the shape to confirm it's 3 rows by 4 columns
2. Print the second student's (index 1) scores across all 4 quizzes
3. Print the average score on the first quiz (index 0) across all 3
   students
4. Print all scores greater than or equal to 70 using a boolean mask

---

## Task 5: Explain in Your Own Words (no code)

Write 3–5 sentences answering: why is a NumPy array faster than a Python
list for doing math on large amounts of data? Do not copy from the
README — write it in your own words. If you can't explain it without
looking, that's a sign to re-read the "Theory" and "Internal
Explanation" sections before moving to Lesson 02.
