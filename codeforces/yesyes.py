def solve(a):
    s=input()
    if s in a:
        return 'YES'
    else:
        return 'NO'

for _ in range((int(input()))):
    a='Yes'*18
    print(solve(a))