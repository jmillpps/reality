import sympy as sp
from sympy import Matrix
import ugft_forms as U

def test_frw_desitter_signatures():
    # quick smoke: FRW-like signatures, not deep identities
    t,x,y,z = U.default_coords()
    a = sp.Function('a')(t)
    g = Matrix.diag(-1, a**2, a**2, a**2)
    Gamma = U.christoffel_symbols(g, (t,x,y,z))
    # Γ^0_{11} = a a', Γ^1_{01} = a'/a (spot checks)
    assert sp.simplify(Gamma[0,1,1] - a*sp.diff(a,t)) == 0
    assert sp.simplify(Gamma[1,0,1] - sp.diff(a,t)/a) == 0

def test_br_projectors_numeric_health():
    g = U.default_metric()
    # Choose a timelike p (p^2 != 0)
    p = Matrix([2, 1, sp.Rational(1,2), -sp.Rational(1,4)])
    P2,P1,P0s,P0w = U.br_projectors_rank2(p, g)
    I = U.br_identity_sym(g)
    # helper
    def close(a,b,eps=1e-10):
        return abs(sp.N(a-b)) < eps
    # completeness on sample entries
    for idx in [(0,0,0,0),(1,1,1,1),(0,1,0,1),(2,2,2,2)]:
        s = P2[idx]+P1[idx]+P0s[idx]+P0w[idx]
        assert close(s, I[idx])
    # orthogonality/idempotency samples
    P2P1 = U.br_compose(P2,P1,g)
    assert all(close(P2P1[i], 0) for i in [ (0,0,0,0), (1,1,1,1) ])
    P2P2 = U.br_compose(P2,P2,g)
    assert all(close(P2P2[i], P2[i]) for i in [ (0,0,0,0), (1,1,1,1) ])

def test_spd_checks():
    from sympy import Matrix
    A = Matrix([[2,0],[0,3]])
    B = Matrix([[1,2],[2,1]])  # leading-minor determinant < 0
    resA = U.is_spd_leading_minors(A)
    assert resA['spd_definite_by_minors'] is True
    resB = U.is_spd_leading_minors(B)
    # conservative symbolic flag (False) because minors not all > 0 numerically
    assert resB['spd_definite_by_minors'] in (False, 0)

def test_wick_rotate_scalar_lagrangian_simple():
    t, tau = sp.symbols('t tau', real=True)
    m = sp.symbols('m', positive=True)
    phi = sp.Function('phi')(t)
    Lm = -sp.Rational(1,2)*sp.diff(phi,t)**2 - sp.Rational(1,2)*m**2*phi**2
    Le = U.wick_rotate_scalar_lagrangian(Lm, t, tau)
    # For the free scalar, time-derivative term flips sign into Euclidean
    assert Le.has(sp.diff(phi, tau)**2)
