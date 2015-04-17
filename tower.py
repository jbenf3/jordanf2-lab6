import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

t,v = np.loadtxt("droptower_vdata.txt", unpack =
               True)
print t
print v

pos = scipy.integrate.cumtrapz(v,t,initial=0)

acc = np.gradient(v)

print acc

pos = pos + 30

plt.plot(t,pos)
plt.plot(t,v)
plt.plot(t,acc)
plt.show()
