import sys
input=sys.stdin.readline
def main():
    a=[]
    for i in range(8):
        x=list(input().strip())
        a.append(x)
    # print(a)
    s = ""
    for i in range(8):
        for j in range(8):
            if a[i][j] != '.':
                s += a[i][j]
    print(s)
    
for _ in range(int(input())):
    main()