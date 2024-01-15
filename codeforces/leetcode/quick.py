import math
import sys
input=sys.stdin.readline
def main():
	n,k=map(int,input().split())
	a=list(map(int,input().split()))
	s,x=0,1
	for i in a:
		if i==x:
			x+=1
			s+=1
	print(math.ceil((n-s)/k))
for _ in range(int(input())):
   main()
   