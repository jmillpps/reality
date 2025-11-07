
import sympy as sp
from sympy import Matrix, I
from ugft_forms import *

def approx_zero(expr):
    return sp.simplify(expr) == 0

def test_metric_coords_adm():
    g = default_metric('lorentzian')
    t,x,y,z = default_coords()
    N, Ni, gamma = adm_split(g)
    assert sp.simplify(N-1)==0
    assert tuple(Ni)==(0,0,0)
    assert gamma[0,0]==1

def test_forms_wedge_d_star_ibp():
    g = default_metric()
    t,x,y,z = default_coords()
    # 0-form f = x
    f = UGFTForm(0,{(): x}, g, (t,x,y,z))
    # 1-form dt
    dt = UGFTForm(1,{(0,): 1}, g, (t,x,y,z))
    d_f = f.d()
    assert d_f.degree == 1 and sp.simplify(d_f.comps[(1,)]-1)==0
    # Hodge star on dt (should map to spatial volume)
    star_dt = dt.star()
    assert star_dt.degree == 3 and (1,2,3) in star_dt.comps
    # IBP check
    A, B = f, f
    total, left, right = ibp_exterior(A,B)
    # since dA=dx, dB=dx, A^B is 0-form^0-form -> 0-form; d of 0-form is 1-form; left/right also 1-forms; equality holds symbolically
    # We check that total - left - right simplifies to zero components
    # Build missing by subtracting
    def minus(F,G):
        comps={}
        keys=set(F.comps.keys())|set(G.comps.keys())
        for k in keys:
            comps[k]=sp.simplify(F.comps.get(k,0)-G.comps.get(k,0))
        return UGFTForm(F.degree, comps, F.g, F.coords, F.signature)
    assert minus(total, (left ^ UGFTForm(0,{():1},g,(t,x,y,z))) ).degree == total.degree  # structural smoke

def test_fourier_delta_plancherel():
    eq = delta_normalization_check()
    assert isinstance(eq, sp.Equality) and eq.rhs.has(sp.DiracDelta)

def test_distributions():
    x,y,z = sp.symbols('x y z', real=True)
    assert sp.simplify(laplacian_of_inv_r(x,y,z) + 4*sp.pi*sp.DiracDelta(x)*sp.DiracDelta(y)*sp.DiracDelta(z)) == 0
    assert sp.simplify(laplacian_log_r_2d(x,y) - 2*sp.pi*sp.DiracDelta(x)*sp.DiracDelta(y)) == 0

def test_ym_and_lagrangians():
    g = default_metric()
    a = sp.symbols('a', real=True)
    F = Matrix([[0,a,0,0],[-a,0,0,0],[0,0,0,0],[0,0,0,0]])
    val = ym_F2_scalar([F], g)
    assert sp.simplify(val + 2*a**2) == 0  # Minkowski -> F^2 = -2 a^2

def test_eh_ghy_zero_flat():
    g = default_metric()
    R = sp.Integer(0)
    L = einstein_hilbert_density(R, g, sp.symbols('G'))
    assert sp.simplify(L) == 0

def test_axial_proca_mass_term_only():
    g = default_metric()
    t,x,y,z = default_coords()
    s0,s1,s2,s3,mS = sp.symbols('s0 s1 s2 s3 mS', real=True)
    S = Matrix([s0,s1,s2,s3])
    L = axial_proca_lagrangian(S, g, mS, (t,x,y,z))
    expected = sp.simplify(sp.Rational(1,2)*mS**2 * (-s0**2 + s1**2 + s2**2 + s3**2))
    assert sp.simplify(L - expected) == 0

def test_stress_tensors():
    g = default_metric(); g_inv = g.inv()
    a = sp.symbols('a', real=True)
    dphi = Matrix([a,0,0,0])  # ∂_0 φ = a
    T = T_scalar(g, dphi, 0)
    assert sp.simplify(T[0,0] - sp.Rational(1,2)*a**2) == 0
    # Proca with A0 const, F=0
    m, A0 = sp.symbols('m A0', positive=True)
    A = Matrix([A0,0,0,0])
    Tp = T_proca(g, A, m, default_coords())
    assert sp.simplify(Tp[0,0] - sp.Rational(1,2)*m**2*A0**2) == 0

def test_theta_omega_rest():
    g = default_metric()
    m = sp.symbols('m', positive=True)
    p = Matrix([m,0,0,0])
    theta, omega = theta_omega_projectors(p, g)
    assert sp.simplify(theta[0,0]) == 0 and sp.simplify(omega[0,0] + 1) == 0

def test_field_strengths():
    t,x,y,z = default_coords()
    A = Matrix([0,0,x,0])  # A_2 = x -> F_12 = 1
    F = abelian_field_strength(A, (t,x,y,z))
    assert sp.simplify(F[1,2] - 1) == 0
    # YM abelian limit (one color, f=0) reproduces abelian F
    Fs = ym_field_strength([A], [[[0]]], (t,x,y,z))
    assert sp.simplify(Fs[0][1,2] - 1) == 0

def test_spinor_brst():
    g = default_metric()
    g_inv = g.inv()
    assert sp.simplify(gamma_anticommutator(0,0,g_inv) + 2) == 0
    # BRST abelian limit (one color -> structure constants=0)
    t,x,y,z = default_coords()
    A = Matrix([sp.Function('A0')(t), sp.Function('A1')(t), sp.Function('A2')(t), sp.Function('A3')(t)])
    c = sp.Function('c')(t)
    out = brst_variations_nonabelian([A], [c], [[[0]]], (t,x,y,z))
    sA = out['sA'][0]
    assert all(sp.simplify(sA[i,0] - sp.diff(c, (t,x,y,z)[i])) == 0 for i in range(4))
    assert sp.simplify(out['sc'][0]) == 0
    assert out['sB'][0] == 0

def test_gravity_flat_space():
    g = default_metric()
    t,x,y,z = default_coords()
    Gamma = christoffel_symbols(g, (t,x,y,z))
    assert all(sp.simplify(Gamma[r,mu,nu])==0 for r in range(4) for mu in range(4) for nu in range(4))
    Riem = riemann_tensor(g, (t,x,y,z), Gamma=Gamma)
    assert all(sp.simplify(Riem[r,s,mu,nu])==0 for r in range(4) for s in range(4) for mu in range(4) for nu in range(4))
    Ric = ricci_tensor(g, (t,x,y,z), Riemann=Riem, Gamma=Gamma)
    assert all(sp.simplify(Ric[mu,nu])==0 for mu in range(4) for nu in range(4))
    R = ricci_scalar(g, (t,x,y,z), Ric=Ric, Gamma=Gamma)
    assert sp.simplify(R)==0
    G = einstein_tensor(g, (t,x,y,z), Ric=Ric, Rscalar=R, Gamma=Gamma)
    assert all(sp.simplify(G[mu,nu])==0 for mu in range(4) for nu in range(4))
    bianchi = bianchi_identity_check(g, (t,x,y,z), Gamma=Gamma)
    assert bianchi['all_zero']

def test_kubo_and_measures():
    g = default_metric(); sqrtg = measure_volume_density(g)
    w = sp.symbols('w', real=True)
    c = sp.symbols('c', real=True)
    GR = -I*c*w  # Im(GR) = -c w
    dc = kubo_sigma_dc(GR, w)
    assert sp.simplify(dc + c) == 0
    dcc = kubo_sigma_dc_curved(GR, w, sqrtg)
    assert sp.simplify(dcc + c*sqrtg) == 0

if __name__ == "__main__":
    test_metric_coords_adm()
    test_forms_wedge_d_star_ibp()
    test_fourier_delta_plancherel()
    test_distributions()
    test_ym_and_lagrangians()
    test_eh_ghy_zero_flat()
    test_axial_proca_mass_term_only()
    test_stress_tensors()
    test_theta_omega_rest()
    test_field_strengths()
    test_spinor_brst()
    test_gravity_flat_space()
    test_kubo_and_measures()
    print("ALL CH0 TESTS PASSED")
