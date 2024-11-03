import math
import sys
input=sys.stdin.readline

def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans = []
    flag = False

    while True:
        arr2 = sorted(a)
        if a == arr2:
            flag = True
            break
        if len(a) <= 2:
            break
        
        ans.append((1, 3))
        three = a[:3]
        cur2 = three[:]
        three.sort()
        
        if cur2[0] == three[1]:
            ind = cur2.index(cur2[0])
        elif cur2[1] == three[1]:
            ind = cur2.index(cur2[1])
        else:
            ind = cur2.index(cur2[2])
            
        a = [a[i] for i in range(len(a)) if i != ind]
    
    if not flag:
        print(-1)
    else:
        print(len(ans))
        for i in ans:
            print(i[0], i[1])

for _ in range(int(input())):
   main()