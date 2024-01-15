import math

for _ in range(int(input())):
    L, R = map(int, input().split())
    max_score = -1
    if L>R:
        for X in range(R, L+1):
            # print(X)
            score = math.ceil((X - L)/2) + math.ceil((R - X)/2)
            max_score = max((max_score), abs(score))
            # print(score)
    else:
        for X in range(L, R+1):
            print(X)
            score = math.ceil((X - L)/2) + math.ceil((R - X)/2)
            max_score = max(max_score, score)
            print(max_score)
        
    print(max_score)
