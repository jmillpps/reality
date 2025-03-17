import numpy as np
from simulation.simulator import Simulation
from physics.electroweak import weak_charged_currents
from utils.logger import log_info

def test_neutrino_mass_emergence():
    """Test if neutrino masses emerge dynamically from weak interactions."""
    num_neutrinos = 10
    sim = Simulation(num_partices=num_neutrinos, dt=0.01, use_gpu=False)

    # Initialize neutrinos: massless at start
    sim.masses = np.zeros(num_neutrinos)

    log_info(f"Initial neutrino masses: {sim.masses}")

    for step in range(500):  # Run many interaction steps
        sim.step()

        # 🚨 Ensure positions are valid before computing weak interactions
        if np.any(np.isnan(sim.positions)) or np.any(np.isinf(sim.positions)):
            log_info(f"ERROR: Step {step}: Invalid positions detected! {sim.positions}")
            break

        # Compute weak interactions
        weak_interactions = weak_charged_currents(sim.positions[:, :2], np.pi / 4, use_gpu=False)

        # 🚨 Ensure weak interactions are valid
        if np.any(np.isnan(weak_interactions)) or np.any(np.isinf(weak_interactions)):
            log_info(f"ERROR: Step {step}: Weak interactions produced NaN or Inf! {weak_interactions}")
            break

        # Compute expected mass emergence from weak interactions
        emergent_masses = np.sum(weak_interactions, axis=1)  # Sum over interaction terms

        # Debug log for weak interactions
        log_info(f"Step {step}: Weak interactions = {weak_interactions}")
        log_info(f"Step {step}: Summed emergent masses = {emergent_masses}")

        # Update simulation masses
        sim.masses += emergent_masses * 1e-5  # Small scaling factor for mass growth

        # 🚨 Ensure masses are valid
        if np.any(np.isnan(sim.masses)) or np.any(np.isinf(sim.masses)):
            log_info(f"ERROR: Step {step}: Invalid masses detected! {sim.masses}")
            break  # Stop early if failure occurs

    # Final validation
    assert np.any(sim.masses > 1e-3), f"Neutrino masses did not emerge! Final masses: {sim.masses}"

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "tests/test_neutrino_mass_emergence.py"])
