import numpy as np
import cupy as cp  # GPU acceleration when available

# Define gravitational constants
G = 6.67430e-11  # Gravitational constant
c = 299792458  # Speed of light (m/s)

def compute_gravitational_force(m1, m2, r, use_gpu=False):
    """
    Compute the gravitational force between two masses.

    :param m1: Mass of first object
    :param m2: Mass of second object
    :param r: Distance between the two masses
    :param use_gpu: If True, uses GPU acceleration
    :return: Gravitational force magnitude
    """
    backend = cp if use_gpu else np
    r_safe = backend.maximum(r, 1e-10)  # Prevent division by zero
    return G * m1 * m2 / r_safe**2

def compute_space_time_warping(m, r, use_gpu=False):
    """
    Compute the space-time curvature caused by mass.

    :param m: Mass of the object causing curvature
    :param r: Distance from the object
    :param use_gpu: If True, uses GPU acceleration
    :return: Warping factor
    """
    backend = cp if use_gpu else np
    r_safe = backend.maximum(r, 1e-10)
    return 1 - (2 * G * m) / (c**2 * r_safe)

def gravitational_wave_propagation(frequency, distance, use_gpu=False):
    """
    Simulate gravitational wave propagation as a metric perturbation.

    :param frequency: Frequency of the gravitational wave
    :param distance: Distance of propagation
    :param use_gpu: If True, uses GPU acceleration
    :return: Gravitational wave perturbation factor
    """
    backend = cp if use_gpu else np
    phase = 2 * np.pi * frequency * (distance / c)
    return backend.exp(1j * phase) / distance

def einstein_curvature_check(positions, masses, use_gpu=False):
    """
    Check whether the system's curvature aligns with Einstein's field equations.

    This function estimates the local space-time curvature by summing over mass-induced perturbations.

    :param positions: Array of particle positions (N,3)
    :param masses: Array of particle masses (N,)
    :param use_gpu: If True, use GPU acceleration
    :return: Boolean (True if curvature is self-consistent, False otherwise)
    """
    backend = cp if use_gpu else np
    N = len(masses)

    # Compute pairwise distances
    r_matrix = backend.linalg.norm(
        positions[:, None, :] - positions[None, :, :], axis=-1
    ) + 1e-10  # Avoid division by zero

    # Compute Einstein curvature tensor components (approximate)
    curvature_matrix = (2 * G * masses[None, :]) / (c**2 * r_matrix)

    # Sum curvature effects
    total_curvature = backend.sum(curvature_matrix)

    # Normalize by system size
    average_curvature = total_curvature / N

    # Theoretical expectation for a stable system
    expected_curvature = (G / c**4) * backend.sum(masses) / N

    # Check if deviation is within an acceptable range
    return backend.abs(average_curvature - expected_curvature) < 1e-6
