for i in range((int(input()))):
    n = int(input()) 
    time = 0  

    while n != 50:  
        if n < 50:  
            n += 2  
        else:  
            n -= 3  
        time += 1  

    print(time)  
