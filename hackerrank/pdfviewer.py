h = list(map(int, input().rstrip().split()))
word = input()
a=[]
e=[]
for i in word:
    a.append(int(ord(i)-96))
# print(ord('z'))
# for i in range(len(h)):
#print(a)
for j in range(len(a)):
    q=a[j]
    
    e.append(h[q-1])
print(max(e)*len(a))    
#print(e)
# print(q)