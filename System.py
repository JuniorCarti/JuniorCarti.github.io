import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
dt = 60 * 60 * 24  # Time step (1 day in seconds)
days = 365  # Number of days to simulate

# Celestial bodies: [mass (kg), initial position (m), initial velocity (m/s)]
sun = {
    "mass": 1.989e30,
    "position": np.array([0.0, 0.0]),
    "velocity": np.array([0.0, 0.0]),
}

earth = {
    "mass": 5.972e24,
    "position": np.array([1.496e11, 0.0]),  # 1 AU from the sun
    "velocity": np.array([0.0, 29780]),  # Earth's orbital velocity
}

mars = {
    "mass": 6.39e23,
    "position": np.array([2.279e11, 0.0]),  # 1.52 AU from the sun
    "velocity": np.array([0.0, 24130]),  # Mars's orbital velocity
}

# List of celestial bodies
bodies = [sun, earth, mars]

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
        total_force = np.array([0.0, 0.0])
        for j, body2 in enumerate(bodies):
            if i != j:
                total_force += gravitational_force(body1, body2)
        # Update velocity and position using Euler's method
        body1["velocity"] += total_force / body1["mass"] * dt
        body1["position"] += body1["velocity"] * dt

# Initialize plot
fig, ax = plt.subplots()
ax.set_xlim(-3e11, 3e11)
ax.set_ylim(-3e11, 3e11)
ax.set_aspect("equal")

# Create scatter plots for each body
scatters = [ax.scatter([], [], label=name) for name in ["Sun", "Earth", "Mars"]]

# Function to initialize the animation
def init():
    for scatter in scatters:
        scatter.set_offsets(np.empty((0, 2)))  # Initialize with empty 2D array
    return scatters

# Function to update the animation
def update(frame):
    update_bodies(bodies, dt)
    for i, body in enumerate(bodies):
        scatters[i].set_offsets([body["position"]])  # Update positions
    return scatters

# Create animation
ani = FuncAnimation(fig, update, frames=days, init_func=init, blit=True, interval=50)

# Add legend and labels
ax.legend()
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Solar System Simulation")

# Show the animation
plt.show()