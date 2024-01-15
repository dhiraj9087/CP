n=int(input())
q,c=[],[]
for i in range(n):
    a=input()
    q.append(a)
#print(q)
max_count = 0
max_elem = None
for elem in q:
    count = q.count(elem)
    if count > max_count:
        max_count = count
        max_elem = elem
print(max_elem)
