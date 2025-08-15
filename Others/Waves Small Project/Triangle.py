# One ordinary day, someone asked me why the ripples on water remain perfectly circular even after throwing a brick into it.
# That question inspired the idea of creating a simple visualization of propagating waves according to wave theory.
#
# The visualization simulates the two-dimensional wave equation on a discrete grid.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

size = 100
frames = 100
damping = 0.99

u = np.zeros((size, size))
u_prev = np.zeros((size, size))

triangle_height = 10
center_x = size // 2
center_y = size // 2

for row in range(triangle_height):
    half_width = row
    left = center_x - half_width
    right = center_x + half_width + 1
    if 0 <= center_y + row < size:
        u[center_y + row, max(0, left):min(size, right)] = 0.5

x = np.arange(0, size)
y = np.arange(0, size)
X, Y = np.meshgrid(x, y)

fig = plt.figure(figsize=(12, 6))

ax3d = fig.add_subplot(1, 2, 1, projection='3d')
surf3d = ax3d.plot_surface(X, Y, u, cmap='viridis', vmin=-1, vmax=1)
ax3d.set_zlim(-1.2, 1.2)
ax3d.set_title("Fale 3D")
ax3d.set_xlabel("X")
ax3d.set_ylabel("Y")
ax3d.set_zlabel("Wysokość fali")

ax2d = fig.add_subplot(1, 2, 2)
img = ax2d.imshow(u, cmap='viridis', vmin=-1, vmax=1, origin='lower')
ax2d.set_title("Widok z góry")
ax2d.set_xlabel("X")
ax2d.set_ylabel("Y")
fig.colorbar(img, ax=ax2d, shrink=0.8)


def update(frame):
    global u, u_prev
    laplacian = (
            np.roll(u, 1, axis=0) +
            np.roll(u, -1, axis=0) +
            np.roll(u, 1, axis=1) +
            np.roll(u, -1, axis=1) -
            4 * u
    )
    u_new = 2 * u - u_prev + 0.2 * laplacian
    u_new *= damping
    u_prev, u = u, u_new

    ax3d.clear()
    ax3d.set_zlim(-1.2, 1.2)
    ax3d.set_title("Fale 3D")
    ax3d.set_xlabel("X")
    ax3d.set_ylabel("Y")
    ax3d.set_zlabel("Wysokość fali")
    ax3d.plot_surface(X, Y, u, cmap='viridis', vmin=-1, vmax=1)

    ax2d.clear()
    ax2d.set_title("Widok z góry")
    ax2d.set_xlabel("X")
    ax2d.set_ylabel("Y")
    ax2d.imshow(u, cmap='viridis', vmin=-1, vmax=1, origin='lower')

    return []


ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=False)
plt.show()
