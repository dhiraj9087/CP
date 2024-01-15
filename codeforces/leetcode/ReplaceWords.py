import math
import sys
input=sys.stdin.readline
def main():
    dictionary = ["cat","bat","rat"]
    sentence = "the cattle was rattled by the battery"
    words=sentence.split()
    d=set(dictionary)
    print(words,d)
    ans=[]
    for i in range(len(words)):
        flag=False
        for j in range(len(words[i])):
            a=words[i][:j+1]
            if a in d:
                ans.append(a)
                flag=True
        if flag==False:
            ans.append(words[i])
    print(ans)


# for _ in range(int(input())):
main()