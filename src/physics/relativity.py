import numpy as np
import cupy as cp  # GPU acceleration when available

# Define fundamental constants
c = 299792458  # Speed of light (m/s)

def lorentz_factor(velocity, use_gpu=False):
    """
    Compute the Lorentz factor (gamma) for a given velocity.

    :param velocity: Velocity of the object (scalar or array)
    :param use_gpu: If True, uses GPU acceleration
    :return: Lorentz factor
    """
    backend = cp if use_gpu else np
    v_safe = backend.minimum(velocity, c * 0.99999)  # Adjusted threshold to 99.999% of c
    gamma = 1 / backend.sqrt(backend.maximum(1 - (v_safe**2 / c**2), 1e-12))
    return gamma.astype(backend.float64)  # Ensure high precision

def compute_space_time_evolution(N, T):
    """
    Compute the relational evolution of space-time.

    :param N: Current space-time state
    :param T: Time evolution step
    :return: Updated space-time state
    """
    return T(N)

def time_dilation(proper_time, velocity, use_gpu=False):
    """
    Compute time dilation due to relativistic effects.

    :param proper_time: Time measured in the object's rest frame
    :param velocity: Velocity of the moving object
    :param use_gpu: If True, uses GPU acceleration
    :return: Dilated time observed in another frame
    """
    backend = cp if use_gpu else np
    gamma = lorentz_factor(velocity, use_gpu)
    return proper_time * gamma
