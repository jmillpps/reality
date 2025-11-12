## 8.1  HEP MET from zero (what it is, how it is computed, and what can go wrong)

### 8.1.1  Geometry and coordinates (the playing field)
- A hadron collider (e.g., the LHC) fires two proton beams along the **$z$–axis**. The **transverse plane** is the **$x$–$`y`$** plane (perpendicular to the beams).
- Directions in the transverse plane are labeled by the **azimuthal angle** $\phi\in(-\pi,\pi]$.
- The detector reconstructs **visible** final–state objects (photons, electrons, muons, hadronic jets, charged/neutral hadrons, etc.) with transverse momentum
$`
  \vec p_T = (p_x,p_y),\qquad p_T = \sqrt{p_x^2+p_y^2}\,.
`$

**Key premise.** To an excellent approximation, the **initial transverse momentum** of the colliding system is **zero**. If we could see *everything* produced, the vector sum of all final–state transverse momenta in an event would be zero in the $x$–$`y`$ plane.

---

### 8.1.2  Definition of HEP MET (the basic observable)
The **missing transverse energy** (MET) is defined event–by–event as the **negative** of the vector sum of all **visible** reconstructed transverse momenta:
$`
\boxed{\;\vec E_T^{\,\text{miss}} \equiv -\sum_{i\in \text{visible}} \vec p_{T,i}\;}\qquad
\text{(a 2–vector in the $x$–$y$ plane)}
`$
Its magnitude is $\text{MET}=\lVert\vec E_T^{\,\text{miss}}\rVert$.

**Interpretation.**
- If truly invisible particles (e.g., neutrinos) carry away transverse momentum $\sum_{\rm inv}\vec p_{T,\,\text{inv}}$, and all visible momenta are measured perfectly, then
$`
  \vec E_T^{\,\text{miss}} \approx \sum_{\rm inv}\vec p_{T,\,\text{inv}}\,.
`$
- If *no* invisible momentum is present, any nonzero MET is from **detector/reconstruction effects** (finite resolution, dead regions, miscalibration, limited acceptance, etc.).

---

### 8.1.3  Estimators (why the number moves around)
Different reconstruction strategies define different “flavors” of MET, all built from the *same* underlying event:
- **PF–MET (Particle Flow):** combines information from all subsystems to reconstruct individual particles, then sums their $\vec p_T$.
- **PUPPI–MET:** PF–like, but down–weights particles consistent with **pileup** (additional soft $pp$ collisions in the same bunch crossing).
- **DeepMET:** a machine–learning regression trained to predict the “true” $\vec E_T^{\,\text{miss}}$ from per–particle and event features.

**Important.** The physics is unchanged by the estimator, but the **response to noise/pileup/instrumental effects** differs. Seeing MET change across PF $\to$ PUPPI $\to$ DeepMET is **expected** and **not** evidence of new physics by itself.

---

### 8.1.4  MET significance (how surprising is the imbalance?)
To compare events under varying detector conditions, we use a **significance**:
$`
\boxed{\; S \;\approx\; \frac{\text{MET}^2}{\sigma_{\text{eff}}^2}\;}, 
\qquad \sigma_{\text{eff}}^2=\sigma_0^2+\big(f_{\rm PU}\,\|\vec p_T^{\,\text{pileup}}\|\big)^2\,.
`$
Here $\sigma_0$ is an intrinsic resolution scale (detector, reconstruction), and the second term increases with **pileup activity**.

- **Low $S$**: imbalance consistent with detector noise.
- **High $S$**: imbalance unlikely under “no true invisibles.”

> **Practical reading.** Tight cuts on $S$ reduce obvious fakes, but do **not** remove all detector–fixed patterns (e.g., cracks) unless those are explicitly handled.

---

### 8.1.5  Control samples (calibration baselines)
Two samples provide **null templates** with $\approx 0$ true MET:
- $Z\!\to\!\ell^+\ell^-$ (two high–quality leptons).
- $\gamma+$ jet (a prompt photon recoiling against a jet).

These are used to **calibrate** response and resolution for each estimator and to **locate** detector effects. If MET remains large or structured in these controls, that points to **instrumental/analysis** issues rather than new invisible particles.

---

### 8.1.6  Worked micro–examples (why vectors matter)

**Case A — pure mismeasurement (no invisible).**  
Two back–to–back jets, true $p_T=100~\text{GeV}$ each, $\phi_1=0$, $\phi_2=\pi$.
- Perfect measurement: $\vec E_T^{\,\text{miss}}=\vec 0$.
- If the second jet is under–measured by $10~\text{GeV}$:
$`
  \vec E_T^{\,\text{miss}} \approx (-10,\,0)\ \text{GeV},\qquad \text{MET}=10~\text{GeV}.
`$
  Direction points **along the mis–measured jet**. This is **fake MET** (detector–driven).

**Case B — invisible $+$ mismeasurement.**  
Keep the $10~\text{GeV}$ under–measured jet and add a neutrino with $p_T=30~\text{GeV}$ at $\phi=\pi/2$.
- Vector sum:
$`
  \vec E_T^{\,\text{miss}} \approx (-10,\,0) + (0,\,30) = (-10,\,30)\ \text{GeV},
`$
  so $\text{MET}=\sqrt{10^2+30^2}\approx 31.6~\text{GeV}$.
- **Lesson:** MET is a **vector**. Angular observables (e.g., $\Delta\phi$ between MET and a leading jet) and **estimator behavior** help separate fakes from real invisibles.

---

### 8.1.7  Common sources of *fake* MET (why “it sounds wrong” at first)
- **Detector–fixed geometry:** cracks, dead/hot cells, masked regions $\Rightarrow$ **hot bands in $\phi$** that do **not** rotate with the sky and often **shrink** when moving PF $\to$ PUPPI $\to$ DeepMET or when applying official halo/noise filters.
- **Pileup:** many soft interactions add unbalanced low–$`p_T`$ vectors; mitigated by per–particle weights (PUPPI) and ML regressors (DeepMET), but not eliminated.
- **Trigger/DAQ selection:** HLT choices and run/era changes can bias which events survive; apparent MET shifts can be **run–dependent** rather than physical.
- **Boundary/analysis choices:** treating a finite region as isolated (not accounting for energy/flow at the edges), or taking low–frequency limits in the wrong order, can **manufacture** apparent deficits.

> **Stop sign — pitfalls to watch (returned to later).**  
> • *Boundary not declared/postings omitted* $\Rightarrow$ the “jar” (bulk integral) will look light.  
> • *Improvements (integration by parts) treated as bulk changes* $\Rightarrow$ false differences between “equivalent” derivations.  
> • *Low–frequency (DC) limits taken in the wrong order* $\Rightarrow$ fake “missing DC” response.  
> • *Unsafe field elimination (bad Schur complement)* $\Rightarrow$ spurious ghosts/deficits on paper.

---

### 8.1.8  Why my first impression was misleading (and how I’ll proceed)
Initially I observed:
- MET **changing** across PF/PUPPI/DeepMET $`\Rightarrow`$ consistent with **estimator sensitivity** to detector and pileup effects.  
- Weak **azimuthal structure** in $\phi$ $\Rightarrow$ consistent with **detector–fixed** geometry.  
- Occasional **time structure** $\Rightarrow$ must be tested against **sidereal** rotation (space–fixed) versus **wall–clock** effects (operations/detector).

**Before** interpreting any residue as new invisible energy, I will:
1. **Calibrate on control samples** ($Z\!\to\!\ell\ell$, $\gamma+$jet) and reproduce known MET resolution/significance.  
2. **Quantify anisotropy** (e.g., Rayleigh or other circular–uniformity tests on MET $\phi$) and apply official detector filters.  
3. **Check estimator invariance** (PF vs PUPPI vs DeepMET) for any remaining tails.  
4. **Test sidereal modulation** by fitting
$`
   \vec E_T^{\,\text{miss}}(t)\!\cdot\!(\cos\omega_\oplus t,\ \sin\omega_\oplus t)
   = A\cos\omega_\oplus t + B\sin\omega_\oplus t + C\,.
`$
   A real *space–fixed* effect should be **consistent across estimators**; detector artifacts should **not**.

Only after these checks will I introduce the **ledger** (bulk vs boundary accounting) and the single new bulk contribution my framework allows. To keep terms straight for later sections:
- **Jar (bulk)** $=$ volume integral of energy density. I will picture these bulk “coins” as **hopfions** (closed tubes in the volume).
- **Rim (boundary)** $=$ surface/edge contributions (gravitational ADM/Brown–York, posted flux, improvement terms). I will picture these boundary “coins” as **knottions** (loops/knots on the boundary).

**Summary of this section.** You now have a complete, baseline understanding of MET in practice: how it is defined, how it is computed, why it varies with estimators, how to gauge its significance, how to use control samples, and why a raw “MET excess” can be misleading without estimator, detector, and boundary audits. Next, I will formalize the ledger rules and retrace the specific mistakes I made before applying them.

## 8.2  The ledger mindset (bulk vs boundary accounting from first principles)

This section translates the energy–accounting rules I rely on later. I assume no prior exposure to UGFT: I state the identity, define the two ledgers, and list the four rules I must enforce whenever I compute or compare energies.

### 8.2.1  The book I must balance (Miller identity)

On any time slice $\Sigma_t$ with lapse $N$ and spatial metric $h_{ij}$, the **total energy** is the sum of a **bulk** integral (“jar”) and a **boundary** term (“rim”):
$`
\boxed{
E_{\text{total}}
=\underbrace{\int_{\Sigma_t} N\sqrt{h}\;T^{0}{}_{0,\text{total}}}_{\text{jar: all field energy densities}}
+\underbrace{E^{\text{ADM/BY}}_{\text{grav}}[\partial\Sigma_t]}_{\text{rim: gravitational boundary energy}}
}
`$
- The jar contains **all propagating sectors**: gauge fields, scalars, Dirac fields, and the axial torsion field $S_\mu$ (introduced later).  
- The rim collects **boundary posts**: gravitational ADM/Brown–York energy and any other surface contributions I explicitly post (see §8.2.3).

This is a bookkeeping identity, not an estimator. Whatever I do inside the region must match what leaves or sits on the boundary.

### 8.2.2  Two pictures to keep it straight (optional mnemonics)

- **Hopfions (jar)**: I will picture **bulk energy** as **closed tubes** filling the volume (a memory aid for volumetric “coins” I count by $\int_{\Sigma_t}N\sqrt{h}\,T^{0}{}_{0}\,d^3x$). No extra physics is implied by the name.  
- **Knottions (rim)**: I will picture **boundary posts** as **loops/knots** that live on, or run along, the boundary $\partial\Sigma_t$ (a memory aid for surface coins I post and sum).

The names help me remember where each contribution lives: tubes in the jar, loops on the rim.

### 8.2.3  Four rules I must enforce (I failed each of these at least once)

1. **Declare boundaries first; post surface power and gravitational energy.**  
   If the region has walls, I must include **Dirichlet–to–Neumann (DtN)/impedance power** (what the field does on the boundary). If the region extends to spatial infinity, I must include **ADM/Brown–York** gravitational energy.  
   The differential statement I use is:
$`
   \frac{d}{dt}\int_{\Sigma_t}N\sqrt{h}\,T^{0}{}_{0}
   = -\oint_{\partial\Sigma_t}\!\text{(Poynting–like flux)}\cdot d\mathbf a \;+\;\int_{\Sigma_t} J\cdot \dot X,
`$
   and the flux term is **posted** to the rim rather than dropped.

2. **Improvements (integration by parts) move only to the ledger, not the bulk.**  
   If I add a divergence to the Lagrangian,
$`
   \mathcal L\to \mathcal L+\nabla_\mu W^\mu,
`$
   then the action gains a **surface** term,
$`
   S\to S+\oint_{\partial\Omega}\sqrt{|h|}\,n_\mu W^\mu,
`$
   and **no bulk equation changes**. Any comparison that ignores the surface post will look inconsistent.

3. **DC corridor and causality (retarded order of limits).**  
   To evaluate low–frequency (near–DC) behavior consistently, I must use **retarded** Green’s functions and take
$`
   \mathbf{k}\to 0\quad\text{then}\quad \omega\to 0^+.
`$
   Swapping the limits can fabricate or erase DC response and break sum rules. With the corridor, $\Im G^R(\omega,0)/\omega\ge 0$ as $\omega\downarrow 0^+$ (passivity).

4. **Schur–safe elimination (effective theory without changing physics).**  
   When I integrate out a mixed field from a quadratic block
$`
   \begin{bmatrix}A & B\\ B^\dagger & C\end{bmatrix},
`$
   the **effective** kernel is
$`
   \boxed{A_{\rm eff}=A-B\,C^{-1}B^\dagger,}
`$
   which preserves positivity and the physical poles. Any residual is a **boundary quadratic** I must post; the bulk observables do not change.

These four rules are the minimum I need to keep jar and rim consistent when I compute, transform, or compare energies.

---

## 8.3  The four mistakes I made (each flagged before I made it)

Each mistake below begins with a **VIOLATION** box summarizing which rule I ignored. I then show exactly what I did, the correct formula, and how I fixed it. These are the specific ways I drove myself to the same “missing mass” that experimental MET would show—until I accounted properly for jar and rim.

### 8.3.1  Mistake A — I treated a finite region as isolated

> **VIOLATION A (boundary & ledger):** I did not declare the boundary or post surface power (DtN/impedance) or ADM/Brown–York.  
> **Consequence:** the jar looked light whenever radiation or filtered flow crossed the boundary.

**What I did.** I cut on fiducial regions and filters, then compared jar integrals as if nothing left or entered the region.

**Correct handling.** The slice balance states
$`
\frac{d}{dt}\int_{\Sigma_t}N\sqrt{h}\,T^{0}{}_{0}
= -\oint_{\partial\Sigma_t}\!\text{(flux)}\cdot d\mathbf a \;+\;\int_{\Sigma_t} J\cdot \dot X.
`$
I must **post** the flux term on the rim. At spatial infinity the gravitational part becomes ADM/Brown–York—also a rim post.

**Fix.** I declared the boundary conditions and posted (i) DtN/impedance power on finite walls and (ii) ADM/Brown–York at infinity. The apparent deficit moved to the rim tally.

---

### 8.3.2  Mistake B — I counted improvements in the bulk

> **VIOLATION B (IBP ⇒ ledger):** I added a divergence (“improvement”) to clean up a tensor and then compared bulk energies as if the physics changed.  
> **Consequence:** two “equivalent” derivations gave different bulk answers.

**What I did.** I used $\mathcal L\to\mathcal L+\nabla_\mu W^\mu$ to simplify expressions, then treated the result as a new bulk energy.

**Correct handling.** Improvements add only a **surface** term to the action,
$`
\Delta S=\oint_{\partial\Omega}\!\sqrt{|h|}\,n_\mu W^\mu,
`$
so **only** the rim changes. The jar cannot change under a pure divergence.

**Fix.** I logged every improvement as a **knottion** (boundary post). The bulk numbers matched across methods once the ledger reflected the move.

---

### 8.3.3  Mistake C — I swapped the DC limits

> **VIOLATION C (retarded/DC corridor):** I took $\omega\to 0$ before $\mathbf{k}\to 0$.  
> **Consequence:** I saw a fake “missing DC” term (wrong low–frequency slope).

**What I did.** To probe static behavior, I damped frequency first and found a negative/vanishing DC slope.

**Correct handling.** With **retarded** Green’s functions,
$`
G^R(\omega,\mathbf k)=\frac{1}{-(\omega+i0^+)^2+\mathbf k^2+m^2},
`$
I must send $\mathbf{k}\to 0$ first, then $\omega\to 0^+$. In that corridor $\Im G^R(\omega,0)/\omega\ge 0$ and DC sum rules hold.

**Fix.** I enforced the corridor. The phantom “missing DC” term disappeared.

---

### 8.3.4  Mistake D — I eliminated a mixed field unsafely

> **VIOLATION D (Schur–safe elimination):** I used $A-B\,C^{-1}B$ (missing $B^\dagger$), which can flip signs and move poles.  
> **Consequence:** I created a ghost/deficit on paper that wasn’t in the physics.

**What I did.** I integrated out a coupled block with an algebraic shortcut.

**Correct handling.** For a positive quadratic block,
$`
A_{\rm eff}=A - B\,C^{-1}B^\dagger
`$
preserves positivity and the pole structure; any difference is a **boundary quadratic** (a post on the rim).

**Fix.** I redid the elimination with the Schur–safe form and logged the resulting surface quadratic. The bulk spectrum and energy were stable.

---

### 8.3.5  What remained after corrections (the real residue)

After I posted boundaries, respected the DC corridor, and eliminated fields safely, the only consistent residue appeared in **spin–rich** configurations. That led me (later in the chapter) to the single new **bulk** contribution my framework allows: a **healthy Proca–like axial–torsion energy** $T^{(S)}_{00}$ (a hopfion in the jar). Its exact form and EFT limit are:

- **Exact near–field (static) energy in the jar**:
$`
  E^{(S)}_{\text{exact}}=\frac{g_S^2}{2}
  \!\int\! d^3r\,d^3r'\;J_5^0(\mathbf r)\,\frac{e^{-m_S|\mathbf r-\mathbf r'|}}{4\pi|\mathbf r-\mathbf r'|}\,J_5^0(\mathbf r')\;\ge 0.
`$
- **Heavy–mass (contact) limit**:
$`
  \Delta\mathcal L_{\rm eff}=-\frac{g_S^2}{2m_S^2}\,J_5^\mu J_{5\mu},\qquad
  E^{(S)}_{\text{contact}}=\frac{g_S^2}{2m_S^2}\!\int\! d^3r\,[J_5^0(\mathbf r)]^2.
`$

This is the “missing coin” I had not counted; once I included it (and kept posting correctly on the rim), the ledger closed.

## 8.4  Putting the rules back on (what changes immediately and how I verify it)

This section is the **re‑run** of the analysis **with the ledger rules enforced**. I describe exactly what I change, what I compute, and what I expect to see **before** introducing any new bulk physics (the axial–torsion coin comes in §8.5). The goal here is to remove bookkeeping artifacts so that any residue is physical.

---

### 8.4.1  Declare boundaries and post them (knottions on the rim)

**What I change.** I make the analysis region and its boundary conditions explicit:

- **Geometry:** choose a time slice $\Sigma_t$; boundary $\partial\Sigma_t$ is either a finite analysis surface (detector walls) or “at infinity” (outgoing radiation).
- **Boundary conditions:** Dirichlet/Neumann/mixed for fields as appropriate; at infinity use a **radiation (Sommerfeld) condition**.

**What I compute and post.**

1) **Surface power (DtN/impedance) to the rim**
$`
P_{\partial\Sigma_t}
=\oint_{\partial\Sigma_t}\!\mathbf{S}\cdot d\mathbf a,
\quad\text{with }\mathbf{S}\text{ the Poynting‑like flux for the fields in the region.}
`$
I **do not** subtract this from the jar; I **post** it on the rim.

2) **Gravitational rim coin (ADM/Brown–York)**
$`
E^{\text{rim}}_{\text{grav}}[\partial\Sigma_t]=E^{\text{ADM}}\quad(\text{or Brown–York on a finite 2‑surface}).
`$

3) **Improvements (IBP) as surface posts**
$`
\mathcal L\to\mathcal L+\nabla_\mu W^\mu
\;\Rightarrow\;
\Delta S=\oint_{\partial\Omega}\!\sqrt{|h|}\,n_\mu W^\mu\quad\text{(post on the rim).}
`$

**What should change in MET‑space.**
- **Detector‑fixed** anisotropy (hot $\phi$ bands) shrinks after official crack/halo/noise filters and after posting boundary flows.
- **Estimator ordering** becomes cleaner: PF tails $>$ PUPPI $>$ DeepMET, with less run‑dependent drift.

**Jar–rim statement I track.**
$`
\frac{d}{dt}\,E_{\text{jar}}
= -\,P_{\partial\Sigma_t}\;+\;\text{(explicit work terms inside $\Sigma_t$)},\qquad
E_{\text{total}}=E_{\text{jar}}+E_{\text{rim}}\;\;\text{(constant in time).}
`$

---

### 8.4.2  Enforce the DC corridor (retarded order of limits)

**What I change.** All low‑frequency checks use **retarded** Green’s functions and the order
$`
\mathbf{k}\to 0\quad\text{then}\quad \omega\to 0^+.
`$

**What I compute.**
- For any response $\chi^R(\omega,\mathbf{k})$, I verify **passivity**
$`
\lim_{\omega\downarrow 0^+}\frac{\Im \chi^R(\omega,\mathbf 0)}{\omega}\;\ge\;0.
`$
- I re‑evaluate any “static” claims with the corridor order and re‑plot the DC neighborhood.

**What should change.**
- Spurious “missing DC” terms disappear (wrong‑order artifacts).
- Sum‑rule checks across frequency reconciliate with time‑domain jar–rim bookkeeping.

---

### 8.4.3  Re‑do field elimination safely (Schur‑safe)

**What I change.** Any effective reduction of a coupled quadratic block
$`
\begin{bmatrix}A & B\\ B^\dagger & C\end{bmatrix}
`$
uses the **Schur complement**
$`
A_{\rm eff}=A-B\,C^{-1}B^\dagger,
`$
not $A-B\,C^{-1}B$.

**What I compute.**
- Positivity check: $A_{\rm eff}$ has the same cone (no new negative modes).
- Poles/eigenfrequencies: physical poles are preserved.
- **Residual:** any leftover appears as a **boundary quadratic** (a post), not a bulk change.

**What should change.**
- Apparent ghosts or energy drops introduced by algebraic shortcuts vanish.
- Differences between “lanes” (e.g., projector vs. covariant) show up **only** in the rim ledger.

---

### 8.4.4  Re‑check estimator/gauge/lane independence after posting

**What I change.** With postings in place, I compare **bulk observables** across:
- **Estimators:** PF, PUPPI, DeepMET (same cuts).
- **Lanes/bases:** e.g., canonical vs. Belinfante; projector vs. covariant.

**What I compute.**
- **Bulk equality:** the jar integral $E_{\text{jar}}$ must match across lanes for identical BCs.
- **Rim reconciliation:** any numerical differences are accounted as knottions (boundary posts).

**What should change.**
- The **same** physical quantity computed two ways is now equal in the bulk.
- All residual differences are **posted** and no longer masquerade as “missing mass.”

---

### 8.4.5  Separate detector‑fixed from space‑fixed patterns

**What I change.** I run two orthogonal tests on the MET vectors that survived tight selections:

1) **Detector‑fixed anisotropy (Rayleigh on MET $\phi$)**
$`
R=\frac{1}{N}\sqrt{\Big(\sum_i \cos\phi_i\Big)^2+\Big(\sum_i \sin\phi_i\Big)^2}.
`$
A drop in $R$ under filters/estimator swaps indicates **instrument/geometry**.

2) **Space‑fixed (sidereal) test**
$`
\text{proj}(t)=\vec E_T^{\,\text{miss}}\!\cdot(\cos\omega_\oplus t,\;\sin\omega_\oplus t)
= A\cos\omega_\oplus t + B\sin\omega_\oplus t + C.
`$
A genuine space‑fixed component must be **estimator‑invariant**; detector‑fixed effects are not.

**What should change.**
- Detector‑fixed features cleanly reduce with postings and estimator quality.
- Any remaining sidereal structure is now easier to see and quantify.

---

### 8.4.6  Produce a closure report (one table per dataset)

**What I record.** For each run/selection I produce a compact ledger:

| Slice | $E_{\text{jar}}$ | $E_{\text{rim}}$ (posts) | $E_{\text{total}}$ | $\Delta E$ | Notes |
|---|---:|---:|---:|---:|---|
| before postings | … | … | … | … | walls not declared |
| + DtN/impedance | … | … | … | … | surface power posted |
| + ADM/BY | … | … | … | … | grav. rim coin posted |
| + IBP posts | … | … | … | … | improvements ledgered |
| + DC corridor | … | … | … | … | retarded, $k\!\to\!0$ then $\omega\!\to\!0^+$ |
| + Schur‑safe | … | … | … | … | effective kernel fixed |

Acceptance: $|\Delta E|\le \varepsilon$ (tolerance set by numerical precision). Any remaining residue is what §8.5 will address (the bulk axial–torsion coin).

---

### 8.4.7  What changes relative to §8.1 (quick map)

- **Estimator drift** is now mostly ledger (rim) and **documented**; PF→PUPPI→DeepMET behaves as expected.  
- **Hot $\phi$ bands** shrink under postings and filters; $R$ drops in control samples.  
- **Fake DC deficits** are gone; frequency–time sum rules agree.  
- **Lane equivalence** holds in the bulk; differences live on the rim.  
- **Residuals** concentrate in **spin‑rich** selections, setting up §8.5 where I add the only new bulk term my framework allows and count it in the jar.

**Checkpoint.** With postings, DC order, and safe elimination in place, the **jar–rim identity holds slice‑by‑slice**. Only after this point do I test whether a **bulk** addition (axial–torsion energy) is required to close the remaining gap.

## 8.5  The axial–torsion bulk coin (hopfions): definition, energy, and how I count it

This section introduces the **only new bulk contribution** I allow after §8.4 has stabilized the ledger: a **healthy Proca‑like axial torsion field** whose energy belongs **in the jar**. I explain why it enters, how it is defined, what its energy density is, how to compute it (exact and EFT/contact), and how I verify that adding it closes the remaining gap.

---

### 8.5.1  Why torsion enters here (physical role of spin)

The residue that survives after boundary posting, DC‑order enforcement, and safe elimination (§8.4) appears **only** in **spin‑rich** configurations. In a framework that already counts gauge, scalar, and Dirac energy in the jar, the missing piece is naturally a field that couples to **spin/axial current**. The axial‑torsion vector $S_\mu$ is that field. If I omit it, I under‑count energy stored near spin sources; if I include it, the jar gains precisely the “coin” needed to match the observed balance.

---

### 8.5.2  Field content and OS locks (definition)

I adopt the operating locks from earlier chapters: metric signature $(-,+,+,+)$, orientation/epsilon/Hodge as fixed there, **retarded** prescription, and explicit couplings.

**Axial–torsion field and Lagrangian**
$`
\boxed{
\mathcal L_S
= -\tfrac14\,H_{\mu\nu}H^{\mu\nu}
+ \tfrac12\,m_S^2\,S_\mu S^\mu
- g_S\,S_\mu J_5^\mu,
\qquad
H_{\mu\nu}=\nabla_\mu S_\nu-\nabla_\nu S_\mu,
}
`$
with $J_5^\mu$ the axial (spin) current built from matter. This is a **Proca‑type** spin‑1 field (three physical polarizations when on‑shell).

**Equations of motion (source form)**
$`
\nabla_\nu H^{\nu\mu}+m_S^2 S^\mu = g_S\,J_5^\mu.
`$
Taking the divergence yields the consistency relation
$`
m_S^2\,\nabla_\mu S^\mu = g_S\,\nabla_\mu J_5^\mu,
`$
so the longitudinal component is fixed by the source; the propagating content is **transverse** and healthy.

---

### 8.5.3  Positivity and causality checks (health/ghost control)

- **Hamiltonian sign.** With the signs above, the quadratic Hamiltonian density in the physical modes is **positive**; there are no negative‑norm (ghost) states in the classical sector I use for energy accounting.
- **Causality.** The principal symbol is hyperbolic. In the high‑frequency limit, wave fronts propagate on or within the light cone (no superluminal fronts). The massive dispersion $ \omega^2=\mathbf{k}^2+m_S^2 $ implies a **spectral gap**; very slow or static processes store energy locally (near‑field) rather than radiate it away.

These checks ensure that any energy I add to the jar from $S_\mu$ is **real, positive, and well‑behaved**.

---

### 8.5.4  Where its energy lives in the ledger (bulk vs boundary)

All **local field energy** from $S_\mu$ is part of the **jar**:
$`
\boxed{
E_{\text{jar}}^{(S)}(t)=\int_{\Sigma_t} N\sqrt{h}\;\,T^{0}{}_{0\,,S}\,d^3x.
}
`$
Any total divergences generated by integration‑by‑parts (IBP) are **posted to the rim** (improvement $\Rightarrow$ surface superpotential), and any radiation/impedance power at a boundary is also posted to the rim. In other words, $T^{0}{}_{0\,,S}$ contributes as a **hopfion (bulk coin)**; only IBP/radiative pieces appear as **knottions (boundary posts)**.

---

### 8.5.5  Static near‑field energy (exact Yukawa fold)

For a time‑independent spin density $J_5^0(\mathbf r)$, the field equation reduces to a screened Poisson problem. The resulting **near‑field energy** stored in $S_\mu$ is
$`
\boxed{
E^{(S)}_{\text{exact}}
=\frac{g_S^2}{2}
\int d^3r\,d^3r'\;
J_5^0(\mathbf r)\,
\frac{e^{-m_S|\mathbf r-\mathbf r'|}}{4\pi\,|\mathbf r-\mathbf r'|}\,
J_5^0(\mathbf r')\;\ge 0.
}
`$
- This is a **pure jar** contribution: a positive, symmetric quadratic form in $J_5^0$.
- Physically: spin sources build a short‑range “Yukawa cloud” of torsion; the energy in that cloud is the bulk coin I had not counted.

**Sanity checks.**
- If the support of $J_5^0$ doubles, $E^{(S)}$ scales quadratically (as expected for a linear field sourced by a current).
- If $m_S$ increases, the range shrinks and the energy localizes more tightly around sources (the “coin” becomes more compact).

---

### 8.5.6  Heavy‑mass (EFT/contact) limit

When $m_S$ is large compared to gradients in $J_5$, I can integrate out $S_\mu$ to obtain an effective local term
$`
\boxed{
\Delta\mathcal L_{\rm eff}
= -\frac{g_S^2}{2m_S^2}\,J_5^\mu J_{5\mu}
\quad\Longrightarrow\quad
E^{(S)}_{\text{contact}}
=\frac{g_S^2}{2m_S^2}\int d^3r\;\big[J_5^0(\mathbf r)\big]^2\,.
}
`$
- This is the low‑energy **shadow of the same coin**. It has the **same sign** and counts the **same bulk energy** to leading order in $1/m_S^2$.
- In practice, for sufficiently smooth $J_5^0$, the contact estimate tracks the exact Yukawa energy within controlled error.

---

### 8.5.7  Dynamical situations (when does torsion radiate?)

For time‑varying sources, the massive dispersion implies two regimes:

- **Sub‑gap driving** $(\omega \ll m_S)$: no propagating torsion waves; energy remains in **evanescent near‑fields** (pure jar). This is where “missing mass” is most easily miscounted if $E^{(S)}$ is omitted.
- **Above‑gap driving** $(\omega \gtrsim m_S)$: torsion can **radiate**. The radiated power is then a **boundary post** (knottion) recorded via a DtN/impedance form at $\partial\Sigma_t$, while the remaining near‑field energy stays in the jar.

Either way, the **jar+rim total** is conserved slice‑by‑slice; the split depends on the driving spectrum.

---

### 8.5.8  How I compute it in practice (analysis recipe)

I follow these steps **after** §8.4 is satisfied:

1) **Fix the boundary and postings.** Declare $\Sigma_t$, set $\partial\Sigma_t$, and enable: ADM/Brown–York (gravity), DtN/impedance (radiation), and all IBP posts (surface terms).
2) **Choose a proxy for $J_5^\mu$.** In data/MC contexts, build $J_5^\mu$ from the axial content of the reconstructed event (e.g., spin‑weighted hadronic/lep channels, polarization observables, or model‑based templates).
3) **Pick the regime.**  
   • If sources are slow/near‑static at the scales of interest: use **contact** $E^{(S)}_{\text{contact}}$.  
   • If structure is comparable to $1/m_S$: compute **exact** $E^{(S)}_{\text{exact}}$ via FFT/convolution or multipole.
4) **Post uncertainties.** Propagate estimator, pileup, and calibration errors into $J_5$ and into the energy integral. Record them in the closure table alongside rim posts.
5) **Closure test.** Re‑evaluate
$`
   E_{\text{total}}=E_{\text{jar}}^{\text{(all std fields)}}+E_{\text{jar}}^{(S)}+E_{\text{rim}}
`$
   and check that the total is stable across lanes/estimators (within tolerance).

**Numerical notes.**
- For $E^{(S)}_{\text{exact}}$, the real‑space Yukawa kernel can be evaluated by FFT:
$`
  \tilde G(\mathbf k)=\frac{1}{\mathbf k^2+m_S^2},\quad
  E^{(S)}_{\text{exact}}=\frac{g_S^2}{2}\int\!\frac{d^3k}{(2\pi)^3}\;\frac{|\tilde J_5^0(\mathbf k)|^2}{\mathbf k^2+m_S^2}.
`$
- For the contact limit, a direct sum/integral over $J_5^0(\mathbf r)^2$ with detector weights suffices.

---

### 8.5.9  Hopf picture (optional mnemonic; not extra physics)

On a slice $\Sigma_t$, normalize a bulk direction field $\hat{\mathbf n}(\mathbf x)$ from $\mathbf S$ or $\mathbf J_5$. The **Hopf invariant**
$`
Q=\frac{1}{16\pi^2}\int_{\Sigma_t}\mathbf A\cdot(\nabla\times\mathbf A)\,d^3x
\quad\text{with}\quad\nabla\times\mathbf A=\tfrac12\,\epsilon_{ijk}\,\hat{\mathbf n}\cdot(\partial_j\hat{\mathbf n}\times\partial_k\hat{\mathbf n})
`$
counts linked **pre‑image loops** (Hopf fibres) inside the **jar**. This is only a **visual aid**: it reminds me that torsion energy can reside in volumetric “tubes” (hopfions), while any topological transfer across $\partial\Sigma_t$ appears as a **boundary post** (knottion).

---

### 8.5.10  What changes once I count it (and how I report it)

- **Jar increases by $E^{(S)}$** in spin‑rich selections; previously “missing” energy now has a **bulk** address.  
- **Rim is unchanged** except for any radiative posts (if above gap) or IBP terms already noted.  
- **Total stays fixed**, now matching across estimators/lanes.

In the closure table I add a dedicated line:

| Slice/Selection | $E_{\text{jar}}^{\text{std}}$ | $E_{\text{jar}}^{(S)}$ | $E_{\text{rim}}$ | $E_{\text{total}}$ | Notes |
|---|---:|---:|---:|---:|---|
| after §8.4 | … | 0 | … | … | pre‑torsion |
| + axial torsion | … | $E^{(S)}_{\text{exact/contact}}$ | … | **unchanged** | residue closed |

This is the point at which the last open discrepancy disappears without inventing a new bucket: I have simply **counted the bulk coin** that belongs in the jar.

## 8.6  Putting HEP MET and UGFT MET together (one pipeline, one ledger, one answer)

In this section I stop treating HEP MET and the UGFT ledger as separate threads. I put them on the **same pipeline**, define the tests I run, state what I accept as **closure**, and show how I keep an audit trail. The point is simple: the **detector‑level imbalance** (HEP MET) is my raw signal, and the **ledger identity**
$`
E_{\text{total}}(t)\;=\;E_{\text{jar}}(t)\;+\;E_{\text{rim}}(t)
`$
is how I account for it. After §8.4 (postings, corridor, safe elimination) and §8.5 (axial–torsion coin in the jar), both sides meet without contradiction.

---

### 8.6.1  One pipeline with two views

**HEP view (detector space).**
- Reconstruct $\vec E_T^{\,\text{miss}}$ with PF, PUPPI, DeepMET.
- Compute MET significance
$`
  S \approx \frac{\text{MET}^2}{\sigma_{\text{eff}}^2},\qquad
  \sigma_{\text{eff}}^2=\sigma_0^2+\big(f_{\rm PU}\,\|\vec p_T^{\,\text{pileup}}\|\big)^2.
`$
- Use control samples ($Z\!\to\!\ell\ell$, $\gamma+$jet) to set baselines.
- Measure anisotropy in detector coordinates (Rayleigh):
$`
  R=\frac{1}{N}\sqrt{\Big(\sum_i \cos\phi_i\Big)^2+\Big(\sum_i \sin\phi_i\Big)^2}.
`$
- Test for space‑fixed structure with the sidereal projection:
$`
  \vec E_T^{\,\text{miss}}(t)\!\cdot\!(\cos\omega_\oplus t,\ \sin\omega_\oplus t)
  = A\cos\omega_\oplus t + B\sin\omega_\oplus t + C.
`$

**Ledger view (field space).**
- **Jar (hopfions):** volume energy
$`
  E_{\text{jar}}=\int_{\Sigma_t}N\sqrt{h}\;T^{0}{}_{0,\text{total}}\;d^3x
  =E_{\text{std}}+E^{(S)}\quad\text{with}\quad
  E^{(S)}=\frac{g_S^2}{2}\!\int\!\frac{d^3k}{(2\pi)^3}\frac{|J_5^0(\mathbf k)|^2}{\mathbf k^2+m_S^2}.
`$
- **Rim (knottions):** boundary posts
$`
  E_{\text{rim}}=E^{\text{ADM/BY}}+\text{(DtN/impedance power)}+\text{(IBP superpotentials)}.
`$
- **DC corridor:** all near‑DC checks use retarded prescription with $\mathbf k\!\to\!0$ **then** $\omega\!\to\!0^+$.

The **same event selection** runs through both views. The detector tests tell me *what looks suspicious*; the ledger books *where the energy goes*.

---

### 8.6.2  Decision tree: bulk vs boundary (what I decide and when)

1) **Does the feature shrink with estimator quality or detector filters?**  
   PF $\to$ PUPPI $\to$ DeepMET reduces it; filters flatten $\phi$ bands $\Rightarrow$ **boundary**. Post it (knottions).

2) **Is the feature consistent across estimators and bases after postings?**  
   Yes $\Rightarrow$ candidate **bulk**. Proceed to sidereal test and spin checks.  
   No $\Rightarrow$ still boundary; look for a missed post or calibration.

3) **Does it rotate sidereally (fit $A,B$) rather than stay fixed in detector $\phi$?**  
   Yes $\Rightarrow$ **space‑fixed** component; check for spin–weighted channels.  
   No $\Rightarrow$ detector/operations effect; keep it in rim.

4) **Is the configuration spin‑rich (nonzero $J_5$) and near‑static?**  
   Yes $\Rightarrow$ compute $E^{(S)}$ (exact or contact) and add to jar.

At each arrow I log the post or addition explicitly. Nothing moves without a receipt.

---

### 8.6.3  What counts as closure (acceptance criteria)

I track a per‑selection **closure residual**
$`
\Delta E \;=\; E_{\text{total}} - \Big(E_{\text{jar}}^{\text{std}} + E^{(S)} + E_{\text{rim}}\Big).
`$

**Acceptance.**
- **Numerical tolerance:** choose $\varepsilon_{\text{num}}$ consistent with integration/resolution error (stated in the report).  
- **Systematic tolerance:** propagate estimator/pileup/calibration and $J_5$ modeling to $\varepsilon_{\text{syst}}$.  
- **Pass if:** $|\Delta E|\le \sqrt{\varepsilon_{\text{num}}^2+\varepsilon_{\text{syst}}^2}$.

I also require **lane invariance** (canonical vs. Belinfante; projector vs. covariant): the **bulk** value must agree across lanes once postings are applied. Any remaining difference must be a boundary post.

---

### 8.6.4  Closure table (what I print for every run/selection)

| Slice/Selection | $E_{\text{jar}}^{\text{std}}$ | $E_{\text{jar}}^{(S)}$ | $E_{\text{rim}}$ | $E_{\text{total}}$ | $\Delta E$ | Notes |
|---|---:|---:|---:|---:|---:|---|
| raw (no posts) | … | 0 | … | … | … | boundary not declared |
| + DtN/impedance | … | 0 | … | … | … | surface power posted |
| + ADM/BY | … | 0 | … | … | … | grav. rim coin posted |
| + IBP posts | … | 0 | … | … | … | improvements ledgered |
| + DC corridor | … | 0 | … | … | … | retarded, $k\!\to\!0$ then $\omega\!\to\!0^+$ |
| + Schur‑safe | … | 0 | … | … | … | effective kernel fixed |
| + axial torsion | … | $E^{(S)}$ | … | … | **≈ 0** | residue closed |

This is the audit trail; I do not delete intermediate rows.

---

### 8.6.5  Error budget (how I assign uncertainties)

- **Detector/reconstruction:** propagate per‑object resolutions into MET and $S$; include estimator‑specific systematics.  
- **Boundary posts:** include uncertainties in filters, acceptance masks, and DtN parameters.  
- **Axial–torsion energy:** include modeling error for $J_5$, discretization of the Yukawa fold or the contact term, and $(m_S,g_S)$ hypotheses.  
- **Correlation handling:** keep a covariance note if the same source affects jar and rim (e.g., acceptance).

I report both absolute and relative contributions in the table’s Notes column.

---

### 8.6.6  How HEP MET plots change once the ledger is active

- **Anisotropy in $\phi$**: drops after postings; residual $\phi$ structure that remains estimator‑invariant becomes a candidate for bulk scrutiny.  
- **Estimator ordering**: PF $>$ PUPPI $>$ DeepMET tails become stable across runs/eras once boundary posts are explicit.  
- **Sidereal projection**: fitting $A,B,C$ becomes cleaner after postings; a space‑fixed component (if present) is no longer masked by detector‑fixed bands.  
- **Controls**: $Z\!\to\!\ell\ell$, $\gamma+$jet match published resolutions once postings are applied; remaining offsets are assigned to rim.

These changes are not “effects”; they are the expected outcome of moving boundary contributions into knottions.

---

### 8.6.7  Minimal pseudocode (how I keep myself honest)

```
for selection in selections:
declare_boundary(selection)               # geometry, BCs
posts = []
posts += post_impedance_power(selection)  # DtN / radiation
posts += post_ADM_BrownYork(selection)
posts += post_IBP_superpotentials(selection)

jar_std = integrate_bulk_std(selection)   # YM + scalars + Dirac
if is_spin_rich(selection):
    if is_contact_regime(selection, mS):
        E_S = (gS**2/(2*mS**2)) * integrate(J5_0**2)
    else:
        E_S = yukawa_fold(J5_0, mS, gS)
else:
    E_S = 0

E_total = compute_total_reference(selection)  # fixed by setup
deltaE = E_total - (jar_std + E_S + sum(posts))

record_closure_row(selection, jar_std, E_S, sum(posts), E_total, deltaE, notes)
assert abs(deltaE) <= tol(selection)
```

I store every intermediate result; nothing is overwritten.

---

### 8.6.8  What would make me doubt a “bulk” interpretation

- The feature **shrinks** with estimator quality or filter updates.  
- The feature **moves** with detector coordinates (not sidereal).  
- Lane/basis calculations of the **bulk** disagree even after postings (a missed ledger item).  
- The residue is **not** correlated with any spin‑weighted observable in a selection where $J_5$ should be large.

If any line above triggers, I go back to §8.4 and re‑audit the postings.

---

### 8.6.9  When I claim a bulk axial–torsion contribution

All of the following must hold:

1) Boundary posts (knottions) are declared and logged; controls are reproduced.  
2) DC corridor and Schur‑safe elimination are in force.  
3) The residue is **estimator‑invariant** and **passes** the sidereal test where applicable.  
4) The selection is **spin‑rich**, and adding $E^{(S)}$ computed from $J_5$ **closes** $\Delta E$ within the stated tolerance.  
5) The result is **lane‑invariant** in the bulk, with differences appearing only as boundary posts.

When these five are true, I count the axial–torsion energy as a **hopfion in the jar** and finalize the closure table.

---

**Summary of §8.6.** HEP MET gives me the imbalance I must explain; the UGFT ledger tells me where to post it. After I move boundary energy into **knottions** and add the axial–torsion **hopfion** to the jar when spin is present, the identity $E_{\text{total}}=E_{\text{jar}}+E_{\text{rim}}$ holds in every lane I try. From this point on, “MET vs MET” is not a disagreement; it is a single pipeline with a complete ledger.

## 8.7  Worked example: closing the ledger on a spin‑rich selection

This section is a concrete walk‑through. I start from detector space (HEP MET), run the boundary/ledger steps from §8.4, add the axial–torsion jar coin from §8.5 where it is warranted, and show the **jar + rim = total** closure explicitly. Numbers below are illustrative to make each step visible; the same recipe applies to real data.

---

### 8.7.1  Selection, boundary, and null checks

**Selection.** I choose a spin‑rich sample (channels where axial current $J_5^\mu$ is non‑negligible).

**Boundary declaration.** Time slice $\Sigma_t$ with analysis boundary $\partial\Sigma_t$.
- Finite walls use a **radiation (Sommerfeld)** condition; I post **DtN/impedance** power.
- At large radius I post **Brown–York/ADM** (if applicable).
- Any integration‑by‑parts (IBP) “improvements” are logged as **surface posts**.

**Null checks in detector space (before adding new bulk):**
- Rebuild $\vec E_T^{\,\text{miss}}$ with **PF**, **PUPPI**, **DeepMET**.
- Tighten on **MET significance** $S \approx \text{MET}^2/\sigma_{\text{eff}}^2$.
- Verify **controls** ($Z\!\to\!\ell\ell$, $\gamma+$jet) reproduce known resolutions.
- Test detector‑fixed anisotropy with **Rayleigh $R$** on MET $\phi$.
- Test space‑fixed structure with the **sidereal projection**:
$`
  \vec E_T^{\,\text{miss}}(t)\!\cdot\!(\cos\omega_\oplus t,\ \sin\omega_\oplus t)
  = A\cos\omega_\oplus t + B\sin\omega_\oplus t + C.
`$
**Result after postings.** Hot $\phi$ bands weaken; estimator ordering stabilizes (PF $>$ PUPPI $>$ DeepMET tails). A small, estimator‑invariant residue remains in this spin‑rich selection—this is what I now check in the ledger.

---

### 8.7.2  Jar and rim without torsion (what still does not close)

**Jar (standard fields only).**
$`
E_{\text{jar}}^{\text{std}}
= \int_{\Sigma_t}N\sqrt{h}\;T^{0}{}_{0,\text{(YM+scalars+Dirac)}}\,d^3x.
`$

**Rim (posts).**
$`
E_{\text{rim}}
= E_{\text{grav}}^{\text{ADM/BY}}
\;+\;P_{\partial\Sigma_t}^{\text{(DtN/impedance)}}
\;+\;\oint_{\partial\Omega} n\!\cdot\!W\quad(\text{IBP improvements}).
`$

**Reference total.** $E_{\text{total}}$ is fixed by the setup (work/flux bookkeeping in the full domain).

**Illustrative numbers (after §8.4 is enforced):**

| Term | Value (arb. units) | Note |
|---|---:|---|
| $E_{\text{jar}}^{\text{std}}$ | 245.7700 | bulk (std sectors) |
| $E_{\text{rim}}$ | 3.2300 | DtN $+$ ADM/BY $+$ IBP posts |
| $E_{\text{total}}$ | 249.00035 | reference |
| Residual $\Delta E = E_{\text{total}}-(E_{\text{jar}}^{\text{std}}+E_{\text{rim}})$ | **0.00035** | still open |

The residual is small but systematic in the spin‑rich selection. I now test the axial–torsion jar coin.

---

### 8.7.3  Build $J_5^\mu$ and choose the regime (exact vs contact)

**Axial source (example model).** On $\Sigma_t$, take a smooth $J_5^0(\mathbf r)$. For an explicit calculation I use a 3‑D Gaussian proxy:
$`
J_5^0(\mathbf r)=J_0\,e^{-r^2/(2\sigma^2)}.
`$

**Two regimes for $E^{(S)}$ (from §8.5):**
- **Exact near‑field (Yukawa fold)** if structure is comparable to $1/m_S$:
$`
  E^{(S)}_{\text{exact}}=\frac{g_S^2}{2}\!
  \int\! d^3r\,d^3r'\;\frac{J_5^0(\mathbf r)\,J_5^0(\mathbf r')}{4\pi|\mathbf r-\mathbf r'|}\,e^{-m_S|\mathbf r-\mathbf r'|}.
`$
- **Heavy‑mass (contact) limit** if $m_S$ is large vs gradients in $J_5$:
$`
  E^{(S)}_{\text{contact}}=\frac{g_S^2}{2m_S^2}\int d^3r\,[J_5^0(\mathbf r)]^2
  =\frac{g_S^2}{2m_S^2}\,J_0^2\,\pi^{3/2}\sigma^3.
`$

For illustration, I use the **contact** estimate with $g_S=1$, $m_S=5$, $J_0=5$, $\sigma=0.05$ (arb. units):
- $\pi^{3/2}\approx 5.568$;
- $\sigma^3 = 0.05^3 = 1.25\times10^{-4}$;
- $J_0^2=25$.

Compute
$`
E^{(S)}_{\text{contact}}
=\frac{1}{2\cdot 25}\cdot 25\cdot 5.568\cdot 1.25\times10^{-4}
=0.5\cdot 5.568\cdot 1.25\times10^{-4}
\approx \mathbf{3.48\times10^{-4}}.
`$

This magnitude matches the residual $\Delta E$ above, within typical numerical tolerance.

---

### 8.7.4  Closure with torsion counted (jar + rim = total)

I add $E^{(S)}$ to the jar and re‑evaluate:

| Term | Value (arb. units) | Note |
|---|---:|---|
| $E_{\text{jar}}^{\text{std}}$ | 245.7700 | unchanged |
| $E_{\text{jar}}^{(S)}$ | **0.000348** | axial–torsion (contact) |
| $E_{\text{rim}}$ | 3.2300 | DtN $+$ ADM/BY $+$ IBP |
| $E_{\text{total}}$ | 249.00035 | reference |
| $\Delta E = E_{\text{total}}-(E_{\text{jar}}^{\text{std}}+E_{\text{jar}}^{(S)}+E_{\text{rim}})$ | **$\approx 0$** | within tolerance |

The missing amount is explained as **bulk near‑field energy** of the axial–torsion field. No new bucket is invented; I have simply counted a jar coin that belongs there.

---

### 8.7.5  What would have failed this test

I would **not** accept a bulk interpretation if any of the following were true:
- The residual **shrinks** with estimator quality or detector filters (boundary).
- The feature is **detector‑fixed** in $\phi$ rather than **sidereal/space‑fixed**.
- Bulk values disagree across lanes (canonical vs. Belinfante, projector vs. covariant) **after postings** (missed ledger item).
- The selection is not **spin‑rich** (no credible $J_5$ to source $S_\mu$).

---

### 8.7.6  Receipt (what I log for audit)

- **Boundary posts (knottions):** DtN/impedance power on $\partial\Sigma_t$; Brown–York/ADM at large radius; IBP superpotentials.  
- **Jar (hopfions):** $E_{\text{jar}}^{\text{std}}$ and $E_{\text{jar}}^{(S)}$ with the formula and parameters used.  
- **DC corridor:** retarded prescription; $\mathbf k\!\to\!0$ then $\omega\!\to\!0^+$.  
- **Schur‑safe elimination:** any effective reductions performed.  
- **Tolerance:** numerical and systematic error used for closure acceptance.  
- **Result:** $\Delta E$ before/after $E^{(S)}$, with a statement that the **sum is stable across estimators and lanes**.

---

### 8.7.7  Minimal “swap‑out” to real data

To reproduce this with real events:
1. Build $J_5^\mu$ proxies from your reconstruction (spin‑weighted observables or model templates).  
2. Decide regime (contact vs exact) from $m_S$ and the spatial scale of $J_5$.  
3. Run the same closure table; post the same rim entries; quote the same tolerances.  
4. Require estimator invariance and, where relevant, sidereal consistency.

**Outcome.** If $E^{(S)}$ closes the residual under these conditions, the **ledger is complete**: jar (including torsion) + rim (posts) = total. If not, I reopen §8.4 and look for a missed post or an analysis shortcut that violated the rules.

