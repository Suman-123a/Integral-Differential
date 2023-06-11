#Monte carlo integration with geometrical interpretatiom 
import matplotlib.pyplot as plt
import numpy as np
def MCI(a,b,f):
	N=10000
	x=np.linspace(a,b,1001)
	ymax=1.2*max(f(x))
	A=(b-a)*ymax
	xval=np.random.uniform(a,b,N)
	yval=np.random.random(N)*ymax
	n=0
	yy,xx,yy1,xx1=[],[],[],[]
	for i in range(N):
		if yval[i]<f(xval)[i]:
			yy.append(yval[i])
			xx.append(xval[i])
			n=n+1
		else:
			yy1.append(yval[i])
			xx1.append(xval[i])
			
	I=A*n/N
	return I,xval,f(xval),xx,yy,xx1,yy1
d1,d2,d3,d4,d5,d6,d7=MCI(0,np.pi,np.sin)
print(d1)
plt.plot(d2,d3,"o")
plt.plot(d4,d5,"o")
plt.plot(d6,d7,"+")
plt.show()


	
	
	