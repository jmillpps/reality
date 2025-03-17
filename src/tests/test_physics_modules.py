import pytest
import numpy as np
from physics.forces import compute_forces_matrix
from physics.gravity import compute_gravitational_force
from physics.quantum import compute_wavefunction
from physics.thermodynamics import compute_entropy, compute_temperature
from physics.relativity import lorentz_factor, time_dilation
from physics.field_equations import einstein_field_equation
from physics.electroweak import weak_charged_currents
from physics.wave_mechanics import wave_interference

def test_compute_forces_matrix():
    positions = np.random.uniform(-1, 1, (10, 3))
    charges = np.random.uniform(-1, 1, 10)
    masses = np.ones(10)
    forces = compute_forces_matrix(positions, charges, masses, use_gpu=False)
    assert forces.shape == (10, 10, 3), "Forces matrix shape incorrect"

def test_compute_gravitational_force():
    force = compute_gravitational_force(1.0, 1.0, 1.0, use_gpu=False)
    assert force > 0, "Gravitational force should be positive"

def test_compute_wavefunction():
    position = np.random.uniform(-1, 1, (10, 3))
    momentum = np.random.uniform(-1, 1, (10, 3))
    wavefunction = compute_wavefunction(position, momentum, use_gpu=False)
    assert wavefunction.shape == (10,), "Wavefunction shape incorrect"

def test_compute_entropy():
    probabilities = np.random.uniform(0, 1, 10)
    probabilities /= probabilities.sum()  # Normalize to sum to 1
    entropy = compute_entropy(probabilities, use_gpu=False)
    assert entropy >= 0, "Entropy should be non-negative"

def test_compute_temperature():
    temperature = compute_temperature(100.0, 10, use_gpu=False)
    assert temperature > 0, "Temperature should be positive"

def test_lorentz_factor():
    velocity = np.array([0.5, 0.7, 0.9]) * 299792458  # Fraction of speed of light
    gamma = lorentz_factor(velocity, use_gpu=False)
    assert np.all(gamma > 1), "Lorentz factor should be greater than 1"

def test_time_dilation():
    proper_time = 1.0
    velocity = 0.9 * 299792458  # 90% speed of light
    dilated_time = time_dilation(proper_time, velocity, use_gpu=False)
    assert dilated_time > proper_time, "Dilated time should be greater than proper time"

def test_einstein_field_equation():
    stress_energy = np.random.uniform(0, 1, (4, 4))
    metric_tensor = np.eye(4)
    einstein_eq = einstein_field_equation(stress_energy, metric_tensor, use_gpu=False)
    assert einstein_eq.shape == (4, 4), "Einstein equation output shape incorrect"

def test_weak_charged_currents():
    fermion_state = np.random.uniform(-1, 1, (10, 2))
    weak_interaction = weak_charged_currents(fermion_state, np.pi / 4, use_gpu=False)
    assert weak_interaction.shape == (10, 2), "Weak interaction output shape incorrect"

def test_wave_interference():
    position = np.linspace(-10, 10, 100)
    k1, k2 = 1.0, 2.0
    interference_pattern = wave_interference(position, k1, k2, use_gpu=False)
    assert interference_pattern.shape == (100,), "Wave interference shape incorrect"

if __name__ == "__main__":
    pytest.main(["-v"])
