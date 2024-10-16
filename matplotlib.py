import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)  # Sine of each x point

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='y = sin(x)', color='blue', linewidth=2)

# Add title and labels
plt.title('Sine Function')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add grid and legend
plt.grid()
plt.legend()

# Show the plot
plt.show()
