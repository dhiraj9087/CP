import math
import sys
input=sys.stdin.readline
def main():
    access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]
    access_times = [["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]
    access_times = [["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]
    d={}
    for i,j in access_times:
        # print(i,j)
        if i in d:
            d[i].append(j)
        else:
            d[i]=[j]
    d2={key:sorted(val) for key,val in d.items()}
    arr=[]
    for i,j in d2.items():
        a=len(j)
        for k in range(a-2):
            if int(j[k+2])-int(j[k])<100:
                arr.append(i)
                break
    print(arr)
        # tar=int(j[0])+100
        # ans=0
        # for k in j:
        #     if tar>=int(k):
        #         ans+=1
        #     if ans>=3:
        #         arr.append(i)
        #         break
        
    print(d2,arr)
# for _ in range(int(input())):
print(main())