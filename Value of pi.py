#Approximating value of π
import numpy as np
aa=[]
n=50000
x=np.random.uniform(-1,1,n)
y=np.random.uniform(-1,1,n)
a=x**2+y**2
for i in range(len(a)):
	if a[i]<=1:
		aa.append(a[i])
inside=len(aa)
pi=4*inside/n
print(pi)