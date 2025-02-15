# Python Arrays - Quick Revision Notes

## 1. Introduction to Arrays

- **Linear Data Structure** → Elements stored in a contiguous block of memory.
- **Fixed Size** → Cannot resize dynamically (use lists for dynamic arrays in Python).
- **Indexed Access** → Direct access using indices.
- **Homogeneous** → Stores elements of the same data type.

## 2. Types of Arrays

- **1D Array:** `[1, 2, 3, 4]`
- **2D Array:** `[[1, 2], [3, 4]]`
- **Multi-Dimensional Array:** `[[[1, 2,3],[4, 5, 6]], [[8, 9, 10],[11, 12, 13]]]`

## 3. Advantages of Arrays

1. **Random Access** → O(1) time complexity for accessing an element.
2. **Efficiency** → Memory-efficient compared to linked lists.
3. **Sorting & Searching** → Works well with sorting and searching algorithms.

## 4. Limitations of Arrays

4. **Fixed Size** → Predefined size restricts flexibility.
5. **Insertion/Deletion Overhead** → Costly as elements must be shifted.
6. **Homogeneous Data** → Cannot store different data types in the same array.

## 5. Basic Array Operations

|Operation|Description|Time Complexity|
|---|---|---|
|**Traversal**|Accessing each element|O(n)|
|**Insertion**|Adding element at a position|O(n)|
|**Deletion**|Removing an element|O(n)|
|**Search**|Finding an element|O(n) (linear) / O(log n) (binary)|
|**Sort**|Arranging elements in order|O(n log n)|
|**Merging**|Combining two arrays|O(n)|

## 6. Memory Address Calculation

### 1D Array

For an array `A` with base address `B`, element size `S`, and index `i`:

- Address of `A[i] = B + (i * S)`

### 2D Array

For a 2D array `A[m][n]`, row `i`, column `j`:

#### Row-Major Order:

- Address of `A[i][j] = B + [(i * n) + j] * S`

#### Column-Major Order:

- Address of `A[i][j] = B + [(j * m) + i] * S`

### Python's Memory Calculation Method

Python uses **dynamic memory allocation** via lists instead of fixed-size arrays. The memory is managed by the **Python memory manager** and the **garbage collector** to optimize storage. Unlike low-level languages like C, Python does not require explicit memory address calculations because it uses **pointers and references** internally.

## 7. Practice Problem: Count Occurrences of Elements

```python
def count_all_freq(arr: list[int]) -> dict:
    freq = {}
    for i in arr:
        freq[i] = freq.get(i, 0) + 1
    return freq
```

## 8. Advanced Concepts

- **NumPy Arrays** → Efficient array handling using the NumPy library.
- **Dynamic Arrays** → Implemented using Python lists (resize dynamically).
- **Sparse Arrays** → Arrays with mostly zero values, stored efficiently.
- **Jagged Arrays** → Arrays with rows of varying sizes.

## 9. Key Libraries for Arrays in Python

7. **array** → Basic array handling (homogeneous elements).
8. **NumPy** → Multi-dimensional arrays with high performance.
9. **pandas** → DataFrame structure built on arrays for efficient data handling.

### Quick Recap:

✅ Arrays have **fixed size**, **indexed access**, and **homogeneous** elements. ✅ Efficient for **searching, sorting, and traversal** but **slow for insertions/deletions**. ✅ Memory address calculation depends on **row-major or column-major order**. ✅ Python uses **dynamic memory allocation** instead of fixed-size arrays. ✅ Use **NumPy** for advanced array operations.

---

This should help you revise **Python Arrays** quickly from basics to advanced topics!