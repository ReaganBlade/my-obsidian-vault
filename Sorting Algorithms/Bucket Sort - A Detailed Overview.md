**Introduction to Bucket Sort**  
Bucket Sort is a non-comparative sorting algorithm that works by distributing elements into a number of buckets. Each bucket is sorted individually (either using a different sorting algorithm or recursively applying bucket sort). Finally, the contents of all the buckets are concatenated to get the sorted result.

**How Bucket Sort Works**

1. **Create Buckets:** Divide the range of input values into smaller, equally spaced intervals called "buckets."
    
2. **Distribute Elements into Buckets:** Place each element into its corresponding bucket based on the value.
    
3. **Sort Each Bucket:** Sort the individual buckets. This can be done using another sorting algorithm, such as insertion sort.
    
4. **Concatenate Sorted Buckets:** After sorting the individual buckets, concatenate them in order.
    

---

### **Python Code Example for Bucket Sort**

```python
def bucket_sort(arr):
    # Step 1: Create buckets
    num_buckets = len(arr)
    min_val, max_val = min(arr), max(arr)
    bucket_range = (max_val - min_val) / num_buckets
    
    buckets = [[] for _ in range(num_buckets)]
    
    # Step 2: Distribute elements into buckets
    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index == num_buckets:
            index -= 1
        buckets[index].append(num)
    
    # Step 3: Sort each bucket
    for i in range(num_buckets):
        buckets[i] = sorted(buckets[i])
    
    # Step 4: Concatenate all sorted buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr

# Example usage
arr = [0.42, 0.32, 0.53, 0.23, 0.71, 0.12, 0.56, 0.93]
sorted_arr = bucket_sort(arr)
print("Sorted Array:", sorted_arr)
```

---

### **Time and Space Complexity**

- **Time Complexity:**
    
    - Best Case: **O(n + k)** (if the data is uniformly distributed across buckets and each bucket is sorted using an efficient algorithm)
        
    - Average Case: **O(n + k)** (assuming uniform distribution, where **n** is the number of elements and **k** is the number of buckets)
        
    - Worst Case: **O(n²)** (if each bucket contains all the elements, and a comparison-based sorting algorithm is used for each bucket)
        
- **Space Complexity:** **O(n + k)**, where **n** is the number of elements and **k** is the number of buckets.
    

---

### **Advantages of Bucket Sort**

- **Efficient for Uniformly Distributed Data:** Bucket Sort performs well when input data is uniformly distributed across a range.
    
- **Can be Parallelized:** The sorting of each bucket can be done in parallel.
    
- **Can be Faster than Comparison-Based Sorts:** When used in the right scenario, it can outperform comparison-based algorithms like QuickSort and MergeSort.
    

---

### **Disadvantages of Bucket Sort**

- **Not Suitable for Non-Uniform Data:** If the input data is not uniformly distributed, bucket sort will not perform well.
    
- **Requires Additional Memory:** It requires extra space for buckets, making it space inefficient when the range of input data is large.
    
- **Inefficient for Large Datasets with Few Unique Keys:** If the input array contains few unique values, bucket sort might not be efficient.
    

---

### **Use Cases of Bucket Sort**

- **Sorting Floating Point Numbers:** Ideal for sorting decimal numbers or continuous data.
    
- **When Data Distribution is Known:** When you know that the data is uniformly distributed across a known range, bucket sort can be very efficient.
    
