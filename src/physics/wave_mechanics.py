import numpy as np
import cupy as cp  # GPU acceleration when available

# Define fundamental constants
hbar = 1.054571817e-34  # Reduced Planck's constant (J·s)


def wave_superposition(wave1, wave2, use_gpu=False):
    """
    Compute the superposition of two wavefunctions.
    
    :param wave1: First wavefunction (complex)
    :param wave2: Second wavefunction (complex)
    :param use_gpu: If True, uses GPU acceleration
    :return: Superimposed wavefunction
    """
    backend = cp if use_gpu else np
    return wave1 + wave2


def wave_packet(position, k0, sigma, use_gpu=False):
    """
    Construct a Gaussian wave packet centered at k0.
    
    :param position: Position vector
    :param k0: Central wavevector
    :param sigma: Width of wave packet
    :param use_gpu: If True, uses GPU acceleration
    :return: Wave packet function
    """
    backend = cp if use_gpu else np
    return backend.exp(-(position**2) / (2 * sigma**2)) * backend.exp(1j * k0 * position)


def quantum_entanglement(state1, state2, use_gpu=False):
    """
    Compute the entangled state of two quantum states.
    
    :param state1: First quantum state (complex vector)
    :param state2: Second quantum state (complex vector)
    :param use_gpu: If True, uses GPU acceleration
    :return: Entangled quantum state
    """
    backend = cp if use_gpu else np
    return backend.kron(state1, state2) / backend.sqrt(2)


def wave_interference(position, k1, k2, use_gpu=False):
    """
    Compute interference pattern of two wavefunctions with different wavevectors.
    
    :param position: Position vector
    :param k1: Wavevector of first wavefunction
    :param k2: Wavevector of second wavefunction
    :param use_gpu: If True, uses GPU acceleration
    :return: Resultant wavefunction with interference effects
    """
    backend = cp if use_gpu else np
    wave1 = backend.exp(1j * k1 * position)
    wave2 = backend.exp(1j * k2 * position)
    return wave1 + wave2
