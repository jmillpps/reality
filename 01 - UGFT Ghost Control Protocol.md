# Chapter 1 — Ghost Control Protocol (Diagnostics, Avoidance, Re‑bounding)

> **Scope.** Operational framework to **detect**, **avoid**, and **re‑bound** ghosts (negative‑energy or negative‑norm modes), tachyons, and gradient instabilities across quantum, gravitational, and cosmological regimes in UGFT.  
> **Operating system.** All Chapter‑0 locks are in force at all times: signature \((-,+,+,+)\), epsilon/Hodge, explicit couplings, trace conventions, ADM measures and \(\delta\), Wick map, response/Kubo normalization, Barnes–Rivers projectors, Larin \(\gamma^5\), integer ledgers, units/hats.  
> **Governance.** Any deviation requires (i) justification, (ii) a worked micro‑example, and (iii) check‑list updates across affected locks.

---

## C1.0  R1 Header — Universal Conventions (declare before any test)

- **Signature & orientation:** \((-,+,+,+)\); \(\epsilon_{0123}=+\sqrt{|g|}\); \(\epsilon^{0123}=+1/\sqrt{|g|}\).  
  Contraction test: \(\epsilon^{\mu\nu\rho\sigma}\epsilon_{\alpha\nu\rho\sigma}=-3!\,\delta^\mu{}_\alpha\).
- **Hodge:** \( *^2=(-1)^{p(4-p)+1}\) (Lorentzian); after Wick, \((*_E)^2=(-1)^p\).  
- **Traces & couplings:** \(\mathrm{Tr}(T^A T^B)=\delta^{AB}\); \(F=dA+gA\wedge A\); \(D_\mu=\partial_\mu+igA_\mu\).  
  **Ledger note:** record any trace/level rescaling when importing external conventions.
- **Measures & ADM‐\(\delta\):** \(\sqrt{|g|}=N\sqrt{\gamma}\); \(\delta_g^{(4)}=\delta(t-t_0)\delta^{(3)}_\gamma/N\).
- **Fourier/response/Kubo:** phase \(e^{i(\omega t-\mathbf k\cdot\mathbf x)}\); retarded \(G^R=-i\Theta(t)\langle[A(t),B(0)]\rangle\); \(\rho=-2\Im G^R\); \(\sigma_{DC}=\lim_{\omega\to0^+}\Im G^R_{JJ}(\omega,0)/\omega\).
- **Wick map:** \(t\to -i\tau\); \(e^0_{(E)}=i e^0,\ e^i_{(E)}=e^i\); \(g^{(E)}_{00}=-g_{00}\); **ledgers unchanged**.  
  **Finite‑T (Matsubara):** periodic/anti‑periodic BCs; maintain reflection positivity and KMS.
- **Projectors/Stückelberg:** massive spin‑1  
  \(\sum_{\lambda=1}^3 \epsilon^\mu_{(\lambda)}\epsilon^\nu_{(\lambda)}=g^{\mu\nu}+p^\mu p^\nu/m^2\) ⇒ rest projector \({\rm diag}(0,1,1,1)\); use Stückelberg to expose longitudinal mode.
- **\(\gamma^5\) policy:** Larin scheme for loop work in axial sectors.

---

## C1.1  Definitions and taxonomy

- **Ghost (dynamical):** propagating DOF with negative kinetic energy (wrong sign in quadratic kinetic form) ⇒ Hamiltonian unbounded below; equivalently, negative residue at a physical pole.  
- **Tachyon:** correct kinetic sign but \(m^2<0\); background instability (not a ghost).  
- **Gradient instability:** correct time‑kinetic sign but wrong gradient sign ⇒ \(c_s^2<0\).  
- **Ostrogradsky ghost:** from non‑degenerate higher‑time‑derivative Lagrangians.  
- **FP/BRST ghosts:** auxiliary Grassmann fields of gauge fixing; not physical in BRST cohomology.

---

## C1.2  Quadratic analysis (minimal testbed)

Expand about a background:
\[
\mathcal L^{(2)}=\tfrac12 \dot{\Phi}^\top \mathbf K\,\dot{\Phi}
-\tfrac12 (\nabla\Phi)^\top \mathbf G\,(\nabla\Phi)
-\tfrac12 \Phi^\top \mathbf M^2\,\Phi
+ \text{(mixing)}.
\]
**Ghost‑free:** \(\mathbf K>0\) on the physical subspace (after constraints).  
**No gradient instability:** \(\mathbf G>0\).  
**No tachyon:** eigenvalues of \(\mathbf M^2\ge 0\) (unless controlled).  
**Residues:** positive at each physical pole after projection.

### C1.2a  Hessian/DOF rank test
Time‑derivative Hessian \(\mathcal H_{ab}=\partial^2\mathcal L^{(2)}/(\partial \dot\Phi_a \partial \dot\Phi_b)\) after constraint solving:  
□ \(\mathrm{rank}\,\mathcal H=N_{\rm DOF}\); □ all non‑zero eigenvalues \(>0\).  
**Stop S‑H** on failure.

### C1.2b  Constraint algebra closure (Dirac)
Run the Dirac–Bergmann algorithm: primary → secondary (→ tertiary) constraints; require closure under time evolution.  
**Stop S‑C** if algebra fails to close or DOF count changes.

### C1.2c  Symplectic 2‑form positivity
Build the canonical (or covariant) symplectic 2‑form \(\Omega\) on the **reduced** phase space; require \(\Omega\) positive‑definite on physical directions.  
**Stop S‑SP** if \(\Omega\) has negative directions.

### C1.2d  Zero‑mode / IR sentinel
On compact spatial sections or with gauge zero‑modes, isolate and treat zero‑modes separately; ensure no spurious negative directions arise in the \(k\to 0\) sector.  
**Stop S‑ZM** if zero‑mode handling alters DOF count or yields negative kinetic energy.

### C1.2e  Equivalence theorem / basis independence
Kinetic positivity and residue signs must be invariant under **invertible local field redefinitions** (equivalence theorem).  
**Stop S‑ET** if ghost/health conclusions depend on field basis.

### C1.2f  Initial‑data compatibility
Chosen initial data must satisfy all primary/secondary constraints (Gauss, diffeo, torsion) and Chapter‑0 ADM/Hodge conventions; inconsistent initial data must not be mistaken for ghosts.  
**Stop S‑ID** on violation.

---

## C1.3  Projectors & polarization

- **BR (rank‑2):** use \(P^{(2)},P^{(1)},P^{(0s)},P^{(0w)}\) (from \(\theta_{\mu\nu},\omega_{\mu\nu}\)); test residues per spin.  
- **Vectors:** Stückelberg \(A_\mu=\hat A_\mu+\partial_\mu\pi/m\), \(\partial\!\cdot\!\hat A=0\); both \(\hat A,\pi\) must be healthy.  
- **Spin‑2:** Pauli–Fierz mass at quadratic order; otherwise reject.

### C1.3a  Strong‑coupling sentry (longitudinal)
With Stückelberg \(S_\mu=\hat S_\mu+\partial_\mu\pi/m_S\), normalize \(\pi_c=m_S\pi\).  
Require EFT domain \(E\le\Lambda \ll 4\pi m_S/g_S\).  
**Stop S‑SC** on violation.

### C1.3b  Field‑space metric positiveness
In the reduced field basis, the kinetic metric \(K_{ab}\) must be **Riemannian** (positive‑definite).  
**Stop S‑FM** if any negative kinetic eigenvalue appears after reduction/redefinition.

### C1.3c  Unitary‑gauge audit
Do not certify health in **unitary gauge alone**; cross‑check residues/positivity in an \(R_\xi\) gauge.  
**Stop S‑UG** if conclusions change across gauges after proper reduction.

### C1.3d  Schur‑complement positivity (mixing hygiene)
For a block kinetic matrix \(K=\begin{pmatrix}A & B\\ B^\top & C\end{pmatrix}\), require \(A>0\) and the Schur complement \(C-B^\top A^{-1}B>0\) (or vice versa).  
**Stop S‑SCHUR** if any leading principal minor or Schur complement is non‑positive.

### C1.3e  Polarization normalization & completeness
After projector tests, verify on‑shell **normalization** and **completeness relations** for physical polarizations; disallow hidden negative‑norm normalizations.  
**Stop S‑POL** on violation.

---

## C1.4  Gauge fixing, BRST & physical Hilbert space

- FP ghosts are auxiliary; physical states are BRST‑closed modulo exact.  
- **Gauge‑parameter independence:** residues and pole masses of physical states are \(\xi\)‑independent; residual \(\xi\)‑dependence indicates incomplete reduction.

### C1.4a  Anomaly/longitudinal sourcing audit
If \(\nabla_\mu J_5^\mu \neq 0\): \(\nabla\!\cdot\!S=(g_S/m_S^2)\,\nabla\!\cdot\!J_5\) remains algebraic.  
Checklist: □ no induced \(\dot\pi^2\); □ no sign flip in \(\pi_c\); □ sources ledgered only.  
**Stop S‑A** on violation.

### C1.4b  FP operator / Gribov sentinel
In the chosen gauge and background, verify the Faddeev–Popov operator has no zero modes; otherwise restrict to a region free of Gribov copies to maintain a positive FP measure.  
**Stop S‑GRZ** if FP zero modes or sign‑indefinite FP determinant are present.

### C1.4c  Slavnov–Taylor / algebraic renormalization
Preserve BRST symmetry and Slavnov–Taylor identities under renormalization. Any anomaly must be ledgered and must **not** induce negative‑metric propagation.  
**Stop S‑ST** if ST identities fail in the renormalized theory.

### C1.4d  BRST cohomology dimension check
The dimension of the physical BRST cohomology (per momentum mode) equals the constrained DOF count; forbid negative‑norm representatives in nontrivial cohomology classes.  
**Stop S‑COH** on mismatch or negative‑norm cohomology.

---

## C1.5  Higher derivatives and the Ostrogradsky gate

Forbid **non‑degenerate** higher‑time‑derivative operators. Use:  
- **Auxiliary‑field cure** — rewrite higher derivatives with auxiliaries; require positive kinetic block if auxiliaries propagate.  
- **Degenerate structure** — enforce algebraic degeneracy so the extra would‑be mode is constrained.

### C1.5a  Degenerate structure (allowable non‑minimal terms)
Construct time‑derivative block \(K_{ab}(\partial_t)\); enforce \(\det K_{ab}=0\) to remove Ostrogradsky mode; check reduced eigenvalues \(>0\).  
**Stop S‑D** if degeneracy fails or reduced Hessian indefinite.

### C1.5b  Non‑local kernels (integrate‑out)
Non‑local quadratic kernels (memory) from integrating out heavy fields must admit a positive spectral representation; no negative‑weight contributions.  
**Stop S‑NL** if spectral positivity fails.

---

## C1.6  Curved backgrounds: hyperbolicity, energy & frames

- **Principal symbol:** strong **hyperbolicity** on globally‑hyperbolic backgrounds.  
- **Microcausality:** retarded support only.  
- **Subluminality:** \(0<c_s^2\le 1\) in local orthonormal frames; **front‑velocity sentinel:** high‑frequency limit yields \(v_{\rm front}=1\).  
- **Energy functional:** free Hamiltonian bounded below on the physical subspace.

### C1.6a  Boundary variational principle (ADM)
Include GHY + required counterterms for non‑minimal couplings; boundary variation must be well‑posed; constraints stable.  
**Stop S‑B** on failure.

### C1.6b  Cosmological backgrounds
For FRW reductions with torsion algebraic: spin‑stiff \(\rho_{\rm spin}\propto a^{-6}\). Re‑evaluate \(\mathbf K,\mathbf G\), \(c_s^2\) on the evolving background to exclude transient gradient instabilities.

### C1.6c  Boundary conditions sentry
Dirichlet/Neumann/mixed BCs must not reintroduce boundary ghosts; boundary energy flux non‑negative.  
**Stop S‑BC** on violation.

### C1.6d  Effective Planck mass & frame‑invariance
For non‑minimal curvature couplings or Weyl/conformal redefinitions, require **positive effective Einstein–Hilbert coefficient** \(M_*^2>0\) and no kinetic sign flips under frame changes.  
**Stop S‑MP** if \(M_*^2\le 0\) or a sign inversion appears after transformation.

### C1.6e  Nonlinear constraint persistence
Extend the constraint analysis one order beyond quadratic; verify no re‑emergent ghost DOF.  
**Stop S‑NLc** if the nonlinear constraint algebra fails or new DOF appear.

### C1.6f  Effective metric for perturbations
For media/EFTs with field‑dependent kinetic structures (e.g., \(P(X)\), k‑essence), perturbations propagate on an **effective metric** \(\mathcal G^{\mu\nu}\). Require Lorentzian signature \((-,+,+,+)\), \(\mathcal G^{00}<0\), and causal cones inside or coincident with \(g^{\mu\nu}\).  
**Stop S‑EM** if \(\mathcal G^{\mu\nu}\) is non‑Lorentzian or superluminal in the front‑velocity limit.

### C1.6g  Corner/edge‑mode sentinel
When boundaries have corners, include corner terms and edge‑mode contributions. Require that no edge mode acquires a negative kinetic term and that canonical charges remain bounded below.  
**Stop S‑CT** on violation.

### C1.6h  Horizon/Killing‑energy sentinel
On stationary spacetimes with timelike Killing vector \(\xi^\mu\), define canonical energy \(E=\int_\Sigma \sqrt{\gamma}\,T_{\mu\nu}\,\xi^\mu n^\nu\). Impose ingoing‑horizon BCs and require non‑negative net energy flux; do not confuse superradiant growth with ghosts.  
**Stop S‑HOR** if horizon BCs or energy flux create negative‑energy propagation.

### C1.6i  Symmetric‑hyperbolic energy estimate
Whenever possible, cast equations in **symmetric‑hyperbolic** form and supply an energy estimate; this controls well‑posedness beyond principal symbol tests.  
**Stop S‑SHYP** if no energy estimate exists or growth violates the bound.

---

## C1.7  Positivity/analyticity and forward constraints

- **Spectral positivity:** Källén–Lehmann non‑negative ⇒ residues \(\ge 0\).  
- **Retarded analyticity:** no UHP poles/cuts; passivity \(\Im G^R(\omega,0)/\omega\ge 0\) for \(\omega>0\).

### C1.7a  Forward‑limit positivity (EFT)
Use dispersion relations in the forward limit (\(t\to 0\)) to constrain Wilson coefficients; parity‑odd pieces must not generate negative absorptive parts.  
**Stop S‑P** on violation.

### C1.7b  Sum‑rule sentry
Implement f‑/moment sum‑rules as global checks (e.g., \(\int_0^\infty \rho(\omega)\,\omega^{-1} d\omega \ge 0\) under standard assumptions).  
**Stop S‑SR** on violation.

### C1.7c  Subtracted positivity with massless exchange
In the presence of massless exchanges (e.g., gravity), use appropriately **subtracted** dispersion relations; apply derivative positivity bounds that remain valid after subtraction.  
**Stop S‑SUB** on violation.

### C1.7d  Cutkosky / optical‑theorem sentinel
Across physical cuts, the discontinuity \(\mathrm{Disc}\,\mathcal M\) must match a sum over **positive** on‑shell phase‑space integrals (Cutkosky).  
**Stop S‑CUT** if any cut contribution is negative or gauge‑variant for physical external states.

### C1.7e  Spectral‑matrix positivity
For any operator set \(\{O_i\}\), the spectral density matrix \(\rho_{ij}(\omega,\mathbf k)\) must be positive‑semidefinite for \(\omega>0\). Test with random linear combinations \(v_i O_i\).  
**Stop S‑MAT** if \(\sum_{ij} v_i^* \rho_{ij} v_j < 0\) for any \(v\).

### C1.7f  Dispersion preconditions (polynomial boundedness)
Before applying dispersion/positivity bounds, verify polynomial boundedness (or supply adequate subtractions) so dispersion integrals converge; otherwise use subtracted/weighted sum‑rules.  
**Stop S‑PB** if preconditions fail.

### C1.7g  KMS / thermal passivity sentinel
At finite \(T\), enforce KMS \(G^>(t)=G^<(t+i\beta)\) and positivity of thermal spectral densities; heat‑bath passivity forbids negative‑work cycles.  
**Stop S‑KMS** on violation.

---

## C1.8  Radiative stability (RG)

- **Wave‑function renormalization:** \(Z>0\) after canonical normalization.  
- **Running masses/couplings:** \(m^2(\mu)>0\) and kinetic eigenvalues \(>0\) across the RG domain; healthy region is an **open set**.  
- **Axial loops:** use Larin \(\gamma^5\).

### C1.8a  Gauge‑parameter sentinel (Nielsen)
Physical pole masses/residues are \(\xi\)‑independent (Nielsen identity).  
**Stop S‑NI** on violation.

### C1.8b  Regulator/regularization sentinel
Forbid regulators that introduce **propagating negative‑metric states** in the EFT regime (e.g., finite‑mass PV ghosts or ad‑hoc higher‑derivative regulators). If used formally, regulator poles must remain parametrically above the UV cutoff and never be treated as dynamical.  
**Stop S‑REG** on violation.

### C1.8c  Scheme‑independence of sign
Finite counterterms must preserve R1 kinetic‑sign locks; no renormalization scheme or field‑redefinition convention may flip an allowed kinetic sign or induce \(Z<0\).  
**Stop S‑SCHEME** on violation.

---

## C1.9  Constructive patterns (avoidance & re‑bounding)

- **Sentinel kinetic forms:**  
  Scalar \(-\tfrac12(\partial\phi)^2 - V(\phi)\); Vector \(-\tfrac14F^2+\tfrac12 m^2 A^2\); Axial torsion \(-\tfrac14H^2+\tfrac12 m_S^2 S^2 - g_S S\!\cdot\!J_5\).  
- **Auxiliary‑field rehabilitation:** rewrite higher derivatives; require positive kinetic block for auxiliaries if dynamical.  
- **Constraint promotion:** use Stückelberg or Lagrange multipliers to eliminate dangerous DOF.  
- **EFT demarcation:** keep any would‑be ghost mass \(\gg\Lambda\); never compute for \(E\gtrsim\Lambda\).  
- **Equivalence theorem:** local field redefinitions preserve S‑matrix and health conclusions.  
- **Forbidden cures:** indefinite‑metric (Lee–Wick) prescriptions disallowed.

---

## C1.10  Topological‑gauge ledger & fibration sentinels

1) **Bundle‑class sentinel (Stop S‑BNDL).** Configuration defines a **well‑posed principal (or gerbe) bundle** on \(M\) with consistent gluing on overlaps; connections agree modulo gauge on triple overlaps. **Abort** if the atlas is inconsistent.  
2) **Characteristic‑class integrality (Stop S‑CHAR).** All ledger integrals (Chern, Pontryagin, Hopf, gerbe \(\int H\), etc.) yield **integers** at the stated normalization/trace; CS/gravitational levels are integers. **Abort** on any integer‑ledger failure.  
3) **Topological‑term positivity (Stop S‑TOPPOS).** Topological terms may shift energy by a boundary (Bogomolny), but must not supply a **bulk kinetic** term with wrong sign. Energy written as “sum of squares \(\pm\) topological bound.” **Abort** if a topological term acts like negative kinetic energy.  
4) **Fibration consistency (Stop S‑FIB).** If a fibration (e.g., Hopf) parameterizes a field, energy density is **chart‑independent** and gluing does not create **edge modes** with negative energy. **Abort** if energy is not invariant under changes of trivialization.  
5) **Higher‑form gauge positivity (Stop S‑HFORM).** For 2‑form/gerbe sectors, the 3‑form curvature \(H\) appears with a **positive** quadratic energy (if dynamical) or is **ledger‑only** (if purely topological). **Abort** if any higher‑form kinetic term has wrong sign.  
6) **Causal/time “\(c\)‑gauge” normalization (Stop S‑CG).** If a causal/time gauge is introduced, constraints (i) preserve Chapter‑0 cones, (ii) fix negative temporal normalizations as **pure gauge**, and (iii) do **not** create a propagating scalar with negative kinetic sign. **Abort** on any violation.  
7) **Hopfion energy bound (Stop S‑HOPF).** For Hopf/knotted sectors, supply a lower‑bound functional (Skyrme‑type) so energy is bounded below by \(\alpha |Q_H|\); no negative directions at fixed \(Q_H\). **Abort** if the functional allows indefinite energy.

---

## C1.A  Worked exemplars

**A1 Scalar:** \(\mathcal L=-\tfrac12(\partial\phi)^2-\tfrac12 m^2\phi^2\) ⇒ kinetic \(>0\), residue \(>0\).  
**Anti‑pattern:** overall sign flip ⇒ ghost.

**A2 Proca:** \(\mathcal L=-\tfrac14F^2+\tfrac12 m^2 A^2\). Stückelberg shows healthy longitudinal; three positive residues.

**A3 Higher‑derivative toy:** \(\mathcal L=-\tfrac12(\partial\phi)^2-\tfrac{1}{2\Lambda^2}(\Box\phi)^2\) ⇒ Ostrogradsky.  
**Cures:** auxiliary rewrite + positive kinetic block; or EFT with \(\Lambda\ll M_g\).

**A4 \(P(X)\) rule:** with \(X=-\tfrac12(\partial\phi)^2\): require \(P_X>0\), \(c_s^2=P_X/(P_X+2XP_{XX})>0\).

---

## C1.B  UGFT axial torsion (P1) — one‑page health audit

**Action:** \(\mathcal L_S=-\tfrac14H^2+\tfrac12 m_S^2 S^2 - g_S S\!\cdot\!J_5\).  
**EOM:** \(\nabla_\nu H^{\nu\mu}+m_S^2 S^\mu=g_S J_5^\mu\); \(\nabla\!\cdot\!S=(g_S/m_S^2)\nabla\!\cdot\!J_5\).  
**Kinetic sign:** matches YM; Proca projector ⇒ rest diag \((0,1,1,1)\).  
**Residues:** positive for \(m_S^2>0\).  
**Microcausality:** retarded support; static Yukawa \(e^{-m_S r}/(4\pi r)\).  
**EC limit:** integrate out \(S_\mu\Rightarrow \Delta\mathcal L_{\rm eff}=-(g_S^2/2m_S^2)J_5^2+\mathcal O(\partial^2/m_S^4)\).  
**Massless‑axial caveat:** \(m_S\to0\) allowed only if \(\nabla\!\cdot\!J_5=0\).

---

## C1.C  Ghost‑check pipeline (deterministic, with stops)

1. **R1 header** (C1.0) — log locks.  
2. **Quadratic extraction** (C1.2) — build \(\mathbf K,\mathbf G,\mathbf M^2\).  
3. **Hessian/DOF** (C1.2a) — rank/positivity. **Stop S‑H.**  
4. **Constraint closure** (C1.2b) — Dirac algebra closes. **Stop S‑C.**  
5. **Symplectic positivity** (C1.2c) — \(\Omega>0\). **Stop S‑SP.**  
6. **Zero‑modes / IR** (C1.2d) — handle \(k\to 0\) sector. **Stop S‑ZM.**  
7. **Equivalence theorem** (C1.2e) — basis‑independent conclusions. **Stop S‑ET.**  
8. **Initial data** (C1.2f) — constraint‑compatible data. **Stop S‑ID.**  
9. **Gauge/constraints** (C1.4) — eliminate non‑propagating vars; check \(\xi\)‑independence.  
10. **Degeneracy** (C1.5a) — higher‑derivatives non‑propagating. **Stop S‑D.**  
11. **Field‑metric** (C1.3b) — \(K_{ab}>0\). **Stop S‑FM.**  
12. **Unitary‑gauge audit** (C1.3c) — cross‑check in \(R_\xi\). **Stop S‑UG.**  
13. **Schur complement** (C1.3d) — mixing block positivity. **Stop S‑SCHUR.**  
14. **Polarization norm** (C1.3e) — normalization/completeness. **Stop S‑POL.**  
15. **Projector residues** (C1.3) — per‑spin residues \(>0\); \(q\) not propagated.  
16. **Dispersion/causality** (C1.6) — hyperbolic; \(0<c_s^2\le 1\); \(v_{\rm front}=1\); retarded.  
17. **Anomaly sourcing** (C1.4a) — longitudinal algebraic & healthy. **Stop S‑A.**  
18. **Gribov/FP** (C1.4b) — no FP zero modes; measure positive. **Stop S‑GRZ.**  
19. **Boundary variation** (C1.6a) — well‑posed; constraints stable. **Stop S‑B.**  
20. **Boundary conditions** (C1.6c) — no boundary ghosts. **Stop S‑BC.**  
21. **Planck mass / frames** (C1.6d) — \(M_*^2>0\); no frame‑flip of signs. **Stop S‑MP.**  
22. **Nonlinear constraints** (C1.6e) — no DOF re‑entry. **Stop S‑NLc.**  
23. **Effective metric** (C1.6f) — Lorentzian \(\mathcal G^{\mu\nu}\), cone nesting OK. **Stop S‑EM.**  
24. **Corner/edge modes** (C1.6g) — no negative kinetic edges. **Stop S‑CT.**  
25. **Horizon/Killing energy** (C1.6h) — BCs and flux OK. **Stop S‑HOR.**  
26. **Symmetric‑hyperbolic** (C1.6i) — energy estimate OK. **Stop S‑SHYP.**  
27. **Bundle class** (C1.10) — well‑posed bundle/gerbe. **Stop S‑BNDL.**  
28. **Characteristic integrality** (C1.10) — integers/levels OK. **Stop S‑CHAR.**  
29. **Topological‑term positivity** (C1.10) — no negative kinetic from topology. **Stop S‑TOPPOS.**  
30. **Fibration consistency** (C1.10) — chart‑independent energy. **Stop S‑FIB.**  
31. **Higher‑form positivity** (C1.10) — \(H\) kinetic OK / ledger‑only. **Stop S‑HFORM.**  
32. **Causal “\(c\)‑gauge”** (C1.10) — constraints OK; no new ghost. **Stop S‑CG.**  
33. **Hopfion bound** (C1.10) — energy \(\ge \alpha |Q_H|\). **Stop S‑HOPF.**  
34. **Non‑local kernels** (C1.5b) — spectral positivity. **Stop S‑NL.**  
35. **Forward positivity** (C1.7a) — EFT Wilsons pass. **Stop S‑P.**  
36. **Sum‑rules** (C1.7b) — integrated positivity. **Stop S‑SR.**  
37. **Subtracted positivity** (C1.7c) — massless exchange OK. **Stop S‑SUB.**  
38. **Cutkosky** (C1.7d) — positive cuts. **Stop S‑CUT.**  
39. **Spectral matrix** (C1.7e) — PSD \(\rho_{ij}\). **Stop S‑MAT.**  
40. **Dispersion preconditions** (C1.7f) — polynomially bounded / subtractions. **Stop S‑PB.**  
41. **KMS / thermal** (C1.7g) — finite‑T passivity & KMS. **Stop S‑KMS.**  
42. **RG guardrails** (C1.8, C1.8a, C1.8b, C1.8c) — \(Z>0\), \(m^2(\mu)>0\), Nielsen OK, regulator OK, **scheme OK**. **Stops S‑NI/S‑REG/S‑SCHEME.**  
43. **Report** — *Healthy* only if all stops pass.

---

## C1.D  Sentinel vs anti‑patterns

**Adopt:** Scalar \(-\tfrac12(\partial\phi)^2 - V\); Vector \(-\tfrac14F^2+\tfrac12 m^2A^2\); Axial torsion \(-\tfrac14H^2+\tfrac12 m_S^2 S^2\).  
**Reject/sequester:** sign‑flipped kinetics; non‑degenerate \((\partial_t^2\Phi)^2\); non‑PF mass terms; regulators with propagating negative‑metric states in EFT domain; schemes that flip \(Z\) signs.

---

## C1.E  Notes on re‑bounding unboundedness

- **Constraint‑by‑design** (Stückelberg/Lagrange multipliers).  
- **Field redefinitions** (equivalence theorem) to diagonalize \(K\); check positivity after canonical normalization.  
- **EFT demarcation**: keep \(\Lambda\) below any would‑be ghost pole; never compute beyond \(\Lambda\).  
- **UV completion**: prefer unitary completions with non‑negative spectral densities; forward positivity then automatic.

---

## C1.F  Quick reference (copy‑paste formulas)

- **Massive spin‑1 propagator (unitary gauge):**
  \[
  D_{\mu\nu}(k)=\frac{-\,g_{\mu\nu}+\dfrac{k_\mu k_\nu}{m^2}}{k^2-m^2+i0^+},\qquad
  k^2=-\omega^2+\mathbf k^2.
  \]
- **Retarded scalar kernel (3+1D):**
  \[
  G^R(t,r)=\frac{\Theta(t)}{4\pi r}\Big[\delta(t-r)-m\,\frac{J_1\!\big(m\sqrt{t^2-r^2}\big)}{\sqrt{t^2-r^2}}\,\Theta(t-r)\Big].
  \]
- **Static Yukawa:** \(G(\mathbf r)=-(4\pi r)^{-1}e^{-mr}\).  
- **Spherical \(\delta\):** \(\nabla^2(1/r)=-4\pi\,\delta^{(3)}(\mathbf r)\), \(\delta^{(3)}(\mathbf r)=\delta(r)/(4\pi r^2)\).
- **Effective metric (k‑essence exemplar):** \(\mathcal G^{\mu\nu}=P_X g^{\mu\nu}-P_{XX}\,\partial^\mu\phi\,\partial^\nu\phi\); require Lorentzian signature and correct cone nesting.

---
