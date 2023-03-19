#harmonic oscillator
import matplotlib.pyplot as plt
import numpy as np
#d2y/dx2=-w^2y
def f(x,y,w):
	return  -w**2*y
def H(xi,xf,y,g,w,n):
	h=(xf-xi)/(n-1)
	xx=[]
	yy=[]
	for i in range(n):
		x=xi+i*h
		xx.append(x)
		g=g+h*f(x,y,w)
		y=y+h*g
		yy.append(y)
	return yy,xx
z1,z2=H(0,18,2,0,2,50000)
plt.plot(z2,z1)
plt.title("harmonic oscillator",size=20)
plt.xlabel("Time",size=20)
plt.ylabel("y(t)",size=20)
plt.show()
n=50000
i=0
#z1=yy,z2=xx
while z1[i]>z1[i+1]:
			i=i+1
T=2*z2[i]
print("time period with w=2:",T)
			