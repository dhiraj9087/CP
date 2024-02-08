# global c
c=0
def ruc():
    global c
    if c==3:
        return
    print(c)
    c+=1
    ruc()
ruc()