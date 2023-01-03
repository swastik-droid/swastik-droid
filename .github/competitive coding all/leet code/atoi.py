def atoi(s: str) -> int:
    s=s.strip(" ")
    s=s.strip("0")
    num=0
    y=1
    
    for i in s:
        if i.isdigit():
            num = num*10 + int(i)
        elif( i == "+"):
            y += 0  
        elif(i == "-"):      
            y -= 2
        
    return num*y
            
        

z=input("s=")
x=atoi(z)
print(x)