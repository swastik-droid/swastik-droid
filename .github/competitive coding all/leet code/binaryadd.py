x=input("a=")
y=input("b=")

a=bin(int(x))
y=bin(int(y))

z=a+b

print(bin(z).format(14,'b'))

