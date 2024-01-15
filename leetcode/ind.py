def main():
    nums = [2,1]
    indexDifference = 0
    valueDifference = 0
    arr = [5,1,4,1]
    index_difference = 2
    value_difference = 4
    # n = len(arr)
    result = []
    n = len(arr)
    x = arr[0]
    idx1 = 0
    mini = arr[0]
    idx2 = 0

    for i in range(index_difference, n):
        if arr[i - index_difference] > x:
            x = arr[i - index_difference]
            idx1 = i - index_difference
        if arr[i - index_difference] < mini:
            mini = arr[i - index_difference]
            idx2 = i - index_difference
        if abs(arr[i] - x) >= value_difference:
            return [idx1, i]
        if abs(arr[i] - mini) >= value_difference:
            result.extend([idx2, i])
    if result:
        return [result[0],result[1]]
    return [-1,-1]
    # n = len(nums)
    # ans = []
    # a,mini = float('-inf'),float('inf')
    # ind1,ind2 = 0,0
    # for i in range(indexDifference, n):
    #     if nums[i - indexDifference] > a:
    #         a = nums[i - indexDifference]
    #         ind1 = i - indexDifference
    #     if nums[i - indexDifference] < mini:
    #         mini = nums[i - indexDifference]
    #         ind2 = i - indexDifference
    #     if abs(nums[i] - a) >= valueDifference:
    #         return [ind1, i]
    #     if abs(nums[i] - mini) >= valueDifference:
    #         ans.extend([ind2, i])
    # return [-1, -1]
print(main())