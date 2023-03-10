#integration with error
import matplotlib.pyplot as mt
import numpy as np

def trap(xi,xf,n):
    yy=[]
    h=(xf-xi)/(n-1)
    for i in range(n):
        x=xi+(i*h)
        y=x*np.exp(-x)
        yy.append(y)  
    s=0
    for i in range(1,n-1):
        s=s+yy[i]
    s=2*s
    s=s+yy[0]+yy[n-1]
    s=.5*h*s
    return s
y1=[]
y2=[]
xi=0
xf=3
n=2
esp=.001
err=1
u=0
while err>=esp:
    g=trap(xi,xf,n)
    y1.append(g)
    y2.append(n)
    err=g-u
    u=g
    n=n+1
print("The value of the integral with accuracy",esp,"is",g)
print("And the no of points taken for the accuracy to reach is",n)
mt.plot(y2,y1)
mt.show()