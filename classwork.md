# Lesson 01: Classwork

Work through these during the lesson session, alongside the instructor.
These are meant to be done live, not alone — if you get stuck, that's the
point where you ask questions.

---

## Exercise 1: List vs Array

1. Create a Python list called `temps_list` containing: `70, 72, 68, 75, 80`
2. Create a NumPy array called `temps_array` containing the same numbers
3. Try to add 10 to every value in `temps_list` using `temps_list + 10`
   and observe the error
4. Add 10 to every value in `temps_array` using `temps_array + 10` and
   confirm it works
5. In one sentence, explain why the list version failed and the array
   version worked

---

## Exercise 2: Inspecting a 2D Array

Given this array:

```python
sales = np.array([
    [120, 150, 90],
    [200, 180, 220],
    [95, 100, 110],
])
```

Answer the following, using code (not just by counting manually):

1. What is `sales.shape`?
2. What is `sales.ndim`?
3. What is `sales.size`?
4. What is `sales.dtype`?

---

## Exercise 3: Indexing and Slicing

Using the `sales` array from Exercise 2:

1. Print the value in row 1, column 2
2. Print the entire second row (index 1)
3. Print the entire third column (index 2)
4. Print only the values greater than 150 using a boolean mask

---

## Exercise 4: Fix the Broken Code

The following code is meant to add two arrays together but currently
raises an error. Run it, read the traceback, and fix it so it works.

```python
prices = np.array([10, 20, 30, 40])
discounts = np.array([1, 2, 3])

final_prices = prices - discounts
print(final_prices)
```

Write down: what was the error type, what caused it, and how you fixed
it.
