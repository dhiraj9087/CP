arr = [2,1,3,5,4,6,7]
k = 2
# arr=[3,2,1]
# k=10
cnt=0
d={}
# while k>cnt:
#     if arr[0]>arr[1]:
#         if arr[0] in d:
#             d[arr[0]]+=1
#         else:
#             d[arr[0]]=1
#         a=d.get(arr[0],0)
#         cnt=max(cnt,a)
#         var=arr[1]
#         arr.remove(arr[1])
#         arr.append(var)
#     else:
#         if arr[1] in d:
#             d[arr[1]]+=1
#         else:
#             d[arr[1]]=1
#         a=d.get(arr[1],0)
#         cnt=max(cnt,a)
#         var=arr[0]
#         arr.remove(arr[0])
#         arr.append(var)
# # print(cnt)
# for i in d:
#     if d[i]==k:
#         print(i)
#         break
maxi=float('-inf')
for i in range(len(arr)):
    if cnt==k:
        print(arr[i])
        break
    if arr[i]>maxi:
        maxi=arr[i]
        # if arr[i] in d:
        #     d[arr[i]]+=1
        # else:
        #     d[arr[i]]=1
        # cnt=d[arr[i]]
        cnt+=1
    else:
        cnt=1

# if k>len(arr)//2:
# 	return(max(arr))
# else:
# 	count=0
# 	curr_max=arr[0]
# 	for i in range(1,len(arr)):
# 	  if count==k:
# 		return(curr_max)
# 		break
# 	  else:
# 		if arr[i]>curr_max:
# 		  curr_max=arr[i]
# 		  count=1
# 		else:
# 		  count+=1
# return(curr_max)