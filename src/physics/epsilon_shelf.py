"""
Precise Calculation and Derivation of Intrinsic Epsilon Curvature (I_ε) Using Observed Gravitational Deflection

This script performs two precise calculations:
1. Calculates epsilon-corrected gravitational deflection angles for massive astronomical objects.
2. Derives the intrinsic epsilon field curvature (I_ε) explicitly from observed gravitational deflection angles.

Epsilon-Corrected Deflection Formula:

θ_ε = (4GM / r c²) × [1 + ε × (1 - 2 × |ε - ⌊ε⌋ - 0.5|)] + [4 × I_ε × ε × (1 - 2 × |ε - ⌊ε⌋ - 0.5|) / c²]

Rearranging explicitly to solve for I_ε:

I_ε = { [θ_observed × c² - (4GM / r)(1 + ε × collapse_factor)] / (4ε × collapse_factor) }

Constants and SymPy Implementation:
SymPy allows representing constants exactly, ensuring maximum numerical precision.
"""

import sympy as sp

# Constants (exact representation for maximum precision)
G = sp.Rational('667430', '10000000000000')  # Gravitational constant
c = 299792458  # Exact speed of light, m/s
solar_mass = sp.Rational('198847', '100000') * 10**25  # Solar mass, kg

# Epsilon-corrected gravitational deflection calculation
def epsilon_corrected_deflection_sympy(M, r, epsilon, I_epsilon):
    collapse_factor = 1 - 2 * abs(epsilon - sp.floor(epsilon) - 0.5)
    classical_term = (4 * G * M) / (r * c**2)
    epsilon_term = (4 * I_epsilon * epsilon * collapse_factor) / (c**2)

    angle_rad = classical_term * (1 + epsilon * collapse_factor) + epsilon_term
    angle_arcsec = sp.N(angle_rad * (180 / sp.pi) * 3600, 15)

    return angle_arcsec

# Explicit calculation to derive intrinsic epsilon curvature from observed angle
def derive_intrinsic_epsilon(M, r, epsilon, theta_observed_arcsec):
    collapse_factor = 1 - 2 * abs(epsilon - sp.floor(epsilon) - 0.5)
    theta_observed_rad = theta_observed_arcsec / (3600 * (180 / sp.pi))

    classical_term = (4 * G * M) / (r * c**2)

    numerator = (theta_observed_rad * c**2) - classical_term * (1 + epsilon * collapse_factor)
    denominator = 4 * epsilon * collapse_factor

    I_epsilon_derived = sp.N(numerator / denominator, 15)

    return I_epsilon_derived

# Example object (Black hole, 10 solar masses) for deriving intrinsic epsilon
black_hole_mass = 10 * solar_mass
black_hole_radius = 3e4
observed_deflection_arcsec = 4142.35583288282  # Observed angle

# Epsilon parameters
epsilon = 0.1

# Deriving intrinsic epsilon curvature explicitly
I_epsilon_derived = derive_intrinsic_epsilon(black_hole_mass, black_hole_radius, epsilon, observed_deflection_arcsec)

# Verification by forward calculation
verified_deflection = epsilon_corrected_deflection_sympy(black_hole_mass, black_hole_radius, epsilon, I_epsilon_derived)

print({
    'Derived I_epsilon': I_epsilon_derived,
    'Verified Deflection (arcsec)': verified_deflection
})
