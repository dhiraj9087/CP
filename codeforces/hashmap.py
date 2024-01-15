# nums1 = [1,2,3]
# nums2 = [2,4,6]
# hash_map_1 = {}
# hash_map_2 = {}

# for num in nums1:
#     hash_map_1[num] = hash_map_1.get(num, 0) + 1
    
# for num in nums2:
#     hash_map_2[num] = hash_map_2.get(num, 0) + 1
# print(hash_map_1)
# print(hash_map_2)
arr = [1,2,2,1,1,3]
# arr.sort()
hash_map={}
for i in arr:
    hash_map[i] = hash_map.get(i, 0) + 1
    print(hash_map[i])

print(hash_map)
