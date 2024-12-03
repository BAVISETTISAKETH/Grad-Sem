# src/visualization.py
import matplotlib.pyplot as plt
import os
from datetime import datetime
from src.config import VISUALS_DIR

def create_visualization(data, columns, title):
    """Create a visualization for the given columns."""
    os.makedirs(VISUALS_DIR, exist_ok=True)
    plt.figure(figsize=(10, 6))
    if len(columns) == 2:
        plt.scatter(data[columns[0]], data[columns[1]])
        plt.xlabel(columns[0])
        plt.ylabel(columns[1])
    else:
        plt.plot(data[columns[0]])
        plt.xlabel(columns[0])
        plt.ylabel("Values")

    plt.title(title)
    visual_path = os.path.join(VISUALS_DIR, f"{title}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
    plt.savefig(visual_path)
    plt.close()
    return visual_path
