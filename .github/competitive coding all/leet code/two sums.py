x=int(input())
nums=[]
for i in range(0,x):
    f=input()
    nums.append(f)
print(nums)    
y=int(input("target="))

for j in nums:
   a=nums[j]
   for k in nums:
       k =j+1
       b=nums[k]
       if (a+b)==y:
          print(nums[j],nums[k])
       else:
          continue   