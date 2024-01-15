# for i in range((int(input()))):
#     n=int(input())
#     a=list(map(int,input().split()))
#     b=list(map(int,input().split()))
#     l=[]
#     flag=True
#     # print(c)
#     for i in range(n):
#         if a[i]!=b[i]:
#             l.append(i)
#     q,w=l[0],l[len(l)-1]
#     for i in range(q-1,-1,-1):
#         if a[i]<=b[q]:
#             q=i
#         else:
#             break
#     for i in range(w+1,n):
#         if a[i]>=b[w]:
#             w=i
#         else:
#             break
#     print(q-1,w-1)
#     # print(l)
   
#         # else:
#         #     print(l[0],l[len(l)-1])
#         #     flag=False


# import sys

# for line in sys.stdin:
#     t = int(line)
#     for _ in range(t):
#         n = int(input())
#         a = list(map(int, input().split()))
#         b = list(map(int, input().split()))
#         c = []
#         for i in range(n):
#             if a[i] != b[i]:
#                 c.append(i)
#         z = len(c)
#         fp = c[0]
#         lp = c[z-1]
#         for i in range(fp-1, -1, -1):
#             if a[i] <= b[fp]:
#                 fp = i
#             else:
#                 break
#         for i in range(lp+1, n):
#             if a[i] >= b[lp]:
#                 lp = i
#             else:
#                 break
#         print(fp+1, lp+1)
import sys

for line in sys.stdin:
    num_test_cases = int(line)
    for _ in range(num_test_cases):
        num_elements = int(input())
        initial_array = list(map(int, input().split()))
        final_array = list(map(int, input().split()))
        changed_indices = []
        for i in range(num_elements):
            if initial_array[i] != final_array[i]:
                changed_indices.append(i)
        num_changed_indices = len(changed_indices)
        first_changed_index = changed_indices[0]
        last_changed_index = changed_indices[num_changed_indices - 1]
        for i in range(first_changed_index - 1, -1, -1):
            if initial_array[i] <= final_array[first_changed_index]:
                first_changed_index = i
            else:
                break
        for i in range(last_changed_index + 1, num_elements):
            if initial_array[i] >= final_array[last_changed_index]:
                last_changed_index = i
            else:
                break
        print(first_changed_index + 1, last_changed_index + 1)
