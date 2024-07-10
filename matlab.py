# Define a class called Solution to store time series data along with corresponding y-values for different concentrations.
class Solution:
    def __init__(self, t, y):
        self.t = t  # Initialize the time array
        self.y = y  # Initialize the array of y-values (different concentrations)

# Example data setup for time and various concentrations.
time = [0, 1, 2, 3, 4]
ligand_concentration = [0, 1, 2, 3, 4]
protein_concentration = [0, 2, 4, 6, 8]
complex_concentration = [0, 1, 4, 9, 16]

# Create an instance of the Solution class with the provided time and concentration data.
solution = Solution(time, [ligand_concentration, protein_concentration, complex_concentration])

# Import matplotlib's pyplot to enable plotting functions.
import matplotlib.pyplot as plt

# Extracting time and concentrations from the solution object.
time = solution.t
ligand_concentration = solution.y[0]
protein_concentration = solution.y[1]
complex_concentration = solution.y[2]

# Setting up a figure for plotting with a specific size.
plt.figure(figsize=(10, 6))

# Plotting ligand concentration over time.
plt.plot(time, ligand_concentration, label='Ligand [L]', color='blue')  # Blue line for ligand

# Plotting protein concentration over time.
plt.plot(time, protein_concentration, label='Protein [P]', color='red')  # Red line for protein

# Plotting complex concentration over time.
plt.plot(time, complex_concentration, label='Complex [PL]', color='green')  # Green line for complex

# Adding a title to the plot.
plt.title('Concentration vs. Time for Ligand, Protein, and Complex')

# Labeling the x-axis.
plt.xlabel('Time (seconds)')

# Labeling the y-axis.
plt.ylabel('Concentration (M)')

# Displaying a legend to identify the different data series.
plt.legend()

# Adding a grid to the plot for better readability of the values.
plt.grid(True)

# Displaying the plot.
plt.show()
