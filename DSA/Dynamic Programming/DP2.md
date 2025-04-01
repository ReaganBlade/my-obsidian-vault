# Steps To Solve a Dynamic Programming Problem

1. Create an empty DP array -> `dp[n + 1]`

2. Find value of `dp[1], dp[2], dp[3]` by basic observation.

3. Create a general Formula

4. `dp[1], dp[2] ... dp[n]` using loop and the general formula

5. `dp[5]` in general is the final answer


### **Problem Statement:**  
Given an array `a` of size `n`, find the maximum sum of elements such that no two selected elements are adjacent in the array.

### **Example Test Cases:**  

#### **Test Case 1:**  
**Input:**  
```plaintext
a = [3, 2, 7, 10]
```
**Output:**  
```plaintext
13
```
**Explanation:**  
Pick `3` and `10` (3 + 10 = 13).

---

#### **Test Case 2:**  
**Input:**  
```plaintext
a = [3, 2, 5, 10, 7]
```
**Output:**  
```plaintext
15
```
**Explanation:**  
Pick `3`, `10`, and `2` (3 + 10 + 2 = 15).

---

#### **Test Case 3:**  
**Input:**  
```plaintext
a = [3, 5, 10, 100, 10, 5]
```
**Output:**  
```plaintext
108
```
**Explanation:**  
Pick `3`, `10`, and `100` (3 + 10 + 100 = 108).