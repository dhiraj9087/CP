# s=set(input())
# print("CHAT WITH HER!" if len(s)%2==0 else "IGNORE HIM!")
# #
s1=input()
s2=input()
s3=input()
s=s1+s2
flag=True
for i in s3:
    if i not in s:
        flag=False
for i in s:
    if s.count(i) !=s3.count(i):
        flag=False
print("YES" if flag else "NO")