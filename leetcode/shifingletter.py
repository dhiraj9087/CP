s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]
# s = "dztz"
# shifts = [[0,0,0],[1,1,1]]
n=len(s)
let= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s=list(s)
chg=0
arr=[0 for i in range(n+1)]
for i in range(len(shifts)):
    st,e,d=shifts[i]
    if d==1:
        chg=1
    else:
        chg=-1
    arr[st]+=chg
    arr[e+1]-=chg

ans=0
for i in range(1,len(s)):
    arr[i]+=arr[i-1]
print(arr)
result=[]
for i in range(n):
    result.append(chr(((ord(s[i]) - ord('a') + v[i]) % 26 + 26) % 26 + ord('a')))




# cum_shifts = [0 for _ in range(len(s)+1)]
        
#         for st, end, d in shifts:
#             if d == 0:
#                 cum_shifts[st] -= 1
#                 cum_shifts[end+1] += 1
#             else:
#                 cum_shifts[st] += 1
#                 cum_shifts[end+1] -= 1
        
#         cum_sum = 0
#         for i in range(len(s)):
#             cum_sum += cum_shifts[i]
            
#             new_code = (((ord(s[i]) + cum_sum) - 97) % 26) + 97
#             s = s[:i] + chr(new_code) + s[i+1:]
        
#         return s