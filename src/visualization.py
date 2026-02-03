import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot_population_trends(time_points, population_data, title="Population Trends Over Time"):
    """
    Plot population trends over time
    
    Parameters:
    time_points (array-like): Time points for x-axis
    population_data (array-like): Population sizes for y-axis
    title (str): Plot title
    """
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, population_data, linewidth=2, color='blue')
    plt.xlabel('Time')
    plt.ylabel('Population Size')
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_cell_size_distribution(cell_sizes, title="Cell Size Distribution"):
    """
    Plot distribution of cell sizes
    
    Parameters:
    cell_sizes (array-like): Array of cell size measurements
    title (str): Plot title
    """
    plt.figure(figsize=(10, 6))
    plt.hist(cell_sizes, bins=30, color='green', alpha=0.7, edgecolor='black')
    plt.xlabel('Cell Size')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()