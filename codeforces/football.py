s = input()
count = 1  
last = s[0]
for i in range(1, len(s)):
    if s[i] == last:
        count += 1
        if count >= 7:
            print("YES")
            break
    else:
        count = 1
        last = s[i]
else:
    print("NO")
