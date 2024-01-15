def main():
    n = 2
    m = 1
    hBars = [2,3]
    vBars = [2]
    ans,prev,c=0,0,0
    hBars.sort()
    vBars.sort()
    for i in range(len(hBars)):
        if i==0:
            c=1
            prev=hBars[i]
            ans=max(ans,c)
        elif hBars[i]==prev+1:
            c+=1
            prev=hBars[i]
        else:
            ans=max(ans,c)
            c=1
            prev=hBars[i]
    ans=max(ans,c)
    ans2,prev2,c2=0,0,0
    for i in range(len(vBars)):
        if i==0:
            c2=1
            prev2=vBars[i]
            ans2=max(ans2,c2)
        elif vBars[i]==prev2+1:
            c2+=1
            prev2=vBars[i]
        else:
            ans2=max(ans2,c2)
            c2=1
            prev2=vBars[i]
    ans2=max(ans2,c2)
    res=min(ans,ans2)
    return (res+1)**2

print(main())