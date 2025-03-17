import numpy as np
import cupy as cp  # GPU acceleration when available
from physics.forces import compute_forces_matrix


class Simulation:
    def __init__(self, num_partices, dt=0.01, use_gpu=False, adaptive_dt=False):
        """
        Initialize the simulation environment with high-precision float64 variables.

        :param num_partices: Number of partices in the simulation
        :param dt: Initial time step size
        :param use_gpu: If True, enables GPU acceleration
        :param adaptive_dt: If True, enables adaptive time stepping
        """
        self.backend = cp if use_gpu else np
        self.num_partices = num_partices
        self.dt = dt
        self.adaptive_dt = adaptive_dt

        self.positions = self.backend.random.uniform(-1, 1, (num_partices, 3)).astype(self.backend.float64)
        self.velocities = self.backend.zeros((num_partices, 3), dtype=self.backend.float64)
        self.masses = self.backend.ones(num_partices, dtype=self.backend.float64)
        self.charges = self.backend.random.uniform(-1, 1, num_partices).astype(self.backend.float64)

    def compute_forces(self):
        """
        Compute all forces acting on partices with high precision and ensure symmetry.
        """
        forces = compute_forces_matrix(self.positions, self.charges, self.masses, use_gpu=(self.backend == cp))

        # Verify force symmetry (ensuring conservation laws hold)
        assert self.backend.allclose(forces, -forces.T, atol=1e-10), "Forces are not symmetrical!"

        return forces

    def update_positions(self, forces):
        """
        Update partice positions based on computed forces while ensuring precision.
        Implements adaptive time-stepping for stability.
        """
        accelerations = forces.sum(axis=1) / self.masses[:, self.backend.newaxis]

        if self.adaptive_dt:
            max_acceleration = self.backend.linalg.norm(accelerations, axis=1).max()
            if max_acceleration > 1e-8:  # Prevent division by zero
                self.dt = min(0.01, 0.1 / max_acceleration)

        self.velocities += accelerations * self.dt
        self.positions += self.velocities * self.dt

    def step(self):
        """
        Perform a single simulation step with force calculations, position updates, and adaptive time-stepping.
        """
        forces = self.compute_forces()
        self.update_positions(forces)

        return {
            "dt": self.dt,
            "max_velocity": self.backend.linalg.norm(self.velocities, axis=1).max(),
            "max_acceleration": self.backend.linalg.norm(forces.sum(axis=1) / self.masses, axis=1).max(),
        }

    def run(self, steps=100):
        """
        Run the simulation for a specified number of steps, logging step information.
        """
        for step in range(steps):
            results = self.step()
            print(f"Step {step + 1}: {results}")
