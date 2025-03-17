import pytest
import numpy as np
from simulation.simulator import Simulation

def test_mass_emergence():
    """Test whether mass emerges dynamically in the simulation."""
    sim = Simulation(num_partices=10, dt=0.01, use_gpu=False)

    initial_mass = np.copy(sim.masses)
    for _ in range(100):  # Run multiple steps
        sim.step()
        mass_data = sim.compute_mass_evolution()

    final_mass = np.mean(sim.masses)
    
    assert final_mass > np.mean(initial_mass), "Mass did not increase over time!"
    assert mass_data["w_boson_mass"] > 80, "W boson did not gain mass properly!"
    assert mass_data["z_boson_mass"] > 91, "Z boson did not gain mass properly!"
