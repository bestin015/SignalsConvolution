import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

num=np.array([5,5])
den=np.array([1,5,6])
H= signal.TransferFunction(num,den)
print('H(s)=',H)
t,y = signal.step(H)
plt.plot(t,y)
plt.title("step response")
plt.xlabel("t")
plt.ylabel("y")
plt.grid()
plt.show()
