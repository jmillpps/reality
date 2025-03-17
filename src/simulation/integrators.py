import numpy as np
import cupy as cp  # GPU acceleration when available


def euler_step(position, velocity, acceleration, dt, use_gpu=False):
    """
    Perform a single Euler integration step.
    
    :param position: Current position array
    :param velocity: Current velocity array
    :param acceleration: Current acceleration array
    :param dt: Time step size
    :param use_gpu: If True, uses GPU acceleration
    :return: Updated position and velocity
    """
    backend = cp if use_gpu else np
    new_velocity = velocity + acceleration * dt
    new_position = position + new_velocity * dt
    return new_position, new_velocity


def verlet_step(position, velocity, acceleration, prev_acceleration, dt, use_gpu=False):
    """
    Perform a single Verlet integration step.
    
    :param position: Current position array
    :param velocity: Current velocity array
    :param acceleration: Current acceleration array
    :param prev_acceleration: Previous step acceleration array
    :param dt: Time step size
    :param use_gpu: If True, uses GPU acceleration
    :return: Updated position and velocity
    """
    backend = cp if use_gpu else np
    new_position = position + velocity * dt + 0.5 * acceleration * dt**2
    avg_acceleration = 0.5 * (acceleration + prev_acceleration)
    new_velocity = velocity + avg_acceleration * dt
    return new_position, new_velocity


def rk4_step(position, velocity, acceleration_func, dt, use_gpu=False):
    """
    Perform a single Runge-Kutta 4 (RK4) integration step.
    
    :param position: Current position array
    :param velocity: Current velocity array
    :param acceleration_func: Function to compute acceleration
    :param dt: Time step size
    :param use_gpu: If True, uses GPU acceleration
    :return: Updated position and velocity
    """
    backend = cp if use_gpu else np
    
    k1_v = acceleration_func(position) * dt
    k1_x = velocity * dt
    
    k2_v = acceleration_func(position + 0.5 * k1_x) * dt
    k2_x = (velocity + 0.5 * k1_v) * dt
    
    k3_v = acceleration_func(position + 0.5 * k2_x) * dt
    k3_x = (velocity + 0.5 * k2_v) * dt
    
    k4_v = acceleration_func(position + k3_x) * dt
    k4_x = (velocity + k3_v) * dt
    
    new_velocity = velocity + (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6
    new_position = position + (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6
    
    return new_position, new_velocity
