import math
import sys
input=sys.stdin.readline
px, py, ax, ay, bx, by = 0, 0, 0, 0, 0, 0
def getDistance(p, q, x, y):
    return (p - x) ** 2 + (q - y) ** 2
def checkIfPresentInCircle(cx, cy, dx, dy, w):
    d = getDistance(cx, cy, dx, dy)
    return d <= w ** 2

def check(w):
    isStartInFirstCircle = checkIfPresentInCircle(ax, ay, 0, 0, w)
    isHomeInFirstCircle = checkIfPresentInCircle(ax, ay, px, py, w)

    if isStartInFirstCircle and isHomeInFirstCircle:
        return True
    isStartInSecondCircle = checkIfPresentInCircle(bx, by, 0, 0, w)
    isHomeInSecondCircle = checkIfPresentInCircle(bx, by, px, py, w)

    if isStartInSecondCircle and isHomeInSecondCircle:
        return True

    if not checkIfPresentInCircle(ax, ay, 0, 0, w) and not checkIfPresentInCircle(bx, by, 0, 0, w):

        return False
    if not checkIfPresentInCircle(ax, ay, px, py, w) and not checkIfPresentInCircle(bx, by, px, py, w):
        return False
    d = getDistance(ax, ay, bx, by)
    if d > 4 * w ** 2:
        return False

    return True
def main():
    global px, py, ax, ay, bx, by
    px, py = map(int, input().split())
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())

    if px == 0 and py == 0:
        print(0)
        return

    l, r = 0, 4000
    ans = 4000

    for _ in range(200):
        mid = (l + r) / 2.0

        if check(mid):
            ans = mid
            r = mid
        else:
            l = mid

    print(format(ans, '.10f'))
    # px,py=map(int,input().split())
    # ax,ay=map(int,input().split())
    # bx,by=map(int,input().split())
    # AB = (math.sqrt((ax-bx)*(ax-bx) + (ay-by)*(ay-by)))/2
    # PA = math.sqrt((px-ax)*(px-ax) + (py-ay)*(py-ay))
    # PB = math.sqrt((px-bx)*(px-bx) + (py-by)*(py-by))
    # # print(AB,PA,PB)
    # # a=[AB,PA,PB]
    # # a.sort()
    # # print(a[1])
    # ans=float('inf')
    # if AB>=PA or AB>=PB:
    #     ans=min(ans,AB)
    # if 2*AB<=2*PA:
    #     ans=min(ans,PA)
    # if 2*AB<=2*PB:
    #     ans=min(ans,PB)
    # print(ans)
for _ in range(int(input())):
   main()