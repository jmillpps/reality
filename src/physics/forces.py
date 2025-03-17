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
    Compute gravitational and electromagnetic forces between particles.
    """
    num_particles = len(positions)
    forces = np.zeros((num_particles, num_particles, 3))

    for i in range(num_particles):
        for j in range(i + 1, num_particles):
            r_vec = positions[j] - positions[i]
            r_mag = np.linalg.norm(r_vec) + 1e-10  # Avoid division by zero
            r_hat = r_vec / r_mag

            # Gravity
            G_force = (6.67430e-11 * masses[i] * masses[j]) / (r_mag ** 2)
            forces[i, j] += G_force * r_hat
            forces[j, i] -= G_force * r_hat

            # Electromagnetism (Coulomb force)
            if charges[i] * charges[j] != 0:
                k_e = 8.987551787e9  # Coulomb's constant
                E_force = (k_e * charges[i] * charges[j]) / (r_mag ** 2)
                forces[i, j] += E_force * r_hat
                forces[j, i] -= E_force * r_hat

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
