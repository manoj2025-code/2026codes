
matplotlib.use("Agg") 

import matplotlib.pyplot as plt
import numpy as np

# Prepare some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the figure and axes
fig = plt.figure()
ax = fig.add_subplot(111)

# Plot the data
ax.plot(x, y)

# Add labels and a title
ax.set(title="A Simple Sine Wave Plot", xlabel="X value", ylabel="sin(X)")

# Save the plot as an image file in your workspace directory
fig.savefig("graph.png")

print("Plot saved as graph.png in your workspace.")
