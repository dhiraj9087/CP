def boyer_moore_majority_vote(arr):
    candidate = None
    count = 0
    
    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    # Verify if the candidate is actually the majority
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return None  # No majority element

# Example usage
arr = [2, 2, 1, 1, 1, 2, 2]
print(boyer_moore_majority_vote(arr))  # Output: 2