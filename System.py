import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
dt = 60 * 60 * 24  # Time step (1 day in seconds)
days = 365  # Number of days to simulate

# Celestial bodies: [mass (kg), initial position (m), initial velocity (m/s)]
sun = {
    "mass": 1.989e30,
    "position": np.array([0.0, 0.0, 0.0]),
    "velocity": np.array([0.0, 0.0, 0.0]),
}

mercury = {
    "mass": 3.3011e23,
    "position": np.array([5.791e10, 0.0, 0.0]),  # 0.39 AU from the sun
    "velocity": np.array([0.0, 47360, 0.0]),  # Mercury's orbital velocity
}

venus = {
    "mass": 4.8675e24,
    "position": np.array([1.082e11, 0.0, 0.0]),  # 0.72 AU from the sun
    "velocity": np.array([0.0, 35020, 0.0]),  # Venus's orbital velocity
}

earth = {
    "mass": 5.972e24,
    "position": np.array([1.496e11, 0.0, 0.0]),  # 1 AU from the sun
    "velocity": np.array([0.0, 29780, 0.0]),  # Earth's orbital velocity
}

mars = {
    "mass": 6.39e23,
    "position": np.array([2.279e11, 0.0, 0.0]),  # 1.52 AU from the sun
    "velocity": np.array([0.0, 24130, 0.0]),  # Mars's orbital velocity
}

jupiter = {
    "mass": 1.898e27,
    "position": np.array([7.785e11, 0.0, 0.0]),  # 5.20 AU from the sun
    "velocity": np.array([0.0, 13070, 0.0]),  # Jupiter's orbital velocity
}

saturn = {
    "mass": 5.683e26,
    "position": np.array([1.429e12, 0.0, 0.0]),  # 9.58 AU from the sun
    "velocity": np.array([0.0, 9690, 0.0]),  # Saturn's orbital velocity
}

# List of celestial bodies
bodies = [sun, mercury, venus, earth, mars, jupiter, saturn]

# Function to calculate gravitational force
def gravitational_force(body1, body2):
    r = body2["position"] - body1["position"]
    distance = np.linalg.norm(r)
    force_magnitude = G * body1["mass"] * body2["mass"] / distance**2
    force_direction = r / distance
    return force_magnitude * force_direction

# Function to update positions and velocities
def update_bodies(bodies, dt):
    for i, body1 in enumerate(bodies):
        total_force = np.array([0.0, 0.0, 0.0])
        for j, body2 in enumerate(bodies):
            if i != j:
                total_force += gravitational_force(body1, body2)
        # Update velocity and position using Euler's method
        body1["velocity"] += total_force / body1["mass"] * dt
        body1["position"] += body1["velocity"] * dt

# Initialize 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlim(-2e12, 2e12)
ax.set_ylim(-2e12, 2e12)
ax.set_zlim(-2e12, 2e12)
ax.set_aspect("auto")

# Create scatter plots for each body
scatters = [ax.scatter([], [], [], label=name) for name in ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"]]

# Function to initialize the animation
def init():
    for scatter in scatters:
        scatter._offsets3d = (np.empty(0), np.empty(0), np.empty(0))  # Initialize with empty arrays
    return scatters

# Function to update the animation
def update(frame):
    update_bodies(bodies, dt)
    for i, body in enumerate(bodies):
        scatters[i]._offsets3d = ([body["position"][0]], [body["position"][1]], [body["position"][2]])  # Update positions
    return scatters

# Create animation
ani = FuncAnimation(fig, update, frames=days, init_func=init, blit=True, interval=50)

# Add legend and labels
ax.legend()
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel("z (m)")
ax.set_title("3D Solar System Simulation")

# Show the animation
plt.show()