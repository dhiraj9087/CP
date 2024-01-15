for i in range((int(input()))):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    q,s={},0
    for i in range(len(a)):
        if a[i] in q.keys():
            q.update({a[i]:min(b[i],b[a[i]])})
        else:
            q.update({a[i]:b[i]})
    #print(q)
    sorted_q = dict(sorted(q.items(), key=lambda x: x[1]))
    #print(sorted_q)
    if len(sorted_q)<k:
        print("-1")
    else:
        z=[]
        for i in sorted_q.values():
            z.append(i)
        #print(z)
        for i in range(k):
            s+=z[i]
        print(s)
    # for i in range(len(q)):











# # cook your dish here
# t=int(input())
# for i in range(t):
#     n,k = map(int,input().split())
#     a = list(map(int,input().split()))
#     b = list(map(int,input().split()))
#     d={}
#     for i in range(n):
#         if a[i] not in d:
#             d[a[i]]=b[i]
#         else:
#             d[a[i]]=min(b[i],d[a[i]])
#     if len(d)<k:
#         print(-1)
#     else:
#         array=[]
#         for dd in d:
#             array.append(d[dd])
#         array.sort()
#         sum = 0
#         for i in range(k):
#             sum += array[i]
#         print(sum)