
x=int(input())
y=[]
for i in range(0,x):
    f=input()
    y.append(f)
print(y)    
a=int()
for i in y:
    if i not in y :
        a += 1
    else:
        continue
print(a)        
