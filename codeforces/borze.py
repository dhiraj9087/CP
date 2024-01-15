s=input()

result = ""
i = 0
while i < len(s):
    if s[i] == ".":
        result += "0"
        i += 1
    elif s[i:i+2] == "-.":
        result += "1"
        i += 2
    elif s[i:i+2] == "--":
        result += "2"
        i += 2
print(result)
