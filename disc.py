import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

num=[5,5]
den=[1,5,6]
Ts=0.1
num_d,den_d=signal.cont2discrete((num,den),Ts)[0:2]
H= signal.TransferFunction(num_d,den_d)
print('H(s)=',H)
t,y = signal.step(H)
plt.stem(t,y)
plt.title("step response")
plt.xlabel("t")
plt.ylabel("H(s)")
plt.grid()
plt.show()