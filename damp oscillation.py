#damped oscillation
import matplotlib.pyplot as plt
import numpy as np
def f(x,y,g,w,b):
	return -2*b*g-w**2*y
def D(xi,xf,y,g,n,w,b):
	xx=[]
	yy=[]
	h=(xf-xi)/(n-1)
	for i in range(n):
		x=xi+i*h
		xx.append(x)
		ya=y
		y=y+h*g
		g=g+h*f(x,ya,g,w,b)
		yy.append(y)
	return xx,yy
z1,z2=D(0,10,1,0,500,6,18)
z3,z4=D(0,10,1,0,500,6,1)
z5,z6=D(0,10,1,0,500,6,49)
plt.title("damped oscillation",size=20)
plt.xlabel("Time",size=20)
plt.ylabel("y(t)",size=20)
plt.plot(z3,z4,":",label="UNDERDAMPED")
plt.plot(z1,z2,"--",label="CRITICAL-DAMPED")
plt.plot(z5,z6,label="OVER-DAMPED")
plt.legend()
plt.show()

