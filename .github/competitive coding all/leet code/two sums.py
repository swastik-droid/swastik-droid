x=int(input())
nums=[]
for i in range(0,x):
    f=int(input())
    nums.append(f)
print(nums)    
y=int(input("target="))

for j,k in enumerate(nums):
  a=k
  c=j+1
  for n in range(c,len(nums)):
     b=nums[n]
     z=a+b
     if z==y:
        print("[{0},{1}]".format(j,n))
     else:
        continue      