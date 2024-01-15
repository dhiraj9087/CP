# processorTime = [10,20]
# tasks = [2,3,1,2,5,8,4,3]
processorTime = [8,10]
tasks = [2,2,3,1,8,7,4,5]
tasks.sort()
processorTime.sort(reverse=True)
print(processorTime,tasks)
ans=0
for i in range(len(processorTime)):
    for j in range(4):
        if i!=0:
            j=4+j
        ans=max(ans,processorTime[i]+tasks[j])
        print(ans)
print(ans)