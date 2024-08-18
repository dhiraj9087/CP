st = []
arr=[10,12,15]
mini = float('inf')
for i in range(len(arr)):
    if not st:
        st.append([arr[i],min(arr[i],mini)])

    else:
        st.append([arr[i],st[-1][1]])
print(st)
