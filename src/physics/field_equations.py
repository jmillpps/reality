import numpy as np
import cupy as cp  # GPU acceleration when available

# Define fundamental constants
G = 6.67430e-11  # Gravitational constant
c = 299792458  # Speed of light (m/s)

def stress_energy_tensor(density, pressure, momentum_flux, use_gpu=False):
    """
    Compute the stress-energy tensor for a perfect fluid.
    
    :param density: Energy density (scalar or array)
    :param pressure: Isotropic pressure (scalar or array)
    :param momentum_flux: Momentum flux vector (array-like)
    :param use_gpu: If True, uses GPU acceleration
    :return: 4x4 Stress-Energy Tensor
    """
    backend = cp if use_gpu else np
    
    T = backend.zeros((4, 4))
    T[0, 0] = density * c**2  # Energy component
    T[1, 1] = T[2, 2] = T[3, 3] = pressure  # Spatial pressure terms
    
    # Momentum flux terms
    for i in range(1, 4):
        T[0, i] = T[i, 0] = momentum_flux[i - 1] * c  
    
    return T


def einstein_tensor(ricci_tensor, ricci_scalar, metric_tensor, use_gpu=False):
    """
    Compute the Einstein tensor from the Ricci tensor and Ricci scalar.
    
    :param ricci_tensor: 4x4 Ricci tensor
    :param ricci_scalar: Scalar curvature
    :param metric_tensor: 4x4 metric tensor
    :param use_gpu: If True, uses GPU acceleration
    :return: 4x4 Einstein tensor
    """
    backend = cp if use_gpu else np
    return ricci_tensor - (0.5 * ricci_scalar * metric_tensor)


def einstein_field_equation(stress_energy, metric_tensor, use_gpu=False):
    """
    Compute the Einstein field equations (EFE): G_uv = (8πG/c^4) * T_uv.
    
    :param stress_energy: 4x4 stress-energy tensor
    :param metric_tensor: 4x4 metric tensor
    :param use_gpu: If True, uses GPU acceleration
    :return: 4x4 Einstein field equation tensor
    """
    backend = cp if use_gpu else np
    
    # Compute Ricci scalar as trace of the Ricci tensor
    ricci_scalar = backend.trace(stress_energy)
    
    # Compute Ricci tensor approximation
    ricci_tensor = stress_energy / c**4
    
    # Compute Einstein tensor
    G_uv = einstein_tensor(ricci_tensor, ricci_scalar, metric_tensor, use_gpu)
    
    return (8 * np.pi * G / c**4) * G_uv
