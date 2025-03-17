import pytest
from simulation.simulator import Simulation
from utils.logger import log_info

def test_simulation_step():
    """Test a single simulation step to verify computations and logging."""
    sim = Simulation(num_partices=10, dt=0.01, use_gpu=False)
    results = sim.step()
    
    assert "entropy" in results, "Entropy calculation missing from simulation results."
    assert "temperature" in results, "Temperature calculation missing from simulation results."
    assert "lorentz_factors" in results, "Lorentz factor computation missing from simulation results."
    assert "weak_interactions" in results, "Weak interactions missing from simulation results."
    
    log_info("Test simulation step executed successfully.")

if __name__ == "__main__":
    pytest.main(["-v", "src/tests/test_simulation.py"])
