# def sub(ind,ans,arr,n):
#     if ind==n:
#         print(*ans)
#         return
#     ans.append(arr[ind])
#     sub(ind+1,ans,arr,n)
#     ans.pop()
#     sub(ind+1,ans,arr,n)



# arr=[9,6,4397,492]
# n=len(arr)
# ans=[]
# sub(0,ans,arr,n)
# Enter your code here. Read input from STDIN. Print output to STDOUT


  # return 0
def main():
  n,c=map(int,input().split())
  arr=list(map(int,input().split()))
  ans=[]
  tar=c
  flag=False
  def fun(ind,ans,arr,tar,n):
    if ind==n:
      if sum(ans)==tar:
        # flag=True
        # print(1)
        return 1
      # print(0)
      return 0
    ans.append(arr[ind])
    fun(ind+1,ans,arr,tar,n)
    ans.pop()
    fun(ind+1,ans,arr,tar,n)
    # return flag
  # a=(fun(0,ans,arr,tar,n))

  # print(fun(0,ans,arr,tar,n))
  # if flag==True:
  #   print(1)
  #   return
  # print(0)
  return fun(0,ans,arr,tar,n)
for _ in range(int(input())):
  print(main())
# def sub(ind, ans, arr, n):
#     print(*ans)
#     for i in range(ind, n):
#         ans.append(arr[i])
#         sub(i + 1, ans, arr, n)
#         ans.pop()


# arr = [9, 6, 4397, 492]
# n = len(arr)
# ans = []
# sub(0, ans, arr, n)