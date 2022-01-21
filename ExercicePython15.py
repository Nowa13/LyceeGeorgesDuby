from random import *
c=0
n=100000
for i in range(0,n):
    x=random()
    y=random()
    if x*x+y*y<=1:
        c=c+1
print(4*c/n)