n = int(input().strip())

scores = list(map(int, input().rstrip().split()))



h1=[]
l1=[]
for i in range(len(scores)):
        if(scores[i]>scores[0]):
            h1.append(scores[i])
        elif(scores[i]<scores[0]):
            l1.append(scores[i])
# h=set(h)
# l=set(l)
h = []
[h.append(x) for x in h1 if x not in h]
l = []
[l.append(x) for x in l1 if x not in l]
#return h
#print((l))
s=0
q=0
M=max(scores)
m=min(scores)
#print(m)
# i=0
# while(h[i]!=M):
#         if(h[i]>scores[0]):
#             s+=1
#         i+=1
# print(s)
# for i in range(len(h)):
#     if(h[i]!=M):
#         if(h[i]>scores[0]):
#             s+=1
# print(s)

w=scores[0]
for i in range(len(h)):
    if(h[i]>w):
        s=s+1
        w=h[i]
#         print(h[i])
#print(s)
e=scores[0]
for i in range(len(l)):
    
    if(l[i]<e):
        q=q+1
        e=l[i]
#print(s)
print(s,q)


