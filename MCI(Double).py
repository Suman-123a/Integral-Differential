#Monte carlo double integration
import matplotlib.pyplot as plt
import numpy as np
def MCI1(a,b,c,d,g):
	n=10000
	x=np.random.uniform(a,b,n)
	y=np.random.uniform(c,d,n)
	t=(b-a)*(d-c)*np.mean(g(x,y))#integral value
	return t
def g(x,y):
	return 1-x**2-y**2
r=MCI1(0,1,0,1,g)
print(r)
