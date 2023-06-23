import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

num = [5, 5]
den = [1, 5, 6]
Ts = 0.1

num_d, den_d = signal.cont2discrete((num, den), Ts)[0:2]
H = signal.TransferFunction(num_d, den_d)
print('H(s) =', H)

t, y = signal.step(H)

# Create the unit step signal
step_duration = int(t[-1] / Ts)  # Duration of the unit step signal based on the last time point of t
step = np.ones(step_duration)

# Convolve unit step signal with the step response
convolved = np.convolve(y, step, mode='full')[:len(t)]  # Truncate to match the length of t

# Plot the step response and the convolved signal
plt.stem(t, y, label='Step Response')
plt.stem(t, convolved, label='Convolved')
plt.title("Step Response Convolution with Unit Step Signal")
plt.xlabel("t")
plt.ylabel("H(s)")
plt.grid()
plt.legend()
plt.show()
