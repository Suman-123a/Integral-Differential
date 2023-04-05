import matplotlib.pyplot as plt
import numpy as np
def f1(x,y,z):
	return z
def f2(x,y,z,b,w):
	return -2*b*z-w**2*y
	
#RK2 2nd order eqn
def rk2(x,y,z,b,w,h):
	xx,yy,zz=[],[],[]
	for i in range(2000):
		a1=h*f1(x,y,z)
		b1=h*f2(x,y,z,b,w)
		a2=h*f1(x+h,y+a1,z+b1)
		b2=h*f2(x+h,y+a1,z+b1,b,w)
		y=y+(a1+a2)/2
		z=z+(b1+b2)/2
		x=x+h
		xx.append(x)
		yy.append(y)
		zz.append(z)
	return xx,yy,zz
g1,g2,g3=rk2(0,1,0,49,6,0.01)

#RK4 2nd order eqn
def rk4(x,y,z,b,w,h):
	xx,yy,zz=[],[],[]
	for i in range(2000):
		a1=h*f1(x,y,z)
		b1=h*f2(x,y,z,b,w)
		a2=h*f1(x+h/2,y+a1/2,z+b1/2)
		b2=h*f2(x+h/2,y+a1/2,z+b1/2,b,w)
		a3=h*f1(x+h/2,y+a2/2,z+b2/2)
		b3=h*f2(x+h/2,y+a2/2,z+b2/2,b,w)
		a4=h*f1(x+h,y+a3,z+b3)
		b4=h*f2(x+h,y+a3,z+b3,b,w)
		y=y+(a1+2*a2+2*a3+a4)/6
		z=z+(b1+2*b2+2*b3+b4)/6
		x=x+h
		xx.append(x)
		yy.append(y)
		zz.append(z)
	return xx,yy,zz
g1,g2,g3=rk4(0,1,0,1,6,0.01)
plt.plot(g1,g2)
plt.show()
	