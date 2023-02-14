#generalised integral program
import math as mt
import numpy as np
def g(x):
	return np.exp(-x**2)

def trap(xi,xf,n,f):
	h=(xf-xi)/(n-1)
	yy=[]
	for i in range(n):
		x=xi+i*h
		y=f(x)
		yy.append(y)
	s=0
	for i in range(1,n-1):
		s=s+yy[i]
		
	s=yy[0]+2*s+yy[n-1]
	s=0.5*h*s
    
	
	return s
d=trap(0,1,100,g)
print(d)
