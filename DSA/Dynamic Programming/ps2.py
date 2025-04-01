'''
Given an array `a` of size `n`, find the maximum sum of elements such that no two selected elements are adjacent in the array.

Test Case 1:
Input:  
a = [3, 2, 7, 10]

Output: 13

Explanation:  
Pick `3` and `10` (3 + 10 = 13).

'''

def maxNonAdjSum(arr: list[int], n: int) -> int:

    # 1. Create an empty DP array
    dp = [0] * (n)
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(3, n):
        dp[i] = max(dp[i-1], arr[i] + dp[i-2])

    return dp[n-1]


print(maxNonAdjSum([3, 2, 7, 10], 4))