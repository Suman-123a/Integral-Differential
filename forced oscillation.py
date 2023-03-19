#forced oscillator
import matplotlib.pyplot as plt
import numpy as np
def d(t,y,g,w,b,f,w1):
	return -2*b*g-w**2*y+f*np.sin(w1*t)
def F(ti,tf,y,g,w,b,f,w1,n):
	h=(tf-ti)/(n-1)
	yy=[]
	tt=[]
	gg=[]
	for i in range(n):
		t=ti+i*h
		tt.append(t)
		ya=y
		y=y+h*g
		g=g+h*d(t,ya,g,w,b,f,w1)
		yy.append(y)
		gg.append(g)
	return tt,yy,gg
z1,z2,z3=F(0,100,0,1,2.23,0.25,1,1.05,30000)
n=100000
aa=[]
vv=[]
pp=[]
#plt.plot(z1[8000:n],z2[8000:n])
#plt.show()
a=max(z2[9000:n])
print(a)
for i in np.arange(0.5,5,0.02):
	pp.append(i)
	z1,z2,z3=F(0,100,0,0,2.23,0.25,1,i,10000)
	a=max(z2[-1000:])
	aa.append(a)
	v=max(z3[-1000:])
	vv.append(v)
plt.title("forced oscillator",size=20)
plt.xlabel("frequency",size=20)
plt.ylabel("amplitude",size=20)	
plt.plot(pp,aa,"--",label="displacement amplitude resonance")
plt.plot(pp,vv,label="velocity amplitude resonance")
plt.legend()
plt.show()

	
	
	