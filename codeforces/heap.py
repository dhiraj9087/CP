import heapq

def findKthLargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        # print(heap)
        if len(heap) > k:
            heapq.heappop(heap)
        print(heap)

# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
findKthLargest(nums,k)
