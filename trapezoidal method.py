#trapezoidal method integration
import math as mt
import numpy as np
xi=0
xf=np.pi
n=100

def trap(xi,xf,n):
	h=(xf-xi)/(n-1)
	yy=[]
	for i in range(n):
		x=xi+i*h
		y=mt.sin(x)
		yy.append(y)
	s=0
	for i in range(1,n-1):
		s=s+yy[i]
		
	s=yy[0]+2*s+yy[n-1]
	s=0.5*h*s
    
	
	return s
y=trap(xi,xf,n)
print("The result of the integration=",y)