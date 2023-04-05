import matplotlib.pyplot as plt
import numpy as np
def f1(x,y,z):
	return z
def f2(x,y,z,b,w,p,w1):
	return -2*b*z-w**2*y+p*np.sin(w1*x)
def rk4(x,y,z,b,w,h,p,w1):
	xx,yy,zz=[],[],[]
	for i in range(2000):
		a1=h*f1(x,y,z)
		b1=h*f2(x,y,z,b,w,p,w1)
		a2=h*f1(x+h/2,y+a1/2,z+b1/2)
		b2=h*f2(x+h/2,y+a1/2,z+b1/2,b,w,p,w1)
		a3=h*f1(x+h/2,y+a2/2,z+b2/2)
		b3=h*f2(x+h/2,y+a2/2,z+b2/2,b,w,p,w1)
		a4=h*f1(x+h,y+a3,z+b3)
		b4=h*f2(x+h,y+a3,z+b3,b,w,p,w1)
		y=y+(a1+2*a2+2*a3+a4)/6
		z=z+(b1+2*b2+2*b3+b4)/6
		x=x+h
		xx.append(x)
		yy.append(y)
		zz.append(z)
	return xx,yy,zz
g1,g2,g3=rk4(0,0,0,0.35,2.23,0.01,1,1.05)
plt.plot(g1,g2)
plt.show()
	