string=input()
seen = set()
for i in range(len(string) - 1, -1, -1):
    if string[i] in seen:
        string = string[:i] + string[i+1:]
        #print(string[::-1])
    seen.add(string[i])
print(string[::-1])

