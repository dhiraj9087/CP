rating = [2,5,3,4,1]
n=len(rating)
x,y,z=0,1,2
ans=0
# while x<n and y<n and z<n:
#     if rating[x]<rating[y]:
#         if rating[y]<rating[z]:
#             ans+=1
#             y+=1
#             z+=1
#         else:
#             z+=1
#         x+=1
#         y+=1
#     else:
#         y+=1
        
#     x+=1
# print(ans)
for i in range(n):
    ll=ls=rl=rs=0
    for j in range(i):
        if rating[j]>rating[i]:
            ll+=1
        elif rating[j]<rating[i]:
            ls+=1
    for j in range(i+1,n):
        if rating[j]>rating[i]:
            rl+=1
        elif rating[j]<rating[i]:
            rs+=1
    ans+=(ls*rl)+(ll*rs)
print(ans)