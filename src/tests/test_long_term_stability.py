import pytest
import numpy as np
from simulation.simulator import Simulation

def test_long_term_stability():
    """Run the simulation for an extended period and ensure stability."""
    sim = Simulation(num_partices=10, dt=0.01, use_gpu=False)

    for _ in range(1000):  # Extended time steps
        sim.step()

    # Ensure no NaNs or infinities in positions or velocities
    assert not np.any(np.isnan(sim.positions)), "NaN values detected in positions!"
    assert not np.any(np.isinf(sim.positions)), "Infinity values detected in positions!"
    assert not np.any(np.isnan(sim.velocities)), "NaN values detected in velocities!"
    assert not np.any(np.isinf(sim.velocities)), "Infinity values detected in velocities!"
