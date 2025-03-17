import numpy as np
import cupy as cp  # GPU acceleration when available

def euler_step(position, velocity, acceleration, dt, use_gpu=False):
    """
    Perform a single Euler integration step with high precision.
    """
    backend = cp if use_gpu else np
    new_velocity = velocity.astype(backend.float64) + acceleration.astype(backend.float64) * dt
    new_position = position.astype(backend.float64) + new_velocity * dt
    return new_position, new_velocity

def verlet_step(position, velocity, acceleration, prev_acceleration, dt, use_gpu=False):
    """
    Perform a single Verlet integration step with high precision.
    """
    backend = cp if use_gpu else np
    new_position = position.astype(backend.float64) + velocity.astype(backend.float64) * dt + 0.5 * acceleration.astype(backend.float64) * dt**2
    avg_acceleration = 0.5 * (acceleration + prev_acceleration)
    new_velocity = velocity.astype(backend.float64) + avg_acceleration.astype(backend.float64) * dt
    return new_position, new_velocity

def rk4_step(position, velocity, acceleration_func, dt, use_gpu=False):
    """
    Perform a single RK4 integration step with high precision.
    """
    backend = cp if use_gpu else np

    k1_v = acceleration_func(position).astype(backend.float64) * dt
    k1_x = velocity.astype(backend.float64) * dt

    k2_v = acceleration_func(position + 0.5 * k1_x).astype(backend.float64) * dt
    k2_x = (velocity + 0.5 * k1_v).astype(backend.float64) * dt

    k3_v = acceleration_func(position + 0.5 * k2_x).astype(backend.float64) * dt
    k3_x = (velocity + 0.5 * k2_v).astype(backend.float64) * dt

    k4_v = acceleration_func(position + k3_x).astype(backend.float64) * dt
    k4_x = (velocity + k3_v).astype(backend.float64) * dt

    new_velocity = velocity.astype(backend.float64) + (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6
    new_position = position.astype(backend.float64) + (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6

    return new_position, new_velocity
