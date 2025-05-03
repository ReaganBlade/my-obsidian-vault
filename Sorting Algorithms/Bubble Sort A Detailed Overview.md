Bubble Sort (Sinking Sort or Exchange Sort) is one of the simplest sorting algorithms in computer science. Though it is not suitable for large datasets due to its poor time complexity, it is often used in teaching because of its simplicity and ease of understanding.

---

**How Bubble Sort Works**

Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until no swaps are needed, indicating that the list is sorted. After each iteration, the largest unsorted element "bubbles up" to its correct position.

**Algorithm Steps:**

1. Start from the first element and compare it with the second.

2. If the first is greater than the second, swap them.

3. Move to the next pair and repeat.

4. Continue until the end of the list.

5. Repeat the entire process for the remaining unsorted part of the list.

---

**Python Code Example**

```python
# Bubble Sort Function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True
        if not swapped:
            break
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array is:", sorted_arr)
```

---

**Time Complexity**

- **Best Case:** O(n) – when the array is already sorted (with optimization).
    
- **Average Case:** O(n^2)
    
- **Worst Case:** O(n^2) – when the array is in reverse order.
    

**Space Complexity**

- O(1) – in-place sorting.
    

---

**Stability**

- Bubble Sort is a **stable** sorting algorithm, meaning it preserves the relative order of equal elements.
    

---

**When to Use Bubble Sort**

- For small datasets.
    
- When simplicity and clarity of code matter more than performance.
    
- In educational settings to demonstrate the concept of sorting.
    

---

**Advantages**

- Simple to understand and implement.
    
- Requires no extra space (in-place).
    
- Can detect if the list is already sorted.
    

**Disadvantages**

- Very inefficient for large datasets.
    
- High time complexity compared to more advanced sorting algorithms.
    

---

**Conclusion**

Bubble Sort is a fundamental sorting algorithm that is rarely used in real-world applications due to its inefficiency on large datasets. However, its conceptual simplicity makes it a great tool for teaching sorting mechanics and algorithmic thinking.