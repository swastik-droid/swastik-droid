import math
import os
import random
import re
import sys

x=int(random.randrange(0,101))
print(x)
y=x%2
if x !=0 and y!=0:
    print("Weird")
else:
    if 2 <= x <= 7:
        print("not Weird")
    elif 6 <= x <= 20:
        print("Weird")
    elif 21<=x<=30:
        print("not weird")    
    else:
        print("not Weird")       