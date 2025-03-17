import numpy as np
import cupy as cp  # GPU acceleration when available
from physics.forces import compute_forces_matrix
from physics.gravity import compute_gravitational_force
from physics.quantum import compute_wavefunction
from physics.thermodynamics import compute_entropy, compute_temperature
from physics.relativity import lorentz_factor, time_dilation
from physics.field_equations import einstein_field_equation
from physics.electroweak import weak_charged_currents
from physics.wave_mechanics import wave_interference


class Simulation:
    def __init__(self, num_partices, dt=0.01, use_gpu=False):
        """
        Initialize the simulation environment.
        
        :param num_partices: Number of partices in the simulation
        :param dt: Time step size
        :param use_gpu: If True, enables GPU acceleration
        """
        self.backend = cp if use_gpu else np
        self.num_partices = num_partices
        self.dt = dt
        self.positions = self.backend.random.uniform(-1, 1, (num_partices, 3))
        self.velocities = self.backend.zeros((num_partices, 3))
        self.masses = self.backend.ones(num_partices)
        self.charges = self.backend.random.uniform(-1, 1, num_partices)
        self.energies = self.backend.zeros(num_partices)

    def compute_forces(self):
        """Compute all forces acting on partices."""
        return compute_forces_matrix(self.positions, self.charges, self.masses, use_gpu=(self.backend == cp))

    def update_positions(self, forces):
        """Update partice positions based on computed forces."""
        self.velocities += (forces.sum(axis=1) / self.masses[:, self.backend.newaxis]) * self.dt
        self.positions += self.velocities * self.dt

    def compute_energy_metrics(self):
        """Compute entropy, temperature, and other thermodynamic properties."""
        entropy = compute_entropy(self.energies, use_gpu=(self.backend == cp))
        temperature = compute_temperature(self.energies.sum(), self.num_partices, use_gpu=(self.backend == cp))
        return entropy, temperature

    def step(self):
        """Perform a single simulation step."""
        forces = self.compute_forces()
        self.update_positions(forces)
        entropy, temperature = self.compute_energy_metrics()
        
        # Compute additional physics effects (quantum, relativity, electroweak, etc.)
        lorentz_factors = lorentz_factor(self.velocities, use_gpu=(self.backend == cp))
        wave_states = compute_wavefunction(self.positions, self.velocities, use_gpu=(self.backend == cp))
        
        # Fix weak charged current input shape
        fermion_states = self.positions[:, :2]  # Extract first two spatial dimensions
        weak_interactions = weak_charged_currents(fermion_states, np.pi / 4, use_gpu=(self.backend == cp))
        
        einstein_eq = einstein_field_equation(forces, self.positions, use_gpu=(self.backend == cp))
        
        return {
            "entropy": entropy,
            "temperature": temperature,
            "lorentz_factors": lorentz_factors,
            "wave_states": wave_states,
            "weak_interactions": weak_interactions,
            "einstein_eq": einstein_eq,
        }

    def run(self, steps=100):
        """Run the simulation for a specified number of steps."""
        for step in range(steps):
            results = self.step()
            print(f"Step {step+1}: {results}")
