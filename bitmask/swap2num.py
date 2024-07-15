import math
def swap():
    a=5
    b=6
    a=a^b
    b=a^b
    a=a^b
    print(a,b)


def ithset(n,i):
    # n>>i
    if (n) & 1<<i ==0:
        print("no")
    else:
        print("yes")

def setith(n,i):
    a=1<<i
    n=n|a
    print(n)

def clearith(n,i):
    a=1<<i
    a=~a
    n=n&a
    print(n)

def toggleith(n,i):
    a=1<<i
    n=n^a
    print(n)


def removelastset(n):
    n=n&(n-1)
    print(n)

def ispower2(n):
    if n==0:
        return False
    return (n&(n-1))==0 

def rightmostbit(n):
    num = n&(n-1)
    a = n ^ num
    print(int(math.log(a,2)))
rightmostbit(16)
