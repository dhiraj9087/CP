def counting_sort(arr):
    if not arr:
        return arr

    # Find range of array elements
    max_element = max(arr)
    min_element = min(arr)
    range_of_elements = max_element - min_element + 1

    # Create a count array to store count of individual elements
    count_arr = [0 for _ in range(range_of_elements)]

    # Store count of each character
    for num in arr:
        count_arr[num - min_element] += 1

    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    # Build the output array
    output = [0 for _ in range(len(arr))]
    for i in range(len(arr)-1, -1, -1):
        output[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1

    return output

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))  # Output: [1, 2, 2, 3, 3, 4, 8]