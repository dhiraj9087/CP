def find_next_smaller(arr):
    n = len(arr)
    result = [-1] * n  # Initialize result array with -1
    stack = []

    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        # Remove elements from stack that are greater than or equal to current element
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        
        # If stack is not empty, top of stack is the next smaller element
        if stack:
            result[i] = stack[-1]
        
        # Push current element to stack
        stack.append(arr[i])

    return result

# Example usage
arr = [2,1,5,6,2,3]
print("Original array:", arr)
print("Next smaller elements:", find_next_smaller(arr))