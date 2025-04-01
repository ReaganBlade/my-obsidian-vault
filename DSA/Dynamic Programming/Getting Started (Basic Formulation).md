### **Problem Statement:**

You are given an array `arr` of size `n`, where each element represents an index in another array `nums`. You need to return an output array where `result[i]` is the sum of elements in `nums` from index `0` to `arr[i]`.

### **Example:**

#### **Input:**

```plaintext
nums = [3, 1, 4, 1, 5, 9, 2, 6]  
arr = [2, 4, 6]  
```

#### **Output:**

```plaintext
[3+1+4, 3+1+4+1+5, 3+1+4+1+5+9+2]  
=> [8, 14, 23]
```

### **Efficient Approach:**

1. **Precompute prefix sums:** Create a `prefix[]` array where `prefix[i] = sum(nums[0] to nums[i])`.
2. **Answer queries in O(1):** For each `arr[i]`, return `prefix[arr[i]]`.

### **Code:**

```python
def prefixSumQueries(nums, arr):
    prefix = [0] * (len(nums) + 1)
    
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    
    return [prefix[idx] for idx in arr]

# Example Usage
nums = [3, 1, 4, 1, 5, 9, 2, 6]
arr = [2, 4, 6]
print(prefixSumQueries(nums, arr))  # Output: [8, 14, 23]
```

This runs in **O(n) for preprocessing** and **O(1) per query**, making it efficient.  
Does this match your problem?