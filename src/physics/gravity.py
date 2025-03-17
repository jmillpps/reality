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
    Uses Schwarzschild metric approximation.
    
    :param m: Mass of the object causing curvature
    :param r: Distance from the object
    :param use_gpu: If True, uses GPU acceleration
    :return: Warping factor
    """
    backend = cp if use_gpu else np
    r_safe = backend.maximum(r, 1e-10)
    return 1 - (2 * G * m) / (c**2 * r_safe)


def compute_time_dilation(m, r, use_gpu=False):
    """
    Compute time dilation due to gravitational field.
    
    :param m: Mass of gravitating object
    :param r: Distance from the mass
    :param use_gpu: If True, uses GPU acceleration
    :return: Time dilation factor
    """
    return np.sqrt(compute_space_time_warping(m, r, use_gpu))
