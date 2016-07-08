import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.genfromtxt('FI3.txt')
data2 = np.genfromtxt('class3.txt')
x=data[:,0]
y=data[:,1]
t=data2[:,0]
v=data2[:,1]
z = np.polyfit(x, y, 4)
f = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.figure()
plt.subplot(211)
plt.plot(x,y,'o', x_new, y_new)
plt.xlim(xmin=0)
plt.xlabel('current (in pA)')
plt.ylabel('firing rate (in Hz')
plt.ylim(ymin=0)
plt.subplot(212)
plt.plot(t,v,'r*',linestyle='-')
plt.ylabel('voltage (in mV)')
plt.xlabel('time step(in t)')
plt.xlim(xmax=1)
plt.show()
#plt.plot(data[:,0],data[:,1],'r*',linestyle='-')
#plt.show()