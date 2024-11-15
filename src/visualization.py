# src/visualization.py
import matplotlib.pyplot as plt
import os
from datetime import datetime

def create_visualization(data, column_x, column_y, title):
    """Create and save a simple line plot visualization."""
    plt.figure()
    plt.plot(data[column_x], data[column_y], marker='o')
    plt.title(title)
    plt.xlabel(column_x)
    plt.ylabel(column_y)

    # Save the visualization with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"history/visuals/{title}_{timestamp}.png"
    plt.savefig(filename)
    plt.close()
    
    print(f"Visualization saved as {filename}")
    return filename  # Return the path for reference
