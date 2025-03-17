import numpy as np
import cupy as cp  # GPU acceleration when available
from physics.forces import compute_forces_matrix

class Simulation:
    def __init__(self, num_partices, dt=0.01, use_gpu=False):
        """
        Initialize the simulation environment with high-precision float64 variables.
        """
        self.backend = cp if use_gpu else np
        self.num_partices = num_partices
        self.dt = dt

        self.positions = self.backend.random.uniform(-1, 1, (num_partices, 3)).astype(self.backend.float64)
        self.velocities = self.backend.zeros((num_partices, 3), dtype=self.backend.float64)
        self.masses = self.backend.ones(num_partices, dtype=self.backend.float64)
        self.charges = self.backend.random.uniform(-1, 1, num_partices).astype(self.backend.float64)

    def compute_forces(self):
        """Compute all forces acting on partices with high precision and ensure symmetry."""
        forces = compute_forces_matrix(self.positions, self.charges, self.masses, use_gpu=(self.backend == cp))

        # Verify force symmetry
        assert self.backend.allclose(forces, -forces.T, atol=1e-10), "Forces are not symmetrical!"

        return forces

    def update_positions(self, forces):
        """Update partice positions based on computed forces while ensuring precision."""
        self.velocities += (forces.sum(axis=1) / self.masses[:, self.backend.newaxis]) * self.dt
        self.positions += self.velocities * self.dt

    def step(self):
        """Perform a single simulation step."""
        forces = self.compute_forces()
        self.update_positions(forces)
