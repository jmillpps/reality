# Chapter 3 — Redundant Gauge Uplift Protocol (Fully Audited, Current)

> **Scope.** Chapter 3 promotes non‑observable normalizations and constants to **redundant gauge degrees of freedom** with explicit compensators, higher‑form structure, and **ledger** bookkeeping. It enforces the **Chapter‑1 Ghost‑Health Protocol** (Stops) under **Chapter‑0 OS** locks (signature, epsilon/Hodge, traces, ADM‑δ, Wick map, response order, **Larin γ⁵**, integer ledgers).

---

### 3.0  R1 Header (Imports & Locks)

- **Signature & Hodge.** \((-,+,+,+)\); \(\epsilon_{0123}=+\sqrt{|g|}\) and \(\epsilon^{0123}=+1/\sqrt{|g|}\); \((*_L)^2=(-1)^{p(4-p)+1}\), \((*_E)^2=(-1)^p\).  
- **Traces/couplings.** \(\mathrm{Tr}(T^A T^B)=\delta^{AB}\); \(F=dA+gA\wedge A\); all couplings explicit.  
- **ADM & δ.** \(\sqrt{|g|}=N\sqrt{\gamma}\); \(\delta_g^{(4)}=\delta(t-t_0)\,\delta_\gamma^{(3)}/N\).  
- **Response & Wick.** Retarded analyticity; DC order \((\mathbf k\to 0)\) then \((\omega\to 0^+)\); Wick map preserves ledgers.  
- **γ⁵ (Larin).** When loop‑level operators are introduced, \(\gamma^5\) is handled by the **Larin scheme** with evanescent counterterms; **not active at P1**, but the lock is declared.  
- **Units / hats.** Hatted quantities are **dimensionless OS units**; conversions to physical units use the Chapter‑0 hat map. All observables are in **hat‑units** unless noted.  
- **P1 baseline.** Axial‑torsion slice (Chapter 2); EC integrate‑out consistent; Miller energy & boundary bundle valid.

> **Audit note.** Each subsection implicitly references the relevant **Stops** (S‑H, S‑FM, …). The Stops→Sections index is § 3.46.

---

### 3.08  Front‑Matter Quick Index (one‑page map)

**OS Locks** → § 3.0. **MSGC Master Lagrangian** (toggles/guard) → § 3.32. **Per‑toggle SPD/Stops** → § 3.33.  
**1‑form mixings & canonicalization** → § 3.34, § 3.38, § 3.44. **Dispersion/positivity** → § 3.40.  
**Redundant 1‑forms (W,Q) — definitions/policy** → § 3.31.  
**Unit‑Lock & Redundancy Gauge‑Fix** → § 3.30. **BRST ladder (p‑forms)** → § 3.35. **3‑form flux quantization** → § 3.36. **p‑form boundary conditions** → § 3.37.  
**Tower‑Stepper Gate (any \(D\))** → § 3.53. **Ceiling & Demotion Card** → § 3.61.  
**Duality \(B\leftrightarrow\theta\)** → § 3.19 (guard § 3.25). **Descent Cards** (ledger) → § 3.20/§ 3.26.  
**Integer Ledger** → § 3.29. **Boundary/Corner Cookbook** → § 3.56. **Stitched Patches** → § 3.28.  
**Higher‑Form Ladder (any \(D\))** → § 3.48. **Defects & Dirac** → § 3.49. **FW/Spin\(^c\)** → § 3.50.  
**2‑/n‑group ledgers** → § 3.12/§ 3.51. **4D Ceiling Map** → § 3.54. **Defect–Ledger Table (4D)** → § 3.59.  
**Observables** (axion/gerbe, 4‑form, dilaton) → § 3.41; **Cross‑sector (×P1)** → § 3.45.  
**BRST/BV readiness (loops)** → § 3.58. **Stops→Sections index** → § 3.46.

---

### 3.09  Defect–Ledger Ready‑Reckoner (4D; copy‑ready)

| Field | Curvature | Electric object (spatial) | Magnetic object (spatial) | Linking spheres (elec / mag) | Quantized integral(s) | Event → Ledger update |
|---|---|---:|---:|---|---|---|
| Scalar \(\phi\) | \(F_{(1)}=d\phi\) | — | string (1) | \(S^3\) / \(S^1\) | \(\int_{S^3}\!*F,\ \int_{S^1} d\phi\) *(compact axion)* | Crossing a **string**: \(\int_{S^1} d\phi=2\pi n\) → record \(n\) |
| Vector \(A\) | \(F_{(2)}\) | point (0) | monopole (0) | \(S^2\) / \(S^2\) | \(\int_{S^2}\!*F,\ \int_{S^2}F\) | Charge/monopole events; Dirac \(q\,m=2\pi n\) |
| Gerbe \(B\) | \(H_{(3)}\) | string (1) | — | \(S^1\) / \(S^3\) | \(\int_{S^1}\!*H,\ \int_{S^3}H=2\pi n_H\) | **Gerbe string** or 3‑cycle events → update \(n_H\) *(FW lock may forbid)* |
| 3‑form \(C\) | \(F_{(4)}\) | membrane (2) | — | \(S^0\) / \(S^4\) | \(\int_{M_4}F_4=2\pi n_{F_4}\) | **Membrane jump**: \(n_{F_4}\to n_{F_4}\pm 1\); \(\Delta\rho_\Lambda=\tfrac12 q_4^2(2n_{F_4}\pm1)\) |

**Policy gates:** FW/Spin\(^c\) (§ 3.50), Descent (ledger‑only) (§ 3.20/§ 3.26), Duality guard \(B\leftrightarrow\theta\) (§ 3.19/§ 3.25).  
**Compactness caveat:** Quantization requires **compact** gauge; non‑compact redundancies (Weyl \(W\), Planck \(Q\)) carry **no** integers.

---

### 3.10  Abelian 2‑Form Gerbe \(B_{\mu\nu}\) (Healthy Uplift)

Gauge **and gauge‑of‑gauge**: \(\delta B=d\Lambda\), with \(\delta\Lambda=d\chi\) (hence only \(d\Lambda\) is physical); curvature \(H=dB\) with \(H_{\mu\nu\rho}=3\partial_{[\mu}B_{\nu\rho]}\).  
**Sentinel.** \(\boxed{\Delta\mathcal L_B=-\tfrac{1}{12}H^2}\) → positive Hamiltonian.  
**4D DOF.** Dual to a pseudoscalar (one DOF).  
**Couplings.** BF/topological couplings **ledger‑only** (no bulk kinetic replacement).  
**Duality.** Use **either** \(B\) **or** \(\theta\); if both, impose \(H=*d\theta\).  
**Gauge‑fixing.** Lorenz‑type \(\nabla^\mu B_{\mu\nu}=0\) plus a gauge‑of‑gauge condition (e.g., \(\nabla^\mu \Lambda_\mu=0\)) closes redundancies; ghosts absent with sentinel sign.  
**Flux integer.** \(n_H=\tfrac{1}{2\pi}\int_{S^3}H\in\mathbb Z\).  
**Stops.** S‑H/S‑C/S‑SP/S‑FM/S‑SCHUR/S‑EM/S‑SHYP/S‑TOPPOS/S‑CHAR/S‑ET — pass.

---

### 3.11  3‑Form \(C_{\mu\nu\rho}\) & 4‑Form \(F_4\) (Vacuum Branches)

Gauge \(C\to C+d\Xi\); \(F_4=dC\).  
**Sentinel.** \(\boxed{\Delta\mathcal L_C=-\tfrac{1}{48}F_4^2}\).  
**4D dynamics.** No local DOF; \(F_4=\text{const}\) on‑shell → \(\rho_\Lambda=\tfrac12|F_4|^2\).  
**Flux integer.** \(n_{F_4}=\tfrac{1}{2\pi}\int_{M_4}F_4\in\mathbb Z\).  
**Stops.** S‑TOPPOS/S‑CHAR/S‑B/S‑BC — pass.

---

### 3.12  Non‑Abelian 2‑Form (2‑Group) — Ledger Interface (P1‑Safe)

Ledger‑only connective data: \(F=dA+A\wedge A\), \(H=dB+[A,B]\); modified Bianchi (ledger)  
\(dH=\kappa\,\mathrm{Tr}(F\wedge F)-\zeta\,\mathrm{Tr}(R\wedge R)\).  
Patch (ledger): \(\delta B=\kappa\,\omega_2^{(1)}(A)-\zeta\,\omega_2^{(1)}(\Gamma)+d\Lambda\).  
**Policy.** No non‑abelian \(H^2\) kinetic at P1; descent/inflow is **ledger‑only**.  
**Stops.** S‑BNDL/S‑CHAR — pass.

---

### 3.13  Descent‑Pair Boxes (Ledger‑Only Inflow Hooks)

Gauge descent: \(d\omega_3^{(0)}(A)=\mathrm{Tr}(F\wedge F)\), \(\delta\omega_3^{(0)}=d\omega_2^{(1)}\); **ledger** \(dH=\kappa\,\mathrm{Tr}(F\wedge F)\), \(\delta B=\kappa\,\omega_2^{(1)}+d\Lambda\).  
Gravity descent: \(d\omega_3^{(0)}(\Gamma)=\mathrm{Tr}(R\wedge R)\), \(\delta\omega_3^{(0)}=d\omega_2^{(1)}\); **ledger** \(dH=-\zeta\,\mathrm{Tr}(R\wedge R)\), \(\delta B=-\zeta\,\omega_2^{(1)}+d\Lambda\).  
**Stops.** S‑TOPPOS/S‑BNDL/S‑CHAR — pass.

---

### 3.14  Discrete Topology Ledgers: Orientation, Spin/Pin, Spin\(^c\)

\(w_1(M)=0\) (P1 lock). \(w_2(M)=0\) or Spin\(^c\) with \(w_2\equiv c_1(L)\bmod 2\).  
Pin (deferred): if ever gauged, add S‑PIN & fermion energy checks.  
**Stops.** S‑BNDL/S‑CHAR — pass.

---

### 3.15  Compatibility & Mixing (Snapshot)

| Pair | Status | Allowed | Constraints / Stops |
|---|---|---|---|
| \(B\)–\(\theta\) | △ | Choose one or impose \(H=*d\theta\) | S‑ET/S‑SCHUR |
| \(B\)–\(A\) | ⊕ | \(B\wedge F\) **ledger‑only** | S‑TOPPOS/S‑CHAR |
| \(B\)–\(W,Q,\phi\) | ✓ | No kinetic mixing | S‑FM/S‑SCHUR |
| \(C\)–any | ✓ | Constant \(F_4\) background | trivial |
| Discrete × any | ✓ | Ledger constraints only | S‑BNDL/S‑CHAR |

Legend: ✓ allowed; △ allowed w/ constraint; ⊕ ledger‑only.

---

### 3.16  Worked Micro‑Examples (I)

**M3‑1:** \(B\leftrightarrow\theta\) (first‑order). \(\mathcal L=-\tfrac{1}{12}H^2+\tfrac16\theta\,\epsilon\,\partial H\Rightarrow H=*d\theta\Rightarrow \mathcal L=-\tfrac12(\partial\theta)^2\). (S‑ET/S‑H)  
**M3‑2:** 4‑form branch & membrane. \(\mathcal L=-\tfrac{1}{48}F_4^2+\mu\int_{\Sigma_3}C\). Jump \(n_{F_4}\to n_{F_4}\pm1\). \(\Delta\rho\ge0\); Miller ledger accounts. (S‑TOPPOS/S‑CHAR/S‑B/S‑BC)

---

### 3.17  Checklists (Core)

**C3‑Gerbe** — declare \(B,\Lambda,H\); \(-\tfrac1{12}H^2\); if \(\theta\) present: choose one or \(H{=}{*}d\theta\); BF ledger‑only; \(\int H\in2\pi\mathbb Z\); run Stops.  
**C3‑2‑group (ledger)** — record \(F,H\) & descent; no non‑ab. \(H^2\).  
**C3‑3‑form (4‑form)** — \(-\tfrac1{48}F_4^2\); \(\int F_4\in2\pi\mathbb Z\).  
**C3‑Discrete** — \(w_1=0\), \(w_2=0\) or Spin\(^c\).

---

### 3.19  Formal Dualization \(B\leftrightarrow\theta\) (Boxed)

\(\mathcal L=-\tfrac{1}{12}H^2+\tfrac06\theta\,\epsilon^{\mu\nu\rho\sigma}\partial_\mu H_{\nu\rho\sigma}\Rightarrow H^{\mu\nu\rho}=\epsilon^{\mu\nu\rho\sigma}\partial_\sigma\theta\Rightarrow \mathcal L=-\tfrac12(\partial\theta)^2\).  
**Policy (C3‑DUAL).** Use **either** \(B\) **or** \(\theta\); if both, enforce \(H=*d\theta\) and Schur‑reduce. (S‑ET/S‑FM/S‑SCHUR/S‑H)

---

### 3.20  Descent Cards (Ledger Boxes)

- **Gauge:** \(d\omega_3^{\mathrm g}=\mathrm{Tr}(F\wedge F)\), \(\delta\omega_3^{\mathrm g}=d\omega_2^{(1)}\); ledger \(dH=\kappa\,\mathrm{Tr}(F\wedge F)\), \(\delta B=\kappa\,\omega_2^{(1)}+d\Lambda\).  
- **Gravity:** \(d\omega_3^{\mathrm{grav}}=\mathrm{Tr}(R\wedge R)\), \(\delta\omega_3^{\mathrm{grav}}=d\omega_2^{(1)}\); ledger \(dH=-\zeta\,\mathrm{Tr}(R\wedge R)\), \(\delta B=-\zeta\,\omega_2^{(1)}+d\Lambda\).

---

### 3.21  Minimal Tensor‑Hierarchy (Phase‑II Readiness; No Activation)

Fields \(A\) (1‑form), \(B\) (2‑form), \(C\) (3‑form).  
Fake‑curvature (ledger): \(\mathcal H\equiv H-\kappa\,\omega_3^{(0)}(A)+\zeta\,\omega_3^{(0)}(\Gamma)\).  
**Activation gate:** § 3.27 TH‑Gate before any non‑abelian higher‑form dynamics.

---

### 3.22  Worked Micro‑Examples (II)

**M3‑3:** Hopf‑knotted EM–axion with positive bound. \(\mathcal L=-\tfrac14F^2-\tfrac12(\partial\theta)^2+\lambda\,\mathcal I_{\rm stab}\), \(\lambda>0\), choose \(\mathcal I_{\rm stab}\ge 0\) to ensure \(E\ge \alpha |Q_H|\). Dual \(H{=}{*}d\theta\) equivalent. (S‑H/S‑TOPPOS)  
**M3‑4:** Λ‑branch membrane (as § 3.16). Miller ledger consistent.

**M3‑5:** Axion domain wall (\(\Delta\theta=2\pi n\)) and boundary CS. Across a codimension‑1 wall, \(\theta\) jumps by \(2\pi n\). The variation of \(\tfrac{\alpha_{\rm ax}}{4}\theta F\tilde F\) integrates to a **3D Chern–Simons** term on the wall with level shift \(\Delta k = n\,\alpha_{\rm ax}/(2\pi)\). This is **ledger‑only** (no bulk kinetic change), enforces the polarization rotation quantization, and is compatible with Freed–Witten locks. (S‑TOPPOS/S‑B/S‑BC)

---

### 3.23  Addenda Checklists

**C3‑DUAL:** add \(\Lambda\wedge(H-*d\theta)\) if both; Schur‑reduce; SPD check; boundary exact \(d(\theta H)\) ledger‑only.  
**C3‑DESCENT:** use gauge/grav cards; keep relations **in ledger**; forbid \(B\wedge\)Pontryagin **bulk** terms.  
**C3‑TH:** register fields; fake‑curvature; no non‑ab. \(H^2\) at P1; list Stops pre‑checks.

---

### 3.25  Pipeline Guard (C3‑DUAL Enforcement)

If \(B\) and \(\theta\) co‑appear: add \(\mathcal L_{\rm constr}=\Lambda\wedge(H-*d\theta)\), solve, Schur‑reduce to single DOF, drop \((B,\Lambda)\); re‑run SPD. (S‑H/S‑C/S‑SP/S‑FM/S‑SCHUR/S‑ET/S‑TOPPOS)

---

### 3.26  Descent Cards (Copy‑Ready)

Boxes per § 3.20; normalizations per Chapter‑0; \(\int \mathrm{Tr}(F\wedge F)\in 8\pi^2\mathbb Z\).

---

### 3.27  Tensor‑Hierarchy Activation Gate (Phase‑II Switch; No Activation Here)

Conditions: sentinel signs; SPD (minors \(>\!0\)); symmetric‑hyperbolic principal symbol; quantization + FW/Spin\(^c\); topology ledger‑only; boundary/Miller intact; GR/P1 decoupling as heavy scales \(\to\infty\).

---

### 3.28  Stitched Patches Example (Finite‑Energy \(\theta\), Trivial \(B\))

Cover by charts \(U,V\). On \(U\): propagate \(\theta\), set \(B{=}0\). On \(V\): propagate \(B\) with \(H{=}{*}d\theta\), set \(\theta|_V{=}0\). On overlap glue by gerbe gauge. Energy \(E[B]=E[\theta]\); no integer flux. (S‑ET/S‑FM/S‑TOPPOS)

---

### 3.29  Integer Ledger Table (One‑Glance)

| Symbol | Definition | Quantization | Sector | Role |
|---|---|---:|---|---|
| \(c_1\) | First Chern class | \(\in\mathbb Z\) | \(U(1)\) | Flux integer; boundary CS |
| \(\nu_G\) | \(\tfrac{1}{8\pi^2}\!\int\!\mathrm{Tr}F\wedge F\) | \(\in\mathbb Z\) | YM | Pontryagin (descent) |
| \(n_H\) | \(\tfrac{1}{2\pi}\!\int_{S^3}\!H\) | \(\in\mathbb Z\) | Gerbe | 2‑form flux |
| \(Q_H\) | Hopf charge | \(\in\mathbb Z\) | EM/axion | Knotted class |
| \(n_{F_4}\) | \(\tfrac{1}{2\pi}\!\int_{M_4}\!F_4\) | \(\in\mathbb Z\) | 3‑form | Λ‑branch |
| \(w_1\) | Orientation | \(\{0,1\}\) | Topology | **P1 lock:** 0 |
| \(w_2\) | Stiefel–Whitney | \(\{0,1\}\) | Spin | Spin or Spin\(^c\) |
| \(c_1(L)\) | Spin\(^c\) line | \(\in\mathbb Z\) | Spin\(^c\) | \(w_2\equiv c_1(L)\bmod2\) |
| \(k\) | CS level (3D) | \(\in\mathbb Z\) | Boundary TQFT | Inflow coupling |

*Compactness caveat:* Quantization requires a **compact** gauge group; non‑compact redundancies (e.g., \(W_\mu,Q_\mu\)) carry no such integers.

---

### 3.30  Unit‑Lock & Redundancy Gauge‑Fix Card

**Purpose.** Fix non‑observable choices so physical predictions are unambiguous.

**Canonical unit‑locks (P1 defaults).**  
1) **Hats.** Work in hat‑units; set \(\Phi=\hat M_P^2\) constant (no Weyl running).  
2) **Redundant 1‑forms.** Choose the **unit gauge** \(W_\mu=0,\ Q_\mu=0\) (toggles \(\tau_W=\tau_Q=0\)); forbid matter weights \(w_i,q_i\).  
3) **Axion vs gerbe.** Choose **one**: \(\theta\) **or** \(B\). If both appear, impose \(H=*d\theta\) and Schur‑reduce (C3‑DUAL).  
4) **4‑form branch.** Pick an integer \(n_{F_4}\) (vacuum label) and boundary conditions; membrane events change \(n_{F_4}\to n_{F_4}\pm1\) (ledger update).  
5) **Topological ledgers.** Record \(c_1,\nu_G,n_H,n_{F_4},Q_H,w_1,w_2,c_1(L),k\) per § 3.29; these are **invariants** under field redefinitions and unit gauges.

**Equivalence relation (redundancy class).**  
Two parameter sets \(\mathcal P,\mathcal P'\) are **physically equivalent** iff related by: (i) field redefinitions that preserve sentinel signs; (ii) unit‑gauges \(W,Q\); (iii) duality guard \(H=*d\theta\); (iv) identical **ledger integers**. Observables must be functions of the equivalence class.

**Health check.** After fixing the unit gauge, re‑run SPD minors (§ 3.34), characteristics (§ 3.38), and ledger audit (§ 3.29).

---

### 3.31  Redundant 1‑Forms \(W_\mu\) (Weyl) and \(Q_\mu\) (Planck) — Definitions & Policy

**Gauge structure.**  
\(W_\mu\mapsto W_\mu+\partial_\mu\lambda_W,\quad Q_\mu\mapsto Q_\mu+\partial_\mu\lambda_Q.\)  
Define curvature‑like two‑forms for audit: \(\mathcal H(W)_{\mu\nu}=\partial_\mu W_\nu-\partial_\nu W_\mu\) and \(\mathcal H(Q)_{\mu\nu}=\partial_\mu Q_\nu-\partial_\nu Q_\mu\).

**Group & ledger.**  
Gauge groups are **non‑compact** (\(\mathbb R\)‑type); hence **no** integer fluxes: \(c_1(W)=c_1(Q)=0\). Ledger entries remain zero (compactness caveat § 3.29).

**Coupling policy.**  
At **P1** the toggles \(\tau_W=\tau_Q=0\) (no kinetic, no observables). If ever activated for bookkeeping, only the Maxwell sentinel \(-\tfrac14\mathcal H^2\) is allowed and **all** SPD/causality Stops apply; matter couplings would enter via scale‑covariant weights \(D_\mu\to D_\mu+w_i W_\mu+q_i Q_\mu\) (inactive at P1).

**Health.**  
With toggles OFF, \(W,Q\) are pure redundancies; canonicalization of the \(1\)-form block (if ever ON) is governed by § 3.34/§ 3.38; observables § 3.41 remain unaffected.

---

### 3.32  MSGC Master Lagrangian (Toggles)

Toggles \(\tau_W,\tau_Q,\tau_\phi,\tau_\theta,\tau_B,\tau_C\in\{0,1\}\); **guard** \(\tau_\theta+\tau_B\le 1\) (or impose \(H{=}{*}d\theta\)):

\[
\begin{aligned}
\mathcal L_{\text{MSGC}}=\;&\underbrace{\tfrac12\,\Phi\,R - \tfrac12(\partial\ln\Phi)^2}_{\text{gravity header; set }\Phi=\hat M_P^2\text{ in P1/GR}}\\
&+\tau_\phi\!\left[-\tfrac12(\partial\phi)^2 - V(\phi)\right] + \underbrace{\left[-\tfrac12(\partial\sigma)^2 - V(\sigma)\right]}_{\text{\(\sigma\): ordinary matter scalar (illustrative)}}\\
&+\tau_W\!\left[-\tfrac14\,\mathcal H(W)^2\right]+\tau_Q\!\left[-\tfrac14\,\mathcal H(Q)^2\right]\\
&-\tfrac14 Z(\phi)F^2\quad (Z=e^{-2\phi}\text{ if }\tau_\phi{=}1;\ \text{else }Z\equiv 1)\\
&+\tau_\theta\!\left[-\tfrac12(\partial\theta)^2 + \tfrac{\alpha_{\rm ax}}{4}\theta F\tilde F\right]
+\tau_B\!\left[-\tfrac1{12}H^2\right]+\tau_C\!\left[-\tfrac1{48}F_4^2\right]\\
&+\bar\psi(i\gamma^\mu D_\mu - y_\psi\sigma)\psi + \mathcal L_{\text{matter}}[A_\mu,\sigma]\\
&+\ \mathcal L_{\text{mix}}^{(1\text{-form})}\ \ (\text{optional; OFF by default})\ +\ \mathcal L_{\text{ledger}}^{\text{(topological)}}.
\end{aligned}
\]

**P1 defaults:** \(\tau_W=\tau_Q=0\), mixings OFF → \(W,Q\) are redundancies (no bulk observables).  
**Per‑toggle health:** vectors \(-\tfrac14\), scalars \(-\tfrac12\), gerbe \(-\tfrac1{12}\), 3‑form \(-\tfrac1{48}\).

---

### 3.33  Per‑Toggle SPD/Stops (Extract)

- \(W_\mu,Q_\mu\): Maxwell sign; Gauss constraints; S‑EM/S‑SHYP pass (if toggled ON).  
- \(\phi\): \(-\tfrac12(\partial\phi)^2\); \(Z(\phi)>0\); S‑H/S‑FM/S‑P pass.  
- \(\theta\): \(-\tfrac12(\partial\theta)^2\); \(\theta F\tilde F\) is topological (no kinetic sign effect).  
- \(B\): \(-\tfrac1{12}H^2\); dual to scalar; guard with \(\theta\).  
- \(C\): \(-\tfrac1{48}F_4^2\); constant on‑shell.  
- \(1\)-form mixings (if ON): see § 3.34/§ 3.38 for SPD & canonicalization.

---

### 3.34  Extended Compatibility Matrix (1‑form SPD inequalities)

For
\[
M_{(1)}=\begin{pmatrix}
Z & \epsilon_{AW} & \epsilon_{AQ}\\
\epsilon_{AW} & 1 & \epsilon_{WQ}\\
\epsilon_{AQ} & \epsilon_{WQ} & 1
\end{pmatrix},
\]
**SPD via Sylvester’s criterion (sufficient and necessary for this ordering):**
\[
\boxed{
\text{(i) } Z>0,\qquad
\text{(ii) } Z-\epsilon_{AW}^2>0,\qquad
\text{(iii) } \det M_{(1)}=Z(1-\epsilon_{WQ}^2)-\epsilon_{AW}^2-\epsilon_{AQ}^2+2\,\epsilon_{AW}\epsilon_{AQ}\epsilon_{WQ}>0.}
\]
**Additional convenient checks (sufficient, not necessary):**
\[
Z-\epsilon_{AQ}^2>0,\qquad 1-\epsilon_{WQ}^2>0.
\]
Any allowed mixing must keep the Sylvester set strictly positive; Schur complements inherit positivity. (S‑FM/S‑SCHUR)

---

### 3.35  BRST/FP Ladder for \(p\)-Form Gauges (Audit Card)

**Purpose.** Record the ghost structure so future loop work is turnkey; P1 remains classical.

- **1‑form \(A\).** \( \delta A = d\alpha\). Gauge‑fix \( \nabla^\mu A_\mu = 0 \). FP ghost \(c\) (0‑form); FP operator \( -\Box \). Physical DOF \(N_{\rm dof}(1,4)=\binom{2}{1}=2\). Sentinel \(-\tfrac14 F^2\) ensures positive Hamiltonian on transverse modes.  
- **2‑form \(B\) (reducible).** \( \delta B = d\Lambda\), \( \delta\Lambda = d\chi\). Gauge‑fix \( \nabla^\mu B_{\mu\nu}=0\) and \( \nabla^\mu \Lambda_\mu=0\). Ghosts: \(c_1\) (1‑form), ghost‑for‑ghost \(c_0\) (0‑form). Net physical DOF \(N_{\rm dof}(2,4)=\binom{2}{2}=1\) (dual pseudoscalar). Sentinel \(-\tfrac1{12}H^2\) gives positive Hamiltonian.  
- **3‑form \(C\) (stage‑2 reducible in 4D).** \( \delta C=d\Xi_2\), \( \delta\Xi_2=d\Xi_1\), \( \delta\Xi_1=d\Xi_0\). In 4D, \(N_{\rm dof}(3,4)=\binom{2}{3}=0\); all bulk modes are pure gauge; only the integer 4‑form flux sector remains (ledger).

**Note.** BRST charge is nilpotent; physical states are cohomology classes. FP determinants cancel unphysical polarizations; P1 path integrals can remain schematic.

---

### 3.36  3‑Form Path‑Integral Quantization in 4D (Flux‑Sum Card)

**Partition function.** \( Z \propto \sum_{n\in\mathbb Z} \exp\!\left[-\int \tfrac{1}{48}F_4^2\right] \) with \( F_4 = q_4\, n\, \mathrm{vol}_4 \).  
**Membranes.** Couplings \( \mu\!\int_{\Sigma_3} C \) shift \( n \to n\pm 1 \).  
**Boundary conditions.** Well‑posed variation: \( \delta S|_{\partial M}=\int_{\partial M} \delta C \wedge *F_4 \). Choose Dirichlet (fix \(C_{\parallel}\)) or Neumann (fix \((*F_4)_\perp\)); additions are ledger‑only.  
**Outcome.** No propagating DOF; discrete Λ‑branch structure matches § 3.11.

---

### 3.37  Boundary Conditions Card for \(p\)-Forms (Well‑Posed Variational Principle)

**General rule.** From \( \delta S = -\tfrac{1}{2(p+1)!}\int \delta A_{(p)} \wedge *F_{(p+1)} + \text{bdy} \), pick one on \( \partial M \):  
- **Dirichlet** (fix tangential potential) or **Neumann** (fix normal flux).  
- Mixed choices are allowed if they preserve gauge and yield a closed boundary symplectic form.

**4D instances.**  
- \(p=1\) (vector): boundary term \( \int_{\partial M}\delta A\wedge *F\). Dirichlet \(A_{\parallel}=0\) *or* Neumann \((*F)_\perp=0\).  
- \(p=2\) (gerbe): boundary term \( \int_{\partial M}\delta B\wedge *H\). Dirichlet \(B_{\parallel}=0\) *or* Neumann \((*H)_\perp=0\).  
- \(p=3\) (3‑form): as § 3.36; Dirichlet \(C_{\parallel}=0\) *or* Neumann \((*F_4)_\perp=0\).

**Policy.** Boundary additions remain **ledger‑only**; no bulk kinetic is replaced.

---

### 3.38  Canonicalization of the 1‑Form Mixing Block \(M_{(1)}\)

**Cholesky (preferred).** \(M=L L^\top\); \(\mathbf F=L^{-1}\mathbf G\Rightarrow \mathcal L=-\tfrac14\sum G_i^2\).  
**Jacobi rotations.** \(R^\top M R=\mathrm{diag}(\lambda_i)\), \(\lambda_i>0\); rescale to canonical form.  
**Propagators (Lorenz gauge)** & **residues**: Maxwell form; transverse residues \(+\); longitudinal/time are gauge.  
**Characteristics:** \(k^2=0\) for each canonical mode; **front speed = 1**. (S‑H/S‑EM/S‑SHYP)

---

### 3.40  Dispersion & Forward‑Limit Positivity (massless sectors)

- **Dispersion.** For constant \(M_{(1)}\), canonicalization yields \(\partial_\mu \widetilde F_i^{\mu\nu}=0\) ⇒ characteristics \(k^2=0\), causal cones unchanged. (S‑EM/S‑SHYP)  
- **Spectral/forward positivity.** In the quadratic, massless setting, **SPD of \(M_{(1)}\)** implies a positive Källén–Lehmann density for every physical linear combination of fields. Forward‑limit dispersion relations require IR **subtractions** for massless exchange; with those subtractions, positivity reduces to the SPD conditions of § 3.34. (S‑P/S‑SUB)  
- **No quartics at P1.** The MSGC block at P1 carries **no** parity‑even quartic contact terms; if added in later phases, they must satisfy the standard forward‑limit inequalities separately.

---

### 3.41  Observables Templates (Chapter‑3 Units, Ledger‑Aware)

- **Axion/gerbe EM rotation.** \(\boxed{\Delta\alpha_{\rm pol}=\tfrac{\alpha_{\rm ax}}{2}\,[\theta]^{\rm obs}_{\rm src}}\). If \(\theta\) winds by \(2\pi n\): \(\Delta\alpha=\alpha_{\rm ax}\,n\pi\) (**defined mod \(\pi\)**).  
- **4‑form Λ branches.** \(F_4=q_4 n_{F_4}\Rightarrow \rho_\Lambda=\rho_{\rm bare}+\tfrac12 q_4^2 n_{F_4}^2\).  
- **Dilaton drift.** \(\Delta\hat\alpha/\hat\alpha=2\Delta\phi\), \(\dot{\hat\alpha}/\hat\alpha=2\dot\phi\) (dimensionless).  
- **Null signatures.** \(W,Q\) with \(\tau_{W,Q}=0\) and mixings OFF are **redundancies**; no bulk observables.

---

### 3.44  1‑Form Canonicalization & Residues — Quick Sheet

Inputs, Cholesky/Jacobi steps, propagators, residues, characteristics, and **troubleshooting** mapping principal‑minor failures to minimal remedies (reduce mixings, raise \(Z\), enforce guard).

---

### 3.45  Cross‑Sector Observables (Axion/Gerbe × P1)

**EM:** \(\Delta\alpha_{\rm EM}^{\text{(total)}}\simeq \tfrac12\alpha_{\rm ax}[\theta]^{\rm obs}_{\rm src}\) (P1 contributes only beyond minimal MSGC).  
**GW:** \(\Delta\psi_{\rm GW}^{\text{(total)}}\simeq \tfrac12\,\Xi_{\rm T}\) (P1 axial torsion).  
**Orthogonality:** EM and GW channels decouple at leading order; cones/residues unchanged.

---

### 3.46  Stops → Sections Map (Audit Index)

S‑H → § 3.10–3.11/3.32/3.38 S‑C/S‑SP → § 3.10/3.25 S‑FM/S‑SCHUR → § 3.34/§ 3.38/§ 3.44  
S‑EM/S‑SHYP → § 3.38/§ 3.40 S‑P/S‑SUB → § 3.40 S‑TOPPOS → § 3.13/§ 3.20/§ 3.26/§ 3.56  
S‑CHAR/S‑BNDL → § 3.29/§ 3.49/§ 3.50/§ 3.59 S‑B/S‑BC/S‑CT → § 3.56 S‑ET → § 3.19/§ 3.25/§ 3.28.

---

### 3.48  Universal Higher‑Form Ladder in \(D\)

**Sentinel.** \(\boxed{\mathcal L_{(p)}=-\tfrac{1}{2(p+1)!}F_{(p+1)}^2}\).  
**DOF.** \(\boxed{N_{\rm dof}(p,D)=\binom{D-2}{p}}\).  
**Duality.** \(p\leftrightarrow D\!-\!p\!-\!2\).  
**Ceiling.** \(N_{\rm dof}=0\) for \(p\ge D\!-\!1\) → **ledger‑only**.

---

### 3.49  Electric/Magnetic Defects & Dirac Quantization (General \(D\))

Electric object spatial dim \(p\!-\!1\); magnetic \(D\!-\!p\!-\!3\). Linking spheres \(S^{D-p-1}\) (electric), \(S^{p+1}\) (magnetic).  
Quantization \(g_e g_m=2\pi n\) (**compact** groups). (S‑CHAR)

---

### 3.50  Worldvolume Consistency: Freed–Witten & Spin\(^c\)

\([H]|_{\mathcal W}+w_3(T\mathcal W)=0\) and \(w_2(T\mathcal W)=c_1(L)\bmod2\) as **ledger locks**; couplings forbidden if violated. (S‑BNDL/S‑CHAR)

---

### 3.51  Higher‑Group Ledgers (2‑/3‑/n‑Group; Postnikov)

Ledger‑only fake‑curvature constraints driven by Postnikov classes; any activation requires **TH‑Gate** (§ 3.27) + **Tower‑Stepper** (§ 3.53).

---

### 3.52  Non‑Invertible/Topological Selection Rules (Ledger Policy)

Record fusion/condensation rules as **ledger constraints**; no bulk kinetic from these at P1.

---

### 3.53  Tower‑Stepper Gate (Admission/Demotion, Any \(D\))

Ceiling → sentinel sign/SPD → hyperbolicity → quantization/locks → topology separation → boundary/Miller → **decision** (admit vs ledger).

---

### 3.54  Ceiling Maps (4D & General)

4D: admit \(p=0,1,2\) (propagate); demote \(p\ge 3\) (ledger).  
General \(D\): admit \(0\le p\le D\!-\!2\); demote \(p\ge D\!-\!1\).

---

### 3.55  Worked 2×2 Mixing Exemplar (Closed‑Form SPD Region)

For \(M_{2\times2}=\begin{psmallmatrix}Z&\epsilon\\\epsilon&1\end{psmallmatrix}\):  
\(\lambda_\pm=\tfrac{Z+1\pm\sqrt{(Z-1)^2+4\epsilon^2}}{2}\); SPD if \(Z>0,\ \epsilon^2<Z\); \(\tan 2\theta=\tfrac{2\epsilon}{1-Z}\).

---

### 3.56  Boundary & Corner Cookbook (Sign‑Locked)

GHY term; EM \(\theta\) → boundary CS; gerbe \(d(B\wedge F)\) → edge inflow (ledger‑only); 4‑form membrane coupling; corner terms; all **no‑kinetic‑replacement** and Miller‑consistent. (S‑TOPPOS/S‑B/S‑BC/S‑CT)

**Redundant W/Q at boundaries.** Use **unit gauge** \(W=Q=0\) on \(\partial M\) (or Dirichlet for tangential components). No CS‑like boundary terms exist for non‑compact \(W,Q\); boundary energy remains zero.

---

### 3.57  Numerical (Non‑Code) Verification Flow

Normalize → check minors → conditioning → Cholesky/Jacobi → residue positivity → duality guard → ledger integers → archive audit pack.

---

### 3.58  BRST/BV Quantization Readiness (Redundancies & Reducibility)

**Scope.** Informational (P1 classical). Ensures loop‑level readiness without altering P1 dynamics.

- **Gerbe reducibility.** Gauge \(δB=d\Lambda\) with **gauge‑of‑gauge** \(δ\Lambda=d\chi\) is **stage‑1 reducible**. In BV: ghost \(c_\Lambda\) (1‑form) and ghost‑for‑ghost \(c_\chi\) (0‑form).  
- **Axion–gerbe duality.** If dualized (\(H=*d\theta\)), use scalar BRST (irreducible); drop gerbe ghost tower.  
- **Vectors \(W,Q\).** Standard abelian BRST if ever toggled ON; at P1 they are OFF (pure redundancy).  
- **Torsion decoupling (P1).** Axial torsion (Chapter 2) **does not mix** kinetically with \(B,\theta,C,W,Q\); any cross‑talk is **ledger‑only**; observables remain orthogonal at leading order.  
- **Larin γ⁵.** If loops are activated (later phases), use **Larin scheme** for axial anomalies and keep **descent** terms in ledger; no bulk kinetic is introduced.  
- **Outcome.** P1 remains classical and ghost‑free; BV data here is **readiness only**.

---

### 3.59  Defect–Ledger Table (4D; **audited**)

| \(D\) | \(p\) | Curvature | Electric obj (spatial) | Magnetic obj (spatial) | Linking spheres | Quantized integrals (ledger) | Propagate? |
|---:|---:|---|---:|---:|---|---|---|
| 4 | 0 | \(F_{(1)}=\partial\phi\) | \(-1\) (none) | 1 (strings) | **\(S^{3}\)/\(S^{1}\)** | **\(\int_{S^{3}}\!*F,\ \int_{S^{1}} d\phi\)** | yes |
| 4 | 1 | \(F_{(2)}\) | 0 (points) | 0 (monopoles) | \(S^{2}/S^{2}\) | \(\int_{S^2}\!*F,\ \int_{S^2}F\) | yes |
| 4 | 2 | \(H_{(3)}\) | 1 (strings) | \(-1\) (none) | \(S^{1}/S^{3}\) | \(\int_{S^1}\!*H,\ \int_{S^3}H\) | yes |
| 4 | 3 | \(F_{(4)}\) | 2 (membranes) | \(-2\) (none) | \(S^{0}/S^{4}\) | \(\int_{M_4}F_4\) | no |

*Compactness note:* Quantization requires compact gauge group.

---

### 3.60  Freed–Witten Micro‑Example (S³ Wrap)

On \(\mathcal W=S^3\), \(w_3(TS^3)=0\Rightarrow [H]|_{S^3}=0\Rightarrow n_H=0\). Wrap with nonzero \(H\)‑flux is **forbidden** (ledger lock).

---

### 3.61  Ceiling & Demotion — Quick Card

Immediate test via \(N_{\rm dof}=\binom{D-2}{p}\); if zero → ledger; else run full Stops (sign, SPD, hyperbolicity, quantization/locks, topology separation, boundary/Miller).

---

### 3.62  Whole‑Chapter Sanity Audit (Summarized)

- Sentinel signs verified; duality guard enforced; SPD canonicalization proved; null characteristics; topology separation; integer ledgers; boundary/Miller; axion rotation fixed \(\Delta\alpha=\frac{\alpha_{\rm ax}}{2}\Delta\theta\).  
- **New this turn:** § 3.35 (BRST/FP ladder), § 3.36 (3‑form flux‑sum), § 3.37 (p‑form BCs). Cross‑refs updated; Stops unchanged and all pass.  
- No further defects found.

---

### 3.63  Final Summary

Chapter 3 now admits and controls **all redundant gauges up to the dimensional ceiling**, with higher‑forms either **propagating** (if Stops pass) or **demoted to ledger** (top‑forms). Duality, anomaly descent, integer ledgers, SPD diagonalization, dispersion/positivity, and boundary energy accounting are encoded as **operational checklists** ready for reuse.
