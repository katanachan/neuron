import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.loadtxt('FIclass1.txt')
np.insert(data,0,0)
x=data[:,0]
y=data[:,1]
z = np.polyfit(x, y, 4)
f = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x,y,'o', x_new, y_new)
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.show()
#plt.plot(data[:,0],data[:,1],'r*',linestyle='-')
#plt.show()