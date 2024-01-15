s = "leetscode"
dictionary = ["leet","code","leetcode"]
# s="sayhelloworld"
# dictionary = ["hello","world"]
a=""
for i in range(len(dictionary)):
    if dictionary[i] in s:
        a=a+dictionary[i]
print(abs(len(a)-len(s)))
