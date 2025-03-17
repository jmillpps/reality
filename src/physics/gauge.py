import numpy as np
import cupy as cp  # Use CuPy for GPU acceleration when available

# Define gauge symmetry constants
g_weak = 0.653  # Weak interaction coupling constant
g_strong = 1.22  # Strong interaction coupling constant
g_em = 0.302  # Electromagnetic coupling constant

# SU(3) Gell-Mann matrices for strong force
gell_mann_matrices = [
    np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]]),
    np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
    np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]]),
    np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]]),
    (1 / np.sqrt(3)) * np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]])
]

# SU(2) Pauli matrices for weak force
pauli_matrices = [
    np.array([[0, 1], [1, 0]]),
    np.array([[0, -1j], [1j, 0]]),
    np.array([[1, 0], [0, -1]])
]

# U(1) is an Abelian group, so it's just a phase factor
def u1_transformation(theta):
    """Applies a U(1) phase transformation"""
    return np.exp(1j * theta)


def apply_su2_transformation(vector, theta, use_gpu=False):
    """
    Applies an SU(2) transformation using Pauli matrices.
    
    :param vector: 2D state vector
    :param theta: Rotation angle
    :param use_gpu: Whether to use GPU acceleration
    :return: Transformed vector
    """
    backend = cp if use_gpu else np
    transformation_matrix = backend.cos(theta) * backend.eye(2) - 1j * backend.sin(theta) * pauli_matrices[2]
    return backend.dot(transformation_matrix, vector)


def apply_su3_transformation(vector, theta, generator_index, use_gpu=False):
    """
    Applies an SU(3) transformation using Gell-Mann matrices.
    
    :param vector: 3D state vector
    :param theta: Rotation angle
    :param generator_index: Index of the Gell-Mann matrix to use
    :param use_gpu: Whether to use GPU acceleration
    :return: Transformed vector
    """
    backend = cp if use_gpu else np
    transformation_matrix = backend.cos(theta) * backend.eye(3) - 1j * backend.sin(theta) * gell_mann_matrices[generator_index]
    return backend.dot(transformation_matrix, vector)
