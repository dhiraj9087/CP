# s1=input()
# s2=input()
# s3=input()
# s4=input()
# # for i in range(4):
# s1white=s1.count('.')
# s1black=s1.count('#')
# s2white=s2.count('.')
# s2black=s2.count('#')
# s3white=s3.count('.')
# s3black=s3.count('#')
# s4white=s4.count('.')
# s4black=s4.count('#')
# if s1white+s2white>4 or s1black+s2black>4:
#     print("YES")
# elif s3white+s4white>4 or s3black+s4black>4:
#     print("YES")
# else:
#     print("NO")

arr=[input().strip() for i in range(4)]

for i in range(3):
    for j in range(3):
        s=""
        s=s+arr[i][j]+arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1]
        # print(s)
        if s.count('#')>=3:
            print("YES")
            exit()
        elif s.count('.')>=3:
            print("YES")
            exit()
print("NO")

