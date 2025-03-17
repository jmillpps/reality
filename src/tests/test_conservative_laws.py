import pytest
import numpy as np
from simulation.simulator import Simulation

def test_energy_conservation():
    """Verify that total energy is conserved across simulation steps."""
    sim = Simulation(num_partices=10, dt=0.01, use_gpu=False)
    initial_energy = sim.energies.sum()
    
    for _ in range(100):  # Run multiple steps
        sim.step()

    final_energy = sim.energies.sum()
    assert np.isclose(initial_energy, final_energy, rtol=1e-5), "Total energy not conserved!"

def test_momentum_conservation():
    """Verify that total momentum is conserved in the system."""
    sim = Simulation(num_partices=10, dt=0.01, use_gpu=False)
    initial_momentum = sim.velocities.sum(axis=0)
    
    for _ in range(100):  # Run multiple steps
        sim.step()

    final_momentum = sim.velocities.sum(axis=0)
    assert np.allclose(initial_momentum, final_momentum, rtol=1e-5), "Total momentum not conserved!"

def test_force_symmetry():
    """Ensure Newton's third law (action-reaction) holds in force computations."""
    sim = Simulation(num_partices=10, dt=0.01, use_gpu=False)
    forces = sim.compute_forces()
    
    # Verify equal and opposite forces
    for i in range(len(forces)):
        for j in range(i + 1, len(forces)):
            assert np.allclose(forces[i, j], -forces[j, i], rtol=1e-5), "Forces are not symmetric!"

if __name__ == "__main__":
    pytest.main(["-v", "tests/test_conservation_laws.py"])
