import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample data for the portfolio
stocks = [
    {"name": "Stock A", "return": 0.12, "risk": 0.15, "diversification": 0.8},
    {"name": "Stock B", "return": 0.08, "risk": 0.10, "diversification": 0.9},
    {"name": "Stock C", "return": 0.15, "risk": 0.20, "diversification": 0.7},
    {"name": "Stock D", "return": 0.10, "risk": 0.12, "diversification": 0.85},
    {"name": "Stock E", "return": 0.18, "risk": 0.25, "diversification": 0.6},
]

# Extract data for plotting
names = [stock["name"] for stock in stocks]
returns = [stock["return"] for stock in stocks]
risks = [stock["risk"] for stock in stocks]
diversifications = [stock["diversification"] for stock in stocks]

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# Scatter plot for the stocks
scatter = ax.scatter(returns, risks, diversifications, c=diversifications, cmap="viridis", s=100)

# Add labels and title
ax.set_xlabel("Expected Return")
ax.set_ylabel("Risk (Standard Deviation)")
ax.set_zlabel("Diversification Score")
ax.set_title("3D Portfolio Visualization")

# Add annotations for each stock
for i, name in enumerate(names):
    ax.text(returns[i], risks[i], diversifications[i], name, fontsize=9)

# Add a colorbar
cbar = fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=5)
cbar.set_label("Diversification Score")

# Show the plot
plt.show()