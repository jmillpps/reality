import numpy as np
import cupy as cp  # GPU acceleration when available

# Define electroweak constants
g_weak = 0.653  # Weak interaction coupling constant
g_hypercharge = 0.357  # U(1) hypercharge coupling constant
v_higgs = 246.0  # Higgs vacuum expectation value (GeV)

def higgs_potential(phi, use_gpu=False):
    """
    Compute the Higgs potential V(phi) = -μ^2 |φ|^2 + λ |φ|^4.
    
    :param phi: Higgs field value
    :param use_gpu: If True, uses GPU acceleration
    :return: Higgs potential value
    """
    backend = cp if use_gpu else np
    mu_squared = -(v_higgs**2) / 2  # Approximate mass term
    lambd = 0.13  # Higgs self-coupling constant
    return mu_squared * backend.abs(phi)**2 + lambd * backend.abs(phi)**4

def weak_charged_currents(fermion_state, mixing_angle, use_gpu=False):
    """
    Compute weak charged currents using SU(2) mixing.
    
    :param fermion_state: Input fermion state vector (doublet)
    :param mixing_angle: Weak mixing angle (θ_W)
    :param use_gpu: If True, uses GPU acceleration
    :return: Transformed weak-interaction doublet
    """
    backend = cp if use_gpu else np
    
    # SU(2) weak interaction mixing matrix
    mixing_matrix = backend.array([
        [backend.cos(mixing_angle), backend.sin(mixing_angle)],
        [-backend.sin(mixing_angle), backend.cos(mixing_angle)]
    ])
    return backend.dot(fermion_state, mixing_matrix.T)

def z_boson_mass(use_gpu=False):
    """
    Compute the Z boson mass using electroweak symmetry breaking.
    
    :param use_gpu: If True, uses GPU acceleration
    :return: Z boson mass (GeV)
    """
    backend = cp if use_gpu else np
    return (v_higgs / 2) * backend.sqrt(g_weak**2 + g_hypercharge**2)

def w_boson_mass(use_gpu=False):
    """
    Compute the W boson mass from the weak interaction coupling.
    
    :param use_gpu: If True, uses GPU acceleration
    :return: W boson mass (GeV)
    """
    backend = cp if use_gpu else np
    return (v_higgs / 2) * g_weak
