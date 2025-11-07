
import sympy as sp
from sympy import Matrix, I
import ugft_forms as U

# ---------- Forms & Hodge edge tests ----------
def test_wedge_associativity_and_nilpotent():
    g = U.default_metric()
    t,x,y,z = U.default_coords()
    dt = U.UGFTForm(1, {(0,): 1}, g, (t,x,y,z))
    dx = U.UGFTForm(1, {(1,): 1}, g, (t,x,y,z))
    dy = U.UGFTForm(1, {(2,): 1}, g, (t,x,y,z))
    lhs = (dt ^ dx) ^ dy
    rhs = dt ^ (dx ^ dy)
    assert lhs.degree == 3 and rhs.degree == 3 and lhs.comps == rhs.comps
    # α ∧ α = 0
    zero = dx ^ dx
    assert zero.comps == {}

def test_hodge_involution_on_1_form():
    g = U.default_metric()
    t,x,y,z = U.default_coords()
    dt = U.UGFTForm(1, {(0,): 1}, g, (t,x,y,z))
    star2 = dt.star().star()
    # In 4D Lorentzian: *^2 acts as +1 on 1-forms (p(D-p)+s even with s=1)
    assert star2.degree == 1 and sp.simplify(star2.comps[(0,)] - 1) == 0 and len(star2.comps)==1

def test_d_top_form_zero_and_d_of_constant_one_form_zero():
    g = U.default_metric()
    t,x,y,z = U.default_coords()
    dt = U.UGFTForm(1, {(0,): 1}, g, (t,x,y,z))
    assert U.UGFTForm(4, {(0,1,2,3): 1}, g, (t,x,y,z)).d().comps == {}
    assert dt.d().comps == {}

# ---------- Wick & Boundary / ADM edge tests ----------
def test_wick_helpers_and_boundary():
    g = U.default_metric('lorentzian')
    t,x,y,z = U.default_coords()
    dt = U.UGFTForm(1, {(0,): sp.Symbol('dt')}, g, (t,x,y,z))
    dtau = U.wick_time_map_dt_to_tau(dt)
    assert sp.simplify(dtau.comps[(0,)] + I*sp.Symbol('dt')) == 0
    ge = U.wick_metric_to_euclidean(g)
    assert ge[0,0] == 1 and ge[1,1] == 1
    L4 = U.UGFTForm(4, {(0,1,2,3): sp.Symbol('L')}, g, (t,x,y,z))
    L4E = U.wick_action_4form_to_euclidean(L4)
    assert sp.simplify(L4E.comps[(0,1,2,3)] + I*sp.Symbol('L')) == 0
    gamma = Matrix.diag(2,3,5)
    assert sp.simplify(U.ghy_boundary_density(7, gamma) - 7*sp.sqrt(2*3*5)) == 0

def test_adm_generic_shift_and_lapse():
    # Build metric from given N, N_i, gamma_ij and ensure adm_split recovers them.
    N = sp.Symbol('N', positive=True)
    u,v,w = sp.symbols('u v w', real=True)
    a,b,c = sp.symbols('a b c', positive=True)
    gamma = Matrix.diag(a, b, c)
    g00 = -(N**2) + (u**2/a + v**2/b + w**2/c)
    g0i = Matrix([u, v, w])
    g = Matrix([[g00, u, v, w],
                [u,   a, 0, 0],
                [v,   0, b, 0],
                [w,   0, 0, c]])
    N_out, Ni_out, gamma_out = U.adm_split(g)
    assert sp.simplify(N_out - N) == 0
    assert tuple(sp.simplify(x) for x in Ni_out) == (u, v, w)
    assert sp.simplify(gamma_out.det() - gamma.det()) == 0

# ---------- Fourier & Kubo edge tests ----------
def test_kubo_dc_linear_imag():
    w = sp.symbols('w', real=True)
    sigma = sp.symbols('sigma', real=True, positive=True)
    GR = I*sigma*w
    assert sp.simplify(U.kubo_sigma_dc(GR, w) - sigma) == 0

def test_kubo_curved_measure():
    g = U.default_metric()
    w = sp.symbols('w', real=True)
    sigma = sp.symbols('sigma', real=True)
    GR = I*sigma*w
    meas = U.measure_volume_density(g)
    out = U.kubo_sigma_dc_curved(GR, w, meas)
    assert sp.simplify(out - meas*sigma) == 0

# ---------- Projectors & BR ----------
def test_barnes_rivers_completeness_and_idempotency_samples():
    m = sp.symbols('m', positive=True)
    p = Matrix([m,0,0,0])
    rep = U.br_check_identities(p, U.default_metric())
    assert rep['completeness_ok']
    assert rep['orthogonality_sample_ok']
    assert rep['idempotency_sample_ok']

def test_brst_abelian_limit():
    t,x,y,z = U.default_coords()
    A0 = Matrix([sp.Function('A0')(t),0,0,0])
    c  = sp.Function('c')(t)
    out = U.brst_variations_nonabelian([A0],[c], [[[0]]], (t,x,y,z))
    sA0 = out['sA'][0]
    assert sp.simplify(sA0[0] - sp.diff(c, t)) == 0 and all(sp.simplify(sA0[i])==0 for i in [1,2,3])
    assert sp.simplify(out['sc'][0]) == 0

# ---------- GR tensors: FRW sanity check ----------
def test_frw_ricci_scalar():
    # Spatially flat FRW: ds^2 = -dt^2 + a(t)^2 (dx^2+dy^2+dz^2)
    t = sp.symbols('t', real=True)
    a = sp.Function('a')(t)
    g = Matrix.diag(-1, a**2, a**2, a**2)
    coords = (t, sp.Symbol('x', real=True), sp.Symbol('y', real=True), sp.Symbol('z', real=True))
    R = U.ricci_scalar(g, coords)
    # Known result: R = 6( a''/a + (a')^2/a^2 )
    ap = sp.diff(a,t); app = sp.diff(a,t,2)
    R_expected = 6*(app/a + (ap/a)**2)
    assert sp.simplify(sp.together(R - R_expected)) == 0

# ---------- Geometry (metric-compatibility & torsion) ----------
def test_nonmetricity_zero_for_levi_civita():
    t,x,y,z = U.default_coords()
    a = sp.Function('a')(t)
    g = Matrix.diag(-1, a**2, a**2, a**2)
    Gamma = U.christoffel_symbols(g, (t,x,y,z))
    Q = U.nonmetricity_Q(g, Gamma)
    assert all(sp.simplify(Q[a_,m,n])==0 for a_ in range(4) for m in range(4) for n in range(4))

def test_contorsion_from_simple_torsion():
    T = sp.MutableDenseNDimArray.zeros(4,4,4)
    tau = sp.symbols('tau', real=True)
    T[0,1,2] = tau
    K = U.contorsion_from_torsion(T)
    # K_{0,1,2} = 1/2( T_{0,1,2} - T_{1,2,0} + T_{2,0,1} ) = 1/2 * tau
    assert sp.simplify(K[0,1,2] - tau/2) == 0

# ---------- YM/Maxwell builders ----------
def test_abelian_field_strength_basic_symmetry():
    t,x,y,z = U.default_coords()
    A = Matrix([0,0,x,0])
    F = U.abelian_field_strength(A, (t,x,y,z))
    assert sp.simplify(F[1,2]-1) == 0 and sp.simplify(F[2,1]+1) == 0

def test_ym_field_strength_abelian_reduction():
    # two colors with zero structure constants => reduce to abelian per color
    t,x,y,z = U.default_coords()
    A1 = Matrix([0,0,x,0])
    A2 = Matrix([0,0,0,0])
    zeros = [[[0,0],[0,0]], [[0,0],[0,0]]]
    Fs = U.ym_field_strength([A1,A2], zeros, (t,x,y,z))
    assert sp.simplify(Fs[0][1,2]-1) == 0 and sp.simplify(Fs[0][2,1]+1) == 0
    assert all(sp.simplify(Fs[1][i,j])==0 for i in range(4) for j in range(4))

# ---------- Mass dimensions & epsilon ----------
def test_mass_dimensions_and_epsilon_identity():
    assert U.mass_dimension_field('scalar',4) == 1
    assert U.mass_dimension_field('vector',4) == 1
    assert U.mass_dimension_field('spinor',4) == sp.Rational(3,2)
    assert U.mass_dimension_field('fieldstrength',4) == 2
    assert U.mass_dimension_field('metric',4) == 0
    assert U.mass_dimension_field('gauge_coupling',4) == 0
    assert U.mass_dimension_field('newtonG',4) == -2
    mu, alpha = sp.symbols('mu alpha')
    assert U.epsilon_contraction_test() == -sp.factorial(3)*sp.KroneckerDelta(mu, alpha)

if __name__ == "__main__":
    fails = []
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                print(f"--> {name}")
                fn()
                print(f"<-- {name} OK")
            except Exception as e:
                import traceback
                print(f"XX  {name} FAIL: {e}")
                traceback.print_exc()
                fails.append((name, e))
    if fails:
        print(f"FAILED: {len(fails)} tests")
        raise SystemExit(1)
    print("ALL CH0 EDGE TESTS PASSED")
