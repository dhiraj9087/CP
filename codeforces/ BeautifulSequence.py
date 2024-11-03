# for i in range((int(input()))):
#     n=int(input())
#     a=list(map(int,input().split()))
#     flag=0
#     for i in range(n):
#         if i+1 in a[i::]:
#             flag=1
#             # print(i+1)
#     if flag==1:
#         print("YES")
#     else:
#         print("NO")
def GasStation(strArr): 
    L = int(strArr[0])
    
    # Split each gas:cost pair and store them as tuples of integers
    strArr[1:] = [x.split(":") for x in strArr[1:]]
    
    # Create a dictionary where each station's gas difference and next station are stored
    ht = {i: (int(strArr[i][0]) - int(strArr[i][1]), i + 1) for i in range(1, L)}
    print(ht)
    # Ensure the last station loops back to the first station
    ht[L] = (int(strArr[L][0]) - int(strArr[L][1]), 1)
    
    # Try starting from each station and check if the car can complete the loop
    for station in range(1, L + 1):
        current = station
        gas = 0
        for j in range(L):
            gas += ht[current][0]
            if gas < 0:
                break
            current = ht[current][1]
        else:
            return str(station)
    
    return "impossible"

# Example input without extra list characters
input_data = ["4", "3:1", "2:2", "1:2", "0:1"]
print(GasStation(input_data))
