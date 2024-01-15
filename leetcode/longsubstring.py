# s=input()
# dict={}
# for i in s:
#     d=s.count(i)
#     dict[i]=d
# print(dict)
# print(min(dict))
s='abcabcbb'
max_len = 0
for i in range(len(s)):
    char_set=set()
    for j in range(i,len(s)):
        if s[j] in char_set:
            break
        char_set.add(s[j])
        print(char_set)
        max_len = max(max_len,j-i+1)

#return (max_len)