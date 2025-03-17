import pytest
import numpy as np
from simulation.simulator import Simulation

def test_gravity_and_electromagnetism():
    """Check if gravity and electromagnetism interact correctly in a mixed-charge system."""
    sim = Simulation(num_partices=10, dt=0.01, use_gpu=False)
    
    # Assign masses and charges randomly
    sim.masses = np.random.uniform(1, 10, size=sim.num_partices)
    sim.charges = np.random.uniform(-1, 1, size=sim.num_partices)
    
    forces = sim.compute_forces()
    
    # Ensure forces follow expected physical behavior
    for i in range(len(forces)):
        for j in range(i + 1, len(forces)):
            if sim.charges[i] * sim.charges[j] > 0:
                assert np.linalg.norm(forces[i, j]) < np.linalg.norm(forces[j, i]), "Charge interaction incorrect!"
            else:
                assert np.linalg.norm(forces[i, j]) > 0, "Opposite charges should attract!"

def test_weak_force_at_high_energy():
    """Check if weak force interactions behave correctly at relativistic speeds."""
    sim = Simulation(num_partices=10, dt=0.01, use_gpu=False)
    
    # Assign high velocities
    sim.velocities = np.random.uniform(0.8 * 299792458, 0.99 * 299792458, (sim.num_partices, 3))
    
    weak_interactions = sim.step()["weak_interactions"]

    assert not np.any(np.isnan(weak_interactions)), "Weak interactions failed at high energy!"
    assert np.any(weak_interactions > 0), "Weak force should be nonzero at high energy!"

if __name__ == "__main__":
    pytest.main(["-v", "tests/test_interaction_cross_validation.py"])
