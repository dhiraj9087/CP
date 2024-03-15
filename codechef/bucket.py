import math
import sys
input=sys.stdin.readline
def main():
    num_buckets = int(input())
    buckets = list(map(int,input().split()))
    ones_count = 0
    twos_count = 0
    more_count = 0
    for bucket_size in buckets:
        if bucket_size == 1:
                ones_count += 1
        else:
            if bucket_size > 2:
                more_count += bucket_size - 2
                twos_count += 1
            else:
                twos_count += 1
    alice_score = 0
    bob_score = 0
    alice_score += (ones_count + 1) // 2
    bob_score += ones_count // 2
    flag = False
    flag = ones_count % 2 != 0
    if flag:
        if more_count % 2 == 1:
            flag = False
    else:
        if more_count % 2 == 1:
            flag = True
    if flag:
        alice_score += twos_count
    else:
        bob_score += twos_count
    if alice_score > bob_score:
        print("Alice")
    elif bob_score > alice_score:
        print("Bob")
    else:
        print("Draw")

for _ in range(int(input())):
   main()