import math
import sys
input=sys.stdin.readline
def main():
    h,n=map(int,input().split())
    a=list(map(int,input().split()))
    c=list(map(int,input().split()))
    arr=[[a[i],c[i]] for i in range(n)]
    n = len(arr)
    turn = 0
    cooldowns = [0] * n  # Cooldown timer for each attack
    
    while h > 0:
        total_damage = 0
        for i in range(n):
            if cooldowns[i] <= turn:
                total_damage += arr[i][0]  # Apply attack damage
                cooldowns[i] = turn + arr[i][1]  # Set the cooldown
        
        h -= total_damage  # Reduce boss health by the total damage dealt
        turn += 1 
    print(turn)
for _ in range(int(input())):
   main()