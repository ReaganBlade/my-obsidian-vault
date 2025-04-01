def second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements
    
    stack = []
    first_max = second_max = float('-inf')

    for num in arr:
        while stack and stack[-1] < num:
            second_max = max(second_max, stack.pop())  # Track second largest
        stack.append(num)
        first_max = max(first_max, num)
    
    return second_max if second_max != float('-inf') else None

# Example usage:
arr = [5, 1, 9, 3, 7, 6]
print(second_largest(arr))  # Output: 7
