#euler method of analysis
import matplotlib.pyplot as plt
import numpy as np
x1=np.linspace(0,5,500)
y1=np.exp(-x1)
#dy/dx=-y
def f(x,y):
	return -y
xi=0
xf=5
n=500
h=(xf-xi)/(n-1)
xx=[]
yy=[]
y=1
for i in range(n):
	x=xi+i*h
	xx.append(x)
	y=y+h*f(x,y)
	yy.append(y)
	
plt.plot(xx,yy)
plt.plot(x1,y1)
plt.show()
print("The numerical value of the solution=",y)