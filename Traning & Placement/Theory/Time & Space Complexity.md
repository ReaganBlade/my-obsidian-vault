## 1. Introduction

Time and Space Complexity are essential concepts in computer science and algorithm design. They help us analyze the efficiency of algorithms in terms of execution time and memory consumption.

---
## 2. Time Complexity

Time Complexity refers to the amount of time an algorithm takes to complete as a function of the input size (n). It helps in determining how fast an algorithm runs.
### 2.1 Asymptotic Notations

To express time complexity, we use asymptotic notations:

- **Big O (O)**: Worst-case complexity (upper bound)
- **Theta (Θ)**: Average-case complexity (tight bound)
- **Omega (Ω)**: Best-case complexity (lower bound)
### 2.2 Common Time Complexities

| Complexity   | Notation   | Example Algorithm                |
| ------------ | ---------- | -------------------------------- |
| Constant     | O(1)       | Accessing an element in an array |
| Logarithmic  | O(log n)   | Binary Search                    |
| Linear       | O(n)       | Linear Search                    |
| Linearithmic | O(n log n) | Merge Sort                       |
| Quadratic    | O(n²)      | Bubble Sort                      |
| Cubic        | O(n³)      | Matrix Multiplication            |
| Exponential  | O(2ⁿ)      | Recursive Fibonacci              |
| Factorial    | O(n!)      | Traveling Salesman Problem       |

### 2.3 How to Calculate Time Complexity

To determine the time complexity of an algorithm:
1. Identify the basic operations (e.g., comparisons, assignments).
2. Count the number of operations in terms of input size (n).
3. Consider worst-case scenarios.
4. Use asymptotic notation to express complexity.
#### Example 1: Loop Complexity
```python
for i in range(n):
    print(i)
```

- Runs **n** times → **O(n)** complexity.

#### Example 2: Nested Loop Complexity
```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

- Runs **n × n** times → **O(n²)** complexity.

#### Example 3: Logarithmic Complexity
```python
i = 1
while i < n:
    i *= 2
```

- Runs approximately **log₂(n)** times → **O(log n)** complexity.

---

## 3. Space Complexity
Space Complexity refers to the amount of memory required by an algorithm to run, including input data storage and auxiliary space.
### 3.1 Components of Space Complexity
- **Fixed Part**: Independent of input size (e.g., program code, constants).
- **Variable Part**: Depends on input size (e.g., dynamic memory allocation, recursion stack).
### 3.2 Common Space Complexities

| Complexity  | Notation | Example Algorithm       |
| ----------- | -------- | ----------------------- |
| Constant    | O(1)     | Swapping two variables  |
| Linear      | O(n)     | Storing an array        |
| Quadratic   | O(n²)    | Storing a 2D matrix     |
| Logarithmic | O(log n) | Recursive Binary Search |

### 3.3 How to Calculate Space Complexity
1. Identify variables, arrays, and data structures used.
2. Count memory required in terms of input size (n).
3. Consider recursion depth if applicable.
#### Example 1: Constant Space
```python
def sum_two_numbers(a, b):
    return a + b
```
- Uses fixed memory → **O(1)** complexity.

#### Example 2: Linear Space
```python
def store_elements(n):
    arr = [i for i in range(n)]
    return arr
```

- Uses an array of size **n** → **O(n)** complexity.
#### Example 3: Recursive Space
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```
- Recursion depth **n** → **O(n)** space complexity.
---
## 4. Trade-offs Between Time and Space Complexity
Sometimes, improving time complexity requires more space, and vice versa. For example:
- **Memoization** (Dynamic Programming) improves time complexity but increases space complexity.
- **In-place Sorting** algorithms reduce space complexity but may have higher time complexity.
### Example: Fibonacci Calculation
- **Recursive Approach**: O(2ⁿ) time, O(n) space.
- **Memoization Approach**: O(n) time, O(n) space.
- **Iterative Approach**: O(n) time, O(1) space.
---
## 5. Conclusion

Understanding time and space complexity is crucial for writing efficient algorithms. By analyzing complexity, developers can optimize code for better performance, ensuring scalability and efficiency in real-world applications.

---
## 6. References

- Introduction to Algorithms - Cormen et al.
- The Algorithm Design Manual - Steven S. Skiena