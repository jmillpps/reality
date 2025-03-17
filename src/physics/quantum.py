import numpy as np
import cupy as cp  # GPU acceleration when available

# Define fundamental constants
hbar = 1.054571817e-34  # Reduced Planck's constant (J·s)
c = 299792458  # Speed of light (m/s)

def compute_wavefunction(position, momentum, use_gpu=False):
    """
    Compute the wavefunction using a plane wave approximation.

    :param position: Nx3 position matrix
    :param momentum: Nx3 momentum matrix
    :param use_gpu: If True, uses GPU acceleration
    :return: Nx1 Complex wavefunction values
    """
    backend = cp if use_gpu else np

    # Compute wavefunction in vectorized form
    k = momentum / hbar
    phase = backend.sum(k * position, axis=1)  # Dot product for each row
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

def pmns_matrix(theta12, theta13, theta23, delta_cp):
    """
    Compute the Pontecorvo-Maki-Nakagawa-Sakata (PMNS) matrix for neutrino oscillations.

    :param theta12: Solar mixing angle
    :param theta13: Reactor mixing angle
    :param theta23: Atmospheric mixing angle
    :param delta_cp: CP-violating phase
    :return: 3x3 PMNS matrix
    """
    s12, c12 = np.sin(theta12), np.cos(theta12)
    s13, c13 = np.sin(theta13), np.cos(theta13)
    s23, c23 = np.sin(theta23), np.cos(theta23)
    delta = np.exp(1j * delta_cp)

    U_pmns = np.array([
        [c12 * c13, s12 * c13, s13 * delta],
        [-s12 * c23 - c12 * s23 * s13 * delta, c12 * c23 - s12 * s23 * s13 * delta, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * delta, -c12 * s23 - s12 * c23 * s13 * delta, c23 * c13]
    ])

    return U_pmns
