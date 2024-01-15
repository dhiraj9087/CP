# #5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39







if __name__ == '__main__':
    result=[]
    s=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        result+=[[name,score]]
        s+=[score]
    d=sorted(set(s))[1]
    #print(d)
    #print(result)
    for a,c in sorted(result):                  #loop to check both name and                                                    score  at same time
        if c==d:                            
            print(a)
    