garbage = ["G","P","GP","GG"]
travel = [2,4,3]
garbage = ["MMM","PGM","GP"]
travel = [3,10]
g,p,m=0,0,0
n=len(garbage)
g_l,p_l,m_l=n-1,n-1,n-1
for i in range(n-1,-1,-1):
    if "G" in garbage[i]:
        break
    else:
        g_l-=1
for i in range(n-1,-1,-1):
    if "P" in garbage[i]:
        break
    else:
        p_l-=1
for i in range(n-1,-1,-1):
    if "M" in garbage[i]:
        break
    else:
        m_l-=1

# print(g_l,p_l,m_l)
for i in range(p_l+1):
    p+=(garbage[i].count("P"))
    if i>0:
        p+=(travel[i-1])
for i in range(g_l+1):
    g+=(garbage[i].count("G"))
    if i>0:
        g+=(travel[i-1])
for i in range(m_l+1):
    m+=(garbage[i].count("M"))
    if i>0:
        m+=(travel[i-1])
    # print(p)
print(p,g,m)

