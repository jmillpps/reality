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
