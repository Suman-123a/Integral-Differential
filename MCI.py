#Monte carlo integration
import matplotlib.pyplot as plt
import numpy as np
def MCI(a,b,f):
	n=10000
	x=np.random.uniform(a,b,n)
	t=(b-a)*np.mean(f(x))#integral 
	e=np.std(f(x))/np.sqrt(n)#error
	return t,e
def f(x):
	return np.sin(x)
d1,d2=MCI(0,np.pi,f)
print(d1,d2)
aa=[]
for i in range(10000):
	a1,a2=MCI(0,np.pi,f)
	aa.append(a1)
plt.xkcd()
plt.hist(aa,bins=40)
plt.show()




