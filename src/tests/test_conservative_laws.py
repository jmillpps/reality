import numpy as np
from simulation.simulator import Simulation

def test_energy_conservation():
    """Verify that total energy is conserved across simulation steps."""
    sim = Simulation(num_partices=10, dt=0.01, use_gpu=False)
    initial_energy = sim.energies.sum()

    for _ in range(100):  # Run multiple steps
        sim.step()

    final_energy = sim.energies.sum()
    assert np.isclose(initial_energy, final_energy, rtol=1e-5), f"Energy not conserved! Initial: {initial_energy}, Final: {final_energy}"

def test_momentum_conservation():
    """Verify that total momentum is conserved in the system."""
    sim = Simulation(num_partices=10, dt=0.01, use_gpu=False)
    initial_momentum = sim.velocities.sum(axis=0)

    for _ in range(100):  # Run multiple steps
        sim.step()

    final_momentum = sim.velocities.sum(axis=0)
    assert np.allclose(initial_momentum, final_momentum, rtol=1e-5), f"Momentum not conserved! Initial: {initial_momentum}, Final: {final_momentum}"
