import matplotlib.pyplot as plt
import numpy as np
def f(x,y):
	return -y
	
def rk2(x,y,f):
	xx,yy=[],[]
	h=0.01
	for i in range(1000):
		k1=h*f(x,y)
		k2=h*f(x+h,y+k1)
		y=y+0.5*(k1+k2)
		x=x+h
		xx.append(x)
		yy.append(y)
	return xx,yy
	
def rk4(x,y,f):
	xx,yy=[],[]
	h=0.01
	for i in range(1000):
		k1=h*f(x,y)
		k2=h*f(x+0.5*h,y+0.5*k1)
		k3=h*f(x+0.5*h,y+0.5*k2)
		k4=h*f(x+h,y+k3)
		y=y+(k1+2*k2+2*k3+k4)/6
		x=x+h
		xx.append(x)
		yy.append(y)
	return xx,yy
z1,z2=rk4(0,1,f)
plt.plot(z1,z2)
plt.show()
	
	
	