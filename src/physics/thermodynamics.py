import numpy as np
import cupy as cp  # GPU acceleration when available

# Define fundamental constants
k_B = 1.380649e-23  # Boltzmann constant (J/K)


def compute_entropy(probabilities, use_gpu=False):
    """
    Compute the entropy of a system using the Shannon entropy formula.
    
    :param probabilities: Array of probabilities for different microstates
    :param use_gpu: If True, uses GPU acceleration
    :return: Entropy value
    """
    backend = cp if use_gpu else np
    probabilities = backend.maximum(probabilities, 1e-10)  # Avoid log(0)
    return -k_B * backend.sum(probabilities * backend.log(probabilities))


def compute_temperature(energy, num_particles, use_gpu=False):
    """
    Compute the temperature of a system using the equipartition theorem.
    
    :param energy: Total energy of the system
    :param num_particles: Number of partices in the system
    :param use_gpu: If True, uses GPU acceleration
    :return: Temperature in Kelvin
    """
    backend = cp if use_gpu else np
    return (2 / 3) * (energy / (num_particles * k_B))


def compute_free_energy(energy, entropy, temperature, use_gpu=False):
    """
    Compute the Helmholtz free energy of a system.
    
    :param energy: Internal energy
    :param entropy: System entropy
    :param temperature: Temperature in Kelvin
    :param use_gpu: If True, uses GPU acceleration
    :return: Free energy
    """
    backend = cp if use_gpu else np
    return energy - temperature * entropy


def compute_heat_capacity(energy_variance, temperature, use_gpu=False):
    """
    Compute the heat capacity at constant volume.
    
    :param energy_variance: Variance of energy fluctuations
    :param temperature: Temperature in Kelvin
    :param use_gpu: If True, uses GPU acceleration
    :return: Heat capacity
    """
    backend = cp if use_gpu else np
    return energy_variance / (k_B * temperature**2)
