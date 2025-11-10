# Chapter 2 - UGFT Gravitational Gauge Slice (P1) & Miller Equivalence
> **Unified, self‑contained reference (Chapter‑0 style).**  
> Authoritative formulation of the gravitational gauge sector with **dynamical axial torsion** (P1) and the **Miller mass–energy equivalence**.  
> Everything below is sign‑locked, gauge‑normalized, and ready for derivations and audits.

---

## 0) R1 Header — Universal Conventions (state at the top of any derivation)

**Signature & orientation.** Minkowski \((-,+,+,+)\); \(\epsilon_{0123}=+\sqrt{|g|}\); \(\epsilon^{0123}=+1/\sqrt{|g|}\).  
Contraction test: \(\epsilon^{\mu\nu\rho\sigma}\epsilon_{\alpha\nu\rho\sigma}=-3!\,\delta^\mu{}_\alpha\).

**Hodge dual.** \( *^2=(-1)^{p(4-p)+1}\) in Lorentzian; after Wick, \((*_E)^2=(-1)^p\).

**Traces & couplings.** Gauge trace \(\mathrm{Tr}(T^A T^B)=\delta^{AB}\); spinor/Lorentz traces use \(\mathrm{tr}\).  
Couplings **explicit**: \(F=dA+g\,A\wedge A\); \(D_\mu=\partial_\mu+i g A_\mu^A T^A\).

**Spinors.** \(\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}\); \(\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3\).  
Minimal torsion coupling is **axial** only: \(J_5^\mu=\bar\psi\gamma^\mu\gamma^5\psi\). Use **Larin** scheme for \(\gamma^5\) in loop regularization.

**Indices & frames.** Spacetime \(\mu,\nu\); tangent \(a,b\); adjoint \(A,B\). Tetrad ladder \(g_{\mu\nu}=\eta_{ab}e^a{}_\mu e^b{}_\nu\).  
Symmetrization/antisymmetrization is **weight‑one**.

**Measures & ADM delta.** \(\sqrt{|g|}=N\sqrt{\gamma}\).  
\(\displaystyle \delta_g^{(4)}(x,x_0)=\delta(t-t_0)\,\delta^{(3)}_\gamma/N\), so \(\int d^4x \sqrt{|g|}\,\delta_g^{(4)}=1\).  
Spherical identities: \(\nabla^2(1/r)=-4\pi\,\delta^{(3)}(\mathbf r)\), \(\delta^{(3)}(\mathbf r)=\delta(r)/(4\pi r^2)\).

**Fourier/response/Kubo.** Phase \(e^{\,i(\omega t-\mathbf k\cdot\mathbf x)}\).  
\(G^R_{AB}(t)=-i\,\Theta(t)\langle[A(t),B(0)]\rangle\), \(\rho=-2\,\mathrm{Im}\,G^R\).  
\(\displaystyle \sigma_{\rm DC}=\lim_{\omega\to0^+}\frac{1}{\omega}\,\mathrm{Im}\,G^R_{J^iJ^i}(\omega,\mathbf 0)\) (include \(\sqrt{\gamma}\) in curved space).

**Wick rotation.** \(t\to -i\tau\); \(e^0_{(E)}= i e^0,\ e^i_{(E)}=e^i\); equivalently \(g^{(E)}_{00}=-g_{00},\ g^{(E)}_{0i}=0\).  
**Ledgers (integers) are unchanged under Wick.**

**Projectors & Stückelberg.** Massive spin‑1 completeness:
\[
\sum_{\lambda=1}^{3}\epsilon^\mu_{(\lambda)}(p)\,\epsilon^\nu_{(\lambda)}(p)
= g^{\mu\nu}+\frac{p^\mu p^\nu}{m^2}\quad\Rightarrow\quad\text{rest projector }{\rm diag}(0,1,1,1).
\]
Stückelberg split \(S_\mu=\hat S_\mu+\partial_\mu\pi/m\) with \(\partial\!\cdot\!\hat S=0\).

**Gauge fixing & BRST (concise).** Abelian: \(\mathcal L_{GF}=-(2\xi)^{-1}(\nabla\!\cdot\!A)^2\) (ghosts decouple).  
Non‑Abelian: \(\mathcal L_{GF}=-(2\xi)^{-1}(\nabla_\mu A^{A\mu})^2\), \(\mathcal L_{FP}=\bar c^A(-D_\mu D^\mu)^{AB}c^B\).

**Wilson & Chern–Simons.** \(W_R[\gamma]=(\dim R)^{-1}\mathrm{Tr}_R\,\mathcal P\exp(i g\oint_\gamma A)\).  
Define \(\mathcal A\equiv gA\) so that
\[
S_{CS}=\frac{k}{4\pi g^2}\int\mathrm{Tr}\Big(\mathcal A\wedge d\mathcal A+\tfrac{2}{3}\mathcal A\wedge\mathcal A\wedge\mathcal A\Big).
\]
Track integer level \(k\) together with the trace convention.

---

## 1) Geometry & Torsion (first‑order formalism; health policy)

**Cartan data.** \(T^a=De^a\), \(R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b\).  
Impose metricity (metric‑affine reduction): \(Q_{\alpha\mu\nu}=0\).

**Irreducible decomposition.**
\[
T_{\mu\nu\rho}=\tfrac13(t_\nu g_{\mu\rho}-t_\rho g_{\mu\nu})+\tfrac16\epsilon_{\mu\nu\rho\sigma}S^\sigma+q_{\mu\nu\rho},
\]
with \(t_\mu\equiv T^\nu{}_{\mu\nu}\), \(S_\mu\equiv \tfrac16\epsilon_{\mu\nu\rho\sigma}T^{\nu\rho\sigma}\), and \(q_{\mu\nu\rho}\) traceless and \(\epsilon\)-traceless.

**Health policy (P1 sentinel).** **Only the axial vector \(S_\mu\) propagates.** Keep \(t_\mu\) and \(q_{\mu\nu\rho}\) algebraic (or zero).  
This avoids spin‑2 ghosts and isolates the healthy spin‑1 torsion mode.

---

## 2) Fields & Action (bulk + boundary/ledger)

**Matter+gauge+gravity+axial torsion (minimal working form).**
\[
\boxed{\;
\begin{aligned}
\mathcal L_{\rm bulk}
&=\frac{1}{16\pi G}R
-\frac12\,\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})
-\frac14\,H_{\mu\nu}H^{\mu\nu}
+\frac12 m_S^2\,S_\mu S^\mu
- g_S\,S_\mu J_5^\mu \\[2pt]
&\quad -\frac12\,\partial_\mu\phi\,\partial^\mu\phi - V(\phi)
+\mathcal L_{\rm Dirac}+\mathcal L_{\rm Skyrme}\;,
\end{aligned}
}
\]
with \(H_{\mu\nu}\equiv \nabla_\mu S_\nu-\nabla_\nu S_\mu\), \(J_5^\mu\equiv \bar\psi\gamma^\mu\gamma^5\psi\), and  
\(\mathcal L_{\rm Skyrme}=\tfrac{\lambda}{4}\,\mathrm{Tr}([L_\mu,L_\nu][L^\mu,L^\nu])\) (positive \(\lambda\)).

**Boundary & topological bundle (ledger‑only).**  
- **GHY:** \(S_{GHY}=(8\pi G)^{-1}\int_{\partial\mathcal M}\sqrt{|h|}\,K\).  
  *Extrinsic curvature (ADM):* \(K_{ij}=\tfrac{1}{2N}\big(-\partial_t\gamma_{ij}+D_i N_j+D_j N_i\big)\).  
- **Nieh–Yan / Holst:** \(\mathcal N\!Y=d(e^a\wedge T_a)-e^a\wedge e^b\wedge R_{ab}\), and \(e^a\wedge e^b\wedge *R_{ab}/\gamma\).  
- **CS:** as in §0, with \(\mathcal A\equiv gA\).  
All topological pieces contribute to **integer ledgers** and do **not** modify bulk equations of motion.

---

## 3) Equations of Motion (Miller system) & Continuity

**Einstein (metric).** \(\displaystyle G_{\mu\nu}=8\pi G\,(T^{\rm matter}_{\mu\nu}+T^{\rm YM}_{\mu\nu}+T^{(S)}_{\mu\nu})\).  
Bianchi identity \(\nabla^\mu G_{\mu\nu}=0\Rightarrow \nabla^\mu T^{\rm total}_{\mu\nu}=0\).

**Axial torsion.** \(\displaystyle \nabla_\nu H^{\nu\mu}+m_S^2 S^\mu=g_S J_5^\mu,\qquad \nabla_\mu S^\mu=\frac{g_S}{m_S^2}\,\nabla_\mu J_5^\mu\).  
*Note:* if \(\nabla\!\cdot\!J_5\neq 0\) (e.g., explicit mass terms or topological inflow), the divergence is absorbed algebraically by \(S_\mu\).

**Yang–Mills.** \(D_\nu F^{\nu\mu}=J^\mu_{\rm gauge}\).  
**Scalar.** \(\Box\phi - V'(\phi)=0\).  
**Dirac.** \((i\gamma^\mu D_\mu-m_\psi - g_S \gamma^\mu\gamma^5 S_\mu)\psi=0\).

---

## 4) Stress–Energy, Hamiltonians & Positivity (sign‑locked)

**Yang–Mills.** \(T^{\rm YM}_{\mu\nu}=\mathrm{Tr}\!\left(F_{\mu\alpha}F_{\nu}{}^{\alpha}-\tfrac14 g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\right)\).

**Axial torsion (Proca‑type).**
\[
T^{(S)}_{\mu\nu}
= H_{\mu\alpha}H_\nu{}^\alpha
-\tfrac14 g_{\mu\nu}H_{\alpha\beta}H^{\alpha\beta}
+ m_S^2\!\left(S_\mu S_\nu-\tfrac12 g_{\mu\nu}S_\alpha S^\alpha\right).
\]

**Scalar.** \(T^{(\phi)}_{\mu\nu}=\partial_\mu\phi\,\partial_\nu\phi-\tfrac12 g_{\mu\nu}\partial_\alpha\phi\,\partial^\alpha - g_{\mu\nu}V(\phi)\).  
**Dirac (Belinfante).** \(T^{(\psi)}_{\mu\nu}=\tfrac{i}{4}\big[\bar\psi\gamma_{(\mu}\!\!\stackrel{\leftrightarrow}{D}_{\nu)}\psi\big]-g_{\mu\nu}\mathcal L_{\rm Dirac}\).

**Positivity check.** With \((-,+,+,+)\): \(T^{(\phi)}_{00}=\tfrac12\dot\phi^2+\tfrac12|\nabla\phi|^2+V(\phi)\ge 0\) for \(V\ge 0\).  
**Hamiltonian densities (flat frame).**  
\(E^i_S\equiv H^{i0}\), \(B^i_S \equiv \tfrac12\epsilon^{ijk}H_{jk}\).  
\(\displaystyle T^{(S)}_{00}=\tfrac12(\mathbf E_S^2+\mathbf B_S^2)+\tfrac12 m_S^2(S_0^2+\mathbf S^2)\).  
\(\displaystyle T^{\rm YM}_{00}=\tfrac12\,\mathrm{Tr}(\mathbf E^2+\mathbf B^2)\).

---

## 5) Causality & Green’s Functions (response‑first)

**Momentum‑space propagator (Proca).**  
\[
D_{\mu\nu}(k)=\frac{-\,g_{\mu\nu}+\dfrac{k_\mu k_\nu}{m^2}}{k^2-m^2+i0^+}\,,\qquad
k^2\equiv g^{\alpha\beta}k_\alpha k_\beta = -\omega^2+\mathbf k^2.
\]

**Retarded pole (frequency‑momentum).** \(\displaystyle G^R(\omega,\mathbf k)=[-(\omega+i0^+)^2+\mathbf k^2+m^2]^{-1}\) (analytic for \(\mathrm{Im}\,\omega>0\)).

**Time‑domain kernel (3+1D).**  
\(\displaystyle G^R(t,r)=\frac{\Theta(t)}{4\pi r}\!\left[\delta(t-r)-m\,\frac{J_1\!\big(m\sqrt{t^2-r^2}\big)}{\sqrt{t^2-r^2}}\,\Theta(t-r)\right]\).

**Curved‑space Hadamard form (local).**  
For a scalar‑like sector: \(G^R(x,x')=\Theta(\Delta t)\big[U(x,x')\,\delta(\sigma)+V(x,x')\,\Theta(-\sigma)\big]\),  
where \(\sigma\) is Synge’s world function. The **tail term** \(V\) encodes curvature‑driven inside‑cone support.

**Static Yukawa (spatial).** \(\displaystyle G(\mathbf r)=-(4\pi r)^{-1}e^{-m r}\).

**Principal symbol (Proca operator).** \(P^\mu{}_\nu(\xi)=-(\xi^2)\delta^\mu{}_\nu+\xi^\mu\xi_\nu\) — hyperbolic on globally‑hyperbolic backgrounds.  
**Microcausality.** Support on/inside the forward lightcone; subluminal characteristics.

---

## 6) Einstein–Cartan Decoupling (heavy‑field integrate‑out)

For \(m_S^2\gg \partial^2\), solve algebraically
\[
S_\mu \simeq \frac{g_S}{m_S^2}\,J_{5\mu}\;,
\]
then back‑substitute:
\[
\boxed{\,\Delta\mathcal L_{\rm eff}= -\frac{g_S^2}{2 m_S^2}\,J_5^\mu J^5_\mu + O(\partial^2/m_S^4)\, .}
\]
**PPN‑clean GR** in the strict decoupling limit \(m_S\to\infty\) or \(g_S\to 0\):  
no new long‑range forces; torsion yields only short‑range, spin‑dependent Yukawa interactions.

---

## 7) Global & Topological Structure (integer ledgers)

**Wilson loops.** \(W_R[\gamma]=(\dim R)^{-1}\mathrm{Tr}_R\,\mathcal P\exp(i g\oint_\gamma A)\); record center class \(z_\gamma\in Z(G)\).

**Pontryagin integer.** \(\displaystyle \nu_G=(8\pi^2)^{-1}\!\int\!\mathrm{Tr}(F\wedge F) \in \mathbb Z\).

**Chern–Simons (explicit \(g\)).** Using \(\mathcal A\equiv gA\),
\[
S_{CS}=\frac{k}{4\pi g^2}\int\!\mathrm{Tr}\!\left(\mathcal A\wedge d\mathcal A+\tfrac23\mathcal A\wedge\mathcal A\wedge\mathcal A\right),
\]
so **level \(k\)** is an integer independent of \(g\) and the trace convention is explicit.

**Nieh–Yan and Holst.** Included in \(S_{\rm topo}\) and tracked in the integer ledger; they do **not** affect bulk EOM.  
**Wick invariance.** Ledger integers do not change under Wick rotation.

---

## 8) Gauge Fixing, BRST & Ghosts (curved‑space hygiene)

**Abelian.** \(\mathcal L_{GF}=-(2\xi)^{-1}(\nabla\!\cdot\!A)^2\); ghosts decouple with \(\mathcal L_{FP}=\bar c(-\nabla^2)c\).

**Non‑Abelian.** \(\mathcal L_{GF}=-(2\xi)^{-1}(\nabla_\mu A^{A\mu})^2\), \(\mathcal L_{FP}=\bar c^{A}(-D_\mu D^\mu)^{AB}c^B\),  
with adjoint Laplacian \(D_\mu^{AB}=\nabla_\mu\delta^{AB}+g f^{ACB}A_\mu^C\).

---

## 9) Projectors & UV Diagnostics (health checks)

**Massive spin‑1 (Proca) projector.**  
\(\displaystyle \sum_{\lambda=1}^{3}\epsilon^\mu_{(\lambda)}\epsilon^\nu_{(\lambda)}=g^{\mu\nu}+p^\mu p^\nu/m^2 \Rightarrow\) rest projector \(\mathrm{diag}(0,1,1,1)\).

**Barnes–Rivers (rank‑2).** Build \(P^{(2)},P^{(1)},P^{(0s)},P^{(0w)}\) with \(\theta_{\mu\nu}=g_{\mu\nu}-p_\mu p_\nu/p^2\), \(\omega_{\mu\nu}=p_\mu p_\nu/p^2\).  
**Residues ≥ 0** in all spin sectors; do **not** propagate the \(q\)‑sector.

**Stückelberg.** \(S_\mu=\hat S_\mu+\partial_\mu\pi/m\) (transverse \(\hat S\)) clarifies UV counting and isolates healthy poles.

---

## 10) Response, Kubo & Positivity (analyticity tests)

**Spectral positivity & passivity.** \(\rho(\omega,\mathbf k)\ge 0\); \(\mathrm{Im}\,G^R(\omega,0)/\omega\ge 0\) for \(\omega>0\).  
**DC limit.** In curved backgrounds, include \(\sqrt{\gamma}\); take \(\mathbf k\to 0\) then \(\omega\to 0^+\).

---

## 11) Harmonic Identities (spherical sector) & Scope Separation

**\(S^2\) harmonics.** \(\int Y_{\ell m}^*Y_{\ell' m'}\,d\Omega=\delta_{\ell\ell'}\delta_{mm'}\); \(\nabla^2 Y_{\ell m}=-\ell(\ell+1)Y_{\ell m}\).  
Vector/tensor bases: \(Y^{E}_{(\ell m)i}=D_i Y_{\ell m}\), \(Y^{B}_{(\ell m)i}=\epsilon_i{}^{j}D_j Y_{\ell m}\); tensor pieces from \(D_iD_j Y_{\ell m}\) (trace‑removed).

**Guardrail.** Use these **only** in spherical Coulomb problems. Do **not** mix with axial/tube holonomy formulas.

---

## 12) Units & Dimensions (hat‑map restored at the end)

Natural units inside (\(\hbar=c=1\)):  
\([\partial]=1,\ [A]=1,\ [F]=2,\ [S]=1,\ [\psi]=3/2,\ [\phi]=1,\ [g]=0,\ [G^{-1}]=2\).  
Restore physical units at the end via the UGFT hat‑map (e.g., \(\hat m_S=m_S\,\hbar/c\), \(\hat E=E\,\hbar\) depending on normalization).

---

## 13) Observables (hooks for phenomenology)

**Spin–spin Yukawa (polarized matter).** \(\displaystyle V_{SS}(r)\propto \frac{g_S^2}{4\pi}\,\frac{e^{-m_S r}}{r}\).  
Averages to zero at leading order for unpolarized macroscopic bodies.

**Gravitational waves.** Minimal dispersion/polarization mixing; parity‑odd birefringence may arise when allowed by ledgered topological terms (e.g., CS/Holst).  
Templates must respect the causal kernel above and PPN/GW constraints in the decoupling corner.

**Cosmology (note).** Axial torsion treated algebraically behaves like a **spin‑stiff** component \(\rho_{\rm spin}\propto a^{-6}\); check compatibility with early‑universe bounds.

**PPN clean limit.** Reproduce GR (two tensor polarizations; standard PPN parameters) for \(m_S\!\to\!\infty\) or \(g_S\!\to\!0\).

---

## 14) Recipes & Viability Bar (use this checklist every time)

**Recipes (R1–R5).**  
**R1:** Begin with the header in §0.  
**R2:** Wick audit: apply the tetrad/metric map; confirm ledgers unchanged.  
**R3:** Response/Kubo: ensure retarded analyticity; use the DC order of limits.  
**R4:** Heavy‑field integrate‑out: keep through \(O(\partial^2/m^4)\).  
**R5:** UV/projectors: use BR/Stückelberg; check residues in each spin channel.

**Viability Bar (VB1–VB6).**
- **VB1 — No ghosts/tachyons.** Correct kinetic signs; \(m_S^2>0\); do **not** propagate \(q\); projector residues ≥ 0.
- **VB2 — Causality/sub‑luminal.** Hyperbolic principal symbol; retarded support only.
- **VB3 — Positivity/analyticity.** \(T_{00}\ge 0\) (this signature); spectral positivity and passivity.
- **VB4 — Radiative stability.** Use Larin \(\gamma^5\); preserve the healthy corner under 1‑loop RG (no tuned relations that fail under flow).
- **VB5 — GR decoupling.** EC contact as in §6; clean PPN/GW behavior as \(m_S\!\to\!\infty\) or \(g_S\!\to 0\).
- **VB6 — Global/topology.** Ledger integers (Pontryagin, CS, Nieh–Yan/Holst) stable; boundary‑only contributions; CS uses explicit \(g\) normalization.

---

### Quick Kernel One‑Liners (at a glance)
- **Momentum‑space Proca:** \(D_{\mu\nu}(k)=\dfrac{-g_{\mu\nu}+k_\mu k_\nu/m^2}{k^2-m^2+i0^+}\).  
- **Retarded pole:** \(G^R(\omega,\mathbf k)=[-(\omega+i0^+)^2+\mathbf k^2+m^2]^{-1}\).  
- **Time domain:** \(G^R(t,r)=\dfrac{\Theta(t)}{4\pi r}\!\left[\delta(t-r)-m\dfrac{J_1(m\sqrt{t^2-r^2})}{\sqrt{t^2-r^2}}\,\Theta(t-r)\right]\).  
- **Static Yukawa:** \(G(\mathbf r)=-(4\pi r)^{-1}e^{-mr}\).  
- **Spherical delta:** \(\nabla^2(1/r)=-4\pi\,\delta^{(3)}(\mathbf r)\), \(\delta^{(3)}(\mathbf r)=\delta(r)/(4\pi r^2)\).  
- **Hadamard (curved):** \(G^R=\Theta(\Delta t)\big[U\,\delta(\sigma)+V\,\Theta(-\sigma)\big]\) (tail \(V\) encodes curvature).

---

### Scope Guardrails (never violate)
- Do **not** mix spherical Coulomb identities with axial/tube holonomy equations.  
- For strictly static electric fields, prefer **Coulomb gauge**; avoid pitfalls of \(A_0=0\) with time‑independent fields.  
- Do **not** open additional spin‑connection kinetic sectors unless they are manifestly ghost‑free and heavy enough to decouple.
