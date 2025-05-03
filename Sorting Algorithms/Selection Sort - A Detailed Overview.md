Selection Sort is a simple and intuitive comparison-based sorting algorithm. Although inefficient for large datasets, it helps build a foundation for understanding sorting concepts.

---

**How Selection Sort Works**

Selection Sort divides the input list into two parts: the sublist of items already sorted and the sublist of items remaining to be sorted. It repeatedly selects the smallest (or largest) element from the unsorted sublist and moves it to the end of the sorted sublist.

**Algorithm Steps:**

1. Start with the first element and assume it's the minimum.
    
2. Compare this minimum with the rest of the elements.
    
3. If a smaller element is found, update the minimum.
    
4. Swap the found minimum with the first element.
    
5. Move to the next position and repeat until the list is sorted.
    

---

**Python Code Example**

```python
# Selection Sort Function
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array is:", sorted_arr)
```

---

**Time Complexity**

- **Best Case:** O(n^2)
    
- **Average Case:** O(n^2)
    
- **Worst Case:** O(n^2)
    

**Space Complexity**

- O(1) – in-place sorting.
    

---

**Stability**

- Selection Sort is **not stable** by default, as it may change the relative order of equal elements.
    

---

**When to Use Selection Sort**

- When memory is limited.
    
- When the dataset is small.
    
- For educational purposes to illustrate sorting logic.
    

---

**Advantages**

- Easy to implement.
    
- Does not require additional memory (in-place).
    
- Performs well on small lists.
    

**Disadvantages**

- Poor performance on large lists.
    
- Not a stable sort.
    
- Inefficient compared to other algorithms like Merge Sort or Quick Sort.
    

---

**Conclusion**

Selection Sort is an elementary sorting algorithm known for its simplicity. While not suitable for large-scale data, it serves well in learning environments and memory-constrained scenarios. Understanding its logic provides a strong foundation for more advanced sorting techniques.