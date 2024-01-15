# n=int(input())
# s,s1=0,0
# for i in range(n):
#     a,b=map(int,input().split())
#     s+=a
#     s1+=b
# # print(ev,od)
# # i=0
# if s%2==0 and s1%2==0:
#     print(0)
# elif s%2!=0 and s1%2!=0:
#     print(1)
# else:
#     print(-1)
def min_time_to_rotate_dominoes(n, dominoes):
    upper_sum = sum(dominoes[i][0] for i in range(n))
    lower_sum = sum(dominoes[i][1] for i in range(n))

    if upper_sum % 2 == 0 and lower_sum % 2 == 0:
        return 0
    elif upper_sum % 2 != lower_sum % 2:
        return -1
    else:
        for i in range(n):
            if (dominoes[i][0] % 2 != dominoes[i][1] % 2):
                return 1
        return -1

# Example usage:
n = 3
dominoes = [(1, 2), (3, 4), (5, 6)]
result = min_time_to_rotate_dominoes(n, dominoes)
print(result)