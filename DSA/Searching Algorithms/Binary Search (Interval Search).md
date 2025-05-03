Binary Search is a highly efficient algorithm for finding an element in a sorted list or array. It works by repeatedly dividing the search interval in half, thereby reducing the number of comparisons required to find the target.

---

**How Binary Search Works**

Binary Search compares the target value to the middle element of the array:

- If the target equals the middle element, the search ends.
    
- If the target is smaller, it continues on the left subarray.
    
- If the target is larger, it continues on the right subarray.
    

This process repeats until the element is found or the search space is exhausted.

**Algorithm Steps:**

1. Set `low = 0` and `high = length of array - 1`.
    
2. While `low <= high`:
    
    - Calculate `mid = (low + high) // 2`.
        
    - If `arr[mid] == target`, return `mid`.
        
    - If `arr[mid] < target`, set `low = mid + 1`.
        
    - If `arr[mid] > target`, set `high = mid - 1`.
        
3. If the loop ends, return -1 (not found).
    

---

**Python Code Example (Iterative Binary Search)**

```python
# Iterative Binary Search

def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

---

**Python Code Example (Recursive Binary Search)**

```python
# Recursive Binary Search

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)
```

---

**Time Complexity**

- **Best Case:** O(1) – when the target is the middle element.
    
- **Average Case:** O(log n)
    
- **Worst Case:** O(log n)
    

**Space Complexity**

- **Iterative:** O(1)
    
- **Recursive:** O(log n) due to the recursion stack
    

---

**When to Use Binary Search**

- When the dataset is sorted.
    
- When frequent and fast searches are needed.
    
- When handling large-scale data efficiently.
    

---

**Advantages**

- Significantly faster than Linear Search for large datasets.
    
- Time complexity is logarithmic (O(log n)).
    

**Disadvantages**

- Only works on sorted data.
    
- Recursive version consumes extra space on the stack.
    

---

**Conclusion**

Binary Search is a powerful technique for locating elements in sorted data. Whether implemented iteratively or recursively, it drastically reduces search time compared to Linear Search. Its performance and reliability make it a standard approach in many computing problems.