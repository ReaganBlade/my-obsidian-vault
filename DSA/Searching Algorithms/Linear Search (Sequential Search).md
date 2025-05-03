Linear Search, also known as Sequential Search, is one of the simplest and most fundamental searching algorithms in computer science. It is primarily used to find the position of a target element within a list or an array. The search progresses sequentially, element by element, until the desired value is found or the end of the data structure is reached.

---

**How Linear Search Works**

Linear Search starts at the beginning of a data structure and checks each element one by one. If the element matches the target, the index of that element is returned. If the search reaches the end of the structure without finding the element, the algorithm concludes that the element is not present.

**Algorithm Steps:**

1. Start from the first element of the array.
    
2. Compare the current element with the target.
    
3. If it matches, return the index.
    
4. If it doesn't match, move to the next element.
    
5. Repeat steps 2-4 until the end of the array.
    
6. If the element is not found, return -1 (or an equivalent indicator).
    

---

**Python Code Example**

```python
# Linear Search Function
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Target found, return index
    return -1  # Target not found

# Example usage
my_list = [10, 20, 30, 40, 50]
target = 30
result = linear_search(my_list, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
```

---

**Time Complexity**

- **Best Case:** O(1) – when the target is the first element.
    
- **Average Case:** O(n) – where n is the number of elements.
    
- **Worst Case:** O(n) – when the element is at the end or not present.
    

**Space Complexity**

- O(1) – as it does not require any extra space apart from a few variables.
    

---

**When to Use Linear Search**

- When dealing with small datasets.
    
- When the data is unsorted.
    
- When simplicity is more important than performance.
    
- When only one or a few searches are to be performed.
    

---

**Advantages**

- Easy to implement and understand.
    
- Does not require the data to be sorted.
    
- Works on any linear data structure (arrays, linked lists, etc.).
    

**Disadvantages**

- Inefficient for large datasets.
    
- Slower compared to more advanced searching algorithms like Binary Search.
    

---

**Comparison with Other Search Algorithms**

- **Binary Search:** More efficient but requires sorted data. Time complexity is O(log n).
    
- **Hashing:** Offers O(1) average time for search but needs additional memory and setup.
    

---

**Conclusion**

Linear Search is a fundamental algorithm that lays the groundwork for understanding more advanced searching techniques. While it is not the most efficient in terms of performance, its simplicity and ease of use make it valuable in certain scenarios, especially with small or unsorted datasets.