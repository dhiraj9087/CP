def main():
    n = int(input()) 
    if(360%(180-n)==0):
        print("YES")
    else:
        print("NO")
for _ in range(int(input())):
    main()