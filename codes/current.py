import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
I_0 = 1  # Initial current
R_over_L = 1e7  # R/L

# Define the time range
t = np.linspace(0, 1e-6, 1000)  # Time from 0 to 1e-6 seconds

# Calculate the current values
I = I_0 - (4/5) * I_0 * np.exp(-10**7 * t)

# Plot the graph
plt.plot(t, I, label=r'$I(t) = I_0 - \frac{4}{5}I_0 e^{-10^{7}t}$')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.title('Current vs. Time')
plt.legend()
plt.grid(True)
plt.show()
