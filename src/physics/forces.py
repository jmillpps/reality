import numpy as np
import cupy as cp  # GPU acceleration when available

# Define fundamental constants
G = 6.67430e-11  # Gravitational constant
k_e = 8.9875517923e9  # Coulomb's constant
lambda_w = 0.1  # Weak force range (arbitrary value for now)
d_cutoff = 0.5  # Strong force cutoff range (arbitrary value for now)
C = 1.0  # Weak force coefficient
S = 1.0  # Strong force coefficient

def compute_force(r, q1, q2, m1, m2, use_gpu=False):
    """
    Compute the total force between two partices using the Unified Force Equation.
    Supports both CPU (NumPy) and GPU (CuPy) execution.

    :param r: Distance between two partices
    :param q1, q2: Charge values of the partices
    :param m1, m2: Mass values of the partices
    :param use_gpu: If True, uses CuPy for GPU acceleration
    :return: Total force magnitude
    """
    backend = cp if use_gpu else np

    r_safe = backend.maximum(r, 1e-10)  # Prevent division by zero

    # Compute gravitational force
    F_grav = G * m1 * m2 / r_safe**2

    # Compute electromagnetic force
    F_em = k_e * q1 * q2 / r_safe**2

    # Compute weak nuclear force (short-range, exponentially decaying)
    F_weak = C * backend.exp(-r_safe / lambda_w)

    # Compute strong nuclear force (confinement behavior)
    F_strong = S * r_safe * backend.exp(-r_safe / d_cutoff)

    # Total force
    F_total = F_grav + F_em + F_weak + F_strong

    return F_total

def compute_forces_matrix(positions, charges, masses, use_gpu=False):
    """
    Compute the pairwise forces between all partices in a system.
    Supports GPU acceleration for large-scale simulations.

    :param positions: Nx3 array of partice positions
    :param charges: N-length array of partice charges
    :param masses: N-length array of partice masses
    :param use_gpu: If True, performs computation on GPU
    :return: NxN force matrix
    """
    backend = cp if use_gpu else np

    N = positions.shape[0]
    forces = backend.zeros((N, N, 3))

    for i in range(N):
        for j in range(i + 1, N):
            r_vec = positions[j] - positions[i]
            r = backend.linalg.norm(r_vec)
            F = compute_force(r, charges[i], charges[j], masses[i], masses[j], use_gpu)

            # Apply force symmetrically
            forces[i, j] = (F / (r + 1e-10)) * r_vec
            forces[j, i] = -forces[i, j]

    return forces

def compute_mass_resistance(delta_P, delta_T):
    """
    Compute mass as resistance to change in momentum over time.

    :param delta_P: Change in momentum
    :param delta_T: Change in time
    :return: Computed mass
    """
    return delta_P / delta_T

def compute_total_energy(positions, charges, masses, use_gpu=False):
    """
    Compute the total energy of the system based on interaction forces.

    :param positions: Nx3 array of partice positions
    :param charges: N-length array of partice charges
    :param masses: N-length array of partice masses
    :param use_gpu: If True, performs computation on GPU
    :return: Total energy of the system
    """
    backend = cp if use_gpu else np
    forces = compute_forces_matrix(positions, charges, masses, use_gpu)
    energy = backend.sum(forces)
    return energy
