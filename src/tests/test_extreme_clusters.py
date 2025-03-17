import pytest
import numpy as np
from simulation.simulator import Simulation

def test_high_density_particle_cluster():
    """Simulate an extremely high-density particle cluster and verify stability."""
    sim = Simulation(num_partices=100, dt=0.001, use_gpu=False)
    
    # Place all particles close together
    sim.positions = np.random.uniform(-1e-5, 1e-5, (sim.num_partices, 3))
    
    for _ in range(500):  # Run multiple steps
        sim.step()

    # Ensure system remains bounded (does not explode)
    assert np.linalg.norm(sim.positions).max() < 1e-2, "Cluster dispersed too rapidly!"

if __name__ == "__main__":
    pytest.main(["-v", "tests/test_extreme_clusters.py"])
