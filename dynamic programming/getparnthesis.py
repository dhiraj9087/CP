n=9
res=[]
def gen(lcount,rcount,tmp):
    
    if lcount==0 and rcount==0:
        res.append(tmp)
    if lcount>0:
        gen(lcount-1,rcount,tmp+"(")
    if rcount>lcount:
        gen(lcount,rcount-1,tmp+")")
gen(n,n,"")
# return res