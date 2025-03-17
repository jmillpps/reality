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
    v_safe = backend.minimum(velocity, c * 0.99)  # Limit velocity to 99% of c
    return 1 / backend.sqrt(1 - (v_safe**2 / c**2))

def relativistic_energy(mass, velocity, use_gpu=False):
    """
    Compute the relativistic total energy of an object.
    
    :param mass: Rest mass of the object
    :param velocity: Velocity of the object
    :param use_gpu: If True, uses GPU acceleration
    :return: Relativistic energy
    """
    backend = cp if use_gpu else np
    gamma = lorentz_factor(velocity, use_gpu)
    return gamma * mass * c**2


def relativistic_momentum(mass, velocity, use_gpu=False):
    """
    Compute the relativistic momentum of an object.
    
    :param mass: Rest mass of the object
    :param velocity: Velocity of the object
    :param use_gpu: If True, uses GPU acceleration
    :return: Relativistic momentum
    """
    backend = cp if use_gpu else np
    gamma = lorentz_factor(velocity, use_gpu)
    return gamma * mass * velocity


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
