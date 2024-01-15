# s="001110101101101111"
# k=10
s = "100011001"
k = 3
# s = "1011"
# k = 2
# one=s.count('1')

result = []
n = len(s)
l = 0
c = 0
mini=float('inf')
for r in range(n):
    if s[r] == '1':
        c += 1
    while c == k:
        result.append(s[l:r + 1])
        if s[l] == '1':
            c -= 1
        l += 1
q=float('inf')
d="q"
ans=[]
for i in result:
    if len(i)<=q:
        q=len(i)
        d=i

print(d)
for i in result:
    if len(i)==len(d):
        ans.append(i)
print(min(ans))

# print(ans)
# n = len(s)
# min_len = float('inf')
# start_index = -1
# for i in range(n):
#     count_ones = 0
#     for j in range(i, n):
#         if s[j] == '1':
#             count_ones += 1

#         if count_ones == k:
#             if j - i + 1 < min_len:
#                 min_len = j - i + 1
#                 start_index = i

# if start_index == -1:
#     print("")

# print(s[start_index:start_index + min_len])