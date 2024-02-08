
def pal(l):
    global n
    if l>=n//2:
        return True
    if s[l]!=s[n-l-1]:
        return False
    return pal(l+1)


s="qwererq"
n=len(s)
print(pal(0))