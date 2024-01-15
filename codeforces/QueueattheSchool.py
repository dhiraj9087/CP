def main():
    n,t=map(int,input().split())
    s=input()
    # s=list(s)
    while t:
        s=s.replace('BG','GB')
        t-=1
    print(s)
main()