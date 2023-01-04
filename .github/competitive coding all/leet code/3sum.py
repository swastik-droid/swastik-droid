def threesum(nums: list[int]) -> list[list[int]]:
    s=[]
    for i,j in enumerate(nums):
        a=j
        for k in range(i+1,len(nums)):
            b=nums[k]
            c=nums[k+1]
            if b+c == a*(-1):
                x=list(a,b,c)
                s.append(x)
            else:
                continue
    return s


y=input(" ")
print(y)
z=threesum(y)
print(z)
            
            