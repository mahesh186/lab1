import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
j=cm.sqrt(-1)
pi=3.14
def dtft(x):
	N=len(x)
	y=[]
	w=np.linspace(0,2*pi,1000)
	for i in range(0,1000):
		s=0
		for n in range(0,N,1):
			s=s+(x[n]*np.exp(-j*w[i]*n))
		y=np.append(y,s)
	return y
t=np.arange(0,100,0.1)
x=np.sin(2*pi*t)
y=dtft(x)
plt.subplot(2,2,1)
plt.plot(np.angle(y))
plt.subplot(2,2,2)
plt.title("magnitude",color="b")
plt.plot(np.abs(y))
plt.show()
