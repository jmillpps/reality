import numpy as np
import cupy as cp  # GPU acceleration when available

# Define fundamental constants
hbar = 1.054571817e-34  # Reduced Planck's constant (J·s)
c = 299792458  # Speed of light (m/s)


def compute_wavefunction(position, momentum, use_gpu=False):
    """
    Compute the wavefunction using a plane wave approximation.
    
    :param position: Position vector
    :param momentum: Momentum vector
    :param use_gpu: If True, uses GPU acceleration
    :return: Complex wavefunction value
    """
    backend = cp if use_gpu else np
    x, y, z = position
    p_x, p_y, p_z = momentum
    k = backend.array([p_x / hbar, p_y / hbar, p_z / hbar])
    phase = backend.dot(k, backend.array([x, y, z]))
    return backend.exp(1j * phase)


def compute_uncertainty_relation(delta_x, delta_p):
    """
    Compute the Heisenberg Uncertainty Relation.
    
    :param delta_x: Position uncertainty
    :param delta_p: Momentum uncertainty
    :return: Heisenberg uncertainty value (should be >= hbar/2)
    """
    return delta_x * delta_p


def compute_neutrino_oscillation_probability(theta, delta_m2, L, E):
    """
    Compute the probability of neutrino oscillation.
    
    :param theta: Mixing angle
    :param delta_m2: Mass-squared difference
    :param L: Travel distance
    :param E: Neutrino energy
    :return: Oscillation probability
    """
    return np.sin(2 * theta) ** 2 * np.sin(1.27 * delta_m2 * L / E) ** 2
