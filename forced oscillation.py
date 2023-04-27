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
n=100000
aa=[]
vv=[]
pp=[]
z1,z2,z3=F(0,100,0,0,2.23,0.35,1,1.05,10000)
#solution
plt.plot(z1[-3000:n],z2[-3000:n])
plt.show()
#amplitude
u=max(z2[-3000:n])
print("amplitude=",u)
#time period
i=4000
while z2[i]*z2[i+1]>0:
	i=i+1
T1=z1[i]
while z2[i+1]*z2[i+2]>0:
	i=i+1
T2=z1[i]
T=2*(abs(T1-T2))
print("time period=",T)

for i in np.arange(0.5,5,0.02):
	pp.append(i)
	z1,z2,z3=F(0,100,0,0,2.23,0.35,1,i,10000)
	a=max(z2[-1000:])
	aa.append(a)
	
	v=max(z3[-1000:])
	vv.append(v)
	
i=10
while aa[i+1]>aa[i]:
	i=i+1
print("amplitude resonant frequency=",pp[i])
j=10
while vv[j+1]>vv[j]:
	j=j+1
print("velocity resonant frequency=",pp[j])
	
plt.title("forced oscillator",size=20)
plt.xlabel("frequency",size=20)
plt.ylabel("amplitude",size=20)	
plt.plot(pp,aa,"--",label="displacement amplitude resonance")
plt.plot(pp,vv,label="velocity amplitude resonance")
plt.legend()
plt.show()	