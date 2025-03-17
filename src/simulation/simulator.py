class Simulation:
    def __init__(self, num_partices, dt=0.01, use_gpu=False, adaptive_dt=False):
        """
        Initialize the simulation environment with high-precision float64 variables.
        """
        self.backend = cp if use_gpu else np
        self.num_partices = num_partices
        self.dt = dt
        self.adaptive_dt = adaptive_dt

        self.positions = self.backend.random.uniform(-1, 1, (num_partices, 3)).astype(self.backend.float64)
        self.velocities = self.backend.zeros((num_partices, 3), dtype=self.backend.float64)
        self.masses = self.backend.ones(num_partices, dtype=self.backend.float64)
        self.charges = self.backend.random.uniform(-1, 1, num_partices).astype(self.backend.float64)
        self.energies = self.backend.zeros(num_partices, dtype=self.backend.float64)

        # Store initial energy for renormalization checks
        self.initial_energy = None

    def compute_forces(self):
        """
        Compute all forces acting on partices with high precision and ensure symmetry.
        """
        forces = compute_forces_matrix(self.positions, self.charges, self.masses, use_gpu=(self.backend == cp))

        # Verify force symmetry (ensuring conservation laws hold)
        assert self.backend.allclose(forces, -forces.swapaxes(0, 1), atol=1e-10), "Forces are not symmetrical!"

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
                self.dt = min(0.01, 0.1 / max_acceleration, 1e-5)

        self.velocities += accelerations * self.dt
        self.positions += self.velocities * self.dt

        # Update energy dynamically
        kinetic_energy = 0.5 * self.masses * self.backend.sum(self.velocities ** 2, axis=1)
        self.energies[:] = kinetic_energy  # Update energy array

    def step(self, step_count=0):
        """
        Perform a single simulation step with force calculations, position updates, and adaptive time-stepping.
        Includes adaptive energy renormalization.
        """
        forces = self.compute_forces()
        self.update_positions(forces)

        # Compute weak force interactions
        fermion_states = self.positions[:, :2]  # Extract first two spatial dimensions
        weak_interactions = weak_charged_currents(fermion_states, np.pi / 4, use_gpu=(self.backend == cp))

        # Initialize energy reference on first step
        if self.initial_energy is None:
            self.initial_energy = self.energies.sum()

        # Adaptive energy renormalization if drift > 0.1%
        current_energy = self.energies.sum()
        if abs(current_energy - self.initial_energy) / self.initial_energy > 1e-3:
            self.velocities *= self.backend.sqrt(self.initial_energy / current_energy)

        return {
            "dt": self.dt,
            "max_velocity": self.backend.linalg.norm(self.velocities, axis=1).max(),
            "max_acceleration": self.backend.linalg.norm(forces.sum(axis=1) / self.masses, axis=1).max(),
            "weak_interactions": weak_interactions,
            "total_energy": self.energies.sum(),
        }

    def run(self, steps=100):
        """
        Run the simulation for a specified number of steps, logging step information.
        """
        for step in range(steps):
            results = self.step(step_count=step)
            print(f"Step {step + 1}: {results}")
