def is_leap(year):
    leap = False
    if(year%4==0 and year%100==0 and year%400==0):
        return True
    else:
        return False
    # Write your logic here
    
    #return leap

year = int(input())
print(is_leap(year))