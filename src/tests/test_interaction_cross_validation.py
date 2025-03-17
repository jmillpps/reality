import pytest
import numpy as np
from simulation.simulator import Simulation

def test_gravity_and_electromagnetism():
    """Check if gravity and electromagnetism interact correctly in a mixed-charge system."""
    sim = Simulation(num_partices=10, dt=0.01, use_gpu=False)

    # Assign random masses and charges
    sim.masses = np.random.uniform(1, 10, size=sim.num_partices)
    sim.charges = np.random.uniform(-1, 1, size=sim.num_partices)

    forces = sim.compute_forces()

    # Ensure forces follow expected physical behavior
    for i in range(len(forces)):
        for j in range(i + 1, len(forces)):
            if sim.charges[i] * sim.charges[j] > 0:  # Like charges should repel
                assert np.linalg.norm(forces[i, j]) > np.linalg.norm(forces[j, i]) * 0.99, "Charge interaction incorrect!"
            elif sim.charges[i] * sim.charges[j] < 0:  # Opposite charges should attract
                assert np.linalg.norm(forces[i, j]) > 1e-10, "Opposite charges should attract!"
