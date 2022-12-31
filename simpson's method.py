#simpson method integration
import math as mt
import numpy as np
xi=0
xf=3
n=9

yy=[]
s=0
def symp(xi,xf,n):
	h=(xf-xi)/(n-1)
    
	for i in range(n):
		x=xi+i*h
		y=x**2
		yy.append(y)
	s1=0
	for i in range(1,n-1,2):
		s1=s1+yy[i]
	s1=4*s1
	s2=0
	for i in range(2,n-1,2):
		s2=s2+yy[i]
	s2=2*s2
	s=yy[0]+s1+s2+yy[n-1]
	s=(1/3)*h*s
	return s
y=symp(xi,xf,n)
print("The result of the integration=",y)