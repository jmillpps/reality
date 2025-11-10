# Introduction

This chapter codifies the mathematical and unit conventions that will be used throughout the Unified Geometric Field Theory (UGFT) program. Its purpose is to fix, in one place, the precise definitions, normalizations, and scope rules that every subsequent derivation and computation assumes. By making these conventions explicit and self‑consistent, we remove ambiguity in gauge, geometric, and gravitational calculations; ensure that conservation laws and anomaly ledgers are evaluated with the correct numerical factors; and guarantee reproducibility when translating between natural units and laboratory scales.

We proceed from general to specific. First, we define the unit system and the map back to measurable quantities. Next, we set the algebraic normalization of gauge generators and the canonical coefficients of kinetic and interaction terms that appear across the gauge, sigma‑model, Skyrme, and gravitational sectors. We then formalize the use of invariant measures and source terms (including the spherical “no‑extra‑\(r\)” rule for Gauss’s law), and we state the scope rules that separate electrostatic analyses (Coulomb gauge, spherical symmetry) from magnetostatic or axial/holonomy analyses (temporal or axial setups). Boundary and topological structures are treated with care: Chern–Simons terms are fixed as boundary terms with quantized levels that close anomaly ledgers without altering bulk equations of motion. The gravitational normalization is specified in first‑order (Einstein–Cartan) form with torsion algebraically tied to spin density, and the time‑foliation choice used for well‑posed evolution is recorded. Finally, we state the integer‑valued ledgers and the associated charge‑quantization lattice that underwrite integrality of fluxes and anomaly sums.

Each section of this chapter is normative. For every convention we provide (i) a precise mathematical statement, (ii) its immediate implications for equations of motion, conserved quantities, and diagnostics, and (iii) a brief note on how the convention is applied across electromagnetic, non‑Abelian, gravitational/cosmological, and transport calculations. Where relevant, we include the restoration map to SI units to enable direct comparison with empirical scales.

## A.0 Notation & Indexing Preliminaries

This subsection fixes the symbols, index ranges, exterior‑calculus conventions, orientations, and sign choices used throughout the chapter. All later definitions (units, normalizations, ledgers) inherit these conventions.

### A.0.1 Index Sets and Metrics
- **Spacetime indices:** \(\mu,\nu,\rho,\sigma = 0,1,2,3\).
- **Spatial indices:** \(i,j,k = 1,2,3\).
- **Tangent‑space (Lorentz) indices:** \(a,b,c,d = 0,1,2,3\).
- **Gauge adjoint indices:** \(A,B,C = 1,\dots,\dim G\).
- **Internal matter/representation indices:** \(I,J,\dots\) as needed.
- **Metric signature:** \((-,+,+,+)\) (“mostly plus”).
- **Raising/lowering:** with \(g_{\mu\nu}\) and \(\eta_{ab}=\mathrm{diag}(-,+,+,+)\).
- **Symmetrization / antisymmetrization (weight‑one):**
  \[
  X_{(\mu\nu)} \equiv \tfrac12(X_{\mu\nu}+X_{\nu\mu}),\qquad
  X_{[\mu\nu]} \equiv \tfrac12(X_{\mu\nu}-X_{\nu\mu}).
  \]

### A.0.2 Exterior Calculus and Differential Forms
- **Wedge product:** for a \(p\)-form \(\alpha\) and a \(q\)-form \(\beta\),
  \(\alpha\wedge\beta = (-1)^{pq}\,\beta\wedge\alpha\).
- **Exterior derivative:** \(d:\Lambda^p\to\Lambda^{p+1}\) with \(d^2=0\).
- **Hodge dual:** for a \(p\)-form \(\alpha\) in 4D,
  \[
  (*\alpha)_{\mu_{1}\dots\mu_{4-p}}
  = \frac{1}{p!}\,\epsilon_{\mu_{1}\dots\mu_{4-p}}{}^{\nu_{1}\dots\nu_{p}}\,
    \alpha_{\nu_{1}\dots\nu_{p}},
  \]
  and
  \[
  *^2\,\alpha = (-1)^{p(4-p)+1}\,\alpha
  \quad\text{(Lorentzian signature with one time direction)}.
  \]
- **Inner product of forms:** \(\alpha\wedge *\beta = \langle\alpha,\beta\rangle\,\mathrm{vol}_4\), with
  \(\langle\alpha,\beta\rangle = \tfrac{1}{p!}\alpha_{\mu_1\dots\mu_p}\beta^{\mu_1\dots\mu_p}\).

### A.0.3 Orientation, Levi‑Civita, and Volume Elements
- **Orientation:** fixed by \(\epsilon_{0123}=+\sqrt{|g|}\), \(\epsilon^{0123}=+1/\sqrt{|g|}\).
- **Symbol vs tensor:** the totally antisymmetric symbol \([\mu\nu\rho\sigma]\) has \([0123]=+1\); the tensor is \(\epsilon_{\mu\nu\rho\sigma}=\sqrt{|g|}\,[\mu\nu\rho\sigma]\).
- **Spacetime volume form:** \(\mathrm{vol}_4 = \sqrt{|g|}\,d^4x\);
  in tetrads, \(\mathrm{vol}_4 = \tfrac{1}{4!}\,\epsilon_{abcd}\,e^a\wedge e^b\wedge e^c\wedge e^d\).
- **3D spatial Levi‑Civita:** \(\epsilon_{ijk}=\sqrt{\gamma}\,[ijk]\) on a spatial slice with metric \(\gamma_{ij}\).
- **Stokes’ theorem:** \(\displaystyle \int_M d\alpha = \int_{\partial M}\alpha\), with outward‑normal orientation on \(\partial M\).

### A.0.4 Gauge Connections, Covariant Derivatives, and Field Strengths
- **Generators:** \(T^A\) taken Hermitian with \([T^A,T^B]=i f^{ABC}T^C\) and \(\mathrm{Tr}(T^A T^B)=\delta^{AB}\).
- **Connection one‑form (adjoint):** \(A = A_\mu^A T^A\,dx^\mu\).
- **Curvature two‑form (Yang–Mills):** \(F = dA + A\wedge A\), i.e.
  \[
  F_{\mu\nu}^A = \partial_\mu A_\nu^A - \partial_\nu A_\mu^A + f^{ABC}A_\mu^B A_\nu^C.
  \]
  In the Abelian case, \(F=dA\).
- **Dual field strength:** \({}^*F^{\mu\nu} = \tfrac12\,\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}\).
- **Gauge‑covariant derivative on matter (rep \(R\)):**
  \[
  D_\mu = \partial_\mu + i\,A_\mu^A\,T^A_{(R)},\qquad
  D = d + i\,A \;\;\text{(on differential forms/sections)}.
  \]
  On adjoint‑valued forms, \(D\Phi = d\Phi + [A,\Phi]\).
- **Bianchi identity and equations of motion (schematic):**
  \[
  D F = 0,\qquad D{*F} = J,
  \]
  with \(J\) the appropriate current \(p\)-form (Abelian: \(dF=0,\ d{*F}=J\)).

### A.0.5 Tetrads, Spin Connection, Curvature, and Torsion
- **Tetrad:** \(e^a = e^a{}_\mu\,dx^\mu\), metric \(g_{\mu\nu}=\eta_{ab}\,e^a{}_\mu e^b{}_\nu\).
- **Spin connection:** \(\omega^a{}_b\) (metric‑compatible unless stated).
- **Curvature two‑form:** \(R^a{}_b = d\omega^a{}_b + \omega^a{}_c\wedge\omega^c{}_b\).
- **Torsion two‑form:** \(T^a = De^a = de^a + \omega^a{}_b\wedge e^b\).
- **Coordinate Riemann tensor (for reference):**
  \[
  R^\rho{}_{\sigma\mu\nu}
  = \partial_\mu \Gamma^\rho_{\nu\sigma}
    - \partial_\nu \Gamma^\rho_{\mu\sigma}
    + \Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma}
    - \Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma}.
  \]

### A.0.6 Notational Shortcuts
- **Commutator/anticommutator:** \([X,Y]=XY-YX\), \(\{X,Y\}=XY+YX\).
- **Contractions:** repeated indices are summed; \(\lrcorner\) denotes interior product when needed.
- **Projection to spatial slices:** \(n^\mu n_\mu=-1\), \(\gamma_{\mu\nu}=g_{\mu\nu}+n_\mu n_\nu\); spatial Hodge star \(*_\gamma\) acts with \(\gamma_{ij}\).

> **Scope:** These conventions are fixed for the remainder of the chapter and are assumed in all definitions of units, normalizations, measures, ledgers, and diagnostics.

---

## A.1 Natural (Hat) Units and Dimensional Restoration

This section establishes the unit system used throughout and provides explicit rules for restoring dimensionful quantities when comparing to experiment. All subsequent normalizations and conservation laws are stated in this unit system.

### A.1.1 Unit System and Notation

- **Natural (hat) units:** we set
  \[
  \hbar = c = k_B = 1.
  \]
  In these units, energy, mass, inverse length, inverse time, and temperature share the same dimension. We denote dimensionless (natural‑unit) quantities with a hat, e.g. \(\hat{X}\).

- **Action and densities:** the action is dimensionless, \([S]=1\). In 4D, the Lagrangian density has mass dimension \([{\cal L}]=4\).

- **Dimension (mass) assignments in 4D:**
  \[
  [\partial_\mu]=1,\quad [A_\mu]=1,\quad [F_{\mu\nu}]=2,\quad
  [\phi]=1\ \text{(canonical scalar)},\quad [\psi]=\tfrac{3}{2},\quad
  [J^\mu]=3.
  \]
  For a unit‑vector sigma field \(\hat n\) (target \(S^2\)), \([\hat n]=0\) by definition.

- **Dimensionless couplings:** gauge couplings and self‑couplings are taken dimensionless in 4D, e.g. \([g]=0\). (The fine‑structure constant \(\alpha\) is also dimensionless.)

- **Gravitational normalization:** in first‑order form with Einstein–Cartan variables,
  \[
  S_{\rm grav}=\frac{1}{16\pi G}\int \epsilon_{abcd}\,e^a\wedge e^b\wedge R^{cd}\ +\ \cdots,
  \]
  with \([G]=-2\) (mass dimension \(-2\)) and \([R]=2\). The tetrad \(e^a\) is dimensionless in the differential‑form normalization used here; dimensions enter through \(G\) and curvature.

### A.1.2 Canonical Normalizations (as Units Conventions)

The following coefficients are fixed as part of the unit choice and are used uniformly in all sectors:
- **Yang–Mills kinetic term:** \(-\tfrac{1}{4} F^A_{\mu\nu}F^{A\,\mu\nu}\) with generators normalized by \(\mathrm{Tr}(T^A T^B)=\delta^{AB}\).
- **Sigma‑model kinetic term:** \(\tfrac{1}{2}\,(\partial_\mu \hat n)\cdot(\partial^\mu \hat n)\) for a unit‑vector target field \(\hat n\).
- **Skyrme term:** \(\tfrac{\lambda}{4}\,\big(\hat n\cdot(\partial_\mu \hat n\times \partial_\nu \hat n)\big)^2\).
- **Electromagnetic identification:** the gauge coupling satisfies \(g^2=4\pi\alpha\) (dimensionless).

These are **unit conventions**: any legacy mass scales are absorbed into field redefinitions so that the coefficients above appear exactly as written in hat units. When restoring dimensions, reinsert the appropriate scales as detailed below.

### A.1.3 Dimensional Restoration: General Recipe

To compare with SI or other engineering units, introduce a single reference energy scale \(E_\star\) (with associated length \(\ell_\star=\hbar c/E_\star\) and time \(t_\star=\hbar/E_\star\)). The map from hat to physical quantities is:

- **Kinematics**
  \[
  x^\mu = \ell_\star\,\hat{x}^\mu,\qquad
  t = t_\star\,\hat t,\qquad
  p_\mu = E_\star\,\hat p_\mu,\qquad
  E=E_\star\,\hat E,\qquad
  T = \frac{E_\star}{k_B}\,\hat T\quad (k_B=1\ \text{in hats}).
  \]

- **Fields and currents**
  \[
  A_\mu = E_\star\,\hat A_\mu,\qquad
  F_{\mu\nu} = E_\star^2\,\hat F_{\mu\nu},\qquad
  \phi = E_\star\,\hat\phi\ \ (\text{canonical scalar}),\qquad
  \psi = E_\star^{3/2}\,\hat\psi,\qquad
  J^\mu = E_\star^3\,\hat J^\mu.
  \]
  For a unit‑vector field \(\hat n\), no rescaling is required; if a physical decay constant \(f\) is desired, write \(\phi=f\,\hat n\) and treat \(f\) as the inserted scale.

- **Couplings and parameters**
  \[
  g=\hat g,\qquad \alpha=\hat\alpha,\qquad
  \lambda=\hat\lambda,\qquad
  G = \hat G\,E_\star^{-2}.
  \]
  Dimensionless couplings remain unchanged; Newton’s constant restores with \(E_\star^{-2}\).

- **Densities and measures**
  \[
  d^4x = \ell_\star^4\,d^4\hat x,\qquad
  \sqrt{|g|}\,d^4x = \ell_\star^4\,\sqrt{|\hat g|}\,d^4\hat x,\qquad
  \delta^{(3)}(\mathbf r) = \ell_\star^{-3}\,\delta^{(3)}(\hat{\mathbf r}).
  \]

- **Canonical electromagnetic relations**
  \[
  \mathbf{E} = E_\star^2\,\hat{\mathbf E},\qquad
  \mathbf{B} = E_\star^2\,\hat{\mathbf B},\qquad
  V = E_\star\,\hat V,\qquad
  \rho = E_\star^3\,\hat\rho.
  \]
  Gauss’s law, \(\nabla\cdot\mathbf{E}=\rho\), is dimensionally consistent under the above maps.

### A.1.4 Practical Choices of \(E_\star\)

The restoration scale \(E_\star\) is selected for the target regime:
- **Atomic/QED:** \(E_\star=m_e c^2\). Then \(\ell_\star=\hbar/(m_e c)=a_0/\alpha\) (with \(a_0\) the Bohr radius).
- **Hadronic/HEP:** \(E_\star=1~\mathrm{GeV}\). Then \(1~\mathrm{GeV}^{-1}\approx 0.197~\mathrm{fm}\).
- **Gravitational:** when convenient, \(E_\star=M_{\rm Pl}c^2\) with \(G=1/M_{\rm Pl}^2\) in hats.

Any single choice of \(E_\star\) yields a consistent translation for all quantities appearing in a calculation; switching \(E_\star\) simply rescales hats uniformly.

### A.1.5 Restoration Checklist (for Reproducibility)

1. **Pick \(E_\star\)** consistent with the physical regime and state it once.  
2. **Rescale coordinates and fields** using the maps in §A.1.3.  
3. **Reinsert \(G\)** (and any decay constants \(f\)) with their proper dimensions.  
4. **Verify equations** carry consistent dimensions: \([{\cal L}]=4\), conservation laws dimensionally balanced, and delta‑functions normalized with the correct Jacobians.  
5. **Convert to SI** at the end: energies (J or eV), lengths (m), times (s), temperatures (K), and derived units (e.g., fields, conductivities) follow from the same \(E_\star\) and \(\ell_\star\).

> **Scope:** These rules are normative. All subsequent sections (gauge, sigma/Skyrme, gravitational, measures, and ledgers) assume the hat normalizations above and rely on the restoration maps stated here for comparison with experimental numbers.

---

## A.2 Group and Algebra Normalizations for Gauge Sectors

This section fixes the algebraic conventions for all gauge factors used in the theory. The choices below determine the numerical coefficients in covariant derivatives, field strengths, kinetic terms, currents, and invariants. They are **normative** and apply uniformly to every gauge sector and representation.

### A.2.1 Lie Algebras, Generators, and Structure Constants

- **Gauge algebra:** a direct sum \(\mathfrak{g}=\bigoplus_a \mathfrak{g}_a\) (e.g., \(U(1)\), \(SU(2)\), \(SU(3)\)). Indices \(A,B,C\) always refer to the adjoint of the relevant factor.
- **Generators (Hermitian):** \(T^A\) satisfy
  \[
  [T^A,T^B]= i\,f^{ABC} T^C,
  \qquad
  \mathrm{Tr}(T^A T^B)=\delta^{AB}.
  \]
  The metric on the algebra is therefore \(\delta^{AB}\) and is used to raise/lower adjoint indices.
- **Anticommutator projection (for simple groups):**
  \[
  \{T^A,T^B\}=\frac{2}{N}\,\delta^{AB}\,\mathbf{1} + d^{ABC} T^C
  \quad (\text{for } SU(N)\ \text{in the fundamental}),
  \]
  which defines \(d^{ABC}\) under this normalization.
- **Casimir and Dynkin index (representation \(R\)):**
  \[
  T^A_{(R)} T^A_{(R)} = C_2(R)\,\mathbf{1}_R, 
  \qquad
  \mathrm{Tr}_R(T^A T^B) = T(R)\,\delta^{AB}.
  \]
  With our choice \(\mathrm{Tr}(T^A T^B)=\delta^{AB}\) in the **fundamental** of \(SU(N)\), one has
  \[
  T(F)=1,\qquad
  C_2(F)=\frac{N^2-1}{N},\qquad
  C_2(\text{Adj})=2N.
  \]
- **Completeness (SU(N), fundamental):**
  \[
  \sum_{A=1}^{N^2-1} (T^A)_{ij}(T^A)_{kl}
  = \delta_{il}\,\delta_{jk} - \frac{1}{N}\,\delta_{ij}\,\delta_{kl}.
  \]

### A.2.2 Covariant Derivatives, Field Strengths, and Couplings

- **Couplings by factor:** each simple or Abelian factor \(\mathfrak{g}_a\) carries a coupling \(g_a\).
- **Covariant derivative on matter (rep \(R\) of factor \(a\)):**
  \[
  D_\mu = \partial_\mu + i\,g_a\,A_\mu^{A}\,T^A_{(R)}.
  \]
- **Non‑Abelian curvature:**
  \[
  F_{\mu\nu}^{A} = \partial_\mu A_\nu^{A} - \partial_\nu A_\mu^{A}
  + g_a\,f^{ABC} A_\mu^{B} A_\nu^{C}.
  \]
  In differential‑form notation this is \(F = dA + g_a\,A\wedge A\).
- **Abelian curvature:**
  \[
  F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu,
  \qquad F = dA.
  \]
- **Kinetic term (canonical for all factors):**
  \[
  \mathcal{L}_{\text{YM}} = -\frac{1}{4}\,F_{\mu\nu}^{A} F^{A\,\mu\nu},
  \]
  which, together with \(\mathrm{Tr}(T^A T^B)=\delta^{AB}\), fixes the overall normalization.
- **Fine‑structure identification (Abelian):**
  \[
  g_{U(1)}^2 = 4\pi\,\alpha,
  \]
  so that the electrostatic field of a point source of charge \(Q = Z\,g_{U(1)}\) reads
  \(E_r = Q/(4\pi r^2)\) in natural units.

> **Note on notation:** When a compact adjoint form \(F=dA+A\wedge A\) or \(D=d+iA\) is used, the coupling is implicitly absorbed into \(A\). When matching to \(\alpha\) or comparing different factors, we keep \(g_a\) explicit as above.

### A.2.3 Currents, Charges, and Source Normalization

- **Non‑Abelian matter currents (rep \(R\)):**
  \[
  J^{A\,\mu} = \frac{\partial \mathcal{L}}{\partial A_\mu^{A}}
  \quad \Rightarrow \quad
  D_\mu F^{A\,\mu\nu} = J^{A\,\nu}.
  \]
- **Abelian matter current (charge \(q\), dimensionless):**
  \[
  J^\mu = q\,\bar\psi \gamma^\mu \psi + \cdots,\qquad
  D_\mu = \partial_\mu + i\,g_{U(1)}\,q\,A_\mu.
  \]
- **Invariant source measure:** point sources in spherical coordinates use
  \(\delta^{(3)}(\mathbf r) = \delta(r)/(4\pi r^2)\). Gauss’s law retains its canonical flux form without extraneous \(r\)-weights.

### A.2.4 Product Groups, Orthogonality, and Mixing

- **Direct product:** for \(\mathfrak{g}=\oplus_a \mathfrak{g}_a\), all traces and commutators are block‑diagonal: \(\mathrm{Tr}(T^A_{(a)}T^B_{(b)})=\delta_{ab}\,\delta^{AB}\).
- **Kinetic mixing:** absent at the level of conventions (diagonal kinetic terms). If present in a model extension, mixing matrices are made explicit and diagonalized to restore the canonical \(-\tfrac14 F^2\) form before applying these normalizations.

### A.2.5 Summary of Fixed Choices

1. **Generator normalization:** \(\mathrm{Tr}(T^A T^B)=\delta^{AB}\) (all factors).
2. **Commutator sign:** \([T^A,T^B]=i f^{ABC} T^C\).
3. **Kinetic term:** \(-\tfrac14 F^A_{\mu\nu}F^{A\,\mu\nu}\) for each factor.
4. **Coupling placement:** \(D_\mu=\partial_\mu + i g_a A_\mu^A T^A\), \(F = dA + g_a A\wedge A\).
5. **SU(N) invariants (fundamental):** \(T(F)=1\), \(C_2(F)=(N^2-1)/N\), \(C_2(\text{Adj})=2N\), completeness as above.
6. **Abelian normalization:** \(g_{U(1)}^2=4\pi\alpha\); charges \(q\) are dimensionless numbers multiplying \(g_{U(1)}\).

### A.2.6 Operational Checklist

- Choose the gauge factor(s) and representation(s) \(R\); use the fixed \(\mathrm{Tr}\) normalization to compute \(T(R)\) and \(C_2(R)\).
- Write \(D_\mu\) and \(F_{\mu\nu}\) with explicit \(g_a\); verify that the kinetic term is canonically normalized.
- For sources and boundary problems, apply the invariant measure and Gauss’s law with no extra \(r\)-weights.
- For composite sectors or multiple factors, keep kinetic terms diagonal; if mixing is introduced, diagonalize first, then apply these conventions.

> **Scope:** The algebraic and kinetic normalizations here are used verbatim in all subsequent sections (measures, boundary terms, ledgers, transport, and gravitational couplings).

---

```markdown
# A.0  Notation & Indexing Preliminaries (final integrated version)

> **Dependency order:** indices → trace symbols → exterior calculus → orientation/Hodge → differential operators → covariant measures → gauge algebra → Wilson loops → tetrads → spinors → Fourier & Kubo → Wick → spherical basis.

---

### A.0.1  Indices, Metrics, and Raising/Lowering
- **Spacetime:** \(\mu,\nu,\rho,\sigma=0,1,2,3\), metric signature \((-,+,+,+)\).  
- **Spatial:** \(i,j,k=1,2,3\).  
- **Lorentz (tangent):** \(a,b,c,d=0,1,2,3\), with \(\eta_{ab}=\mathrm{diag}(-,+,+,+)\).  
- **Gauge adjoint:** \(A,B,C=1,\dots,\dim G\).  
- **Matter/representation:** \(I,J,\dots\).  
- **Raising/lowering:** \(V^\mu=g^{\mu\nu}V_\nu\), \(V^a=\eta^{ab}V_b\).  
  Mixed objects: \(V^a{}_\mu=e^a{}_\nu g^{\nu\rho}V_\rho\).  
- **Kronecker:** \(\delta^\mu{}_\nu,\delta^a{}_b\); \(\gamma_{ij}\) is the induced spatial metric.

*(Global sentinels: hat-unit system, \(\mathrm{Tr}(T^A T^B)=\delta^{AB}\), σ-term ½, Skyrme λ/4.)*

---

### A.0.2  Trace Symbols
\(\mathrm{Tr}\) = trace over **gauge** indices (\(\mathrm{Tr}(T^A T^B)=\delta^{AB}\));  
\(\mathrm{tr}\) = trace over **spinor / Lorentz** indices (\(\mathrm{tr}\,\mathbb{1}_4=4\)).

---

### A.0.3  Symmetrization and Exterior Calculus
\[
X_{(\mu\nu)}=\tfrac12(X_{\mu\nu}+X_{\nu\mu}),\quad
X_{[\mu\nu]}=\tfrac12(X_{\mu\nu}-X_{\nu\mu}).
\]  
Wedge product: \(\alpha\wedge\beta=(-1)^{pq}\beta\wedge\alpha\).  
Exterior derivative: \(d:\Lambda^p\!\to\!\Lambda^{p+1}\), \(d^2=0\).

---

### A.0.4  Orientation and Hodge Dual
- \(\epsilon_{0123}=+\sqrt{|g|}\), \(\epsilon^{0123}=+1/\sqrt{|g|}\); spatial \(\epsilon_{ijk}=\sqrt{\gamma}[ijk]\).  
- \(\mathrm{vol}_4=\sqrt{|g|}\,d^4x\); on a slice, \(dV=\sqrt{\gamma}\,d^3x\).  
- Hodge dual (Lorentzian):  
  \[
  (*\alpha)_{\mu_1\dots\mu_{4-p}}
  =\frac{1}{p!}\epsilon_{\mu_1\dots\mu_{4-p}}{}^{\nu_1\dots\nu_p}\alpha_{\nu_1\dots\nu_p},
  \quad *^2=(-1)^{p(4-p)+1}.
  \]
- Euclidean note: after Wick rotation, \((*_{\rm E})^2=(-1)^p\).

---

### A.0.5  Differential Operators and Curvature Contractions
\[
\nabla_\mu V^\nu=\partial_\mu V^\nu+\Gamma^\nu_{\mu\rho}V^\rho,\qquad
\Box\equiv\nabla_\mu\nabla^\mu=g^{\mu\nu}\nabla_\mu\nabla_\nu.
\]
Spatial Laplacian \(\nabla^2=\gamma^{ij}D_iD_j\).

Riemann:
\[
R^\rho{}_{\sigma\mu\nu}=
\partial_\mu\Gamma^\rho_{\nu\sigma}-\partial_\nu\Gamma^\rho_{\mu\sigma}
+\Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma}
-\Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma}.
\]
Ricci \(R_{\mu\nu}=R^\rho{}_{\mu\rho\nu}\); scalar \(R=g^{\mu\nu}R_{\mu\nu}\); Einstein \(G_{\mu\nu}=R_{\mu\nu}-\tfrac12g_{\mu\nu}R\).

---

### A.0.6  Covariant Measures and Delta Functions
\[
\int d^4x\,\sqrt{|g|}\,\delta^{(4)}_g(x,x_0)f(x)=f(x_0),\qquad
\delta^{(4)}_g=\delta(t-t_0)\delta^{(3)}_\gamma.
\]
Three-dimensional delta: \(\int d^3x\,\sqrt{\gamma}\,\delta^{(3)}_\gamma(x,x_0)f(x)=f(x_0)\).  
In \(q^i\): \(\delta^{(3)}_\gamma=\delta(q^1\!-\!q^1_0)\delta(q^2\!-\!q^2_0)\delta(q^3\!-\!q^3_0)/\sqrt{\gamma}\).  
Spherical origin: \(\boxed{\delta^{(3)}(\mathbf r)=\delta(r)/(4\pi r^2)}\).

---

### A.0.7  Gauge Algebras and Connections (explicit \(g\))
Generators \(T^A\) Hermitian, \([T^A,T^B]=i f^{ABC}T^C\), \(\mathrm{Tr}(T^A T^B)=\delta^{AB}\).  
Coupling \(g_a\) is dimensionless in 4D.  
\[
D_\mu=\partial_\mu+i\,g_a\,A_\mu^A T^A_{(R)},\qquad
F=dA+g_a\,A\wedge A,
\]
\[
F_{\mu\nu}^A=\partial_\mu A_\nu^A-\partial_\nu A_\mu^A+g_a f^{ABC}A_\mu^B A_\nu^C.
\]
*(Explicit \(g\) kept for consistency with ledger and AB work.)*

---

### A.0.8  Wilson Lines and Holonomy
Abelian: \(W[\gamma]=\exp\!\big(iq\!\oint_\gamma A_\mu dx^\mu\big)\).  
Non-Abelian (rep \(R\)): 
\[
W_R[\gamma]=\mathrm{Tr}_R\,\mathcal{P}\exp\!\left(i\,g\!\oint_\gamma A_\mu^A T^A dx^\mu\right),
\]
with center class \(z_\gamma\in Z(G)\) recorded in integer ledgers.

---

### A.0.9  Tetrads, Spin Connection, and Torsion
\(e^a=e^a{}_\mu dx^\mu\), \(g_{\mu\nu}=\eta_{ab}e^a{}_\mu e^b{}_\nu\).  
\(\omega^a{}_b\) metric-compatible unless stated.  
\[
R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b,\qquad
T^a=De^a=de^a+\omega^a{}_b\wedge e^b.
\]

---

### A.0.10  Spinors and Clifford Algebra
\(\{\gamma^a,\gamma^b\}=2\eta^{ab}\), \(\gamma^\mu=e_a{}^\mu\gamma^a\); \(\bar\psi=\psi^\dagger\gamma^0\).  
\(\gamma^5=i\gamma^0\gamma^1\gamma^2\gamma^3\); \(\gamma^{ab}=\tfrac12[\gamma^a,\gamma^b]\).  
\[
D_\mu\psi=(\partial_\mu+\tfrac14\omega_\mu{}^{ab}\gamma_{ab}+i\,g\,q\,A_\mu)\psi,
\quad
[D_\mu,D_\nu]\psi=(\tfrac14R_{\mu\nu}{}^{ab}\gamma_{ab}+i\,g\,F_{\mu\nu})\psi.
\]

---

### A.0.11  Fourier Transforms and Kubo Conventions
\[
\tilde f(\omega,\mathbf{k})=\!\int\!dt\,d^3x\,e^{\,i(\omega t-\mathbf{k}\cdot\mathbf{x})}f(t,\mathbf{x}),\quad
f(t,\mathbf{x})=\!\int\!\frac{d\omega\,d^3k}{(2\pi)^4}e^{-i(\omega t-\mathbf{k}\cdot\mathbf{x})}\tilde f.
\]
Retarded \(G^R_{AB}(t)=-i\theta(t)\langle[A(t),B(0)]\rangle\); 
\(G^R_{AB}(\omega)=\int dt\,e^{i\omega t}G^R_{AB}(t)\); 
\(\rho_{AB}=-2\,\mathrm{Im}\,G^R_{AB}\).  

**Kubo:**  
If \(J^i_{\rm tot}=\int d^3x\,j^i\), use \(\sigma_{\rm DC}=(\beta/V)\int_0^\infty dt\,\langle J^i_{\rm tot}(t)J^i_{\rm tot}(0)\rangle\).  
For density \(j^i\), omit \(1/V\) and use \(\beta\).  
Curved space adds \(\sqrt{\gamma}\,d^3x\).  

---

### A.0.12  Euclidean Continuation
Wick rotation: \(t\to -i\tau\), \(g_{00}\to +g^{\rm(E)}_{00}\); \(\epsilon^{0123}_{\rm(E)}=+1\).  
In Euclidean 4D, \((*_{\rm E})^2=(-1)^p\).  
Integer ledgers (\(c_1,\nu_G,\nu_R,k\)) are unchanged under continuation.

---

### A.0.13  Spherical Basis Identities
\[
\int d\Omega\,Y_{\ell m}^\*(\theta,\phi)Y_{\ell'm'}(\theta,\phi)=\delta_{\ell\ell'}\delta_{mm'},
\quad
\nabla^2f(r)=\tfrac1{r^2}\partial_r(r^2\partial_r f),
\quad
\nabla^2\!\left(\tfrac1{r}\right)=-4\pi\,\delta^{(3)}(\mathbf r).
\]