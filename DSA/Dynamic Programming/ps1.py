'''
You are given an array `arr` of size `n`, where each element represents an index in another array `nums`. You need to return an output array where `result[i]` is the sum of elements in `nums` from index `0` to `arr[i]`.

Example:

Input:

nums = [3, 1, 4, 1, 5, 9, 2, 6]  
arr = [2, 4, 6]  


Output:
[3+1+4, 3+1+4+1+5, 3+1+4+1+5+9+2]  
=> [8, 14, 23]
'''

# Memoization

def getQueryResult(n: int, arr: list[int], queries: list[int]) -> list[int]:
    # create a dp array
    dp = [0] * (n + 1)
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]

    for i in range(3, n + 1):
        dp[i] = dp[i-1] + arr[i]

    result = []
    for i in queries:
        result.append(dp[i])

    return result
