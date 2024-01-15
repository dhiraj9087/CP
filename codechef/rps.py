import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    d={'R':'P','P':'S','S':'R'}
    win=[]
    for i in s:
            win.append(d[i])
    if n<=2:
        print(''.join(win))
        return
    tar=n//2 + 1
    # print(win,n-tar)
    c=n
    for i in range(n):
        if c>n//2+1:
            if win[i]!='P':
                win[i]='P'
                c-=1
        # if c<n-tar+1:
        #     if win[i]!='P':
        #         win[i]='P'
        # c+=1
    print(''.join(win))
for _ in range(int(input())):
   main()