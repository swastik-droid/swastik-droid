import math
x=int(input("x="))

if x>2:
    y=x
    z=(y+(x/y))/2
    while abs(y-z)>=0.00001:
        y=z
        z=(y+(x/y))/2
        print(math.floor(z))
else:
    print(math.floor(x))