x=input("s=")
w=list(x)
solution=int()

for i,j in enumerate(w):
    if j=="I":
        solution+=1
    elif j=="V":
        solution+=5
    elif j=="X":
        solution+=10
    elif j=="L":
        solution+=50
    elif j=="C":
        solution+=100
    elif j=="D":
         solution+=500          
    elif j=="M": 
        solution+=1000
    else:
        continue   
print(solution)                