# Chapter Zero — UGFT Operating Conventions and Practices

**Purpose.** This chapter is the operating system (OS) for UGFT. It fixes index sets, signs, duals, measures, algebra normalizations, transform/response rules, torsion and metric‑affine structure, integer ledgers, and the operational recipes that make derivations reproducible with minimal cognitive load. All later chapters import these choices; nothing here is re‑decided elsewhere.  
**Governance rule.** Any change to Chapter 0 requires (i) a clear justification, (ii) a worked micro‑example, and (iii) updates to every affected checklist. *No downstream chapter may locally override a Chapter‑0 lock.* [Lock: Gov]

---

## 0.1 Global sentinels (non‑negotiable choices, with alternatives and rationale)

**Signature (chosen).** Minkowski $(-,+,+,+)$. *Why:* aligns with QFT pole structure, spectral positivity, and our Kubo/retarded conventions. *Alt:* $(+,-,-,-)$ is convertible but error‑prone (many kinetic/Hodge signs flip).  [Lock: Sig]

**Orientation & Levi–Civita (chosen).** $\epsilon_{0123}=+\sqrt{|g|}$, $\epsilon^{0123}=+1/\sqrt{|g|}$, $[0123]=+1$.  
**Notation lock (no drift).** $`\epsilon_{\mu\nu\rho\sigma}`$ = covariant Levi–Civita tensor; $`[\mu\nu\rho\sigma]`$ = alternating symbol.
$`
\epsilon_{\mu\nu\rho\sigma}=\sqrt{|g|}\,[\mu\nu\rho\sigma],\qquad
\epsilon^{\mu\nu\rho\sigma}=\frac{[\mu\nu\rho\sigma]}{\sqrt{|g|}},
`$
with $[0123]=+1$. Do **not** use $`\varepsilon`$; always $`\epsilon`$.  
**Contraction test (must hold).** $\epsilon^{\mu\nu\rho\sigma}\epsilon_{\alpha\nu\rho\sigma}=-3!\,\delta^\mu{}_\alpha$.  [Lock: Eps]

**Hodge star (chosen).** In 4D Lorentzian: $` *^2=(-1)^{p(4-p)+1}`$. After Wick: $`(*_E)^2=(-1)^p`$.  
**Derived identity:** $`F\wedge *F=\tfrac12 F_{\mu\nu}F^{\mu\nu}\,d^4x`$. *Alt pitfall:* never use Lorentzian $*$ rules in Euclidean manipulations.  [Lock: Hodge]

**Two traces, two worlds (chosen).** $`\mathrm{Tr}`$ = gauge traces with $`\mathrm{Tr}(T^AT^B)=\delta^{AB}`$; $`\mathrm{tr}`$ = spinor/Lorentz traces (e.g., $`\mathrm{tr}\,\mathbb 1_4=4`$). *Alt:* $`\mathrm{Tr}(T^AT^B)=\tfrac12\delta^{AB}`$ appears in the literature; cross‑maps in §0.10/§0.21.  [Lock: Traces]

**Couplings explicit (chosen).** $F=dA+g\,A\wedge A$, $D_\mu=\partial_\mu+i g\,A_\mu^A T^A$.  
*Why:* makes AB phases, RG flow, and ledger bookkeeping transparent.  [Lock: g‑explicit]

**Canonical kinetic sentinels (chosen).**  
- **Yang–Mills:** $\boxed{\ \mathcal L_{YM}=-\tfrac12\,\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})\ }$ with $\mathrm{Tr}(T^AT^B)=\delta^{AB}$. **Cross‑map:** $-\tfrac14 F^A_{\mu\nu}F^{A\mu\nu}$ ↔ $\mathrm{Tr}=\tfrac12\delta^{AB}$.  [Lock: YM]  
- **Scalar (σ‑term):** $\boxed{\ \mathcal L_\sigma=-\tfrac12\,\partial_\mu\phi\,\partial^\mu\phi - V(\phi)\ }$ → $T_{00}^{(\phi)}=\tfrac12\dot\phi^2+\tfrac12|\nabla\phi|^2+V(\phi)\ge0$.  [Lock: Sigma]  
- **Skyrme:** $\boxed{\ \mathcal L_{\mathrm{Skyrme}}=\tfrac{\lambda}{4}\,\mathrm{Tr}([L_\mu,L_\nu][L^\mu,L^\nu])\ }$, $\lambda>0$.  [Lock: Skyrme]

**Integer ledgers (always recorded).** Quantized data $(c_1,\nu_G,\nu_R,k,\ldots)$ and Wilson center classes $z_\gamma\in Z(G)$ are tracked and remain unchanged under Wick rotation.  [Lock: Ledger]

**Checklist 0.1:** Sig; Eps; Hodge; Traces; g‑explicit; YM/σ/Skyrme; Ledger.

---

## 0.2 Indices, frames, forms

**Indices.** Spacetime $\mu,\nu$; spatial $i,j$; tangent $a,b$; adjoint $A,B$; rep $I,J$.  
**Tetrad ladder.** $`g_{\mu\nu}=\eta_{ab}e^a{}_\mu e^b{}_\nu`$; $`V^a=e^a{}_\mu V^\mu`$; $`V_\mu=e^a{}_\mu\eta_{ab}V^b`$.  
**Exterior calculus.** $`d^2=0`$; $`\alpha\wedge\beta=(-1)^{pq}\beta\wedge\alpha`$; $`\alpha\wedge *\beta=\langle\alpha,\beta\rangle\,\mathrm{vol}_4`$.  
**Symmetrization (weight one).** $A_{(\mu\nu)}, A_{[\mu\nu]}, A_{(\mu|\alpha|\nu)}$.  [Lock: Frames&Forms]

**Checklist 0.2:** tetrad ladder; weight‑one sym; wedge/inner‑product.

---

## 0.3 Measures, deltas, and foliation (ADM)

**Volumes.** $`\mathrm{vol}_4=\sqrt{|g|}\,d^4x`$; spatial $`dV=\sqrt{\gamma}\,d^3x`$.  
**ADM & extrinsic curvature.** $(N,N^i,\gamma_{ij})$, $K_{ij}=\frac{1}{2N}(\dot\gamma_{ij}-D_iN_j-D_jN_i)$ (sign matches §0.12).  
**Covariant delta (foliation‑independent).**
$`
\boxed{\ \delta^{(4)}_g(x,x_0)=\frac{\delta(t-t_0)}{N(t_0,\mathbf x_0)}\,\delta^{(3)}_\gamma(\mathbf x,\mathbf x_0),\qquad \int d^4x\,\sqrt{|g|}\,\delta^{(4)}_g=1\ } \quad\text{[Lock: ADM‑δ]}
`$

**Spherical identities.** $\nabla^2(1/r)=-4\pi\,\delta^{(3)}(\mathbf r)$; $\delta^{(3)}(\mathbf r)=\delta(r)/(4\pi r^2)$.

**Checklist 0.3:** ADM‑δ with $N$; $\sqrt\gamma$ in 3D; $K_{ij}$ sign ↔ §0.12.

---

## 0.4 Gauge algebra, connections, Wilson data

**Lie algebra.** Hermitian $T^A$, $[T^A,T^B]=i f^{ABC}T^C$, $\mathrm{Tr}(T^AT^B)=\delta^{AB}$.  
**Connections & strength.** $D_\mu=\partial_\mu+i g\,A_\mu^A T^A$; $F=dA+g\,A\wedge A$; $F_{\mu\nu}^A=\partial_\mu A_\nu^A-\partial_\nu A_\mu^A+g f^{ABC}A_\mu^B A_\nu^C$.  
**Wilson loops (normalization fixed).**
$`
\boxed{\ W_R[\gamma]=\frac{1}{\dim R}\,\mathrm{Tr}_R\,\mathcal P\exp\!\Big(i g\oint_\gamma A\Big)\ },\quad z_\gamma\in Z(G). \quad\text{[Lock: Wilson]}
`$
**Checklist 0.4:** $g$ explicit; trace norm fixed; Wilson norm fixed; $z_\gamma$ logged.

---

## 0.5 Gravity, torsion, contorsion (first‑order form)

**Cartan structure.** $`T^a=De^a=de^a+\omega^a{}_b\wedge e^b`$; $`R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b`$.  
**Contorsion.** $`K^\rho{}_{\mu\nu}=\tfrac12(T^\rho{}_{\mu\nu}-T_\mu{}^\rho{}_\nu+T_\nu{}^\rho{}_\mu)`$; $`T^\rho{}_{\mu\nu}=2K^\rho{}_{[\mu\nu]}`$.  
**Irreducible torsion.** $`t_\mu`$, $`S_\mu=\tfrac{1}{6}\epsilon_{\mu\nu\rho\sigma}T^{\nu\rho\sigma}`$, $`q_{\mu\nu\rho}`$ (traceless). *Policy:* do not propagate $q$ (spin‑2 ghost hazard).  
**Bianchi.** $DT^a=R^a{}_b\wedge e^b,\quad DR^a{}_b=0$.  [Lock: Bianchi]

**Checklist 0.5:** $T=De$; $R=d\omega+\omega\wedge\omega$; $K$–$T$; irreps; Bianchi.

---

## 0.6 Metric‑affine sector (nonmetricity and reduction)

**Nonmetricity.** $Q_{\alpha\mu\nu}\equiv -\nabla_\alpha g_{\mu\nu}$.  
**Impose metricity.** Add $\Lambda^{\alpha\mu\nu}Q_{\alpha\mu\nu}$; varying $\Lambda$ enforces $Q=0$, reducing to Riemann–Cartan torsion sector.  
**Ledgers.** Quantized data unchanged.  [Lock: MA‑reduce]

**Checklist 0.6:** $Q$ defined; constraint declared; ledgers preserved.

---

## 0.7 Spinors and minimal torsion coupling

**Clifford algebra.** $\{\gamma^a,\gamma^b\}=2\eta^{ab}$; $\gamma^\mu=e_a{}^\mu\gamma^a$; $\gamma^{ab}=\tfrac12[\gamma^a,\gamma^b]$; $\gamma^5=i\gamma^0\gamma^1\gamma^2\gamma^3$; $\bar\psi=\psi^\dagger\gamma^0$.  
**Spinor derivative & commutator.**
$`
D_\mu\psi=\Big(\partial_\mu+\tfrac14\,\omega_\mu{}^{ab}\gamma_{ab}+i g\,A_\mu^A T^A\Big)\psi,\qquad
[D_\mu,D_\nu]\psi=\tfrac14 R_{\mu\nu}{}^{ab}\gamma_{ab}\psi+i g\,F_{\mu\nu}\psi.
`$
**Minimal torsion source.** Only axial $S_\mu$ couples at tree level to $J_5^\mu=\bar\psi\gamma^\mu\gamma^5\psi$; $t_\mu$ is unsourced.  
**Euclidean Clifford (Hermitian).** $\{\gamma_E^\mu,\gamma_E^\nu\}=2\delta^{\mu\nu}$, $(\gamma_E^\mu)^\dagger=\gamma_E^\mu$, $\gamma_E^5=\gamma_E^1\gamma_E^2\gamma_E^3\gamma_E^4$ with $(\gamma_E^5)^\dagger=\gamma_E^5$. Map $\gamma_E^4=\gamma^0$, $\gamma_E^i=i\,\gamma^i$ so $\bar\psi\,i\gamma^\mu D_\mu\psi\mapsto \bar\psi_E\,\gamma_E^\mu D_\mu\psi_E$ and $S_E$ is real/positive in the free limit.  [Lock: GammaE]  
**Dim‑reg $\gamma^5$.** Larin‑style: treat $\gamma^5$ as 4D; in $d=4-2\epsilon$ replace axial currents by the $\epsilon$‑tensor form and apply finite $Z_5$ to restore Ward identities.  [Lock: Larin]

**Checklist 0.7:** $\gamma^5$ def; commutator signs; axial sourcing; GammaE; Larin.

---

## 0.8 Fourier, retarded, Kubo

**Fourier pair.**  
$\tilde f(\omega,\mathbf k)=\int dt\,d^3x\,e^{\,i(\omega t-\mathbf k\cdot\mathbf x)}f$,  
$f(t,\mathbf x)=\int\!\frac{d\omega\,d^3k}{(2\pi)^4}e^{-i(\omega t-\mathbf k\cdot\mathbf x)}\tilde f$.  [Lock: FT]  
**Delta identities (phase‑consistent).**  
$\displaystyle \int \frac{d\omega\,d^3k}{(2\pi)^4}e^{-i(\omega t-\mathbf k\cdot\mathbf x)}=\delta(t)\,\delta^{(3)}(\mathbf x)$,  
$\displaystyle \int dt\,d^3x\,e^{\,i(\omega t-\mathbf k\cdot\mathbf x)}=(2\pi)^4\delta(\omega)\,\delta^{(3)}(\mathbf k)$.  [Lock: Delta]  
**Plancherel.** $\displaystyle \int dt\,d^3x\,|f|^2=\int\frac{d\omega\,d^3k}{(2\pi)^4}|\tilde f|^2$.  [Lock: Plancherel]  
**Retarded correlator.** $G^R_{AB}(t)=-i\,\theta(t)\langle[A(t),B(0)]\rangle$; $\rho=-2\,\Im G^R$.  [Lock: Ret]  
**DC Kubo.** $\sigma_{DC}=\lim_{\omega\to0^+}\frac{1}{\omega}\Im G^R_{J^iJ^i}(\omega,\mathbf 0)$, with $\sqrt\gamma$ in curved space.  [Lock: Kubo]

**Checklist 0.8:** FT; Delta/Plancherel; $i0^+$; $\sqrt\gamma$ in curved.

---

## 0.9 Wick rotation (Euclidean rules) — path‑integral weight and map

**Path‑integral weight & continuation.**  
$`Z=\int \mathcal D\Phi\,e^{\,iS_L[\Phi]}`$,\quad $`S_E[\Phi_E]\equiv -i\,S_L[\Phi]\big|_{t\to -i\tau}`$,\quad $`Z=\int \mathcal D\Phi_E\,e^{-S_E[\Phi_E]}`$.  
With $`\boxed{\ g^{\mu\nu}\nabla_\mu\nabla_\nu}`$ (sig $`(-,+,+,+)`$): $`-\tfrac12\,\partial_\mu\phi\,\partial^\mu\phi\mapsto +\tfrac12(\partial\phi)_E^2`$, $`-\tfrac12\,\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})\mapsto +\tfrac12\,\mathrm{Tr}(F_{E,\mu\nu}F_E^{\mu\nu})`$.  [Lock: Wick]

**Tetrad map (chosen).** $`e^{0}_{(E)}=i\,e^{0}`$, $`e^{i}_{(E)}=e^{i}`$ → $`g^{(E)}_{\mu\nu}=\delta_{ab}\,e^a_{(E)\mu}e^b_{(E)\nu}`$ (positive‑definite).  
**Equivalent metric line (when cross‑terms vanish).** $`g^{(E)}_{00}=-g_{00}`$, $`g^{(E)}_{0i}=0`$, $`g^{(E)}_{\mu\nu}=\delta_{\mu\nu}`$.  
**Duals & epsilon.** $`(*_E)^2=(-1)^p`$; $`\epsilon^{0123}_{(E)}=+1`$, $`\epsilon_{(E)0123}=+\sqrt{g_E}`$.  
**Ledgers.** $(c_1,\nu_G,\nu_R,k,\ldots)$ unchanged.

**Checklist 0.9:** Wick map; Euclid $*$; Euclid $\epsilon$; ledgers unchanged.

---

## 0.10 Integer ledgers & Chern–Simons normalization

**Pontryagin integer.**  
$\displaystyle \nu_G=\frac{1}{8\pi^2}\int \mathrm{Tr}(F\wedge F)=\frac{1}{32\pi^2}\int d^4x\,\epsilon^{\mu\nu\rho\sigma}F^A_{\mu\nu}F^A_{\rho\sigma}\in\mathbb Z.$  [Lock: Pontryagin]

**Chern–Simons (with explicit $g$).**  
$\displaystyle S_{CS}=\frac{k}{4\pi}\int \mathrm{Tr}\big(A\wedge dA+\tfrac{2}{3}g\,A\wedge A\wedge A\big),\quad k\in\mathbb Z.$  
Under $A\mapsto U^{-1}AU+\tfrac{i}{g}U^{-1}dU$, the integer $k$ is independent of $g$. Defining $\mathcal A\equiv gA$ gives
$`
S_{CS}=\frac{k}{4\pi g^2}\int \mathrm{Tr}\!\big(\mathcal A\wedge d\mathcal A+\tfrac{2}{3}\mathcal A\wedge\mathcal A\wedge\mathcal A\big).
`$
**Trace/level cross‑table.**

| Gauge trace convention | $\mathrm{Tr}(T^AT^B)$ | Level mapping |
|---|---|---|
| UGFT (this chapter) | $\delta^{AB}$ | $k_{\rm UGFT}=2\,k_{(\mathrm{Tr}=\tfrac12\delta)}$ |
| Textbook alt. | $\tfrac12\delta^{AB}$ | $k_{(\mathrm{Tr}=\tfrac12\delta)}=\tfrac12\,k_{\rm UGFT}$ |

 [Lock: CS]

**Checklist 0.10:** $\nu_G\in\mathbb Z$; $k$ recorded with trace; $g$‑independence noted.

---

## 0.11 Torsion dynamics (baseline and diagnostics)

**Axial Proca sentinel (sign‑locked).**  
$\displaystyle \mathcal L_S=-\tfrac14 H_{\mu\nu}H^{\mu\nu}+\tfrac12 m_S^2 S_\mu S^\mu- g_S S_\mu J_5^\mu,\quad H_{\mu\nu}=\partial_\mu S_\nu-\partial_\nu S_\mu.$  [Lock: Axial‑Proca]

**Baseline (axial‑only Proca).** $(\Box+m_S^2)S_\mu=g_S\,J_5^\mu$; causal retarded pole; static Yukawa; heavy‑field EC limit $\Delta\mathcal L_{\rm eff}=-(g_S^2/2m_S^2)J_5^2+O(m_S^{-4})$.  
**Conditional spin‑connection (curvature‑squared).** Extra spin‑2 ghost unless tuned/decoupled at high mass; keep spin‑1 sectors massive/healthy; do not propagate $q$.

**Checklist 0.11:** hyperbolic; Yukawa; EC sign/factor; spin‑2 ghost absent.

---

## 0.12 Gravity action and boundary term (sign‑locked)

$S_{EH}=\frac{1}{16\pi G}\int d^4x\,\sqrt{|g|}\,R$,  
$S_{GHY}=\frac{1}{8\pi G}\int_{\partial\mathcal M} d^3x\,\sqrt{|h|}\,K$ with outward unit normal.  
**Stokes orientation (matches GHY).** $\int_{\mathcal M} d\omega=\int_{\partial\mathcal M}\iota_n\omega$. ADM $K_{ij}$ in §0.3 matches this sign.  [Lock: Stokes]

**Checklist 0.12:** $K_{ij}$ sign; Stokes orientation; include boundary terms on variation.

---

## 0.13 Gauge fixing and BRST (concrete forms)

**Abelian gauge.** $\mathcal L_{GF}= -\frac{1}{2\xi}(\nabla_\mu A^\mu)^2$; ghosts decouple: $\mathcal L_{FP}=\bar c\,(-\nabla^2)\,c$.  
**Non‑Abelian (curved).** $\mathcal L_{GF}= -\frac{1}{2\xi}(\nabla_\mu A^{A\mu})^2$, $\mathcal L_{FP}=\bar c^{A}\,(-D_\mu D^\mu)^{AB}c^{B}$, $D_\mu^{AB}=\nabla_\mu\delta^{AB}+g\,f^{ACB}A_\mu^{C}$.  
**Adjoint Laplacian (notation lock).** $(\mathcal D^2 X)^A\equiv D_\mu^{AB}D^{\mu,BC}X^C$; Lorentzian $g^{\mu\nu}D_\mu D_\nu$, Euclidean $\delta^{\mu\nu}D_\mu D_\nu$.  [Lock: AdjLap]  
**BRST.** $sA_\mu=D_\mu c$, $sc=-\tfrac12 g[c,c]$, $s\bar c=B$, $sB=0$, $s^2=0$.  [Lock: BRST]

**Checklist 0.13:** gauge choice; FP operator covariant; AdjLap; BRST nilpotent.

---

## 0.14 Response‑first axioms (kernel $\rightarrow$ local EFT)

**Causality.** $G^R$ analytic for $\Im\omega>0$; support only for $t>0$.  
**Positivity.** $\rho(\mu^2,\mathbf k)\ge 0$;  
$G^R(\omega,\mathbf k)=\int_0^\infty d\mu^2\,\rho(\mu^2,\mathbf k)\,[\!-(\omega+i0^+)^2+\mathbf k^2+\mu^2]^{-1}$.  
**Passivity.** $\Im G^R(\omega,\mathbf 0)/\omega\ge 0$ for $\omega>0$.  
**Reconstruction.** Narrow poles ↔ local fields; gapped continua ↔ derivative expansions.  [Lock: Resp]

**Checklist 0.14:** positivity; passivity; reconstruction.

---

## 0.15 Variation identities and stress–energy (sign‑locked)

**IBP.** $\int \sqrt{|g|}\,A\,\nabla_\mu B^\mu=-\int \sqrt{|g|}\,(\nabla_\mu A)B^\mu+\text{bdy}$.  
**Hodge variation.** Fixed $g$: $`\delta(*\alpha)=*(\delta\alpha)`$. Varying $g$: propagate $\delta g$ through $\epsilon$ and contractions.

**Stress–energy (standard).**  
$T_{\mu\nu}^{(S)}=H_{\mu\alpha}H_\nu{}^\alpha-\tfrac14 g_{\mu\nu}H^2+m_S^2(S_\mu S_\nu-\tfrac12 g_{\mu\nu}S^2)$;  
$T_{\mu\nu}^{(YM)}=\mathrm{Tr}\big(F_{\mu\alpha}F_\nu{}^\alpha-\tfrac14 g_{\mu\nu}F^2\big)$;  
$\boxed{\ T_{\mu\nu}^{(\phi)}=\partial_\mu\phi\,\partial_\nu\phi-\tfrac12 g_{\mu\nu}\,\partial_\alpha\phi\,\partial^\alpha\phi-g_{\mu\nu}V(\phi)\ }$.  [Lock: Tμν]

**Checklist 0.15:** IBP/bdy; Hodge var; positivity via these forms.

---

## 0.16 Projectors, polarization sums, Stückelberg (UV diagnostics)

**Massive spin‑1 polarization sum.**
$`
\boxed{\ \sum_{\lambda=1}^{3}\epsilon^{\mu}_{(\lambda)}(p)\,\epsilon^{\nu}_{(\lambda)}(p)= g^{\mu\nu}+\frac{p^{\mu}p^{\nu}}{m^2}\equiv \Pi^{\mathrm T\,\mu\nu}(p)\ } \Rightarrow \Pi^{\mathrm T}=\mathrm{diag}(0,1,1,1)\ \text{in rest frame}.
`$
[Lock: Proj‑1]

**Barnes–Rivers projectors (rank‑2).** With $\theta_{\mu\nu}=g_{\mu\nu}-p_\mu p_\nu/p^2$, $\omega_{\mu\nu}=p_\mu p_\nu/p^2$:  
$P^{(2)}, P^{(1)}, P^{(0\!-\!s)}, P^{(0\!-\!w)}$ as standard. *Usage:* for $p^2\neq0$; after Wick $p^2\to -k_E^2$; handle $p^2\to0$ by limits.  [Lock: BR]

**Stückelberg (vectors).** $`S_\mu=\hat S_\mu+\partial_\mu\pi/m`$, $`\partial\!\cdot\!\hat S=0`$; exposes longitudinal power counting; residues positive in physical sectors.  [Lock: Stk]

**Checklist 0.16:** residues positive; spin‑2 projected out; Stückelberg used.

---

## 0.17 Spherical harmonics (scalar/vector/tensor)

**Scalar.** $`\int Y_{\ell m}^*Y_{\ell' m'}\,d\Omega=\delta_{\ell\ell'}\delta_{mm'}`$; $`\nabla^2 Y_{\ell m}=-\ell(\ell+1)Y_{\ell m}`$.  
**Vector (on $S^2$).** $`Y^{E}_{(\ell m)i}=D_i Y_{\ell m}`$, $`Y^{B}_{(\ell m)i}=\epsilon_i{}^{j}D_j Y_{\ell m}`$; indices via $\gamma_{ij}$.  
**Tensor (on $S^2$).** Trace‑removed parts from $D_iD_j Y_{\ell m}$.  
**Levi–Civita on $S^2$.** $\epsilon_{ij}=\sqrt{\gamma}\,\hat\epsilon_{ij}$, $\hat\epsilon_{\theta\phi}=+1$; raise/lower by $\gamma_{ij}$.  [Lock: S2‑Eps]

**Checklist 0.17:** orthogonality; $S^2$ epsilon normalization.

---

## 0.18 Units, hats, mass dimensions

**4D dimensions.** $[\partial]=1,\ [A]=1,\ [F]=2,\ [\psi]=\tfrac32,\ [g]=0,\ [\phi]=1,\ [e]=0,\ [\omega]=1,\ [T]=1,\ [R]=2,\ [G^{-1}]=2$.  
**Hat map.** Choose $(\Lambda_{UGFT},\ell_{UGFT})$: $\hat x=x/\ell_{UGFT}$, $\hat A=A/\Lambda_{UGFT}$, $\hat\psi=\psi/\Lambda_{UGFT}^{3/2}$, $\hat\phi=\phi/\Lambda_{UGFT}$, $\hat\omega=\omega/\Lambda_{UGFT}$. Drop hats during work; restore by $X=\hat X\,[X]_{UGFT}$.  [Lock: Hats]

**Checklist 0.18:** all equations dimensionless; restoration map used.

---

## 0.19 Kernel one‑liners (time/frequency/static/HE) — with normalization identities

**Distributional Green’s identities.** $`(\Box+m^2)\,G^R(x)=\delta^{(4)}_g(x)`$, $`(\nabla^2-m^2)\,G(\mathbf r)=-\delta^{(3)}(\mathbf r)`$.  [Lock: G‑IDs]  
**Retarded pole (KG/Proca).** $`G^R(\omega,\mathbf k)=[-(\omega+i0^+)^2+\mathbf k^2+m^2]^{-1}`$, $`G^R(t<0)=0`$.  
**Proca time‑domain (3+1D).** $`G^R(t,r)=\frac{\Theta(t)}{4\pi r}\!\left[\delta(t-r)-m\,\frac{J_1(m\sqrt{t^2-r^2})}{\sqrt{t^2-r^2}}\Theta(t-r)\right]`$.  
**Static Yukawa.** $`G(\mathbf r)=-(4\pi r)^{-1}e^{-mr}`$.  
**EC contact (heavy axial mediator).** $`\Delta\mathcal L_{\rm eff}=-(g_S^2/2m_S^2)\,J_5^\mu J^5_\mu+O(m_S^{-4})`$.

**Checklist 0.19:** use appropriate regime line; identities applied.

---

## 0.20 Operation recipes (compact, always visible)

**(R1) Derivation header.** Sig & Eps; indices; reps & $\mathrm{Tr}$; geometry $(e,\omega;R,T)$ or metric‑affine with 
$`
\frac{Q}{\Lambda^{\alpha\mu\nu}}
`$
; gauge $(D,F)$; matter couplings; measures/ADM‑δ; duals; FT/Kubo; ledger.  
**(R2) Wick audit.** $t\to -i\tau$; $(*_E)^2=(-1)^p$; Euclid $\epsilon$; ledgers unchanged.  
**(R3) Linear response.** Ret analyticity; $\rho=-2\Im G^R$; DC via $\Im G^R/\omega$, $\mathbf k=0$, include $\sqrt\gamma$.  
**(R4) Heavy‑field integrate‑out.** Solve algebraic EOM for $m^2\gg\partial^2$; substitute; keep $O(\partial^2/m^4)$.  
**(R5) UV counting.** Polarization sums; Barnes–Rivers; Stückelberg.  [Lock: Recipes]

**Checklist 0.20:** R1 present; others as needed.

---

## 0.21 Literature crosswalk (torsion & traces)

**Axial dualization.** UGFT $S_\mu=\tfrac{1}{6}\epsilon_{\mu\nu\rho\sigma}T^{\nu\rho\sigma}$. If source uses $`S'_\mu=c\,\epsilon_{\mu\nu\rho\sigma}T^{\nu\rho\sigma}`$, then $`S'_\mu=(6c)\,S_\mu`$, $`g'_S=g_S/(6c)`$.  
**Trace vector.** If $t'_\mu=\sigma\,T^\nu{}_{\mu\nu}$, then $t'_\mu=\sigma\,t_\mu$ and couplings flip with $\sigma$.  
**YM kinetic.** $-\tfrac12\mathrm{Tr}(F^2)$ ↔ $-\tfrac14 F^A F^A$ with $\mathrm{Tr}=\tfrac12\delta^{AB}$.  
**CS level.** Rescale $k$ per §0.10 when switching trace conventions.  [Lock: X‑walk]

**Checklist 0.21:** document $(c,\sigma)$ and rescale.

---

## 0.22 Examples (sign‑locked micro‑checks)

**YM (no matter).** $S=-\tfrac12\!\int\! \mathrm{Tr}(F\wedge *F)\Rightarrow D_\mu F^{\mu\nu}=0$.  
**Dirac + gauge + curved.** $\mathcal L=\bar\psi(i\gamma^\mu D_\mu-m)\Rightarrow (i\gamma^\mu D_\mu-m)\psi=0$; $[D_\mu,D_\nu]\psi=\tfrac14 R_{\mu\nu}{}^{ab}\gamma_{ab}\psi+i g\,F_{\mu\nu}\psi$.  
**Axial torsion.** $`(\boxed{\ +m_S^2 })S_\mu=g_S J_5^\mu`$ with kernels of §0.19 and EC limit.  
*More worked examples live in “Examples Pack A”.*  [Lock: Ex]

---

## 0.23 End‑of‑chapter reproducibility audit

1) Sig & Hodge (§0.1) ✔︎  2) Indices & tetrads (§0.2) ✔︎  
3) Measures/ADM‑δ (§0.3) ✔︎  4) Gauge & Wilson norm (§0.4) ✔︎  
5) Cartan data, Bianchi & torsion irreps (§0.5) ✔︎  6) Metric‑affine reduction (§0.6) ✔︎  
7) Spinors/commutator/axial sourcing + GammaE + Larin (§0.7) ✔︎  8) FT/Kubo + Delta/Plancherel (§0.8) ✔︎  
9) Wick map + Euclid $\epsilon$ (§0.9) ✔︎  10) Ledgers & CS table (§0.10) ✔︎  
11) Torsion baseline & ghost audit (§0.11) ✔︎  12) EH+GHY + Stokes (§0.12) ✔︎  
13) Gauge fixing/BRST + AdjLap (§0.13) ✔︎  14) Response axioms (§0.14) ✔︎  
15) Variation & $T_{\mu\nu}$ (§0.15) ✔︎  16) Projectors/Stückelberg (§0.16) ✔︎  
17) $S^2$ harmonics + epsilon (§0.17) ✔︎  18) Hats & dims (§0.18) ✔︎  
19) Kernel one‑liners + G‑IDs (§0.19) ✔︎  20) Recipes (§0.20) ✔︎  
21) Crosswalk (§0.21) ✔︎  22) Examples (§0.22) ✔︎

---

## Appendix A — Wall Chart (At‑a‑Glance)

- **Signature & Hodge.** $(-,+,+,+)$; $` *^2=(-1)^{p(4-p)+1}`$; after Wick $`(*_E)^2=(-1)^p`$. [Lock: Sig][Lock: Hodge]  
- **Orientation.** $\epsilon_{0123}=+\sqrt{|g|}$, $\epsilon^{0123}=+1/\sqrt{|g|}$; $[\cdot]$ is alternating symbol. [Lock: Eps]  
- **Fourier pair.** $\tilde f=\int e^{\,i(\omega t-\mathbf k\cdot\mathbf x)}f$; $f=\int (2\pi)^{-4}e^{-i(\omega t-\mathbf k\cdot\mathbf x)}\tilde f$. [Lock: FT]  
- **Delta & Plancherel.** Phase‑consistent δ’s; $\int|f|^2=\int(2\pi)^{-4}|\tilde f|^2$. [Lock: Delta][Lock: Plancherel]  
- **Retarded pole.** $G^R=[-(\omega+i0^+)^2+\mathbf k^2+m^2]^{-1}$ (support $t>0$). Static Yukawa $=-(4\pi r)^{-1}e^{-mr}$. [Lock: Ret]  
- **ADM delta.** $\delta_g^{(4)}=\delta(t-t_0)\delta^{(3)}_\gamma/N$; $\sqrt{|g|}=N\sqrt\gamma$. [Lock: ADM‑δ]  
- **Bianchi.** $DT^a=R^a{}_b\wedge e^b$, $DR^a{}_b=0$. [Lock: Bianchi]  
- **Axial Proca baseline.** $\mathcal L_S=-\tfrac14 H^2+\tfrac12 m_S^2 S^2- g_S S\cdot J_5$; EC contact $-g_S^2 J_5^2/(2m_S^2)$. [Lock: Axial‑Proca]  
- **CS trace/level mapping.** $\mathrm{Tr}=\delta^{AB}$ ↔ $\mathrm{Tr}=\tfrac12\delta^{AB}$ with $k$ rescale by 2. [Lock: CS]  
- **Projectors.** $\sum_\lambda \epsilon^\mu\epsilon^\nu=g^{\mu\nu}+p^\mu p^\nu/m^2$; BR projectors with $\theta,\omega$. [Lock: Proj‑1][Lock: BR]  
- **Recipes.** R1 header; R2 Wick; R3 response; R4 integrate‑out; R5 UV counting. [Lock: Recipes]

---

## Change governance & provenance (non‑versioned)

- **Rule.** Any change proposes: (1) justification, (2) 5–10 line worked micro‑example, (3) explicit checklist deltas. [Lock: Gov]  
- **Scope.** Update anchor handles where relevant (e.g., [Lock: Sig], [Lock: Wick]) and ensure every affected downstream reference compiles against the new lock.  
- **Record.** Brief one‑line note (title + rationale) at the top of the changed section; remove the note once all downstream chapters are re‑audited.
