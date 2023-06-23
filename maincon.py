import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

num = np.array([5, 5])
den = np.array([1, 5, 6])
H = signal.TransferFunction(num, den)
print('H(s) =', H)

t, y = signal.step(H)

# Create the unit step signal
step_duration = 20  # Duration of the unit step signal
step = np.heaviside(t, 1)

# Convolve unit step signal with the step response
convolved = np.convolve(y, step, mode='full')[:len(t)]  # Truncate to match the length of t

# Plot the step response and the convolved signal
plt.plot(t, y, label='Step Response')
plt.plot(t, convolved, label='Convolved')
plt.title("Step Response Convolution with Unit Step Signal")
plt.xlabel("t")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()
