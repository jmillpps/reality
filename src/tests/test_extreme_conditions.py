import pytest
import numpy as np
from physics.relativity import lorentz_factor, time_dilation
from physics.gravity import compute_gravitational_force, compute_space_time_warping
from physics.quantum import compute_wavefunction


def test_lorentz_factor_extreme():
    """Test Lorentz factor near the speed of light."""
    velocity = np.array([0.99, 0.999, 0.9999]) * 299792458  # 99% to 99.99% of c
    gamma = lorentz_factor(velocity, use_gpu=False)
    assert np.all(gamma > 1), "Lorentz factor should be greater than 1."
    assert np.all(gamma < 1000), "Lorentz factor should not diverge uncontrollably."


def test_time_dilation_extreme():
    """Test extreme time dilation cases."""
    proper_time = 1.0
    velocity = 0.9999 * 299792458  # 99.99% of speed of light
    dilated_time = time_dilation(proper_time, velocity, use_gpu=False)
    assert dilated_time > 10, "Time dilation should be significant at extreme velocities."


def test_gravitational_force_extreme():
    """Test gravitational force at extreme masses and distances."""
    force = compute_gravitational_force(1e30, 1e30, 1e3, use_gpu=False)  # Two massive bodies 1000m apart
    assert force > 1e20, "Gravitational force should be enormous at high masses."


def test_space_time_warping_extreme():
    """Test space-time warping in the presence of a black hole-like mass."""
    warp_factor = compute_space_time_warping(1e30, 100, use_gpu=False)  # Very large mass at 100m
    assert warp_factor < 0.1, "Space-time should be extremely warped near a massive object."


def test_wavefunction_extreme_momentum():
    """Test quantum wavefunction behavior at high momentum."""
    position = np.random.uniform(-1, 1, (10, 3))
    momentum = np.ones((10, 3)) * 1e10  # Extremely high momentum values
    wavefunction = compute_wavefunction(position, momentum, use_gpu=False)
    assert wavefunction.shape == (10,), "Wavefunction shape incorrect for high momentum."


if __name__ == "__main__":
    pytest.main(["-v"])
