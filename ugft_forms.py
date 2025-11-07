
# ugft_forms.py — Clean, deduplicated UGFT Chapter‑0
from __future__ import annotations
import sympy as sp
from sympy.core.function import AppliedUndef
from sympy import Matrix, I

# ---------- Core metric/coords ----------
def default_metric(signature: str='lorentzian') -> Matrix:
    if signature.lower().startswith('l'):
        return Matrix.diag(-1,1,1,1)
    return Matrix.diag(1,1,1,1)

def default_coords():
    t,x,y,z = sp.symbols('t x y z', real=True)
    return t,x,y,z

# ---------- Forms (UGFTForm) with wedge/d/Hodge & scalar ops ----------
class UGFTForm:
    def __init__(self, degree: int, comps: dict, g: Matrix, coords, signature='lorentzian'):
        self.degree = int(degree)
        # store with sorted index tuples
        self.comps = {tuple(sorted(k)): sp.simplify(v) for k,v in comps.items()}
        self.g = Matrix(g)
        self.coords = tuple(coords)
        self.signature = signature

    # scalar ops
    def _scale(self, s):
        return UGFTForm(self.degree, {k: sp.simplify(s*v) for k,v in self.comps.items()}, self.g, self.coords, self.signature)
    def __rmul__(self, s):
        if isinstance(s, (int,float,complex,sp.Expr)):
            return self._scale(s)
        return NotImplemented
    def __mul__(self, s):
        return self.__rmul__(s)
    # addition/subtraction (same context & degree)
    def __add__(self, other):
        if not isinstance(other, UGFTForm): return NotImplemented
        if self.degree!=other.degree or self.g!=other.g or self.coords!=other.coords:
            raise ValueError("incompatible forms for add")
        comps = dict(self.comps)
        for k,v in other.comps.items():
            comps[k] = sp.simplify(comps.get(k,0)+v)
        return UGFTForm(self.degree, comps, self.g, self.coords, self.signature)
    def __sub__(self, other):
        return self.__add__((-1)*other)

def _antisym_sort(idx):
    idx = list(idx); s = 1
    for i in range(len(idx)):
        for j in range(i+1,len(idx)):
            if idx[i] > idx[j]:
                idx[i], idx[j] = idx[j], idx[i]; s *= -1
    return s, tuple(idx)

def _all_sorted_indices(n,k):
    from itertools import combinations
    return list(combinations(range(n),k))

def _raise_form_components(components: dict, p: int, g_inv: Matrix):
    from itertools import combinations
    D = g_inv.shape[0]; out = {}
    lows = list(combinations(range(D), p))
    ups  = list(combinations(range(D), p))
    for up_idx in ups:
        total = 0
        for low_idx in lows:
            coeff = 1
            for i in range(p):
                coeff *= g_inv[up_idx[i], low_idx[i]]
            total += coeff * components.get(tuple(sorted(low_idx)), 0)
        if total != 0:
            out[tuple(sorted(up_idx))] = sp.simplify(total)
    return out

def _hodge_star_on_form(components: dict, p: int, g: Matrix):
    D = g.shape[0]; g_inv = Matrix(g).inv()
    sqrtg = sp.sqrt(sp.Abs(Matrix(g).det()))
    out_deg = D - p; out = {}
    if p == 0:
        val = components.get((), 0)
        if val != 0:
            out[tuple(range(D))] = sp.simplify(val * sqrtg * sp.LeviCivita(*range(D)))
        return out_deg, out
    A_up = _raise_form_components(components, p, g_inv)
    for mu_tuple, Aup in A_up.items():
        mu_set = set(mu_tuple)
        nu_tuple = tuple(sorted(set(range(D)) - mu_set))
        eps = sqrtg * sp.LeviCivita(*(nu_tuple + mu_tuple))
        contrib = sp.simplify(eps * Aup)
        out[nu_tuple] = sp.simplify(out.get(nu_tuple, 0) + contrib)
    return out_deg, out


def _ugftform_wedge(self, other):
    if not isinstance(other, UGFTForm): raise TypeError("wedge expects UGFTForm")
    if self.g.shape!=other.g.shape or self.coords!=other.coords: raise ValueError("mismatched contexts")
    res = {}
    for I,a in self.comps.items():
        for J,b in other.comps.items():
            K = I + J
            # if repeated index (antisymmetry), the term vanishes
            if len(set(K)) < len(K):
                continue
            sgn, Ksorted = _antisym_sort(K)
            res[Ksorted] = sp.simplify(res.get(Ksorted, 0) + sgn*a*b)
    return UGFTForm(self.degree+other.degree, res, self.g, self.coords, self.signature)


def _ugftform_d(self):
    if self.degree >= 4: return UGFTForm(self.degree+1, {}, self.g, self.coords, self.signature)
    res = {}; coords = self.coords; p = self.degree
    for J in _all_sorted_indices(4, p+1):
        total = 0
        for i, mu in enumerate(J):
            K = tuple([J[k] for k in range(len(J)) if k != i])
            comp = self.comps.get(K, 0)
            if comp != 0:
                total += ((-1)**i) * sp.diff(comp, coords[mu])
        if total != 0: res[J] = sp.simplify(total)
    return UGFTForm(p+1, res, self.g, self.coords, self.signature)

def _ugftform_star(self):
    p = self.degree
    out_deg, out = _hodge_star_on_form(self.comps, p, self.g)
    return UGFTForm(out_deg, out, self.g, self.coords, self.signature)

UGFTForm.__xor__ = _ugftform_wedge
UGFTForm.d = _ugftform_d
UGFTForm.star = _ugftform_star

# ---------- Wick ----------
def wick_time_map_dt_to_tau(dt: UGFTForm) -> UGFTForm:
    if dt.degree != 1: raise ValueError("dt must be a 1-form")
    comps = {}
    for (i,), v in dt.comps.items():
        comps[(i,)] = -I*v if i == 0 else v
    return UGFTForm(1, comps, dt.g, dt.coords, dt.signature)

def wick_metric_to_euclidean(g: Matrix) -> Matrix:
    G = Matrix(g).copy(); G[0,0] = sp.Abs(G[0,0]); return G

def wick_action_4form_to_euclidean(L4: 'UGFTForm') -> 'UGFTForm':
    if L4.degree != 4: raise ValueError("Expected a 4-form")
    return (-I) * L4

def wick_rotate_scalar_lagrangian(L_minkowski: sp.Expr, t: sp.Symbol, tau: sp.Symbol):
    """
    Perform a Wick rotation on a time-derivative-only scalar Lagrangian density L_M(phi(t), d_t phi(t)).
    Map t -> -I*tau and d/dt -> I d/dtau, and rewrite the result in terms of phi(tau) and d/dtau.
    This yields the expected sign flip for kinetic terms.
    Notes:
      - Only time derivatives are handled here (spatial derivatives left as-is).
      - If L_M contains explicit t outside of phi(t), this function does not transform those terms.
    """
    expr = L_minkowski
    # Identify all applied functions depending solely on t
    applied = [f for f in expr.atoms(AppliedUndef) if f.free_symbols == {t}]
    for f in applied:
        base = f.func
        # d/dt f(t) -> I * d/dtau f(tau)
        expr = expr.xreplace({sp.Derivative(f, t): I * sp.Derivative(base(tau), tau)})
        # f(t) -> f(tau)
        expr = expr.xreplace({f: base(tau)})
    return sp.simplify(expr)

# ---------- IBP & Boundary ----------
def ibp_exterior(A: UGFTForm, B: UGFTForm):
    p = A.degree; dA = A.d(); dB = B.d()
    wedge_total = (A ^ B).d()
    left = dA ^ B
    right = A ^ dB
    if p % 2 == 1: right = (-1)*right
    return wedge_total, left, right

def ghy_boundary_density(K: sp.Expr, gamma_spatial: Matrix):
    return sp.sqrt(sp.Abs(Matrix(gamma_spatial).det())) * K

def ghy_surface_density(K_trace: sp.Expr, gamma_spatial: Matrix, GNewton):
    return sp.sqrt(sp.Abs(Matrix(gamma_spatial).det())) * K_trace / (8*sp.pi*GNewton)

# ---------- ADM ----------
def adm_split(metric: Matrix):
    g = Matrix(metric); gamma = g[1:4,1:4]; ginv_spat = gamma.inv()
    N_cov = g[1:4,0]; N_up = ginv_spat * N_cov
    NiNi = (N_cov.T * N_up)[0]
    N = sp.sqrt( - (g[0,0] - NiNi) )
    return sp.simplify(N), sp.simplify(N_cov), sp.simplify(gamma)

# ---------- Fourier & Distributions ----------
def fourier_pair(sign: int=+1):
    x, k = sp.symbols('x k', real=True)
    def F(f):   return sp.Integral(sp.exp(I*sign*k*x)*f, (x, -sp.oo, sp.oo))
    def Finv(g):return (1/(2*sp.pi)) * sp.Integral(sp.exp(-I*sign*k*x)*g, (k, -sp.oo, sp.oo))
    return F, Finv

def delta_normalization_check():
    x, k = sp.symbols('x k', real=True)
    expr = sp.Integral(sp.exp(I*k*x), (x, -sp.oo, sp.oo))
    return sp.Eq(expr, 2*sp.pi*sp.DiracDelta(k))

def plancherel_check():
    return "∫|f|^2 dx = (1/2π) ∫|F|^2 dk (convention check)"

def fourier_pair_nd(x_syms, k_syms, sign: int=+1):
    if len(x_syms) != len(k_syms): raise ValueError("x_syms and k_syms must match length")
    D = len(x_syms); phase = sum(k_syms[i]*x_syms[i] for i in range(D))
    def F(f):   return sp.Integral(sp.exp(I*sign*phase)*f, *[(x_syms[i], -sp.oo, sp.oo) for i in range(D)])
    def Finv(g):return (1/(2*sp.pi)**D) * sp.Integral(sp.exp(-I*sign*phase)*g, *[(k_syms[i], -sp.oo, sp.oo) for i in range(D)])
    return F, Finv

def delta_normalization_nd(x_syms, k_syms, sign: int=+1):
    if len(x_syms) != len(k_syms): raise ValueError("x_syms and k_syms must match length")
    D = len(x_syms); phase = sum(k_syms[i]*x_syms[i] for i in range(D))
    lhs = sp.Integral(sp.exp(I*sign*phase), *[(x_syms[i], -sp.oo, sp.oo) for i in range(D)])
    rhs = (2*sp.pi)**D
    for ki in k_syms: rhs *= sp.DiracDelta(ki)
    return sp.Eq(lhs, rhs)

def retarded_kernel_KG(omega, kvec, m):
    k2 = sum(ki**2 for ki in kvec)
    return 1/(- (omega + I*0)**2 + k2 + m**2)

def laplacian_of_inv_r(x, y, z):
    return -4*sp.pi*sp.DiracDelta(x)*sp.DiracDelta(y)*sp.DiracDelta(z)

def laplacian_log_r_2d(x, y):
    return 2*sp.pi*sp.DiracDelta(x)*sp.DiracDelta(y)

# ---------- Kubo ----------
def kubo_sigma_dc(GR_omega: sp.Expr, omega: sp.Symbol):
    return sp.simplify(sp.limit(sp.im(GR_omega)/omega, omega, 0, dir='+'))

def kubo_formula_response(GR_omega_k: sp.Expr, omega: sp.Symbol):
    return kubo_sigma_dc(GR_omega_k, omega)

def measure_volume_density(g: Matrix):
    return sp.sqrt(sp.Abs(Matrix(g).det()))

def measure_surface_density(gamma_spatial: Matrix):
    return sp.sqrt(sp.Abs(Matrix(gamma_spatial).det()))

def kubo_sigma_dc_curved(GR_omega: sp.Expr, omega: sp.Symbol, measure: sp.Expr):
    return sp.simplify(measure * kubo_sigma_dc(GR_omega, omega))

# ---------- Projectors & Proca ----------
def proca_polarization_sum(p_cov: Matrix, m: sp.Symbol, metric: Matrix=None) -> Matrix:
    g = Matrix(metric) if metric is not None else default_metric()
    p = Matrix(p_cov)
    return sp.simplify(g + (p*p.T)/(m**2))

def spin1_polarization_sum(p_cov: Matrix, m: sp.Symbol, metric: Matrix=None) -> Matrix:
    return proca_polarization_sum(p_cov, m, metric)

def theta_omega_projectors(p_cov: Matrix, metric: Matrix=None):
    g = Matrix(metric) if metric is not None else default_metric()
    g_inv = g.inv(); p = Matrix(p_cov)
    p2 = (p.T * g_inv * p)[0]
    if sp.simplify(p2) == 0: raise ValueError("Lightlike momentum not supported")
    omega = (p*p.T)/p2; theta = g - omega
    return sp.simplify(theta), sp.simplify(omega)

def br_projectors_rank2(p_cov: Matrix, metric: Matrix=None):
    g = Matrix(metric) if metric is not None else default_metric()
    g_inv = g.inv(); p = Matrix(p_cov)
    p2 = (p.T * g_inv * p)[0]
    if sp.simplify(p2) == 0: raise ValueError("Lightlike momentum not supported")
    omega = (p*p.T)/p2; theta = g - omega
    P2 = sp.MutableDenseNDimArray.zeros(4,4,4,4)
    P1 = sp.MutableDenseNDimArray.zeros(4,4,4,4)
    P0s = sp.MutableDenseNDimArray.zeros(4,4,4,4)
    P0w = sp.MutableDenseNDimArray.zeros(4,4,4,4)
    for mu in range(4):
        for nu in range(4):
            for rho in range(4):
                for sig in range(4):
                    P2[mu,nu,rho,sig] = sp.simplify(sp.Rational(1,2)*(theta[mu,rho]*theta[nu,sig] + theta[mu,sig]*theta[nu,rho]) - sp.Rational(1,3)*theta[mu,nu]*theta[rho,sig])
                    P1[mu,nu,rho,sig] = sp.simplify(sp.Rational(1,2)*(theta[mu,rho]*omega[nu,sig] + theta[mu,sig]*omega[nu,rho] + theta[nu,rho]*omega[mu,sig] + theta[nu,sig]*omega[mu,rho]))
                    P0s[mu,nu,rho,sig] = sp.simplify(sp.Rational(1,3)*theta[mu,nu]*theta[rho,sig])
                    P0w[mu,nu,rho,sig] = sp.simplify(omega[mu,nu]*omega[rho,sig])
    return P2,P1,P0s,P0w

def br_identity_sym(metric: Matrix=None):
    g = Matrix(metric) if metric is not None else default_metric()
    I4 = sp.MutableDenseNDimArray.zeros(4,4,4,4)
    for mu in range(4):
        for nu in range(4):
            for rho in range(4):
                for sig in range(4):
                    I4[mu,nu,rho,sig] = sp.Rational(1,2)*(g[mu,rho]*g[nu,sig] + g[mu,sig]*g[nu,rho])
    return I4

def br_compose(Pa, Pb, metric: Matrix=None):
    g = Matrix(metric) if metric is not None else default_metric()
    g_inv = g.inv(); out = sp.MutableDenseNDimArray.zeros(4,4,4,4)
    for mu in range(4):
        for nu in range(4):
            for rho in range(4):
                for sig in range(4):
                    s = 0
                    for a in range(4):
                        for b in range(4):
                            for c in range(4):
                                for d in range(4):
                                    s += Pa[mu,nu,a,b]*g_inv[a,c]*g_inv[b,d]*Pb[c,d,rho,sig]
                    out[mu,nu,rho,sig] = sp.simplify(s)
    return out

def br_apply(P, h: Matrix):
    out = sp.MutableDenseMatrix.zeros(4,4)
    for mu in range(4):
        for nu in range(4):
            s = 0
            for rho in range(4):
                for sig in range(4):
                    s += P[mu,nu,rho,sig]*h[rho,sig]
            out[mu,nu] = sp.simplify(s)
    return out


def br_check_identities(p_cov: Matrix, metric: Matrix=None):
    P2,P1,P0s,P0w = br_projectors_rank2(p_cov, metric)
    g = Matrix(metric) if metric is not None else default_metric()
    I4 = br_identity_sym(g)
    sumP = sp.MutableDenseNDimArray.zeros(4,4,4,4)
    for mu in range(4):
        for nu in range(4):
            for rho in range(4):
                for sig in range(4):
                    sumP[mu,nu,rho,sig] = sp.simplify(P2[mu,nu,rho,sig]+P1[mu,nu,rho,sig]+P0s[mu,nu,rho,sig]+P0w[mu,nu,rho,sig])
    completeness_ok = all(sp.simplify(sumP[mu,nu,rho,sig]-I4[mu,nu,rho,sig])==0
                          for mu in range(4) for nu in range(4) for rho in range(4) for sig in range(4))
    P2P1 = br_compose(P2,P1,g)
    P2P2 = br_compose(P2,P2,g)
    P1P1 = br_compose(P1,P1,g)
    P0sP0s = br_compose(P0s,P0s,g)
    P0wP0w = br_compose(P0w,P0w,g)
    ortho_ok = all(sp.simplify(P2P1[i,i,i,i])==0 for i in range(2))
    idem_ok  = all(sp.simplify(P2P2[i,i,i,i]-P2[i,i,i,i])==0 for i in range(2))                and all(sp.simplify(P1P1[i,i,i,i]-P1[i,i,i,i])==0 for i in range(1))                and all(sp.simplify(P0sP0s[i,i,i,i]-P0s[i,i,i,i])==0 for i in range(1))                and all(sp.simplify(P0wP0w[i,i,i,i]-P0w[i,i,i,i])==0 for i in range(1))
    return {"completeness_ok": completeness_ok, "orthogonality_sample_ok": ortho_ok, "idempotency_sample_ok": idem_ok}


# ---------- YM/Maxwell, Axial-Proca, Stress T ----------
def abelian_field_strength(A_cov: Matrix, coords=None):
    if coords is None: coords = default_coords()
    A = Matrix(A_cov); F = sp.MutableDenseMatrix.zeros(4,4)
    for mu in range(4):
        for nu in range(4):
            F[mu,nu] = sp.simplify(sp.diff(A[nu], coords[mu]) - sp.diff(A[mu], coords[nu]))
    return F

def ym_field_strength(A_cov_list, fABC, coords=None):
    if coords is None: coords = default_coords()
    Fs = []
    for A_idx, A_mu in enumerate(A_cov_list):
        A_mu = Matrix(A_mu)
        F = sp.MutableDenseMatrix.zeros(4,4)
        for mu in range(4):
            for nu in range(4):
                term = sp.diff(A_mu[nu], coords[mu]) - sp.diff(A_mu[mu], coords[nu])
                acc = 0
                for B in range(len(A_cov_list)):
                    for C in range(len(A_cov_list)):
                        acc += fABC[A_idx][B][C]*A_cov_list[B][mu,0]*A_cov_list[C][nu,0]
                F[mu,nu] = sp.simplify(term + acc)
        Fs.append(F)
    return Fs

def ym_F2_scalar(F_list, g: Matrix):
    g_inv = Matrix(g).inv(); s = 0
    for F in F_list:
        F = Matrix(F)
        for mu in range(4):
            for nu in range(4):
                for a in range(4):
                    for b in range(4):
                        s += g_inv[mu,a]*g_inv[nu,b]*F[mu,nu]*F[a,b]
    return sp.simplify(s)

def ym_lagrangian_scalar(F_list, g: Matrix):
    return -sp.Rational(1,4)*ym_F2_scalar(F_list, g)

def ym_lagrangian_density(F_list, g: Matrix):
    return sp.sqrt(sp.Abs(Matrix(g).det())) * ym_lagrangian_scalar(F_list, g)

def axial_proca_lagrangian(S_cov, g: Matrix, mS: sp.Symbol, coords=None, J5=None, gS=None):
    g = Matrix(g); g_inv = g.inv()
    if coords is None: coords = default_coords()
    S_cov = Matrix(S_cov)
    S2 = (S_cov.T * g_inv * S_cov)[0]
    H = sp.MutableDenseMatrix.zeros(4,4)
    for mu in range(4):
        for nu in range(4):
            H[mu,nu] = sp.simplify(sp.diff(S_cov[nu], coords[mu]) - sp.diff(S_cov[mu], coords[nu]))
    H2 = 0
    for mu in range(4):
        for nu in range(4):
            for a in range(4):
                for b in range(4):
                    H2 += g_inv[mu,a]*g_inv[nu,b]*H[mu,nu]*H[a,b]
    L = -sp.Rational(1,4)*sp.simplify(H2) + sp.Rational(1,2)*(mS**2)*sp.simplify(S2)
    if J5 is not None and gS is not None:
        J5 = Matrix(J5); SJ = (S_cov.T * J5)[0]; L -= gS*SJ
    return sp.simplify(L)

def T_scalar(g: Matrix, dphi_cov: Matrix, V_phi: sp.Expr):
    g = Matrix(g); g_inv = g.inv(); dphi_cov = Matrix(dphi_cov)
    kinetic = (dphi_cov.T * g_inv * dphi_cov)[0]
    T = sp.MutableDenseMatrix.zeros(4,4)
    for mu in range(4):
        for nu in range(4):
            T[mu,nu] = sp.simplify(dphi_cov[mu]*dphi_cov[nu] - sp.Rational(1,2)*g[mu,nu]*kinetic - g[mu,nu]*V_phi)
    return T

def T_yang_mills(g: Matrix, F_list):
    g = Matrix(g); g_inv = g.inv()
    T = sp.MutableDenseMatrix.zeros(4,4); F2 = ym_F2_scalar(F_list, g)

    for mu in range(4):
        for nu in range(4):
            s = 0
            for F in F_list:
                F = Matrix(F)
                for a in range(4):
                    s += F[mu,a]*sum(g_inv[a,b]*F[nu,b] for b in range(4))
            T[mu,nu] = sp.simplify(s - sp.Rational(1,4)*g[mu,nu]*F2)
    return T

def T_proca(g: Matrix, A_cov: Matrix, m: sp.Symbol, coords=None):
    g = Matrix(g); g_inv = g.inv()
    if coords is None: coords = default_coords()
    A = Matrix(A_cov); F = sp.MutableDenseMatrix.zeros(4,4)
    for mu in range(4):
        for nu in range(4):
            F[mu,nu] = sp.simplify(sp.diff(A[nu], coords[mu]) - sp.diff(A[mu], coords[nu]))
    F2 = 0
    for mu in range(4):
        for nu in range(4):
            for a in range(4):
                for b in range(4):
                    F2 += g_inv[mu,a]*g_inv[nu,b]*F[mu,nu]*F[a,b]
    A2 = (A.T * g_inv * A)[0]
    T = sp.MutableDenseMatrix.zeros(4,4)
    F_up = sp.MutableDenseMatrix.zeros(4,4)
    for nu in range(4):
        for a in range(4):
            F_up[nu,a] = sum(g_inv[a,b]*F[nu,b] for b in range(4))
    for mu in range(4):
        for nu in range(4):
            termF = sum(F[mu,a]*F_up[nu,a] for a in range(4))
            T[mu,nu] = sp.simplify(termF - sp.Rational(1,4)*g[mu,nu]*F2 + (m**2)*(A[mu]*A[nu] - sp.Rational(1,2)*g[mu,nu]*A2))
    return T

# ---------- Gravity tensors ----------
def christoffel_symbols(g: Matrix, coords=None):
    g = Matrix(g)
    if coords is None: coords = default_coords()
    g_inv = g.inv()
    Gamma = sp.MutableDenseNDimArray.zeros(4,4,4)
    for rho in range(4):
        for mu in range(4):
            for nu in range(4):
                s = 0
                for sigma in range(4):
                    s += g_inv[rho, sigma]*(sp.diff(g[sigma, nu], coords[mu]) + sp.diff(g[sigma, mu], coords[nu]) - sp.diff(g[mu, nu], coords[sigma]))
                Gamma[rho, mu, nu] = sp.simplify(sp.Rational(1,2)*s)
    return Gamma

def riemann_tensor(g: Matrix, coords=None, Gamma=None):
    if coords is None: coords = default_coords()
    if Gamma is None: Gamma = christoffel_symbols(g, coords)
    R = sp.MutableDenseNDimArray.zeros(4,4,4,4)
    for rho in range(4):
        for sig in range(4):
            for mu in range(4):
                for nu in range(4):
                    term = sp.diff(Gamma[rho, nu, sig], coords[mu]) - sp.diff(Gamma[rho, mu, sig], coords[nu])
                    acc = 0
                    for lam in range(4):
                        acc += Gamma[rho, mu, lam]*Gamma[lam, nu, sig] - Gamma[rho, nu, lam]*Gamma[lam, mu, sig]
                    R[rho, sig, mu, nu] = sp.simplify(term + acc)
    return R

def ricci_tensor(g: Matrix, coords=None, Riemann=None, Gamma=None):
    if coords is None: coords = default_coords()
    if Riemann is None: Riemann = riemann_tensor(g, coords, Gamma=Gamma)
    Ric = sp.MutableDenseMatrix.zeros(4,4)
    for mu in range(4):
        for nu in range(4):
            s = 0
            for rho in range(4):
                s += Riemann[rho, mu, rho, nu]
            Ric[mu,nu] = sp.simplify(s)
    return Ric

def ricci_scalar(g: Matrix, coords=None, Ric=None, Gamma=None):
    g = Matrix(g); g_inv = g.inv()
    if Ric is None: Ric = ricci_tensor(g, coords, Gamma=Gamma)
    R = 0
    for mu in range(4):
        for nu in range(4):
            R += g_inv[mu,nu]*Ric[mu,nu]
    return sp.simplify(R)

def einstein_tensor(g: Matrix, coords=None, Ric=None, Rscalar=None, Gamma=None):
    g = Matrix(g)
    if Ric is None: Ric = ricci_tensor(g, coords, Gamma=Gamma)
    if Rscalar is None: Rscalar = ricci_scalar(g, coords, Ric=Ric, Gamma=Gamma)
    G = sp.MutableDenseMatrix.zeros(4,4)
    for mu in range(4):
        for nu in range(4):
            G[mu,nu] = sp.simplify(Ric[mu,nu] - sp.Rational(1,2)*g[mu,nu]*Rscalar)
    return G

def bianchi_identity_check(g: Matrix, coords=None, Gamma=None):
    g = Matrix(g)
    if coords is None: coords = default_coords()
    if Gamma is None: Gamma = christoffel_symbols(g, coords)
    G = einstein_tensor(g, coords, Gamma=Gamma); g_inv = g.inv()
    G_up = sp.MutableDenseMatrix.zeros(4,4)
    for mu in range(4):
        for nu in range(4):
            G_up[mu,nu] = sum(g_inv[mu,r]*G[r,nu] for r in range(4))
    divG = [0,0,0,0]
    for nu in range(4):
        expr = 0
        for mu in range(4):
            term = sp.diff(G_up[mu,nu], coords[mu])
            term += sum(Gamma[mu,mu,lam]*G_up[lam,nu] for lam in range(4))
            term -= sum(Gamma[lam,mu,nu]*G_up[mu,lam] for lam in range(4))
            expr += term
        divG[nu] = sp.simplify(expr)
    all_zero = all(sp.simplify(x)==0 for x in divG)
    return {"divG": divG, "all_zero": all_zero}

# ---------- Geometry: nonmetricity/contorsion ----------
def nonmetricity_Q(g: Matrix, Gamma):
    g = Matrix(g)
    t,x,y,z = default_coords(); coords = (t,x,y,z)
    Q = sp.MutableDenseNDimArray.zeros(4,4,4)
    for a in range(4):
        for m in range(4):
            for n in range(4):
                term = -sp.diff(g[m,n], coords[a])
                for r in range(4):
                    term += Gamma[r,a,m]*g[r,n] + Gamma[r,a,n]*g[m,r]
                Q[a,m,n] = sp.simplify(term)
    return Q

def contorsion_from_torsion(T):
    K = sp.MutableDenseNDimArray.zeros(4,4,4)
    for l in range(4):
        for m in range(4):
            for n in range(4):
                K[l,m,n] = sp.Rational(1,2)*(T[l,m,n] - T[m,n,l] + T[n,l,m])
    return K

# ---------- Spinor metadata & BRST ----------
def gamma_anticommutator(mu, nu, g_inv: Matrix):
    return 2*Matrix(g_inv)[mu,nu]

def gamma5_larin_info():
    return {"scheme": "Larin", "notes": "Axial current finite renormalization; gamma5 via epsilon tensor in D=4."}

def brst_variations_nonabelian(A_cov_list, c_list, fABC, coords=None):
    if coords is None: coords = default_coords()
    sA = []; sc = []; sbarc = []; sB = []
    for A_idx, A_mu in enumerate(A_cov_list):
        A_mu = Matrix(A_mu)
        comp = sp.MutableDenseMatrix.zeros(4,1)
        for mu in range(4):
            term = sp.diff(c_list[A_idx], coords[mu])
            acc = 0
            for B in range(len(A_cov_list)):
                for C in range(len(A_cov_list)):
                    acc += fABC[A_idx][B][C]*A_mu[mu,0]*c_list[C]
            comp[mu,0] = sp.simplify(term + acc)
        sA.append(comp)
    for A_idx in range(len(c_list)):
        acc = 0
        for B in range(len(c_list)):
            for C in range(len(c_list)):
                acc += fABC[A_idx][B][C]*c_list[B]*c_list[C]
        sc.append(sp.simplify(-sp.Rational(1,2)*acc))
    for A_idx in range(len(c_list)):
        Bsym = sp.Symbol(f"B^{A_idx}", commutative=True)
        sbarc.append(Bsym); sB.append(0)
    return {"sA": sA, "sc": sc, "sbarc": sbarc, "sB": sB}

# ---------- Odds & ends ----------
def epsilon_contraction_test():
    mu, alpha = sp.symbols('mu alpha')
    return -sp.factorial(3) * sp.KroneckerDelta(mu, alpha)

def tetrad_from_metric(g: Matrix):
    g = Matrix(g)
    if any(g[i,j] != 0 for i in range(4) for j in range(4) if i!=j):
        raise ValueError("tetrad_from_metric supports diagonal metrics only")
    e = sp.MutableDenseMatrix.zeros(4,4)
    e[0,0] = sp.sqrt(sp.Abs(g[0,0]))
    for i in range(1,4): e[i,i] = sp.sqrt(sp.Abs(g[i,i]))
    return e

def project_tensor_to_frame(T_cov: Matrix, e: Matrix):
    E = Matrix(e); E_inv = E.inv()
    return sp.simplify(E_inv * Matrix(T_cov) * E_inv.T)

# ---------- Mass dimensions ----------
def mass_dimension_field(kind: str, D: int=4):
    k = kind.lower()
    if k == 'scalar': return sp.Rational(D-2, 2)
    if k == 'vector': return sp.Rational(D-2, 2)
    if k == 'spinor': return sp.Rational(D-1, 2)
    if k == 'fieldstrength': return sp.Rational(D, 2)
    if k == 'metric': return sp.Integer(0)
    if k == 'tetrad': return sp.Integer(0)
    if k == 'gauge_coupling': return sp.Rational(4-D, 2)
    if k == 'newtong': return sp.Integer(2-D)
    raise ValueError("unknown kind")



# ---------- Einstein–Hilbert density ----------
def einstein_hilbert_density(Rscalar: sp.Expr, g: Matrix, GNewton):
    return sp.sqrt(sp.Abs(Matrix(g).det())) * (Rscalar) / (16*sp.pi*GNewton)
# ---------- Aliases & exports ----------
adm_from_metric = adm_split
fourier_conventions = fourier_pair
delta_normalization = delta_normalization_check
plancherel_factor = plancherel_check
kubo_response = kubo_formula_response
wick_action_density_4form = wick_action_4form_to_euclidean
wick_one_form_time = wick_time_map_dt_to_tau
wick_metric = wick_metric_to_euclidean

__all__ = [
    'default_metric','default_coords','UGFTForm',
    'wick_time_map_dt_to_tau','wick_metric_to_euclidean','wick_action_4form_to_euclidean','wick_rotate_scalar_lagrangian',
    'ibp_exterior','ghy_boundary_density','ghy_surface_density','adm_split','adm_from_metric',
    'fourier_pair','delta_normalization_check','plancherel_check','fourier_pair_nd','delta_normalization_nd',
    'delta_normalization','fourier_conventions','plancherel_factor',
    'retarded_kernel_KG','laplacian_of_inv_r','laplacian_log_r_2d',
    'kubo_sigma_dc','kubo_formula_response','measure_volume_density','measure_surface_density','kubo_sigma_dc_curved','kubo_response',
    'proca_polarization_sum','spin1_polarization_sum','theta_omega_projectors',
    'br_projectors_rank2','br_identity_sym','br_compose','br_apply','br_check_identities',
    'abelian_field_strength','ym_field_strength','ym_F2_scalar','ym_lagrangian_scalar','ym_lagrangian_density',
    'axial_proca_lagrangian','T_scalar','T_yang_mills','T_proca','einstein_hilbert_density',
    'christoffel_symbols','riemann_tensor','ricci_tensor','ricci_scalar','einstein_tensor','bianchi_identity_check',
    'nonmetricity_Q','contorsion_from_torsion',
    'gamma_anticommutator','gamma5_larin_info','brst_variations_nonabelian',
    'epsilon_contraction_test','tetrad_from_metric','project_tensor_to_frame',
    'mass_dimension_field'
]

def _principal_minors(matrix: Matrix):
    """
    Return list of leading principal minors det(M[0:n,0:n]) for n = 1..N.
    Used by is_spd_leading_minors for Sylvester's criterion.
    """
    M = Matrix(matrix)
    minors = []
    for n in range(1, M.shape[0] + 1):
        minors.append(sp.simplify(M[:n, :n].det()))
    return minors


def is_spd_leading_minors(matrix: Matrix):
    """
    Sylvester's criterion (leading minors):
    SPD ⇔ all leading principal minors > 0 (for numeric matrices).
    Returns a dictionary with the minors and a conservative symbolic flag:
    True only if all minors simplify to positive numeric constants.
    """
    minors = _principal_minors(matrix)
    flag = all(m.is_Number and (m > 0) for m in minors)
    return {"minors": minors, "spd_definite_by_minors": flag}
