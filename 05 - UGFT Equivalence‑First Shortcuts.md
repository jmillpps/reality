# Chapter 5 — Equivalence‑First Shortcuts (Advanced but Easier Physics)

> **Scope.** A handbook of **equivalence‑preserving** simplifications that make derivations faster and clearer while **changing nothing** fixed by Chapter‑0 locks and the P1 axial‑torsion slice (Chapter‑2). Items are ordered from **least dependent** (pure Chapter‑0 structure) to **most dependent** (Chapter‑2 EOM and projector diagnostics).  
> **Attribution.** Principles are credited to: **Grassmann**, **Cartan**, **Hodge**, **Levi‑Civita**, **Wick**, **Gauss**, **Riemann–Christoffel–Levi‑Civita**, **Noether**, **Belinfante**, **Schwartz**, **Paley–Wiener**, **Hörmander**, **Neumann**, **Curie**, **Cayley**, **Barnes & Rivers**, **Dirac**, **Stückelberg**, **Ward**, **Faddeev**, **Popov**, **Becchi**, **Rouet**, **Stora**, **Tyutin**, **Helmholtz**, **Hamilton**, **Jacobi**, **Wentzel**, **Kramers**, **Brillouin**, **Hadamard**, **Synge**, **Green**, **Betti**, **Rayleigh**, **Rellich**, **Stokes**, **Plancherel**, **Källén**, **Lehmann**, **Bochner**, **Schwarz**, **Herglotz**, **Nevanlinna**, **Stieltjes**, **Bernstein**, **Widder**, **Sokhotski**, **Plemelj**, **Kramers**, **Kronig**, **Titchmarsh**, **Abel**, **Tauber**, **Hardy–Littlewood**, **Karamata**, **Onsager**, **Casimir**, **Kubo**, **Sylvester**, **Cholesky**, **Friedrichs**, **Fredholm**, **Lax**, **Milgram**, **Riesz**, and (for dimensions) **Buckingham** and **Bridgman**.

---

## 5.0  R1 Header — Imports & Locks

- **Signature & Hodge.** \((-,+,+,+)\); \(\epsilon\) & \(*\) conventions; Wick rules unchanged.  
- **Fourier/response/Kubo.** Phase, Plancherel, retarded \(i0^+\), DC order \((\mathbf k\!\to\!0)\) then \((\omega\!\to\!0^+)\).  
- **Projectors & Stückelberg.** Barnes–Rivers (rank‑2), massive spin‑1 completeness; P1 axial‑torsion rules.  
- **Ledgers.** Topological integers & boundary terms stay ledger‑only.

**Checklist 5.0:** R1 declared; no lock modified.

---

## 5.1  Equivalence Theorem & Basis Independence (Dirac; Stückelberg)

**Principle.** **Local, invertible** field redefinitions (orthonormal frames, helicity bases, SD/ASD splits, Cholesky rescalings, gauge choices) leave poles, residues, and observables invariant.  
**Shortcut.** **Change basis early** to diagonalize the operation at hand (star, projections, kinetic blocks), then compute.

**Checklist 5.1:** redefinitions are local/invertible; sentinel signs preserved.

---

## 5.2  Hat‑Map & Dimensionless Normalization (Buckingham; Bridgman)

**Principle.** Chapter‑0’s hat‑map realizes a **dimensionless normalization**; Buckingham/Bridgman dimensional analysis ensures scale‑invariant manipulations after the map.  
**Shortcut.** Normalize once (hats on), manipulate equations in dimensionless form, restore units (hats off) at the end.

**Checklist 5.2:** mass dimensions respected; hat‑map applied globally.

---

## 5.3  Grassmann–Cartan Exterior Algebra (index‑free wedge)

**Principle (Grassmann, Cartan).** Antisymmetry with weight‑one (anti)symmetrization fixes the wedge algebra coordinate‑independently.  
**Shortcut.** Generate wedge signs by permutation parity; forbid repeated indices; enforce \(d^2=0\) at the algebra level.

**Checklist 5.3:** antisymmetry enforced; \(d^2=0\); weight‑one conventions.

---

## 5.4  Levi‑Civita Contractions & Quick Epsilon Tests (Levi‑Civita)

**Principle.** Locked orientation yields canonical \(\epsilon\)\!–\(\epsilon\) contractions, e.g.  
\[
\epsilon^{\mu\nu\rho\sigma}\epsilon_{\alpha\nu\rho\sigma}=-3!\,\delta^\mu{}_\alpha .
\]
**Shortcut.** Use these as **instant sanity checks** for sign conventions, duals, and index order before any heavy manipulation.

**Checklist 5.4:** orientation \([0123]=+1\); contraction identities match Chapter‑0.

---

## 5.5  Neumann–Curie Symmetry Constraints (Neumann; Curie)

**Principle.** **Neumann’s principle**: any physical property tensor must be invariant under the symmetry operations of the system. **Curie’s principle**: couplings occur only if combined symmetries allow them.  
**Shortcut.** Declare the point/space‑group; project constitutive/response tensors to the **invariant subspace** by group averaging or representation decomposition. Reduce unknowns **before** projector or dispersion work; record time‑reversal/parity signatures for §5.39.

**Checklist 5.5:** symmetry group stated; invariant basis chosen; parities recorded; forbidden couplings set to zero.

---

## 5.6  Divergences & On‑Shell Equivalence (Noether; Belinfante; Stokes)

**Principle.** Adding a **total divergence** or terms **proportional to the Euler–Lagrange equations** leaves classical observables unchanged (boundary terms → **ledgers**; energy‑momentum can be **improved** à la Belinfante).  
**Shortcut.** Integrate by parts freely; discard EOM‑proportional terms **on‑shell**; track only the boundary flux in the ledger bundle.

**Checklist 5.6:** boundary/ledger separation enforced; no bulk kinetic replaced.

---

## 5.7  Distributional Foundations & Tempered Spaces (Schwartz; Paley–Wiener)

**Principle.** Retarded kernels, projector multipliers, and dispersion relations live naturally in the space of **tempered distributions**; Fourier/Hankel transforms exist under controlled growth, with support reflected in analyticity (Paley–Wiener).  
**Shortcut.** Work with tempered test functions; allow distributional limits; avoid undefined products (e.g., \(\delta\cdot \delta\)); if needed, regularize in ways compatible with our **subtractions** and **ledger** policies.

**Checklist 5.7:** tempered growth; legitimate transform/limit exchanges; undefined products avoided or regularized.

---

## 5.8  Microlocal Wavefront Sets & Product Legality (Hörmander)

**Principle.** The **wavefront set** \(WF(u)\) encodes where and in which directions a distribution \(u\) is singular.  
**Shortcuts.**  
- **Product test:** \(u\cdot v\) is defined if there is no \((x,\xi)\in WF(u)\) and \((x,-\xi)\in WF(v)\).  
- **Pullback test:** Pullbacks are legal when \(WF(u)\) avoids the **conormal bundle** of the submanifold.  
- **Convolution & composition:** Microlocal sums of covectors must not create zero‑direction conflicts.  
**Use it to:** justify S–P/K–K manipulations (§§5.36–5.37), Hadamard parametrix (§5.24), and projector multipliers (§§5.17–5.18) whenever singular supports interact.

**Checklist 5.8:** wavefront criteria checked; if violated, regularize before proceeding.

---

## 5.9  Wick‑First Quadratic Equivalence (Wick; Plancherel)

**Principle.** For **quadratic** functionals with Chapter‑0 sign locks, the Wick map is an **equivalence of inner products**:  
\[
S_L \xrightarrow{\,t\to -i\tau\,} S_E=-i\,S_L ,
\]
with the tetrad/metric continuation and \(*\)/\(\epsilon\) rules.  
**Shortcut.** For quadratic audits (norms, positivity, projector residues), **map first** to Euclidean where dot‑products are manifestly positive, check, then map back.

**Checklist 5.9:** use the locked Wick map; ledgers unchanged.

---

## 5.10  Hodge Star Diagonalization on 2‑Forms (Hodge; Cartan)

**Principle.** In 4D Lorentzian, \(*^2=-1\) on 2‑forms.  
**Shortcut.** SD/ASD split \(H_\pm=\tfrac12(H\pm i\,*H)\) so \(*H_\pm=\pm iH_\pm\). **Wick note:** after Wick, eigenvalues \(\pm 1\).

**Checklist 5.10:** Lorentzian \(*^2=-1\) on 2‑forms; Wick flips eigenvalues.

---

## 5.11  Orthonormal Cartan Frames for Local Algebra (Cartan; Riemann–Christoffel–Levi‑Civita)

**Principle.** Tetrad ladder \(g_{\mu\nu}=\eta_{ab}e^a{}_\mu e^b{}_\nu\).  
**Shortcut.** Do **wedge/inner‑product/Hodge** in an orthonormal frame; reinsert connections only for derivatives.

**Checklist 5.11:** frame change only; spin‑connection included when differentiating.

---

## 5.12  Gauss‑Style Reuse of Derivatives (Gauss; Levi‑Civita)

**Principle.** Reuse intermediates for objects with repeated derivatives.  
**Shortcut.** Cache \(\partial_\alpha g_{\mu\nu}\) (or frame derivatives) in  
\(\displaystyle \Gamma^\rho{}_{\mu\nu}=\tfrac12 g^{\rho\sigma}(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu}).\)  
**Special case.** If \(g_{\mu\nu}\) is constant in a chart, \(\Gamma^\rho{}_{\mu\nu}=0\).

**Checklist 5.12:** constant‑metric test chart‑aware; curvature unchanged.

---

## 5.13  Cayley Projectors & Barnes–Rivers Decomposition (Cayley; Barnes & Rivers; Dirac)

**Principle.** Orthogonal, idempotent projectors decompose symmetric tensors and polarization sums.  
**Shortcut.** Use \(\theta_{\mu\nu}=g_{\mu\nu}-p_\mu p_\nu/p^2\), \(\omega_{\mu\nu}=p_\mu p_\nu/p^2\); rely on \(P^{(m)}P^{(n)}=\delta^{mn}P^{(m)}\) and \(\sum_mP^{(m)}=\mathbb 1\).

**Checklist 5.13:** \(p^2=0\) handled by limits; residues checked per spin sector.

---

## 5.14  Vector Helicity Basis (Dirac) — **Alternate to BR for spin‑1**

**Principle.** In momentum space choose transverse circular polarizations \(e^{(\pm)}_i(\mathbf k)\), \(\mathbf k\!\cdot\!e^{(\pm)}=0\).  
**Shortcut.** Reduce a healthy spin‑1 field to **two scalar channels** (helicities \(\pm\)) sharing the KG pole; longitudinal is constrained (Proca/Stückelberg).

**Checklist 5.14:** helicity basis orthonormal; same analytic structure as projectors.

---

## 5.15  Hodge–Helmholtz on Spatial Slices \(\Sigma_t\) (Hodge; Helmholtz)

**Principle.** On a Riemannian 3‑slice \(\Sigma_t\) with suitable BCs,  
\[
v = \nabla\phi \;+\; \nabla\times A \;+\; h,\quad
\alpha = d\beta + \delta\gamma + h,
\]
where \(h\) is **harmonic** (zero‑mode).  
**Shortcut.** For **conserved** sources \((\nabla\!\cdot\!J=0)\), the transverse/co‑exact part is **the** channel; longitudinal is algebraic when present; **harmonic pieces live in the ledger** and are fixed by BCs.

**Checklist 5.15:** BCs declared; \(L^2\) orthogonality on \(\Sigma_t\); harmonic ↔ zero‑mode/ledger.

---

## 5.16  Helmholtz–Proca Transverse Scalarization (Helmholtz; Proca; Stückelberg)

**Principle.** Split vectors into transverse/longitudinal; for massive spin‑1 only transverse propagates.  
**Shortcut (operator identity).**
\[
\boxed{\,S^\mu=g_S(\Box+m_S^2)^{-1}\,\Pi^{\mathrm T\,\mu}{}_\nu\,J_5^\nu,\quad
\nabla_\mu S^\mu=\tfrac{g_S}{m_S^2}\nabla_\mu J_5^\mu\,}
\]
**Continuity/Ward conditioning.** If \(\nabla\!\cdot\!J=0\), then \(\Pi_T J=J\) and the solve is **just a scalar resolvent**; if \(\nabla\!\cdot\!J\neq0\), keep the algebraic longitudinal relation (non‑propagating).  
**Stückelberg path.** \(S_\mu=\hat S_\mu+\partial_\mu\pi/m_S\) with \(\partial\!\cdot\!\hat S=0\); \(\pi\) is algebraic in P1.

**Checklist 5.16:** retarded analyticity; static Yukawa; residues \(>\!0\).

---

## 5.17  Projection–Inverse Commutation Lemma (Helmholtz; Cayley)

**Principle.** For **LTI** operators with compatible BCs, the **Helmholtz/BR projector** commutes with \((\Box+m^2)^{-1}\):  
\[
(\Box+m^2)^{-1}\,\Pi\;=\;\Pi\,(\Box+m^2)^{-1}.
\]
**Shortcut.** **Project first or last** with identical results—choose the simpler order.  
**Guardrail.** If translation invariance is broken (hard boundaries, inhomogeneous media), **do not commute**; use **local Fourier** neighborhoods or **Hadamard** (§5.24), and respect **§§5.7–5.8** (distributional/microlocal) and **§§5.25–5.30** (variational/BCs/reciprocity/radiation/energy).

**Checklist 5.17:** LTI + compatible BCs; otherwise switch to local/hadamard tools.

---

## 5.18  Rank‑2 “Per‑Spin Scalarization” (Barnes & Rivers; Cayley) — **Alternate path**

**Principle.** A symmetric rank‑2 field splits into spin‑2, spin‑1, spin‑0 via BR projectors.  
**Shortcut.** **Invert per spin** with scalar resolvents acting on projected sources:
\[
h_{\mu\nu}=\sum_{s\in\{2,1,0\}}\ \mathcal G_s(\Box)\,\big(P^{(s)}\!\cdot\! T\big)_{\mu\nu},\quad 
\mathcal G_s(\Box)\sim(\Box+m_s^2)^{-1}\ \text{(model‑dependent)}.
\]

**Checklist 5.18:** orthogonality used; massless/lightlike limits treated carefully.

---

## 5.19  Gauge‑Slice Robustness & Ward Cues (Dirac; Stückelberg; Ward)

**Principle.** Physical poles/residues are **gauge‑parameter independent**; unitary‑gauge conclusions must **match** an \(R_\xi\) (or Stückelberg) audit.  
**Shortcut.** Compute in a convenient gauge (unitary), then **cross‑check** residues/poles in \(R_\xi\); disagreement flags missing constraints or basis‑dependent artifacts.

**Checklist 5.19:** residues/poles invariant under \(\xi\); Stückelberg split consistent with §5.16.

---

## 5.20  Nielsen Identity — Gauge‑Parameter Independence (Nielsen; BRST; Faddeev–Popov)

**Principle.** The gauge‑parameter derivative of the effective action is **BRST‑exact**; on physical on‑shell observables it vanishes.  
**Shortcut.** When results appear \(\xi\)‑dependent, compute \(\partial_\xi \Gamma\) and check it reduces to a BRST variation; failure flags a missing constraint or non‑physical projection.

**Checklist 5.20:** BRST nilpotency declared; physical poles/residues \(\xi\)‑independent.

---

## 5.21  Principal Symbol & Hyperbolicity Sentinels (Friedrichs)

**Principle.** Well‑posedness follows from a **symmetric‑hyperbolic** principal symbol and a positive energy estimate.  
**Shortcut.** Before using any propagator shortcut, verify the principal symbol is **Lorentzian** and admits a symmetric‑hyperbolic form; then the causal cone and front velocity are fixed.

**Checklist 5.21:** principal symbol Lorentzian; symmetric‑hyperbolic energy estimate exists.

---

## 5.22  Cone Nesting & Front Velocity (Dirac; Friedrichs)

**Principle.** Physical characteristics must lie **inside or on** the background light cone, and the **front speed** equals 1 in the high‑frequency limit.  
**Shortcut.** After projector/scalarization, test the characteristic polynomial at large \(|p|\): demand \(v_{\rm front}=1\) and cone nesting relative to \(g^{\mu\nu}\).

**Checklist 5.22:** null front speed; cones nested; no superluminal fronts.

---

## 5.23  Eikonal & Stationary‑Phase Rays (Hamilton; Jacobi; WKB)

**Principle.** At high frequency, phases \(S(x)\) satisfy  
\(g^{\mu\nu}\partial_\mu S\,\partial_\nu S = 0\) (massless) or \(= m_{\rm eff}^2\) (massive). Rays follow Hamilton’s equations with Hamiltonian \(H(x,p)=\tfrac12(g^{\mu\nu}p_\mu p_\nu - m_{\rm eff}^2)\).  
**Shortcut.** Use eikonal rays to confirm **front‑speed** and **cone nesting** (§5.22) and to set far‑field boundary conditions before building Hadamard’s local parametrix.

**Checklist 5.23:** principal symbol → eikonal consistent; ray transport respects energy positivity.

---

## 5.24  Hadamard Local Form & Null‑Cone Marching (Hadamard; Synge)

**Principle.** Curved‑space retarded kernels split into light‑cone singular piece \(U\,\delta(\sigma)\) + inside‑cone tail \(V\,\Theta(-\sigma)\).  
**Shortcut.** **March on the cone** for the \(U\) piece; treat \(V\) as a controlled tail. For P1 vectors this matches the transverse part of **§5.16** locally.

**Checklist 5.24:** globally‑hyperbolic patch; match to asymptotic kernels where valid.

---

## 5.25  Variational Boundary Well‑Posedness (GHY; counterterms; ADM‑δ)

**Principle.** The action’s variation must be well‑posed for the intended BCs (e.g., add **GHY** for metric Dirichlet; include necessary counterterms for non‑minimal couplings). Use the **ADM‑δ split** \(\delta_g^{(4)}=\delta(t-t_0)\,\delta^{(3)}_\gamma/N\) when separating time vs spatial boundary terms.  
**Shortcut.** State BC class + boundary additions **before** solving; mismatched variational pairings explain many BC paradoxes.

**Checklist 5.25:** boundary terms added; variation well‑posed in the chosen BC class; ADM‑δ usage consistent with Chapter‑0.

---

## 5.26  Homogeneous Complement & Boundary Uniqueness (Fredholm; Lax–Milgram; Riesz)

**Principle.** Any Green‑function solution equals **particular** \(+\) **homogeneous complement**; the latter is **fixed by boundary conditions**.  
**Shortcut.** Methods (free‑space convolution, images, boundary integrals, Hadamard) are **equivalent** iff they impose the **same BCs**; otherwise, differences live in the homogeneous coefficients → **ledger**.

**Checklist 5.26:** BCs declared; homogeneous complement fixed; no bulk kinetic replaced.

---

## 5.27  Boundary Condition Cookbook (Dirichlet/Neumann/Robin/Periodic; Sommerfeld)

**Principle.** Standard BCs fix the homogeneous complement and guarantee uniqueness when paired with appropriate Green kernels.  
**Shortcuts.**  
- **Dirichlet:** field fixed on boundary; homogeneous modes vanish at boundary.  
- **Neumann:** normal derivative fixed; track flux via Green/Stokes; ledger records net boundary work.  
- **Robin/mixed:** linear combination; impedance‑style parameters guide energy balance.  
- **Periodic/quasi‑periodic:** discrete \(k\)‑lattice; project–inverse commutes within the Brillouin set.  
- **Sommerfeld radiation:** outgoing wave \( (\partial_r u - iku) \to 0 \) as \(r\to\infty\); picks the **retarded** branch and fixes radiation uniqueness (see §5.29).

**Checklist 5.27:** choose BC before inversion; energy/flux book‑kept in ledger; method‑equivalence holds only with identical BCs.

---

## 5.28  Green–Betti Reciprocity (Betti; Green)

**Principle.** For self‑adjoint \(L\) with matching BC pairings,
\[
\int_\Omega (u\,L v - v\,L u)=\int_{\partial\Omega} B(u,v),
\]
so **source–response interchange** holds.  
**Shortcut.** Use this to detect BC/sign mismatches early and to confirm equivalence across methods that impose the **same** BCs.

**Checklist 5.28:** adjointness verified; boundary pairing consistent; reciprocity satisfied.

---

## 5.29  Rellich Radiation Uniqueness (Rellich; Sommerfeld)

**Principle.** For exterior Helmholtz \((\nabla^2+k^2)u=0\) with **Sommerfeld radiation**, \(u\equiv0\) is the only homogeneous solution (given mild regularity).  
**Shortcut.** Pair §5.27’s Sommerfeld condition with this result to guarantee **unique** outgoing solutions; inconsistency flags wrong BCs or sign choices.

**Checklist 5.29:** Sommerfeld verified; exterior domain regular; uniqueness holds.

---

## 5.30  Energy & Flux Ledger (Poynting; Noether)

**Principle.** For linear media, the **power balance** equals time‑rate of stored energy plus **boundary flux** (Poynting‑type) plus **dissipation** (non‑negative for passive systems).  
**Shortcut.** Use the energy identity to:  
(i) confirm **passivity** (non‑negative dissipation);  
(ii) fix **sign conventions** (flux direction vs ledger accounting);  
(iii) check that boundary work matches the **ledger** in §5.47.

**Checklist 5.30:** flux orientation declared; dissipation \(\ge 0\); ledger balance consistent.

---

## 5.31  Order‑of‑Limits & Zero‑Mode Sentry (Plancherel; Kubo)

**Principle.** DC and static limits **do not commute** in general; compact spatial sections can harbor **zero‑modes** that must be treated separately.  
**Shortcut.** Enforce the **locked order** \((\mathbf k\!\to\!0)\) then \((\omega\!\to\!0^+)\); isolate zero‑modes (if any) before taking limits, then recombine.

**Checklist 5.31:** zero‑modes isolated; DC order respected; re‑combine consistently.

---

## 5.32  Plancherel–Kubo Convolution Lanes (Plancherel; Kubo; Green; Stokes)

**Principle.** Linear, time‑translation invariant kernels are **convolutions** whose inverses are fixed by Fourier/Plancherel; DC transport by **Kubo** with the locked order. Green/Stokes identities anchor the distributional manipulations behind static limits and boundary terms.  
**Shortcut.**
\[
G^R(\omega,\mathbf k)=\big[-(\omega+i0^+)^2+\mathbf k^2+m^2\big]^{-1},\qquad
\boxed{\ \sigma_{DC}=\lim_{\omega\to0^+}\frac{1}{\omega}\Im G^R_{J^iJ^i}(\omega,\mathbf 0)\ }.
\]

**Checklist 5.32:** phase conventions respected; \((\mathbf k\!\to\!0)\) then \((\omega\!\to\!0^+)\); boundary terms ledger‑only.

---

## 5.33  Abelian/Tauberian DC Bridges (Abel; Tauber; Hardy–Littlewood; Karamata)

**Principle.** Under mild regularity (Abelian) and monotone/regular‑variation hypotheses (Tauberian), **long‑time tails** \(C(t)\sim t^{-\alpha}\) map to **small‑\(\omega\)** non‑analyticities \(G^R(\omega)\sim \omega^{\alpha-1}\) (phase fixed by causality).  
**Shortcut.** Use these pairs to: (i) infer DC finiteness/divergence from observed tails; (ii) validate or falsify claimed low‑\(\omega\) plateaus; (iii) select proper **subtractions** consistent with asymptotics.

**Checklist 5.33:** hypotheses stated; DC conclusions match tail behavior; subtractions aligned with asymptotics.

---

## 5.34  Massless Limit & IR Regulator \(m\!\to\!0^+\)

**Principle.** The Coulomb limit is \(m\!\to\!0^+\) of Yukawa; this limit may **not commute** with \(\mathbf k\!\to\!0\) or with volume \((L\!\to\!\infty)\) when zero‑modes/harmonics are present.  
**Shortcut.** Keep a small **mass regulator** while solving; isolate **harmonic/zero‑mode** sectors (ledger) via §5.15 and **§§5.26–5.29**; then remove \(m\!\to\!0^+\) after enforcing **§5.31**. Use **passivity/Herglotz** (§5.36) to confirm that regulated DC slopes remain non‑negative; far‑field checks can use **eikonal** (§5.23).

**Checklist 5.34:** regulator path declared; zero‑modes isolated; limits taken in the locked order; DC/passivity preserved.

---

## 5.35  Bochner–Schwarz Positive‑Definiteness (Bochner; Schwarz)

**Principle.** A stationary correlation \(C(t)\) is **positive‑definite** iff its Fourier transform is a **non‑negative measure**.  
**Shortcut.** Use Bochner to check any proposed spectrum or measured \(\tilde C(\omega)\) for **non‑negativity**; mismatches signal violations of stationarity/positivity or preprocessing errors.

**Checklist 5.35:** stationarity verified; spectral measure \(\ge 0\); consistent with Källén–Lehmann.

---

## 5.36  Herglotz–Nevanlinna / Stieltjes Representation (scalar channels)

**Principle.** For passive causal scalar channels, \(G^R(\omega)\) is **Herglotz**: \(\Im G^R/\omega\ge 0\), with an integral representation by a **positive measure** (Stieltjes type for many models).  
**Shortcut.** Enforce **non‑negative DC slope**, monotonic constraints, and large‑\(|\omega|\) asymptotics consistent with **S‑PB/S‑SUB**.

**Checklist 5.36:** passivity holds; positive measure exists; asymptotics match subtractions.

---

## 5.37  Matrix‑Valued Herglotz / Positive‑Real (Pick–Nevanlinna; Loewner; KYP‑style)

**Principle.** For passive **multi‑channel** response, \(G^R(\omega)\) is matrix‑Herglotz (analytic in \(\Im\omega>0\)), and \(\Im G^R(\omega)/\omega \succeq 0\) (Loewner order); it admits an integral representation with a positive matrix measure.  
**Shortcut.** Enforce Loewner‑order positivity and symmetry/reciprocity constraints on blocks; use KYP‑style tests to certify passivity for rational approximants.

**Checklist 5.37:** block‑positivity holds; symmetry/reciprocity consistent; large‑\(|\omega|\) growth matches subtractions.

---

## 5.38  Källén–Lehmann Spectral Representation (quantum channels)

**Principle.** Vacuum two‑point functions admit a positive spectral measure with support on the physical mass shell(s).  
**Shortcut.** When the channel is quantum, use K–L to cross‑check positivity and branch‑cut structure against measured spectra; reconcile with Bochner/Herglotz limits in the classical/linear‑response regime.

**Checklist 5.38:** positive spectral density; support consistent with thresholds; reflection properties obeyed.

---

## 5.39  Bernstein–Widder Complete Monotonicity (Bernstein; Widder)

**Principle.** A causal kernel \(k(t)\) is **completely monotone** (\((-1)^n k^{(n)}(t)\!\ge\!0\) for \(t\!>\!0\)) iff its Laplace transform is **Stieltjes** with non‑negative measure.  
**Shortcut.** Use this **time‑domain** test for passivity/dissipation; it implies the **frequency‑domain** Herglotz properties and non‑negative DC slope for relaxation kernels.

**Checklist 5.39:** complete monotonicity checked; Laplace–Stieltjes representation exists.

---

## 5.40  Sokhotski–Plemelj & \(i0^+\) Prescription (Sokhotski; Plemelj)

**Principle.**  
\[
\frac{1}{x\pm i0^+}= \mathrm{PV}\!\left(\frac{1}{x}\right) \mp i\pi\,\delta(x)
\]
connects spectral density, principal value, and the retarded rule.  
**Shortcut.** Use this identity to pass between real/imag parts, **define** distributional limits, and set up **Kramers–Kronig** (§5.41) cleanly.

**Checklist 5.40:** distributional & microlocal setting (§§5.7–5.8) respected; signs consistent with retarded convention.

---

## 5.41  Kramers–Kronig / Hilbert‑Pair Dispersion (Kramers; Kronig; Titchmarsh)

**Principle.** For retarded responses analytic in the upper half‑plane, \(\Re G^R\) and \(\Im G^R\) are **Hilbert transforms** (up to required **subtractions**); **Schwarz reflection** fixes real/imag parity for real underlying fields.  
**Shortcut.** Cross‑check response components with **Hilbert pairs**; apply **subtractions** (S‑PB/S‑SUB) when asymptotics demand.

**Checklist 5.41:** analyticity domain respected; subtractions documented; DC order retained; reality/reflection obeyed.

---

## 5.42  High‑Frequency Moments & Sum‑Rule Audit (TRK‑type; Kubo/K–K)

**Principle.** High‑frequency expansions of causal responses imply **moment/sum‑rule** constraints—weighted integrals of \(\Im G^R\) tied to static quantities.  
**Shortcut.** Use **K–K with subtractions** to derive moment identities and test spectra for missing weight or wrong asymptotics.

**Checklist 5.42:** correct subtraction order; finite moments exist; static targets identified; deviations flagged.

---

## 5.43  Onsager–Casimir Reciprocity (Onsager; Casimir)

**Principle.** With microreversibility, linear response obeys  
\[
G_{ij}(\omega,\mathbf B)=\epsilon_i\epsilon_j\,G_{ji}(\omega,-\mathbf B),
\]
where \(\epsilon\) encodes time‑reversal parity.  
**Shortcut.** Check reciprocity **before** KMS; with \(\mathbf B\neq 0\) use the **Casimir** sign‑flip rule.

**Checklist 5.43:** parities declared; reciprocity respected (or violation explained by symmetry breaking).

---

## 5.44  Thermal Lanes & KMS Symmetry (Kubo–Martin–Schwinger; FDT)

**Principle.** In thermal equilibrium, correlators satisfy **KMS**; **FDT** ties \(\Im G^R\) to symmetrized correlators.  
**Shortcut.** When thermal lock is ON, use KMS/FDT to relate independent response pieces and validate passivity/positivity; classical limit \((\beta\omega\ll1)\) gives \(\Im G^R/\omega \ge 0\).

**Checklist 5.44:** thermal equilibrium assumed (if activated); KMS parity and classical limit recorded.

---

## 5.45  Symmetry Reductions: Spherical, Cylindrical, Planar (Orthogonality; Hankel; Method of Images)

**Principle.** Use symmetry to reduce dimensionality; treat boundaries as **ledger/bundle** data.  
**Shortcuts.**  
- **Spherical:** expand in \(Y_{\ell m}\); static Yukawa \(\to\) radial Bessel ODE per \(\ell\); spherical Hankel for radial transforms.  
- **Cylindrical:** expand in \(e^{im\phi}\) with **Bessel \(J_m\)** radial transforms; reduce to 1D in \(r\) for axially‑symmetric sources.  
- **Planar:** free‑space convolution + images/boundary integrals; no bulk‑kinetic replacement.

**Checklist 5.45:** use only within the stated symmetry sectors; no Coulomb–axial mixing.

---

## 5.46  Sylvester–Cholesky Canonicalization of 1‑Form Sectors (Sylvester; Cholesky; Dirac)

**Principle.** SPD kinetic blocks \(\Leftrightarrow\) decoupled **Maxwell copies** after orthogonal rescaling; residues remain positive.  
**Shortcut.** For mixing matrix \(M_{(1)}\), demand **SPD** (principal minors \(>\!0\)), factor \(M=L\,L^\top\), and work with canonical fields \(\mathbf G=L^\top\mathbf F\).  
**Schur complement (alternate).** If SPD fails, enforce positivity by Schur complements before retrying.

**Checklist 5.46:** minors \(>\!0\); cones unchanged; residues \(+\).

---

## 5.47  Ledger & Ceiling Enforcement (Quantization & No‑DOF Sectors)

**Principle.** Integer‑quantized data (Pontryagin, CS, \(H\)‑flux, \(F_4\), …) are **ledgers**; in 4D, \(p\!\ge\!3\) carries **no local DOF**.  
**Shortcut.** Treat top‑forms as ledger‑only; enforce \(B\leftrightarrow\theta\) **duality guard**, then reduce to a single propagating DOF.

**Checklist 5.47:** integrality preserved; boundary terms never replace bulk kinetic.

---

## 5.48  Worked Micro‑Examples (complete list)

**M5‑1 (Epsilon sanity).** Verify \(\epsilon\)\!–\(\epsilon\) contractions. *(Levi‑Civita)*  
**M5‑2 (Distributional lane).** Show a Fourier multiplier is tempered; regularize an ill‑defined product ledger‑compatibly. *(Schwartz; Paley–Wiener)*  
**M5‑3 (Microlocal legality).** Apply Hörmander’s product/pullback criteria to a projector–source pair. *(Hörmander)*  
**M5‑4 (Wick‑first quadratic).** Euclidean positivity check, then map back. *(Wick; Plancherel)*  
**M5‑5 (Star‑diag 2‑forms).** Build \(H_\pm\), verify eigen‑\(*\). *(Hodge; Cartan)*  
**M5‑6 (BR vs helicity).** Equality of decompositions for a timelike mode. *(Barnes–Rivers; Dirac)*  
**M5‑7 (Hodge–Helmholtz on \(\Sigma_t\)).** Decompose a vector field; identify harmonic (ledger) mode. *(Hodge; Helmholtz)*  
**M5‑8 (Helmholtz–Proca vs Stückelberg).** Two derivations, same resolvent. *(Helmholtz; Proca; Stückelberg)*  
**M5‑9 (Project–inverse commute).** LTI success; hard wall failure → Hadamard/local Fourier. *(Cayley; Hadamard)*  
**M5‑10 (Eikonal rays).** From principal symbol to rays; far‑field phase via stationary phase. *(Hamilton; Jacobi; WKB)*  
**M5‑11 (Hadamard).** Match \(U\,\delta(\sigma)\) to transverse projector–resolvent; estimate \(V\). *(Hadamard; Synge)*  
**M5‑12 (BC uniqueness).** Images vs boundary integrals with equal BCs → same solution. *(Fredholm; Lax–Milgram)*  
**M5‑13 (BC cookbook).** Sommerfeld radiation fixes outgoing Helmholtz solution; compare to retarded Green’s choice. *(Sommerfeld)*  
**M5‑14 (Green–Betti).** Verify reciprocity for a self‑adjoint \(L\) under matched BCs. *(Betti; Green)*  
**M5‑15 (Rellich).** Show the only Sommerfeld‑radiating homogeneous solution is \(u=0\). *(Rellich)*  
**M5‑16 (Energy & flux).** Check the power balance, flux orientation, and ledger entry. *(Poynting; Noether)*  
**M5‑17 (Order‑of‑limits & zero‑modes).** Non‑commuting limits on compact domain. *(Plancherel; Kubo)*  
**M5‑18 (Abel/Tauber).** From \(C(t)\sim t^{-\alpha}\) infer \(G^R(\omega)\sim \omega^{\alpha-1}\). *(Abel; Tauber; Karamata)*  
**M5‑19 (Massless IR).** Keep small \(m\), solve, isolate harmonics, then \(m\!\to\!0^+\); verify DC/passivity. *(IR regulator)*  
**M5‑20 (Bochner).** Check non‑negative spectral measure from positive‑definite \(C(t)\). *(Bochner; Schwarz)*  
**M5‑21 (Herglotz).** Fit positive measure from \(\Im G^R/\omega\); verify DC slope \(\ge 0\). *(Herglotz; Stieltjes)*  
**M5‑22 (Bernstein–Widder).** Show a relaxation kernel is completely monotone and obtain its Stieltjes measure. *(Bernstein; Widder)*  
**M5‑23 (Sokhotski–Plemelj).** Recover \(\Re G^R\) from \(\Im G^R\) via PV/\(\delta\). *(Sokhotski; Plemelj)*  
**M5‑24 (Kramers–Kronig).** Subtracted Hilbert transform check. *(Kramers; Kronig; Titchmarsh)*  
**M5‑25 (Moments/Sum‑rules).** Verify weighted integrals against static targets. *(TRK‑type; Kubo/K–K)*  
**M5‑26 (Onsager–Casimir).** Check reciprocity with declared parities and \(\mathbf B\) flip. *(Onsager; Casimir)*  
**M5‑27 (Cholesky vs Schur).** SPD canonicalization, fallback via Schur. *(Sylvester; Cholesky)*  
**M5‑28 (Nielsen).** Show \(\partial_\xi\Gamma\) is BRST‑exact; verify pole/residue invariance. *(Nielsen; BRST; FP)*  
**M5‑29 (GHY).** Make the boundary variation well‑posed for metric Dirichlet; reconcile ADM‑δ split with flux ledger. *(GHY; ADM)*  
**M5‑30 (Matrix Herglotz).** Check Loewner‑order positivity of a \(2\times2\) response block; relate to scalar constraints. *(Pick; Loewner)*  
**M5‑31 (Källén–Lehmann).** Extract spectral density for a QFT two‑point function and compare to the linear‑response corridor. *(Källén; Lehmann)*

---

## 5.49  Recipes & Viability Bar (use every time)

**R5‑A (Equivalence first).** **Change basis early** (hats/units, epsilon check, **Neumann–Curie**, divergences/EOM, distributional **and microlocal** lanes, Wick‑first, SD/ASD, frames, helicity, Cholesky).  
**R5‑B (Project then solve).** Apply BR/Helmholtz projectors or **Hodge–Helmholtz on \(\Sigma_t\)** before inversion.  
**R5‑C (Scalarize).** Replace vector/tensor inverses with **scalar resolvents** per sector; **commutation lemma** allows project‑first/last in LTI cases.  
**R5‑D (Gauge‑slice).** Cross‑check unitary results against an \(R_\xi\) (or Stückelberg) audit.  
**R5‑D′ (Nielsen).** After gauge‑slice audit, apply **Nielsen** to enforce \(\xi\)‑independence.  
**R5‑E (Hyperbolicity & rays).** Confirm principal symbol Lorentzian & symmetric‑hyperbolic; check cone nesting/front speed; use **eikonal rays** for far‑field.  
**R5‑F (Boundaries).** Fix the homogeneous complement; select a BC from the **cookbook**; verify **Green–Betti**, **Rellich** uniqueness, and **energy/flux** balance.  
**R5‑F′ (Variational).** Before BC uniqueness, assert **GHY/counterterms** and ADM‑δ split.  
**R5‑G (IR & DC).** Isolate **zero‑modes**; enforce \((\mathbf k\!\to\!0)\) then \((\omega\!\to\!0^+)\); apply **Abel/Tauber**; if Coulombic, use the **massless regulator** lane.  
**R5‑H (Response/dispersion).** **Bochner** (PSD \(\ge0\)) → **Herglotz** (positive measure) → **Bernstein–Widder** (CM kernels) → **Sokhotski–Plemelj** → **Kramers–Kronig** (with **subtractions**) → **Moments/Sum‑rules**.  
**R5‑H′ (Matrix).** For multi‑channel systems, enforce **matrix‑Herglotz** (Loewner positivity) before scalar checks.  
**R5‑H″ (Quantum).** If a vacuum QFT channel, use **Källén–Lehmann**.  
**R5‑I (Reciprocity).** If microreversibility applies, enforce **Onsager–Casimir** before KMS.  
**R5‑J (Thermal).** If thermal lock ON, use **KMS/FDT**.  
**R5‑K (Symmetry lanes).** Prefer spherical/cylindrical/planar lanes within scope.  
**R5‑L (Ledger).** Keep top‑forms/integer fluxes ledger‑only; apply duality guards.

**Viability Bar (VB5‑1…VB5‑30).**  
- **VB5‑1:** Chapter‑0 locks intact (signature/Hodge/Wick; hats/dimensions consistent).  
- **VB5‑2:** Epsilon sanity checks pass.  
- **VB5‑3:** **Neumann–Curie** invariants enforced; forbidden couplings absent.  
- **VB5‑4:** **Distributional lane** respected (tempered, legal transforms/limits).  
- **VB5‑5:** **Microlocal** product/pullback legality satisfied (or regularized).  
- **VB5‑6:** On‑shell divergence/EOM drops only affect ledgers/boundaries.  
- **VB5‑7:** Projector residues \(>\!0\) (spin‑by‑spin).  
- **VB5‑8:** **Gauge‑slice audit**: residues/poles \(\xi\)-independent (or Stückelberg‑consistent).  
- **VB5‑9:** **Nielsen**/BRST audit passes (physical poles/residues \(\xi\)-independent).  
- **VB5‑10:** Principal symbol Lorentzian; symmetric‑hyperbolic energy estimate.  
- **VB5‑11:** Front speed \(=1\); cone nesting OK; **eikonal rays** consistent.  
- **VB5‑12:** **Variational boundary** well‑posed (GHY/counterterms; ADM‑δ).  
- **VB5‑13:** **BC uniqueness** resolved; cookbook BC chosen; homogeneous complement fixed.  
- **VB5‑14:** **Green–Betti** reciprocity holds (matched BC pairings).  
- **VB5‑15:** **Rellich** uniqueness satisfied for radiation problems.  
- **VB5‑16:** **Energy/flux** balance consistent; dissipation \(\ge 0\); ledger matches boundary work.  
- **VB5‑17:** **Zero‑modes isolated**; DC order \((\mathbf k\!\to\!0)\) then \((\omega\!\to\!0^+)\).  
- **VB5‑18:** **Abel/Tauber** consistency between tails and small‑\(\omega\).  
- **VB5‑19:** **Massless regulator** limit safe and documented.  
- **VB5‑20:** **Bochner** spectral non‑negativity satisfied.  
- **VB5‑21:** **Herglotz** measure positive; DC slope non‑negative.  
- **VB5‑22:** **Matrix Herglotz/Loewner** positivity satisfied (or violation explained).  
- **VB5‑23:** **Källén–Lehmann** positivity/support satisfied when applicable.  
- **VB5‑24:** **Bernstein–Widder** complete monotonicity (if relaxation kernel).  
- **VB5‑25:** **Sokhotski–Plemelj** signs correct; PV/\(\delta\) handled distributionally.  
- **VB5‑26:** **Kramers–Kronig** (subtracted) holds; Schwarz reflection obeyed.  
- **VB5‑27:** **Moments/Sum‑rules** satisfied (with correct subtractions).  
- **VB5‑28:** **Onsager–Casimir** holds (or justified violation).  
- **VB5‑29:** 1‑form mixing SPD or Schur‑repaired; Maxwell cones after Cholesky.  
- **VB5‑30:** Ledgers preserved; boundary terms never replace bulk kinetic.

---

## 5.50  Stops → Sections (audit map)

S‑ET → §5.1–§5.2–§5.9–§5.10–§5.14–§5.17–§5.46–§5.47  
**S‑SYM** → §5.5 **S‑DIST** → §5.7 **S‑MICRO** → §5.8  
S‑UG → §5.19 **S‑NI** → §5.20  
S‑EM/S‑SHYP → §5.21–§5.22 **S‑EIK** → §5.23  
**S‑GHY** → §5.25 **S‑BC** → §5.26–§5.27 **S‑REC** → §5.28 **S‑RAD** → §5.29 **S‑EN** → §5.30  
S‑ZM → §5.31  
S‑P/S‑PB/S‑SUB → §5.32–§5.36–§5.40–§5.41  
**S‑MAT** → §5.37 **S‑KL** → §5.38 **S‑SUM** → §5.42 **S‑ONS** → §5.43 **S‑KMS** → §5.44  
S‑BNDL/S‑CHAR/S‑TOPPOS → §5.32–§5.45–§5.47.

---

## 5.51  Ordering Audit (Iteration 14)

**Least→most dependent chain:**  
(5.1 Equivalence) → (5.2 Hats) → (5.3 Grassmann–Cartan) → (5.4 Epsilon) → (5.5 Neumann–Curie) → (5.6 Divergences) → (5.7 Distributional) → (5.8 Microlocal) → (5.9 Wick) → (5.10 Star‑diag) → (5.11 Frames) → (5.12 Gauss) → (5.13 BR) → (5.14 Helicity) → (5.15 Hodge–Helmholtz) → (5.16 Helmholtz–Proca) → (5.17 Project–inverse) → (5.18 Rank‑2) → (5.19 Gauge‑slice) → (5.20 Nielsen) → (5.21 Principal symbol) → (5.22 Cone/front) → (5.23 Eikonal) → (5.24 Hadamard) → (5.25 Variational boundary/GHY) → (5.26 BC uniqueness) → (5.27 BC cookbook) → (5.28 Green–Betti) → (5.29 Rellich) → (5.30 Energy/flux) → (5.31 Order‑of‑limits) → (5.32 Plancherel–Kubo) → (5.33 Abel/Tauber) → (5.34 Massless IR) → (5.35 Bochner) → (5.36 Herglotz scalar) → (5.37 Matrix Herglotz) → (5.38 Källén–Lehmann) → (5.39 Bernstein–Widder) → (5.40 S–P) → (5.41 K–K) → (5.42 Moments) → (5.43 Onsager) → (5.44 KMS) → (5.45 Symmetry lanes) → (5.46 Cholesky) → (5.47 Ledger).  
All dependencies flow forward; **microlocal legality** precedes distribution manipulations; the **variational/BC corridor** is: Hadamard → Variational → Uniqueness → Cookbook → Reciprocity → Rellich → Energy/Flux; the **dispersion corridor** is: Bochner → Herglotz (scalar) → Matrix Herglotz → Källén–Lehmann → Bernstein–Widder → S–P → K–K → Moments.

---

## 5.52  One‑Page Wall Card (at a glance)

- **Equivalence & hats:** local invertible basis changes; dimensionless normalization.  
- **Epsilon → Neumann–Curie → Divergences/EOM → Distributional → Microlocal → Wick:** prune by symmetry, drop total derivatives/EOM terms, ensure tempered **and** wavefront legality, then Euclidean checks.  
- **Star‑diag / frames / Gauss:** local algebra simplified; reuse derivatives.  
- **Project then solve / helicity / spatial Hodge–Helmholtz:** decompose first; projector–inverse commutes (LTI only).  
- **Gauge:** unitary vs \(R_\xi\) must agree; **Nielsen** enforces \(\xi\)‑independence of poles/residues.  
- **Causality:** principal symbol symmetric‑hyperbolic; **front speed = 1**; **eikonal rays**; cones nested.  
- **Curved space & boundaries:** Hadamard cone + tail; **variational well‑posedness (GHY/ADM)** → **BC uniqueness** → **cookbook** → **Green–Betti** → **Rellich** → **energy/flux**.  
- **IR & response:** zero‑modes isolated; DC order fixed; **Kubo → Abel/Tauber → massless regulator**.  
- **Dispersion (multi‑channel & quantum):** **Bochner** (PSD) → **Herglotz** (scalar) → **Matrix Herglotz** (Loewner) → **Källén–Lehmann** (if quantum) → **Bernstein–Widder** (time‑domain CM) → **Sokhotski–Plemelj** → **Kramers–Kronig** (with subtractions) → **moments/sum‑rules**.  
- **Reciprocity & thermal:** **Onsager–Casimir** (if microreversible), then **KMS/FDT** (if thermal).  
- **Symmetry lanes:** spherical / cylindrical / planar.  
- **Canonize once:** SPD ⇒ Cholesky ⇒ Maxwell copies; cones unchanged.  
- **Ledger ceiling:** \(p\ge3\) in 4D = ledger‑only; duality guard enforced.
