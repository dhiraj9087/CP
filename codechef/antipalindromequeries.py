import math
import sys
input=sys.stdin.readline
from collections import Counter
def can_be_beautiful(subarray):
    length = len(subarray)
    if length % 2 != 0:
        return False
    
    if length == 2:
        return subarray[0] != subarray[1]
    
    counts = [0, 0, 0]
    for num in subarray:
        counts[num-1] += 1
    
    distinct_count = sum(1 for count in counts if count > 0)
    max_count = max(counts)
    
    return distinct_count >= 3 and max_count <= length // 2

def main():
    n,q=map(int,input().split())
    a=[0]+list(map(int,input().split()))
    pre1=[0]*(n+1)
    pre2=[0]*(n+1)
    pre3=[0]*(n+1)
    for i in range(1,n+1):
        pre1[i] = pre1[i-1]+(a[i]==1)
        pre2[i] = pre2[i-1]+(a[i]==2)
        pre3[i] = pre3[i-1]+(a[i]==3)
    for _ in range(q):
        l,r = map(int,input().split())
        rng = r-l+1
        if rng%2==1:
            print("No")
        else:
            k=rng//2
            f1 = pre1[r]-pre1[l-1]
            f2 = pre2[r]-pre2[l-1]
            f3 = pre3[r]-pre3[l-1]
            c=0
            if f1>=k:
                c+=1
            if f2>=k:
                c+=1
            if f3>=k:
                c+=1
            if f1<=k and f2<=k and f3<=k and c>=1:
                print("Yes")
            else:
                print("No")
    # for i in range(q):
    #     l,r=map(int,input().split())
    #     l,r=l-1,r-1
    #     if (r-l+1)%2==1:
    #         print("No")
    #     else:
    #         arr = a[l:r+1]
    #         ans = can_be_beautiful(arr)
    #         if ans:
    #             print("Yes")
    #         else:
    #             print("No")
            # d=Counter(arr)
            # rng = r-l+1
            # c=0
            # flag=False
            # for i,j in d.items():
            #     if j>rng//2:
            #         print("No")
            #         flag = True
            #         break
            #     if j==rng//2:
            #         c+=1
            #     if c>1:
            #         print("No")
            #         flag = True
            #         break
            # if flag==False:
            #     print("Yes")
for _ in range(int(input())):
   main()
