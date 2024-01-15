# for i in range((int(input()))):
#     n=int(input())
#     s=input()
#     d={}
#     for i in range(1,len(s)):
#         if s[i-1]!=s[n-i-1+1]:
#             print(s,'anti')
#             break
#         else:
#             print(s,'ti')
#             break
def solve(n, s):
    if n % 2 == 1:
        print(-1)
        return

    cnt = [0] * 26
    for i in range(n):
        cnt[ord(s[i]) - ord('a')] += 1

    for i in range(26):
        if cnt[i] * 2 > n:
            print(-1)
            return

    pairs = 0
    cnt_pairs = [0] * 26
    for i in range(n // 2):
        if s[i] == s[n - i - 1]:
            pairs += 1
            cnt_pairs[ord(s[i]) - ord('a')] += 1

    for i in range(26):
        if cnt_pairs[i] * 2 > pairs:
            print(cnt_pairs[i])
            return

    print((pairs + 1) // 2)


def main():
    t = int(input())
    for _ in range(t):
        n= int(input())
        s=input()
        n = int(n)
        solve(n, s)
        
if __name__ == "__main__":
    main()
