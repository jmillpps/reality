import numpy as np
import cupy as cp  # GPU acceleration when available
from physics.forces import compute_forces_matrix
from physics.electroweak import weak_charged_currents  # Ensure this conserves energy properly
from physics.thermodynamics import compute_entropy, compute_temperature
from physics.relativity import lorentz_factor

class Simulation:
    def __init__(self, num_partices, dt=0.01, use_gpu=False):
        """
        Initialize the simulation with particles, positions, velocities, and forces.
        """
        self.num_partices = num_partices
        self.dt = dt
        self.use_gpu = use_gpu
        self.backend = np  # Placeholder for GPU acceleration support

        # Initialize positions, velocities, masses, and charges
        self.positions = np.random.rand(num_partices, 3)
        self.velocities = np.zeros((num_partices, 3))
        self.masses = np.ones(num_partices)  # Assume unit mass for now
        self.charges = np.zeros(num_partices)  # Default: neutral

        self.adaptive_dt = True
        self.energies = np.zeros(num_partices)
        self.initial_energy = None

    def compute_forces(self):
        """
        Compute all forces acting on particles and enforce symmetry.
        """
        forces = compute_forces_matrix(self.positions, self.charges, self.masses, use_gpu=self.use_gpu)

        # Ensure Newton’s Third Law is enforced: action-reaction symmetry
        forces = (forces - forces.swapaxes(0, 1)) * 0.5
        return forces

    def update_positions(self, forces):
        """
        Update particle positions and velocities using Newton's second law.
        """
        net_forces = forces.sum(axis=1)  # Shape (num_partices, 3)
        accelerations = net_forces / self.masses[:, None]  # Correct shape alignment

        if self.adaptive_dt:
            max_acceleration = self.backend.linalg.norm(accelerations, axis=1).max()
            if max_acceleration > 1e-8:  # Prevent division by zero
                self.dt = min(0.01, 0.1 / max_acceleration, 1e-5)

        self.velocities += accelerations * self.dt
        self.positions += self.velocities * self.dt

    def step(self):
        """
        Perform a single simulation step with force calculations, position updates, and energy renormalization.
        """
        forces = self.compute_forces()
        self.update_positions(forces)

        # Compute weak force interactions
        fermion_states = self.positions[:, :2]
        weak_interactions = weak_charged_currents(fermion_states, np.pi / 4, use_gpu=self.use_gpu)

        if self.initial_energy is None:
            self.initial_energy = self.energies.sum()

        # Compute system entropy from velocity distributions
        velocities_magnitude = np.linalg.norm(self.velocities, axis=1)
        probability_distribution = velocities_magnitude / np.sum(velocities_magnitude + 1e-10)  # Normalize safely
        entropy = compute_entropy(probability_distribution, use_gpu=self.use_gpu)

        # Compute temperature using kinetic energy
        kinetic_energy = 0.5 * np.sum(self.masses[:, None] * self.velocities**2)  # Sum over all particles
        temperature = compute_temperature(kinetic_energy, self.num_partices, use_gpu=self.use_gpu)

        # Compute Lorentz factors for each particle
        lorentz_factors = lorentz_factor(self.velocities, use_gpu=self.use_gpu)  # ✅ Added Lorentz factor computation

        # Adaptive energy renormalization
        current_energy = self.energies.sum()
        if abs(current_energy - self.initial_energy) / (self.initial_energy + 1e-10) > 1e-3:
            scale_factor = np.sqrt(self.initial_energy / (current_energy + 1e-10))
            self.velocities *= scale_factor  # Avoid division by zero

        return {
            "dt": self.dt,
            "max_velocity": self.backend.linalg.norm(self.velocities, axis=1).max(),
            "max_acceleration": self.backend.linalg.norm(forces.sum(axis=1), axis=1).max(),
            "weak_interactions": weak_interactions,
            "total_energy": self.energies.sum(),
            "entropy": entropy,
            "temperature": temperature,
            "lorentz_factors": lorentz_factors,  # ✅ Added Lorentz factors
        }
