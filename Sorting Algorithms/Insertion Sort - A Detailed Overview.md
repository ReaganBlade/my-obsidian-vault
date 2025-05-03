Insertion Sort is a simple and intuitive sorting algorithm, often compared to the method of sorting playing cards in hand. It is efficient for small datasets and nearly sorted data.

---

**How Insertion Sort Works**

Insertion Sort builds the sorted array one element at a time by repeatedly taking the next unsorted element and inserting it into the correct position among the already sorted elements.

**Algorithm Steps:**

1. Assume the first element is already sorted.
    
2. Pick the next element.
    
3. Compare it with elements in the sorted part.
    
4. Shift larger elements one position to the right.
    
5. Insert the element at its correct position.
    
6. Repeat until the array is sorted.
    

---

**Python Code Example**

```python
# Insertion Sort Function
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array is:", sorted_arr)
```

---

**Time Complexity**

- **Best Case:** O(n) – when the array is already sorted.
    
- **Average Case:** O(n^2)
    
- **Worst Case:** O(n^2) – when the array is reverse sorted.
    

**Space Complexity**

- O(1) – in-place sorting.
    

---

**Stability**

- Insertion Sort is **stable**, preserving the relative order of equal elements.
    

---

**When to Use Insertion Sort**

- When the dataset is small.
    
- When the list is nearly sorted.
    
- In online algorithms where data arrives over time.
    

---

**Advantages**

- Simple to understand and implement.
    
- Efficient for small and nearly sorted datasets.
    
- Stable and in-place.
    

**Disadvantages**

- Poor performance on large lists.
    
- Quadratic time complexity in the average and worst case.
    

---

**Conclusion**

Insertion Sort is a fundamental algorithm ideal for small or nearly sorted datasets. Though inefficient for large lists, its simplicity and stability make it useful in specific scenarios and educational contexts.