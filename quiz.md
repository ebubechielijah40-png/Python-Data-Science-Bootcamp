# Lesson 01: Quiz

Answer without looking back at the README first. Check yourself after.

---

**1.** What is the main structural difference between a Python list and
a NumPy array?

**2.** What does "vectorization" mean, in your own words?

**3.** Given `arr = np.array([[1, 2, 3], [4, 5, 6]])`, what does
`arr.shape` return?

**4.** What is the difference between `arr[0]` and `arr[:, 0]` on a 2D
array?

**5.** What will this code print?

```python
a = np.array([10, 20, 30, 40])
mask = a > 20
print(a[mask])
```

**6.** Why does `np.array([1, 2, 3]) + np.array([1, 2])` raise a
`ValueError`?

**7.** True or False: A NumPy array can hold a mix of integers and
strings the same way a Python list can.

**8.** What NumPy attribute would you check first if you got a
`ValueError` mentioning "broadcast"?

---

## Answer Key

1. A NumPy array requires all elements to be the same data type and has
   a fixed shape; a Python list can hold mixed types and has no fixed
   structure.
2. Applying an operation to an entire array at once instead of looping
   through elements one at a time in Python.
3. `(2, 3)` — 2 rows, 3 columns.
4. `arr[0]` returns the first row; `arr[:, 0]` returns the first column
   (all rows, column index 0).
5. `[30 40]`
6. Because the two arrays have different shapes ((3,) and (2,)) and
   NumPy has no way to pair up their elements one-to-one.
7. False — NumPy arrays must be homogeneous (one consistent data type).
8. `.shape` — shape mismatches are the most common cause of broadcast
   errors.
