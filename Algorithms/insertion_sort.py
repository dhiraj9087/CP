def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        print(arr)
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]