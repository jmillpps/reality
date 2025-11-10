# Chapter 4 (Sections 1-8)

## 4.1 Table of Contents and Introduction

### 4.1.1 Table of Contents (Section 4.1)
- 4.1.2 Introduction
- 4.1.3 Connectivity Map

### 4.1.2 Introduction
_See also:_ C0 §0.1–0.4, C2 §0–6, C5 §5.0–5.6, C1 §0–1.2

1\. Introduction — from textbook physics to UGFT
================================================

> This chapter starts exactly where every modern physics course leaves off and takes one careful step further. If you know standard General Relativity (GR), Maxwell/Yang–Mills gauge fields, and the basic scalar/Dirac matter story, you already speak 90% of the language we use. The remaining 10%—our extension—adds a single, well-behaved field that GR does not propagate: an **axial torsion** vector  $S_\mu$ . We show how to think about it, how it couples to familiar matter, and how it fits cleanly into the same energy accounting as everything else.
> The goal of this section is orientation, not detail. We set the pictures and promises up front so the technical work that follows—stress–energy audits, boundary accounting, equivalence proofs—lands with minimal friction.

Everything comes together here in a single movement of geometry, motion, and energy. Space joins the flow as an active medium that guides and records the exchange taking place within it. Each field carries structure shaped by curvature and boundary, forming patterns that reveal how influence moves and how balance is maintained. The expressions that arise build one continuous framework where conservation and interaction share the same foundation. From this point forward, every relation contributes to the same construction, and every motion, from local variation to the shaping of spacetime, follows the same connected rhythm.

* * *

#### 4.1.2.1 What you already know (and what we keep)
--------------------------------------------

*   **Spacetime as a bendable grid.** In GR, mass–energy curves the metric  $g_{\mu\nu}$ , and free fall follows that bend.
*   **Fields as flows.** Electromagnetism and Yang–Mills are ripples and lines of force on that grid, with sources given by charges and currents.
*   **Matter as excitations.** Scalars  $\phi$  and spinors  $\psi$  carry energy and momentum, and couple minimally to gravity and gauge fields.

All of that stays intact. We do not replace GR or gauge theory; we **extend** them.

* * *

#### 4.1.2.2 The one new ingredient: a twist you can picture
---------------------------------------------------

Beyond **bend** (curvature) and **flow** (gauge fields) lives **twist**—a way neighboring arrows can rotate relative to each other as you move through space. The only twist we allow to **propagate** is the **axial** piece, packaged as a 4-vector  $S_\mu$ . Think of  $S_\mu$  as a short-range, spin-sensitive field:

*   It acts like a massive spin-1 (Proca-type) field with healthy kinetic signs.
*   It talks **axially** to matter through an axial current  $J_5^\mu=\bar\psi\gamma^\mu\gamma^5\psi$ .
*   Its range is set by  $m_S^{-1}$ ; in the heavy limit it decouples and you flow back to ordinary GR.

We call this “**P1 policy**”: only the axial torsion irrep propagates; the other torsion pieces remain algebraic (non-wave-carrying). This is the simplest choice that adds new physics without importing ghosts or superluminal headaches.

**Picture in words.** If curvature is how a sheet sags and gauge fields are ripples on that sheet, then  $S_\mu$  is a gentle **twist** in the weave—felt most strongly by spinning matter and fading away with distance like a Yukawa force.

* * *

#### 4.1.2.3 The energy ledger: “coins in the jar, coin on the rim”
----------------------------------------------------------

A universal theme of this chapter is honest accounting. Bulk fields—matter, gauge, and the torsion twist—deposit non-negative **coins** into the energy **jar** via their  $T_{00}$ . Gravity itself contributes a **boundary coin** on the **rim** (the ADM term). The **Miller Equivalence Theorem (MET)**, proved later, says:

> **Total energy = all bulk coins (integrated  $T_{00}$ ) + the gravitational rim coin (ADM).**

No double counting, nothing missing. This framing will guide our computations and our checks.

* * *

#### 4.1.2.4 Why this extension is safe to use
-------------------------------------

We adopt a “**health-first**” stance (cross-checked in Chapter 1):

*   **Causal:** wavefronts respect the light cone; no superluminal fronts.
*   **Ghost-free:** kinetic terms have the right signs; residues at poles are positive.
*   **Well-posed:** the variational problem is clean once boundary terms are added (GHY and friends).
*   **Slice-independent:** choices like gauge parameters or projector bases don’t change physical poles or residues.

You don’t need any of the proofs yet—just the promise that every later formula is run through these filters.

* * *

#### 4.1.2.5 How we compute without getting lost (equivalence-first)
-----------------------------------------------------------

Throughout the chapter we follow a **do the easy thing first, prove it’s equivalent** workflow:

1.  **Choose a basis that behaves.** For vectors and tensors we switch to projector/helicity bases that diagonalize the math (the “prism → beams” picture: a complicated field splits into simple channels).
2.  **Project → scalarize → solve.** Complicated inverses reduce to scalar “resolvents” per physical spin channel. You will see the same kernels you know (retarded propagators, static Yukawa).
3.  **Separate dynamics from book-keeping.** Integrations by parts, boundary choices, and topological integers are kept in a **ledger**. They never change bulk equations—only how flux is recorded at the edge.

This style keeps derivations short while making audits trivial.

* * *

#### 4.1.2.6 What UGFT actually claims (in one paragraph)
------------------------------------------------

UGFT is a **minimal** unification of familiar bulk dynamics (GR + gauge + matter) with a single additional, healthy degree of freedom  $S_\mu$  that couples axially to spin. With standard boundary terms in place, the **total energy** of any isolated solution equals the sum of bulk  $T_{00}$  across all sectors **plus** the gravitational boundary energy. All intermediate rearrangements—basis changes, integrations by parts, different but equivalent solution methods—are tracked so that two people doing the calculation in different “lanes” arrive at the **same** physical answer.

* * *

#### 4.1.2.7 Reading guide (for three audiences)
---------------------------------------

*   **If you are a practicing theorist:** skim the introduction, jump to the stress–energy audit (§4.5 in this chapter’s plan), then the MET proof. The projector formulas and boundary cookbook are placed where you can grab them quickly.
*   **If you are an advanced student:** read this section fully, then follow the equivalence-first lanes through the axial torsion solves and the ledger/ADM accounting.
*   **If you are a careful general reader:** keep the pictures—**bend, flow, twist**; **coins + rim**; **prism → beams**—in mind. The equations will look familiar, and each one will be explained in plain language before it is used.

* * *

#### 4.1.2.8 What comes next
---------------------------------------------------

The rest of Chapter 4 delivers the pieces this introduction only names:

*   A sector-by-sector **stress–energy** with positivity visible at a glance.
*   The complete **equations of motion** and the short-range solutions induced by axial sources.
*   The **MET** proof that locks bulk + boundary energy into one invariant statement.
*   The **falsifiability pack** (signal speeds, DC positivity, short-range spin–spin, gauge-slice invariance, boundary balance).

---

## 4.2 Table of Contents and Introduction

### 4.2.1 Table of Contents (Section 4.2)
- 4.2.2 Eponyms
- 4.2.3 Connectivity Map

### 4.2.2 Eponyms
_See also:_ C0 §0.1–0.4, C5 §5.1–5.3

2\. Author‑defined eponyms (canonicalized for this paper)
=========================================================

> **Purpose.** This section fixes the handful of names, acronyms, and “house rules” we will reuse. Each entry has: a plain‑language gloss, the compact **contract** we rely on later, and a short “where it lives” pointer to Chapters 1, 2, 3, 5. No proofs here—only the canonical definitions we will not revisit.

The framework takes its shape here through the alignment of its essential components. Every quantity that follows being fields, operators, and derivatives, they move within the same mechanical structure that carries energy and curvature through space and time. Gradients set direction, curls describe rotation, divergences mark accumulation, and contractions connect motion to geometry. In canonical form these parts act together in continuous exchange, each maintaining the integrity of scale and orientation as information flows through them. The picture to hold is one of clear machinery, where every element advances another, and where the mathematics already anticipates the boundaries, spectra, and geometric extensions that lie ahead.

* * *

##### 4.2.2.2.1 **OS Locks** (the “operating system” of conventions)
--------------------------------------------------------

**Plain gloss.** The sign, orientation, and normalization decisions that make all equations in this project compatible.

**Contract.**

*   **Signature:**  $(-,+,+,+)$ .
*   **Orientation & Hodge:**  $\epsilon^{0123}=+1$ ; Hodge star  $*$  defined with that orientation.
*   **Units:**  $c=1=\hbar$  unless explicitly restored (we restore  $c$  only when writing ADM mass–energy).
*   **Couplings & traces:** gauge couplings ( $g$ ), axial coupling ( $g_S$ ), and Lie‑algebra traces are explicit.
*   **Boundary measure:** ADM/foliation uses lapse  $N$ , shift  $N^i$ , spatial metric  $h_{ij}$ ;  $\sqrt{|g|}=N\sqrt{h}$ .
*   **Fourier/response locks (see § 2.10):** retarded convention  $\omega\to\omega+i0^+$ ; Kubo/Plancherel consistent across continuous/discrete transforms.
*   **Wick map:** Euclideanization follows the signature above; positivity checks occur after Wick where stated.

**Where it lives:** Chapter 0 (declared once); cited throughout 1–5 when needed.

* * *

##### 4.2.2.2.2 **MGSP1** — _Miller Gravitational Gauge Slice Policy 1_
-----------------------------------------------------------

**Plain gloss.** The minimal, healthy torsion policy: only the **axial** torsion vector propagates.

**Contract.**

*   Torsion irreps decompose into: axial vector  $S_\mu$ , trace vector  $t_\mu$ , and traceless tensor  $q_{\mu\nu\rho}$ .
*   **Propagating DOF:** only  $S_\mu$  (massive spin‑1 → 3 polarizations).
*    $t_\mu$  and  $q_{\mu\nu\rho}$  appear **algebraically** (no wave operator) and can be eliminated on‑shell.
*   Health obligations (no ghosts, hyperbolic principal symbol) are satisfied by the Proca‑type kinetic for  $S_\mu$ .

**Where it lives:** Introduced in Chapter 2; audited by the “Stops” pipeline in Chapter 1; used everywhere in 4 & 5.

* * *

##### 4.2.2.2.3 **MFES** — _Miller Field Equation Set_
------------------------------------------

**Plain gloss.** The unified classical equations used in Chapter 4.

**Contract (schematic).**

$$
\begin{aligned} G_{\mu\nu}&=8\pi G\,T^{\rm total}_{\mu\nu},\\ \nabla_\nu H^{\nu\mu}+m_S^2 S^\mu&=g_S J_5^\mu,\quad H_{\mu\nu}\equiv\nabla_\mu S_\nu-\nabla_\nu S_\mu,\\ D_\nu F^{\nu\mu}&=J^\mu_{\rm gauge},\qquad \Box\phi-V'(\phi)=0,\\ (i\gamma^\mu D_\mu-m_\psi-g_S\gamma^\mu\gamma^5 S_\mu)\psi&=0, \end{aligned}
$$

with  $T^{\rm total}_{\mu\nu}$  the sum of sector stresses computed under the OS locks.

**Where it lives:** Derived in Chapter 4 (§ 4.2 & § 4.5); consistency checks in Chapter 1.

* * *

##### 4.2.2.2.4 **MET** — _Miller Equivalence Theorem_ (energy = bulk + boundary)
---------------------------------------------------------------------

**Plain gloss.** “Coins in the jar plus a coin on the rim”: bulk  $T_{00}$  across all sectors **plus** the gravitational boundary energy equals total energy.

**Contract (statement).**

$$
\boxed{\,E_{\rm total}=\int_{\Sigma} N\sqrt{h}\;T^{0}{}_{0,\,\rm total}\;+\;E_{\rm grav}^{\rm ADM}[\partial\Sigma] \equiv c^2\,M_{\rm ADM}\, .}
$$

**Preconditions.** Asymptotic flatness (or the appropriate quasi‑local substitute), well‑posed boundary data (GHY in place for Dirichlet metric), and fields obeying MFES.

**Invariance.** Adding total divergences or EOM‑proportional “improvements” changes only the boundary ledger; the equality is unchanged.

**Where it lives:** Proved in Chapter 4; boundary mechanics prepared in Chapter 3; used as the energy audit in 4 & 5.

* * *

##### 4.2.2.2.5 **MEFP** — _Miller Equivalence‑First Program_ (how we compute)
------------------------------------------------------------------

**Plain gloss.** Do the easy thing first, then prove it’s equivalent: a workflow that keeps derivations short and auditable.

**Contract (four lanes).**

1.  **Basis‑first.** Go to helicity/projector bases that diagonalize kinetic blocks.
2.  **Project → scalarize → solve.** Reduce each physical channel to a scalar resolvent (one inverse per spin).
3.  **Boundary & ledger corridor.** Declare BCs up front; move method‑dependent differences to the ledger.
4.  **Dispersion & positivity corridor.** Enforce causal/retarded conventions, DC order of limits, and positivity checks.

**Where it lives:** Methods catalog in Chapter 5; applied repeatedly in Chapter 4.

* * *

##### 4.2.2.2.6 **MPSD** — _Miller Projection–Scalarization Dictionary_
-----------------------------------------------------------

**Plain gloss.** The quick translation from “big tensors” to “one scalar inverse per physical channel.”

**Contract (core entries).**

*   **Vectors (Helmholtz–Proca).**  
     $`\Pi^{\rm T}{}^\mu{}_\nu=\delta^\mu{}_\nu-\nabla^\mu\nabla_\nu/\Box`$ ,  
     $`S^\mu = g_S(\Box+m_S^2)^{-1}\,\Pi^{\rm T}{}^\mu{}_\nu J_5^\nu`$ ,  
     $`\nabla_\mu S^\mu=(g_S/m_S^2)\nabla_\mu J_5^\mu`$  (algebraic longitudinal).
*   **Rank‑2 (Barnes–Rivers).**  
    Decompose  $h_{\mu\nu}$  with projectors  $P^{(2)},P^{(1)},P^{(0\text{s})},P^{(0\text{w})}$ ; invert per spin with residues checked in the chosen basis.
*   **Two‑forms (SD/ASD).**  
     $`H_\pm=\tfrac12(H\pm i*H)`$ ; in Euclidean signature, positivity is one line because  $`*^2=+1`$  on 2‑forms.
*   **Mixing blocks (one‑form multiplets).**  
    Use Sylvester criteria and Cholesky to produce a canonical SPD normalization without changing light cones or poles.

**Commutation note.** Under LTI media and compatible BCs, projectors commute with inverses; otherwise, we local‑Fourier or Hadamard‑patch and track remainders in the ledger.

**Where it lives:** Toolbox in Chapter 5; used to solve sources in Chapter 4.

* * *

##### 4.2.2.2.7 **MBLC** — _Miller Boundary–Ledger Corridor_
------------------------------------------------

**Plain gloss.** Separate dynamics from book‑keeping: boundary choices and method differences live in a ledger that does not alter bulk equations.

**Contract.**

*   **Declare BCs first:** Dirichlet/Neumann/Robin/Sommerfeld, plus the needed counterterms (e.g., GHY for metric Dirichlet).
*   **Green–Betti/Rellich** establish reciprocity and uniqueness (for radiation problems).
*   **Method equivalence:** free‑space+homogeneous ≡ images ≡ boundary integrals **under the same BCs**; discrepancies are posted to the **ledger** (boundary flux/topological integer), never to the bulk dynamics.
*   **ADM pairing:** gravitational boundary terms are kept explicit so MET holds transparently.

**Where it lives:** Boundary cookbook in Chapter 3; invoked whenever we integrate by parts in Chapter 4.

* * *

##### 4.2.2.2.8 **MDPC** — _Miller Dispersion–Positivity Corridor_
------------------------------------------------------

**Plain gloss.** The guardrails for response functions: causality, order of limits, and positivity.

**Contract.**

*   **Retarded convention:**  $G^R(\omega,\mathbf k)=G(\omega+i0^+,\mathbf k)$ .
*   **DC order:** take  $\mathbf k\to 0$  **before**  $\omega\to 0^+$ .
*   **Front speed:** high‑frequency wavefronts travel at light speed (cone nesting).
*   **Herglotz/Kramers–Kronig:**  $\Im G^R/\omega\ge 0$  near  $\omega\to0^+$ ; use subtractions where needed; apply moments/sum rules as checks.
*   **Massless limits:** regulate  $m\to0^+$ , isolate harmonics on  $\Sigma_t$ , and remove the regulator only after the DC order is enforced.

**Where it lives:** Diagnostics in Chapter 5; falsifiability pack in Chapter 4.

* * *

##### 4.2.2.2.9 **MLCP** — _Miller Ledger–Ceiling Principle_
------------------------------------------------

**Plain gloss.** In 4D, forms with degree  $p\ge 3$  carry no local propagating DOF—treat them as **ledger‑only** unless dualized to a single representative.

**Contract.**

*   Track integer/topological data (Pontryagin, Chern–Simons level, Nieh–Yan/Holst,  $H$ \-flux,  $F_4$ , …) **in the ledger**; do not replace bulk kinetics with these terms.
*   **Duality guard:** when  $B$  and  $\theta$  are dual, propagate only one; enforce with a Lagrange‑multiplier constraint and Schur reduction to avoid double counting.
*   **Wick invariance of integers:** ledger integers are unaffected by Wick rotation.

**Where it lives:** Topology & duality rules in Chapter 3; cross‑checked in 4 & 5.

* * *

##### 4.2.2.2.10 **MT** — _Miller Transform family_ (spectral standards)
------------------------------------------------------------

**Plain gloss.** One set of Fourier/DFT normalizations so plots, kernels, and Kubo formulas all agree.

**Contract.**

*   **Continuous (MT‑c):**  
     $\displaystyle \tilde f(\omega)=\frac{1}{\sqrt{2\pi}}\!\int\! dt\, e^{+i\omega t} f(t),\quad f(t)=\frac{1}{\sqrt{2\pi}}\!\int\! d\omega\, e^{-i\omega t}\tilde f(\omega)$ .
*   **Discrete (MT‑d):**  
     $\displaystyle \tilde f_k=\frac{1}{\sqrt{N}}\sum_{n=0}^{N-1} e^{+i 2\pi kn/N} f_n,\quad f_n=\frac{1}{\sqrt{N}}\sum_{k=0}^{N-1} e^{-i 2\pi kn/N}\tilde f_k.$ 
*   **Single‑shot (MT‑1S):** A one‑frequency estimator  $\widetilde f(\Omega)=(\Delta t/\sqrt{2\pi})\sum_n w_n f_n e^{-i\Omega n\Delta t}$  that matches MT‑d when  $\Omega$  is on‑grid.

**Where it lives:** Declared in Chapter 0; used in response/dispersion work in Chapters 4–5.

* * *

##### 4.2.2.2.11 **“Coins + Rim”** and **“Prism → Beams”** (visual vocabulary)
------------------------------------------------------------------

**Coins + Rim.** Bulk energy density  $T_{00}$  are the **coins in the jar**; the ADM boundary term is the **coin on the rim**. Together they make the total (MET). Use this metaphor whenever moving terms between bulk and boundary.

**Prism → Beams.** Complicated fields split by a **prism** (projectors) into **beams** (physical channels). Each beam is solved by a scalar resolvent (MPSD), then recombined.

**Where they live:** Figure captions and prose cues in Chapter 4 and the quick‑start in Chapter 5.

* * *

##### 4.2.2.2.12 **Stops** — the Ghost‑Control pipeline
-------------------------------------------

**Plain gloss.** A short mandatory checklist the theory must pass **at each step**.

**Contract (minimum set).**

1.  **Kinetic signs/Hessian rank** (no ghosts).
2.  **Constraint closure** (first/second class; correct DOF count).
3.  **Hyperbolicity & cone nesting** (front speed  $\le 1$ ).
4.  **Symplectic positivity** (Hamiltonian bounded below in the physical subspace).
5.  **Boundary well‑posedness** (GHY/counterterms match chosen BCs).
6.  **Gauge‑slice independence** (Nielsen identity; poles/residues  $\xi$ \-independent).
7.  **Dispersion positivity** (MDPC checks).

**Where it lives:** Chapter 1; applied implicitly in Chapter 4, explicitly in Chapter 5 examples.

* * *

##### 4.2.2.2.13 One‑page **Glossary & Cross‑walk**
---------------------------------------

| Eponym | Plain meaning | What it governs | Where defined | First heavy use |
| --- | --- | --- | --- | --- |
| OS Locks | Shared sign/orientation/normalization | All equations | § 2.1 / Ch. 0 | Everywhere |
| MGSP1 | Only axial torsion propagates | Field content & health | § 2.2 / Ch. 2 | §§ 4.2–4.6 |
| MFES | Unified EOM set | What we solve | § 2.3 / Ch. 4 | § 4.2 onward |
| MET | Energy = bulk  $T_{00}$  + ADM | Energy accounting | § 2.4 / Ch. 4 | § 4.7 |
| MEFP | How we compute, equivalently | Workflow | § 2.5 / Ch. 5 | Throughout § 4 |
| MPSD | Projectors → scalar inverses | Inversion/solves | § 2.6 / Ch. 5 | §§ 4.6–4.8 |
| MBLC | Boundaries & the ledger | Variations/BCs | § 2.7 / Ch. 3 | §§ 4.2, 4.7 |
| MDPC | Causality/positivity corridor | Response/DC limits | § 2.8 / Ch. 5 | §§ 4.8–4.9 |
| MLCP | Topology ceiling & duality guard | Integer/flux data | § 2.9 / Ch. 3 | § 4.10 |
| MT | Fourier/DFT standards | Spectral work | § 2.10 / Ch. 0 | §§ 4.8–4.9 |
| Coins + Rim | Energy metaphor for MET | Intuition | § 2.11 | § 4.7 |
| Prism → Beams | Projector intuition | Intuition & solves | § 2.11 | § 4.6 |

* * *

### 4.2.3 Connectivity Map
**Within Chapter 4 (closely related):**
- §4.1 — Introduction — from textbook physics to UGFT
- §4.4 — UGFT action (bulk, boundary, topology) and the MGSP1 policy
- §4.5 — Miller Field Equation Set (MFES) — full classical system
- §4.7 — The Miller Equivalence Theorem (MET) — statement & proof sketch
- §4.8 — Equivalence-first computation (MEFP) and MPSD lanes
- §4.9 — Causality, hyperbolicity, response & dispersion (MDPC)
- §4.10 — Boundary, uniqueness, topology & ledgers (MBLC + MLCP)
- §4.11 — Spectral standardization — the Miller Transform (MT)
- §4.12 — Sanity limits & effective descriptions
- §4.13 — Legacy & intermediate forms
- §4.14 — Health, gauge-slice independence, and audits

**External chapters (C#):**
- C0 §0.1–0.4
- C5 §5.1–5.3

---

## 4.3 Table of Contents and Introduction

### 4.3.1 Table of Contents (Section 4.3)
- 4.3.2 Classical starting point — standard actions & EOM
- 4.3.3 Connectivity Map

### 4.3.2 Classical starting point — standard actions & EOM
_See also:_ §4.4, §4.5, §4.6, §4.9, §4.10; C0 §0.12, C5 §5.6, C2 §3–5

3\. Classical starting point — standard actions & EOM
===========================================================================================

> This section is your “starter kit.” We walk from the familiar—gravity as a bendable grid, fields as flows, matter as excitations—up to the precise actions, equations of motion, and boundary terms we’ll actually use. Every topic starts in plain language and then climbs the ladder to the full calculus. Nothing “UGFT-new” is introduced here beyond vocabulary and conventions; that arrives in the next sections. Think of this as the ground truth we promise never to contradict.

We start where the classical page is clearest: an action, a variation, an equation of motion. From Newton’s particle to Maxwell’s field and Einstein’s metric, the same engine runs the story. The integral encodes the balance, the Euler–Lagrange rule gives the differential law, and Noether’s insight ties symmetry to conserved flow. With this footing we step toward UGFT without changing the method. We keep the metric for bend and the familiar gauge fields for flow, and we add one short‑range axial twist (S_\mu) that responds to handed currents. Its longitudinal part is fixed by a constraint, its transverse part propagates, and the stress it carries fits into the same energy accounting. What moves is the cast of fields, not the principle. The path from classical actions to UGFT is a continuous line written in the same variational hand.

* * *

##### 4.3.2.3.1 Imports we all share (the “OS locks” in slow motion)
--------------------------------------------------------

**Plain picture.** Before doing any physics we pick our ruler and compass: which way is time, how we count volume, which Fourier sign we use. If two people use the same ruler, they’ll agree on every length they measure later.

**Expert compact.**

*   **Signature & orientation.** Spacetime metric has signature  $(-,+,+,+)$ . Orientation is fixed so  $\epsilon_{0123}=+\sqrt{|g|}$  and  $\epsilon^{0123}=+1/\sqrt{|g|}$ .
*   **Hodge star.** On  $p$ \-forms in 4D Lorentzian,  $*^2=(-1)^{p(4-p)+1}$ . We’ll flip to Euclidean (Wick) when doing positivity one-liners for quadratic forms.
*   **Units.**  $c=\hbar=1$  unless we temporarily restore  $c$  to write  $E=c^2M$  in MET statements.
*   **ADM split (for boundaries).**  $g_{\mu\nu}$  decomposes into lapse  $N$ , shift  $N^i$ , and spatial metric  $h_{ij}$ , with  $\sqrt{|g|}=N\sqrt{h}$ . Spatial delta is  $\delta_\gamma^{(3)}$ , and  $\delta_g^{(4)}=\delta(t-t_0)\,\delta_\gamma^{(3)}/N$ .
*   **Fourier/response locks.** Our Fourier phase is  $e^{\,i(\omega t-\mathbf{k}\cdot\mathbf{x})}$ . “Retarded” means  $\omega\to\omega+i0^+$ . Plancherel/Parseval are kept unitary in both continuous and discrete forms (the “MT” family you saw earlier).
*   **Couplings/traces.** Gauge coupling  $g$  and axial coupling  $g_S$  stay explicit. For non-Abelian fields,  $\mathrm{Tr}(T^AT^B)=\delta^{AB}$ .

> From here on, every sign, factor, and surface measure is determined. We don’t re-decide the ruler halfway through the chapter.

* * *

##### 4.3.2.3.2 Gravity (Einstein–Hilbert + GHY): bend, vary, and balance
-------------------------------------------------------------

**Layman-first.** Imagine a taut rubber sheet. Drop a heavy ball: the sheet curves. That curve tells lighter marbles how to roll. In GR, the sheet is the metric  $g_{\mu\nu}$ , the heavy ball is energy–momentum  $T_{\mu\nu}$ , and the marbles are freely falling worldlines (geodesics). Energy tells space-time how to bend; that bend tells motion how to flow.

**Field-theory form.** The bending is encoded in the scalar curvature  $R$ . The cleanest action that yields Einstein’s equations is Einstein–Hilbert plus a boundary counterterm:

$$
S_{\text{EH+GHY}} =\frac{1}{16\pi G}\int_{\mathcal M}\!\! d^4x\,\sqrt{|g|}\,R \;+\;\frac{1}{8\pi G}\int_{\partial\mathcal M}\!\! d^3x\,\sqrt{|h|}\,K.
$$
*    $\sqrt{|g|}\,R$  is the bulk curvature.
*   The **Gibbons–Hawking–York (GHY)** term makes the variational problem well-posed if we hold the induced metric fixed at the boundary ( $`\delta h_{ij}=0`$ )—without it, varying  $R$  produces a total divergence that spoils the Euler–Lagrange story.

**Variation → field equations.** Varying  $g^{\mu\nu}$  gives

$$
\delta S_{\text{EH}}=\frac{1}{16\pi G}\int_{\mathcal M}\!\sqrt{|g|}\,G_{\mu\nu}\,\delta g^{\mu\nu} \;+\;\frac{1}{16\pi G}\int_{\partial\mathcal M}\!\! d^3x\ \sqrt{|h|}\,(\cdots)\,,
$$

and the boundary variation is exactly canceled by  $\delta S_{\text{GHY}}$  when the boundary metric is fixed. Adding matter with action  $S_\text{matt}$  and defining

$$
T_{\mu\nu} \equiv -\frac{2}{\sqrt{|g|}}\frac{\delta S_\text{matt}}{\delta g^{\mu\nu}},
$$

the stationary condition yields **Einstein’s equation**

$$
G_{\mu\nu}=8\pi G\,T_{\mu\nu},\qquad \nabla^\mu G_{\mu\nu}=0\ \Rightarrow\ \nabla^\mu T_{\mu\nu}=0.
$$

**Boundary energy (why we cared about ADM).** In the ADM 3+1 split, the extrinsic curvature  $K_{ij}$  and the spatial metric  $h_{ij}$  form the canonical data. The Hamiltonian becomes a sum of constraints plus a **surface term** at spatial infinity—**the ADM energy**. That surface term is the “coin on the rim” in our energy ledger; we will add it to the jar of bulk  $T_{00}$  to get total energy (MET).

**Legacy lane kept (for comfort & audits).**

*   **Linearized gravity**: write  $g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}$ , adopt **harmonic/de Donder** gauge  $\partial^\mu\bar h_{\mu\nu}=0$  ( $\bar h_{\mu\nu} = h_{\mu\nu}-\tfrac12 \eta_{\mu\nu}h$ ), and solve  $\Box \bar h_{\mu\nu}=-16\pi G\,T_{\mu\nu}$ .
*   **York–ADM**: constraints  $\mathcal{H}=0$ ,  $\mathcal{H}_i=0$  and a clean way to read off the boundary energy.

* * *

##### 4.3.2.3.3 Gauge fields (Maxwell/Yang–Mills): flows, curvature, and color
------------------------------------------------------------------

**Layman-first.** If gravity is the sag of the sheet, gauge fields are the **ripples and lines of force** running across it. They carry energy and momentum, they push on charges, and—because they’re waves—light is literally one of them.

**Abelian to non-Abelian.** For electromagnetism, the potential  $A_\mu$  has field strength  $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ . For Yang–Mills,  $A_\mu = A_\mu^A T^A$  takes values in a Lie algebra; the field strength adds a commutator:

$$
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu + g\,[A_\mu, A_\nu].
$$

The **action** is universally

$$
S_{\rm YM}=-\frac12\int d^4x\,\sqrt{|g|}\,\mathrm{Tr}\!\left(F_{\mu\nu}F^{\mu\nu}\right).
$$

Varying  $A_\mu$  gives the **Yang–Mills equations**

$$
D_\nu F^{\nu\mu} = g\,J^\mu, \qquad D_\nu \equiv \nabla_\nu + i g [A_\nu,\,\cdot\,].
$$

**Stress–energy and positivity.** The gauge stress–energy is

$$
T^{\rm YM}_{\mu\nu}=\mathrm{Tr}\!\left(F_{\mu\alpha}F_\nu{}^{\alpha}-\tfrac14 g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\right).
$$

In a local inertial frame,  $T_{00}=\tfrac12\mathrm{Tr}(\mathbf{E}^2+\mathbf{B}^2)\ge 0$ .

**Boundary behavior (what you hold fixed).** The variational principle is well-posed by declaring either the potential (Dirichlet-type) or the normal component of the field strength (Neumann-type) on the boundary; for radiating problems, **Sommerfeld** conditions (outgoing waves) plus reciprocity fixes uniqueness.

**Legacy lane kept.**

*   **Lorenz gauge**  $\nabla^\mu A_\mu=0$  and the BRST/Faddeev–Popov apparatus live here for people who like them.
*   For **mixing** among multiple 1-forms (e.g., kinetic matrices), we’ll use **Sylvester** tests and **Cholesky** factors to bring the quadratic form to a canonical SPD normalization without changing the light cone or the physical poles. Later we’ll prove this is equivalent to our projector-first route.

* * *

##### 4.3.2.3.4 Scalars (Klein–Gordon): one number per point, with a landscape
------------------------------------------------------------------

**Layman-first.** A scalar field is like a **temperature map**: a single value at each point that can slosh, ring, and settle into valleys of a potential  $V(\phi)$ .

**Action, equation, stress–energy.**

$$
S_\phi=\int d^4x\,\sqrt{|g|}\left(-\tfrac12\,\partial_\mu\phi\,\partial^\mu\phi - V(\phi)\right),\qquad \Box\phi - V'(\phi)=0,
$$
 
$$
T^{(\phi)}_{\mu\nu}=\partial_\mu\phi\,\partial_\nu\phi - \tfrac12 g_{\mu\nu}(\partial\phi)^2 - g_{\mu\nu}V(\phi).
$$

In a local inertial frame,  $T_{00}=\tfrac12(\dot\phi)^2+\tfrac12(\nabla\phi)^2+V(\phi)\ge 0$  when  $V\ge 0$ .

**Improvements (a note for experts).** The “improved” scalar stress–energy adding a total divergence can make conformal properties manifest; in our energy accounting those improvements shift **only** boundary terms (the ledger), not bulk equations or positivity.

**Boundary choices.** Dirichlet ( $\phi$  fixed) and Neumann ( $n^\mu\partial_\mu\phi$  fixed) correspond to adding or omitting a simple surface term in the variation. Sommerfeld makes sense for outgoing scalar waves.

* * *

##### 4.3.2.3.5 Spinors (Dirac): handedness, covariant derivatives, and  $J_5^\mu$
-----------------------------------------------------------------------

**Layman-first.** Fermions carry **spin and handedness**. “Right-handed” and “left-handed” refer to how an internal arrow (spin) aligns with motion. The difference between them forms the **axial current**  $J_5^\mu$ . That current will later be the one and only “plug” our new torsion field connects to.

**Geometry you actually need.** In curved space we use a tetrad  $`e^a{}_\mu`$  and a spin connection  $\omega_\mu{}^{ab}$ . The gamma matrices are flat-space objects  $\{\gamma^a,\gamma^b\}=2\eta^{ab}$ , and  $\gamma^\mu=e^\mu{}_a\gamma^a$ . The covariant derivative acting on a spinor is

$$
D_\mu\psi = \partial_\mu\psi + \frac{1}{4}\omega_{\mu ab}\gamma^{ab}\psi + i g A_\mu^A T^A\psi,
$$

with  $\gamma^{ab}\equiv \tfrac12[\gamma^a,\gamma^b]$ .

**Action and equation of motion.**

$$
S_\psi = \int d^4x\,\sqrt{|g|}\ \bar\psi\,(i\gamma^\mu D_\mu - m_\psi)\psi,\qquad (i\gamma^\mu D_\mu - m_\psi)\psi=0.
$$

**The axial current—UGFT’s hook.**

$$
J_5^\mu \equiv \bar\psi\,\gamma^\mu\gamma^5\,\psi.
$$

Classically  $\nabla_\mu J_5^\mu= 0$  for massless fermions (modulo anomalies in quantum loops); in this chapter we stay classical. Later, our axial torsion  $S_\mu$  will couple **only** to  $J_5^\mu$ .

**Stress–energy (Belinfante).** The symmetric energy–momentum tensor is constructed to match variation with respect to  $g_{\mu\nu}$ . We keep it implicit here; the explicit form appears in the Appendix so as not to distract from the flow.

**Legacy lane kept.** For loop calculations  $\gamma^5$  requires care (e.g., Larin’s scheme). We flag it here, but it won’t enter the classical story that follows.

* * *

##### 4.3.2.3.6 Massive spin-1 (Proca): short-range waves and algebraic longitudinal
------------------------------------------------------------------------

**Layman-first.** Think of a field like electromagnetism but with a **limited reach**: nudge it here and its influence fades as  $e^{-mr}/r$ . That’s a Proca field: a vector with mass  $m$ . It has three physical wave polarizations (two transverse, one longitudinal), but the “longitudinal” is not freely wavy—its value is fixed by the source.

**Action and EOM.**

$$
S_V=\int d^4x\,\sqrt{|g|}\left(-\tfrac14 H_{\mu\nu}H^{\mu\nu}+\tfrac12 m^2 V_\mu V^\mu\right),\quad H_{\mu\nu}=\nabla_\mu V_\nu-\nabla_\nu V_\mu.
$$

Variation gives

$$
\nabla_\nu H^{\nu\mu}+m^2 V^\mu = J^\mu,\qquad \nabla_\mu V^\mu = \frac{1}{m^2}\nabla_\mu J^\mu.
$$

If  $J^\mu$  is conserved ( $\nabla_\mu J^\mu=0$ ), then  $\nabla_\mu V^\mu=0$  on shell and only the transverse modes propagate.

**Propagator & static limit (expert candy).** In flat space and momentum variables  $k^\mu=(\omega,\mathbf{k})$ ,

$$
D_{\mu\nu}(k)=\frac{-\eta_{\mu\nu}+\frac{k_\mu k_\nu}{m^2}}{k^2-m^2+i0^+},
$$

and a static point source yields the Yukawa potential  $V_0(r)\sim \tfrac{e^{-mr}}{4\pi r}$ .

**Stress–energy (for positivity later).**

$$
T^{(V)}_{\mu\nu}=H_{\mu\alpha}H_\nu{}^{\alpha}-\tfrac14 g_{\mu\nu}H_{\alpha\beta}H^{\alpha\beta} +m^2\!\left(V_\mu V_\nu-\tfrac12 g_{\mu\nu}V_\alpha V^\alpha\right).
$$

In a local inertial frame,  $T_{00}=\tfrac12(\mathbf{E}_V^2+\mathbf{B}_V^2)+\tfrac12 m^2(V_0^2+\mathbf{V}^2)\ge0$ , where  $\mathbf{E}_V$  and  $\mathbf{B}_V$  are the electric-/magnetic-like pieces of  $H$ .

**Why we showed you this.** Our new axial torsion  $S_\mu$  (introduced in §4) behaves exactly like this, with  $m\to m_S$  and source  $g_S J_5^\mu$ . So Proca is the **template** you already know for the new physics to feel natural.

**Legacy lane kept.** The **Stückelberg** split  $V_\mu=\hat V_\mu+\partial_\mu \pi/m$  and  $R_\xi$  gauges are great for loop or gauge-parameter checks; we’ll keep them as an audit lane. Physical poles/residues don’t depend on  $\xi$  (Nielsen identity).

* * *

##### 4.3.2.3.7 Two-forms and higher forms: what truly propagates, what belongs to the ledger
---------------------------------------------------------------------------------

**Layman-first.** Some fields don’t wiggle the way vectors and scalars do. In 4D, a 2-form has just one local bead of information per point (dual to a pseudoscalar), and a 3-form has **no** local beads at all—only a global tally, like the number of turns in a wrapped rope. Those global tallies matter at the boundary but don’t drive bulk dynamics. That’s why we keep a **ledger**.

**Two-form basics.** A 2-form potential  $B$  has field strength  $H=dB$  and action

$$
S_B=-\frac{1}{12}\int d^4x\,\sqrt{|g|}\,H_{\mu\nu\rho}H^{\mu\nu\rho},\qquad d{*H}=0.
$$

On shell in 4D,  $H$  can be written as  $H=*\,d a$  for a pseudoscalar  $a$ : the 2-form is **dual** to a scalar.

**Self/anti-self-dual split (positivity shortcut).** In Euclidean signature,  $*^2=+1$  on 2-forms, so  $H$  decomposes as  $H_\pm=\tfrac12(H\pm *H)$ . The quadratic form becomes  $\|H_+\|^2+\|H_-\|^2\ge 0$  at a glance—useful for quick health checks.

**Three-forms and integers.** In 4D, a 3-form potential’s field strength is a 4-form  $F_4$ , and  $d{*F_4}=0$  implies  $*F_4=$  constant. No local waves—just a constant flux that behaves like a parameter (e.g., an effective cosmological constant). We treat such data as **ledger-only** (topological integers, fluxes, Pontryagin/CS levels, Nieh–Yan/Holst entries): they live at the boundary and in global sectors, not in the bulk equations.

**Duality guard.** When a  $B$ \-field and an axion  $\theta$  are dual descriptions, we **propagate only one** and enforce the relation with a constraint. This prevents double counting and keeps MET’s energy ledger honest.

* * *

##### 4.3.2.3.8 Stress–energy (sector by sector) and the positivity audit you’ll reuse
--------------------------------------------------------------------------

**Layman-first.** Every field deposits “coins” into the energy jar. The simplest check of health is: are all the coins non-negative for small ripples? If the answer is yes, we’re on solid ground.

**Unified definition.** For any matter/gauge/field sector with action  $S[\Phi;g]$ ,

$$
T_{\mu\nu} \equiv -\frac{2}{\sqrt{|g|}}\frac{\delta S}{\delta g^{\mu\nu}}.
$$

Explicitly for the sectors we use most:

$$
\begin{aligned} T^{\rm YM}_{\mu\nu} &=\mathrm{Tr}\!\left(F_{\mu\alpha}F_\nu{}^{\alpha}-\tfrac14 g_{\mu\nu}F^2\right),\\[4pt] T^{(\phi)}_{\mu\nu} &=\partial_\mu\phi\,\partial_\nu\phi-\tfrac12 g_{\mu\nu}(\partial\phi)^2-g_{\mu\nu}V(\phi),\\[4pt] T^{(V)}_{\mu\nu} &=H_{\mu\alpha}H_\nu{}^{\alpha}-\tfrac14 g_{\mu\nu}H^2 +m^2\!\left(V_\mu V_\nu-\tfrac12 g_{\mu\nu}V^2\right). \end{aligned}
$$

**Positivity in a local inertial frame.**

$$
\begin{aligned} T^{\rm YM}_{00}&=\tfrac12 \mathrm{Tr}(\mathbf{E}^2+\mathbf{B}^2)\ge 0,\\ T^{(\phi)}_{00}&=\tfrac12\dot\phi^2 + \tfrac12(\nabla\phi)^2 + V(\phi)\ \ (\text{non-neg. if }V\ge0),\\ T^{(V)}_{00}&=\tfrac12(\mathbf{E}_V^2+\mathbf{B}_V^2)+\tfrac12 m^2 (V_0^2+\mathbf{V}^2)\ge 0. \end{aligned}
$$

These are the same checks we’ll apply to the axial torsion field  $S_\mu$  later—one reason we emphasize the Proca template.

**Improvements don’t change the jar.** Adding a total divergence to a Lagrangian shifts  $T_{\mu\nu}$  by a divergence (“improvement”). On shell, that changes **only** flux through the boundary (the ledger), not the non-negativity of the coins in the jar. This is one of the structural reasons the MET is stable under reformulations.

* * *

##### 4.3.2.3.9 Boundary terms & well-posedness: declare the checkout counter first
-----------------------------------------------------------------------

**Layman-first.** Varying an action is like checking out at a store: the cashier scans each item (bulk term) and then prints a receipt (boundary terms). If you don’t tell the cashier what to do about the last item, you leave with a messy bill. Physics is the same: declare your **boundary conditions** before you start.

**Gravity.** Dirichlet metric data requires **GHY** so the variation has no leftover surface piece. In ADM language, this also isolates the surface energy (ADM mass) that appears in MET.

**Scalars and vectors.** For a scalar,

$$
\delta S_\phi = \int_{\mathcal M}\!\sqrt{|g|}\,(\Box\phi-V'(\phi))\,\delta\phi + \int_{\partial\mathcal M}\!\sqrt{|h|}\,n^\mu\partial_\mu\phi\,\delta\phi.
$$

Fixing  $\phi$  (Dirichlet) kills the boundary variation; fixing  $n\!\cdot\!\partial\phi$  (Neumann) instead requires subtracting a surface term in the action so the bulk variation is clean. Vectors behave similarly with  $A_\mu$  vs  $n_\nu F^{\nu\mu}$  fixed. For radiation, **Sommerfeld** conditions (outgoing waves) plus Green–Betti reciprocity and **Rellich** uniqueness select the physical solution.

**Method equivalence lives in the ledger.** Solving a boundary problem with free-space Green’s functions plus homogeneous solutions, or with images, or with boundary integrals—under the **same BCs**—yields the same bulk solution. Any difference appears as a different partition of **boundary flux** and is therefore a **ledger** issue, not a change to the equations themselves.

* * *

##### 4.3.2.3.10 Legacy lanes we keep (because many readers think in them)
-------------------------------------------------------------

We prefer a projector-first, “equivalence-first” computation style later (fast, auditable). But we keep the classics as **parallel audit trails**:

*   **Gravity:** harmonic/de Donder for linear solves; York–ADM to read constraints and energy.
*   **Gauge:** Lorenz gauge and the BRST/Faddeev–Popov path integral; for multiple 1-forms, Sylvester and Cholesky to diagonalize quadratic forms.
*   **Massive vectors:** Stückelberg plus  $R_\xi$  gauges; check that physical poles/residues don’t depend on  $\xi$  (Nielsen identity).
*   **Forms & boundaries:** SD/ASD splits for 2-forms (Euclidean positivity), and method-of-images vs. boundary integrals unified by reciprocity/Rellich.

Later, Chapter 5 proves these lanes are **equivalent** to our short projector/Helmholtz/Barnes–Rivers lanes up to **ledger** terms.

* * *

##### 4.3.2.3.11 Snap-together guide (narrative version of the side-by-side)
----------------------------------------------------------------

*   **Gravity (EH+GHY → ADM rim coin).** The Einstein–Hilbert bulk term plus GHY yields Einstein’s equation and a clean boundary term. In ADM, that boundary term is the **ADM energy**—the rim coin that, added to bulk  $T_{00}$ , gives total energy in MET.
*   **Gauge (−½Tr  $F^2$  → flows with fixed traces).** We keep group traces and couplings explicit so every later projector and dispersion statement carries the right normalization. Energy density is  $\tfrac12(\mathbf{E}^2+\mathbf{B}^2)$ .
*   **Scalar (Klein–Gordon → DC/positivity seed).** The scalar’s positivity and boundary variations are the simplest template for the DC/positivity corridor we enforce later for every sector.
*   **Dirac (spin connection → axial current).** The Dirac action explains covariant spinors; the **axial current**  $J_5^\mu$  is singled out now because it is the only fermionic source our new  $S_\mu$  will “feel.”
*   **Proca (massive 1-form → torsion template).** The Proca field’s equations, positivity, and Yukawa static limit are a rehearsal for the axial torsion sector—just swap  $V_\mu\mapsto S_\mu$ ,  $m\mapsto m_S$ ,  $J^\mu\mapsto g_S J_5^\mu$ .
*   **Forms/topology (what moves vs. what counts).** 2-forms can be dualized to scalars; 3-forms carry only global counts. Those counts, plus integer topological terms, live in the **ledger** and never replace bulk kinetics.

* * *

##### 4.3.2.3.12 What this equips you to do next
------------------------------------

You now have the **reference kit**: the actions, equations, stress–energies, and boundary practices that every later derivation compiles against. In §4 we **add one field**—a healthy axial torsion vector  $S_\mu$ —and nothing else about the starter kit changes. You’ll see that  $S_\mu$  behaves like Proca, couples axially to matter, respects all the health checks, and, crucially, that our **energy** is the **bulk** integral of  $T_{00}$  from _all_ sectors **plus** gravity’s **boundary** piece. That is the Miller Equivalence Theorem we will prove—carefully, but now with your toolbox already open on the table.

### 4.3.3 Connectivity Map
**Within Chapter 4 (closely related):**
- §4.4 — UGFT action (bulk, boundary, topology) and the MGSP1 policy
- §4.5 — Miller Field Equation Set (MFES) — full classical system
- §4.6 — Stress–energy and positivity (sign-locked, per sector)
- §4.9 — Causality, hyperbolicity, response & dispersion (MDPC)
- §4.10 — Boundary, uniqueness, topology & ledgers (MBLC + MLCP)

**External chapters (C#):**
- C0 §0.12
- C5 §5.6
- C2 §3–5

---

## 4.4 Table of Contents and Introduction

### 4.4.1 Table of Contents (Section 4.4)
- 4.4.2 UGFT action (bulk, boundary, topology) and the MGSP1 policy
- 4.4.3 Connectivity Map

### 4.4.2 UGFT action (bulk, boundary, topology) and the MGSP1 policy
_See also:_ §4.5, §4.6, §4.7, §4.8, §4.9, §4.10, §4.12; C2 §0–6, C3 §3.13–3.20, C0 §0.12, C1 §0–7

4\. UGFT action (bulk, boundary, topology) and the MGSP1 policy
===============================================================

> **What this section presents.**
> 
> 1.  The **unified UGFT action** as a sum of the legacy bulk (from §3) **plus** a new **axial torsion sector**  $S_\mu$ .
> 2.  The **ledger**: boundary and topological entries that record flux and integers without altering bulk equations.
> 3.  The **MGSP1 policy** (“axial-only propagates”) with its health consequences: correct degrees of freedom, positive energy, causal cones.
> 4.  The **field equations** contributed by  $S_\mu$ ; its **Hamiltonian** structure; **hyperbolicity**; **projector / Helmholtz** scalarization and Green kernels; **boundary conditions** specific to  $S_\mu$ ; the **energy** contribution  $T^{(S)}_{00}$ ; and the **decoupling** (heavy-field) limit.  
>     Each topic begins in plain language, then climbs to precise statements and equations.

The structure of nature reveals itself most clearly when the interior of space and its boundary are treated as one continuous whole. It honestly just "feels better" this way and will finally let me rest at night. In the unified field formulation of UGFT, the same expression that describes the bending of space and the motion of fields also fixes how the surface must behave, so that every influence entering or leaving the region is accounted for. Within the volume lies the activity. The curvature, the gauge flows, the axial twist of spacetime while the boundary serves as the faithful record, keeping the balance between what moves inside and what departs. The topology of the domain, unchanged by any smooth deformation, adds a quiet arithmetic of its own, identifying the global shape that no local measurement can alter. The MGSP1 restriction keeps this structure sound. Only the axial part of torsion is allowed to carry energy through space, while the trace and tensor parts remain as background geometry. In this arrangement, geometry and matter no longer confront one another; Instead they work together as facets of a single harmony, where causes unfold within the limits set by light and where nothing escapes the ledger that joins the bulk to its edge.

* * *

##### 4.4.2.4.1 The axial torsion bulk sector and its unique matter coupling
----------------------------------------------------------------

**Intuition first.**  
Add one new, polite degree of freedom: a short-range, spin-1 “twist”  $S_\mu$  that responds to **handedness** in matter. It behaves like a Proca field—never outruns light, stores positive energy, and quiets down exponentially with distance. Its handshake is unique: the **axial** current of fermions  $J_5^\mu$ .

**Definition and placement in the action.**  
Let  $\mathcal L_{\text{legacy}}$  denote the bulk from §3. The UGFT action is

$$
S_{\rm UGFT}= \int_{\mathcal M}\! d^4x\,\sqrt{|g|}\,\Big[\mathcal L_{\text{legacy}}+\mathcal L_S\Big]\;+\;S_{\rm ledger},
$$

with the **new** axial sector

$$
\mathcal L_S\equiv -\frac14\,H_{\mu\nu}H^{\mu\nu} +\frac12 m_S^2\,S_\mu S^\mu - g_S\,S_\mu J_5^\mu, \qquad H_{\mu\nu}\equiv \nabla_\mu S_\nu-\nabla_\nu S_\mu,\quad J_5^\mu\equiv \bar\psi\gamma^\mu\gamma^5\psi .
$$

**Notes for the technical reader.**

*    $S_\mu$  is a **matter one-form** with Proca kinetics built from the Levi–Civita connection; this choice keeps the principal symbol clean and avoids kinetic mixing with the metric at leading order.
*    $[\partial]=1,\ [S]=1,\ [m_S]=1,\ [g_S]=0$ . The axial coupling is parity-odd, as expected from  $\gamma^5$ .
*   The axial coupling is the **sole** renormalizable classical hook to fermions consistent with our locks.

* * *

##### 4.4.2.4.2 The ledger: boundary pairing and topological integers
---------------------------------------------------------

**Intuition first.**  
A clean variational principle and honest global accounting live in a dedicated compartment—the **ledger**. Items here can change surface fluxes or encode integer topology, but they **never** replace bulk kinetics or modify bulk equations.

**Content and role.**

$$
S_{\rm ledger}\equiv S_{\rm GHY}[g]\;+\; S_{\partial,\text{matter/YM}}^{\rm (BC)} \;+\; S_{\rm topo}.
$$
*   **Boundary pairing (gravity):**  $S_{\rm GHY}=\frac{1}{8\pi G}\!\int_{\partial\mathcal M}\!\sqrt{|h|}\,K$  pairs with  $R$  so metric Dirichlet data has a well-posed variation; its asymptotic evaluation yields the **ADM surface energy** used later in the Miller theorem.
*   **Boundary choices (matter & YM):** the specific surface term for each sector is included according to the declared BCs (Dirichlet/Neumann/Robin/Sommerfeld).
*   **Topological integers:** Pontryagin  $\nu_G=\frac{1}{8\pi^2}\!\int\!\mathrm{Tr}(F\wedge F)\in\mathbb Z$ ; Chern–Simons with **rescaled**  $\mathcal A\equiv gA$  so  $k\in\mathbb Z$  is manifest; Nieh–Yan/Holst in the torsional/gravitational ledger.
*   **Duality guard & ceiling:** in 4D,  $p\ge3$  forms have no local DOF—treat as ledger-only. For  $B\leftrightarrow\theta$ , propagate exactly **one** representative and impose the duality by constraint to avoid double counting.

* * *

##### 4.4.2.4.3 MGSP1: the axial-only torsion policy
----------------------------------------

**Intuition first.**  
Torsion splits into three flavors: trace, axial, traceless-tensor. Propagating the wrong pieces invites ghosts or spin-2 pathologies. MGSP1 selects the **axial** flavor only—simple, healthy, sufficient.

**Decomposition and policy.**

$$
T_{\mu\nu\rho} =\tfrac13\!\left(t_\nu g_{\mu\rho}-t_\rho g_{\mu\nu}\right) +\tfrac16\epsilon_{\mu\nu\rho\sigma}S^\sigma +q_{\mu\nu\rho}.
$$

**Policy:** propagate  $S_\mu$  with the Proca kinetic; keep  $t_\mu$  and  $q_{\mu\nu\rho}$  algebraic (non-wave).  
**Consequences:** three physical polarizations; no spin-2 ghosts; clean principal symbol; smooth decoupling as  $m_S\!\to\!\infty$  or  $g_S\!\to\!0$ .

* * *

##### 4.4.2.4.4 Field equations contributed by the axial sector
---------------------------------------------------

**Intuition first.**  
Turning the axial knob adds one equation and one stress–energy block; all other legacy equations remain as in §3.

**Euler–Lagrange for  $S_\mu$ .**

$$
\nabla_\nu H^{\nu\mu}+m_S^2 S^\mu=g_S J_5^\mu, \qquad \nabla_\mu S^\mu=\frac{g_S}{m_S^2}\,\nabla_\mu J_5^\mu\quad(\text{algebraic longitudinal}).
$$

**Stress–energy contribution.**

$$
T^{(S)}_{\mu\nu} =H_{\mu\alpha}H_\nu{}^{\alpha}-\tfrac14 g_{\mu\nu}H_{\alpha\beta}H^{\alpha\beta} +m_S^2\!\left(S_\mu S_\nu-\tfrac12 g_{\mu\nu}S_\alpha S^\alpha\right).
$$

This block is added to the total stress–energy appearing in Einstein’s equation.

* * *

##### 4.4.2.4.5 Hamiltonian structure: constraints, degrees of freedom, positivity
----------------------------------------------------------------------

**Plain picture.**  
A massive spin-1 must carry exactly **three** propagating modes and a Hamiltonian that’s positive on those modes.

**Canonical variables (local inertial chart).**

$$
\Pi^i\equiv \frac{\partial\mathcal L_S}{\partial(\partial_0 S_i)}=H^{0i},\qquad \Pi^0\equiv 0\quad(\text{primary constraint}).
$$

Hamiltonian density:

$$
\mathcal H_S=\tfrac12\,\Pi^i\Pi^i+\tfrac14 H_{ij}H_{ij} +\tfrac12 m_S^2(S_0^2 + S_i S_i) + g_S S_0 J_5^0 - g_S S_i J_5^i.
$$

Time-preserving  $\Pi^0=0$  gives the **secondary** constraint

$$
\partial_i\Pi^i+m_S^2 S_0 - g_S J_5^0=0,
$$

fixing  $S_0$  algebraically. Count: 4 fields − 2 second-class constraints = **3** DOF.  
Eliminating  $S_0$  yields a quadratic form positive in  $\Pi^i,H_{ij},S_i$  for  $m_S^2>0$ : **no ghosts**.

* * *

##### 4.4.2.4.6 Hyperbolicity and causal cones
----------------------------------

**Intuition first.**  
Short-wavelength wavefronts stay inside the light cone.

**Principal symbol.**  
Linearized about a smooth background, with  $k^\mu$  the cotangent,

$$
\mathcal P^\mu{}_\nu(k)=-k^2\delta^\mu{}_\nu+k^\mu k_\nu,
$$

so characteristics satisfy  $k^2=0$ : **front speed = 1**. The mass shifts poles but not the characteristic cone.

* * *

##### 4.4.2.4.7 Projector / Helmholtz scalarization and Green kernels
---------------------------------------------------------

**Intuition first.**  
Split the field with a **prism** (projector) so each physical “beam” solves a scalar equation.

**Transverse projector and resolvent.**

$$
\Pi^{\mathrm T}{}^\mu{}_\nu=\delta^\mu{}_\nu-\frac{\nabla^\mu\nabla_\nu}{\Box},\qquad S^\mu=g_S\,(\Box+m_S^2)^{-1}\,\Pi^{\mathrm T}{}^\mu{}_\nu\,J_5^\nu,
$$

with the longitudinal part fixed algebraically by  $\nabla\!\cdot\!J_5$ .  
**Retarded kernel and static limit.**

$$
G^R(\omega,\mathbf k)=\frac{1}{-(\omega+i0^+)^2+\mathbf k^2+m_S^2},\qquad G^{\rm static}(\mathbf r)=\frac{e^{-m_S r}}{4\pi r}.
$$

Hence polarized fermionic sources generate short-range, causal  $S_\mu$  profiles.

* * *

##### 4.4.2.4.8 Boundary conditions specific to  $S_\mu$
---------------------------------------------

**Intuition first.**  
State what is held fixed at the edge; the variation then has no loose ends.

**Boundary variation (schematic).**

$$
\delta S_S\big|_{\partial\mathcal M}=\int_{\partial\mathcal M}\!\sqrt{|h|}\,n_\nu H^{\nu\mu}\,\delta S_\mu .
$$

**Choices:**

*   **Dirichlet-type:** fix appropriate components of  $S_\mu$  on  $\partial\mathcal M$ .
*   **Neumann-type:** fix normal flux  $n_\nu H^{\nu\mu}$  and include the compensator surface term.
*   **Sommerfeld (radiation):** outgoing-wave conditions select the physical solution; reciprocity and Rellich uniqueness apply.

Any solution method honoring the **same** BCs—free-space + homogeneous completion, images, or boundary integrals—produces the same bulk  $S_\mu$ . Differences live as **ledger** flux.

* * *

##### 4.4.2.4.9 Energy contribution of the axial sector
-------------------------------------------

**Jar coins (local inertial frame).**

$$
T^{(S)}_{00} =\tfrac12(\mathbf E_S^2+\mathbf B_S^2) +\tfrac12 m_S^2 (S_0^2+\mathbf S^2)\ \ge 0.
$$

This is the sector’s explicit, non-negative contribution to the **bulk** energy integral used in the Miller theorem.

* * *

##### 4.4.2.4.10 Decoupling and the effective contact interaction
-----------------------------------------------------

**Intuition first.**  
When the twist is heavy or weakly coupled, it leaves behind a simple local footprint.

**Tree-level elimination.**

$$
S^\mu \approx \frac{g_S}{m_S^2}\,J_5^\mu \quad\Longrightarrow\quad \Delta\mathcal L_{\rm eff}= -\frac{g_S^2}{2m_S^2}\,J_5^\mu J_{5\mu} + O(\partial^2/m_S^4).
$$

This contact controls short-range spin–spin effects and is one falsifiability lane developed later.

* * *

##### 4.4.2.4.11 Optional audit lane: Stückelberg and  $R_\xi$  gauges
----------------------------------------------------------

**Purpose.**  
Expose the longitudinal mode explicitly (useful for certain calculations) without changing physical content.

**Construction.**

$$
S_\mu=\hat S_\mu+\frac{1}{m_S}\partial_\mu\pi,\quad \mathcal L_S=-\tfrac14 \hat H^2 + \tfrac12 m_S^2 \hat S^2 -\tfrac12(\partial\pi)^2 - g_S\hat S_\mu J_5^\mu - \frac{g_S}{m_S}\pi\,\nabla_\mu J_5^\mu,
$$

with gauge-fixing  $\mathcal L_{\rm gf}=-\tfrac{1}{2\xi}(\nabla\!\cdot\!\hat S+\xi m_S\pi)^2$ . Physical poles/residues are  $\xi$ \-independent (Nielsen identity), matching the projector-resolvent lane.

* * *

##### 4.4.2.4.12 What this section has delivered
------------------------------------

*   The **unified** UGFT action with the axial torsion sector  $S_\mu$  and its **unique** axial coupling  $g_S S\!\cdot\!J_5$ .
*   The **ledger** architecture that pairs boundary terms with the variation and records topology as integers while leaving bulk equations untouched.
*   The **MGSP1** policy and its full health consequences: correct DOF, positive Hamiltonian, and causal principal symbol.
*   The axial sector’s **equations of motion**, **projector/Helmholtz** resolvent and kernels, **boundary conditions**, and **energy** contribution.
*   The **decoupling** limit and an audit-ready **Stückelberg** lane.

With these pieces in hand, the next steps flow directly: sector-by-sector energy audits, representative axial-source solves, and the proof of the **Miller Equivalence Theorem** equating bulk energy (jar) with the gravitational boundary contribution (rim).

### 4.4.3 Connectivity Map
**Within Chapter 4 (closely related):**
- §4.5 — Miller Field Equation Set (MFES) — full classical system
- §4.6 — Stress–energy and positivity (sign-locked, per sector)
- §4.7 — The Miller Equivalence Theorem (MET) — statement & proof sketch
- §4.8 — Equivalence-first computation (MEFP) and MPSD lanes
- §4.9 — Causality, hyperbolicity, response & dispersion (MDPC)
- §4.10 — Boundary, uniqueness, topology & ledgers (MBLC + MLCP)
- §4.12 — Sanity limits & effective descriptions

**External chapters (C#):**
- C2 §0–6
- C3 §3.13–3.20
- C0 §0.12
- C1 §0–7

---

## 4.5 Table of Contents and Introduction

### 4.5.1 Table of Contents (Section 4.5)
- 4.5.2 Miller Field Equation Set (MFES) — full classical system
- 4.5.3 Connectivity Map

### 4.5.2 Miller Field Equation Set (MFES) — full classical system
_See also:_ §4.4, §4.6, §4.7, §4.8, §4.9, §4.10; C2 §3 & §12, C1 §0–4

5\. Miller Field Equation Set (MFES) — full classical system
=============================================================================

> **What this section presents.** A single, closed set of field equations for the UGFT dynamics, together with the constraint algebra, Cauchy data, hyperbolicity and energy structures, projector/Helmholtz solution machinery, boundary prescriptions, and effective/decoupling limits. Each topic begins in everyday language and then walks—step by step—into the exact calculus a working theorist uses.

The satisfaction of a physical theory lies in the coherence of its equations. Each must express a single aspect of one law, yet all must fit together so that none can be changed without disturbing the rest. The Miller Field Equation Set achieves such coherence: it joins the curvature that measures how space and time are bent, the gauge fields that record the flow of charge and spin, the familiar matter currents, and the short-range torsional twist that responds to the handedness of matter. Though written in many symbols, these equations share one geometry and one conservation: the divergence of the total stress vanishes, and with it the balance between field and source is maintained point by point. Every equation tells a fragment of one story—how energy, momentum, and spin are distributed and how they shape the stage on which events unfold. The harmony among them is not imposed from outside; it is born from the structure of the spacetime itself, whose symmetry demands that cause and effect remain inseparable from the geometry that conveys them.

* * *

##### 4.5.2.5.1 Orientation: one fabric, four motions, three ledgers of accountability
--------------------------------------------------------------------------

**Plain picture.** Imagine one fabric (spacetime) through which four motions pass:  
(1) the **bend** of the fabric (gravity),  
(2) **flows** racing along it (Yang–Mills fields),  
(3) **excitations** riding those flows (scalars and spinors), and  
(4) a short-range **twist** of the weave (axial torsion  $S_\mu$ ).

Each motion “talks” to the others through exactly one door: stress–energy feeds the bend, gauge currents feed the flows, the **axial** current feeds the twist. The **ledger** sits at the boundary recording flux and topological integers so bulk equations don’t change when we rearrange by parts or swap equivalent methods.

**Equation-level map.** MFES = Einstein with **total** stress–energy + Proca-type dynamics for  $S_\mu$  sourced by  $J_5^\mu$  + Yang–Mills with covariant current + scalar/Dirac equations (with the axial coupling included). The locks from the project (signature, traces, Fourier/retarded, ADM measures) are assumed and need not be restated.

* * *

##### 4.5.2.5.2 The full set in compact form (then we unpack each structure)
----------------------------------------------------------------

$$
\begin{aligned} \textbf{Gravity:}\quad & G_{\mu\nu} = 8\pi G\,T^{\rm total}_{\mu\nu}, \qquad T^{\rm total}_{\mu\nu}= T^{\rm YM}_{\mu\nu}+T^{(S)}_{\mu\nu}+T^{(\phi)}_{\mu\nu}+T^{(\psi)}_{\mu\nu}+\cdots \\[4pt] \textbf{Axial torsion:}\quad & \nabla_\nu H^{\nu\mu}+m_S^2 S^\mu = g_S J_5^\mu,\qquad H_{\mu\nu}\equiv \nabla_\mu S_\nu-\nabla_\nu S_\mu,\\[-2pt] &\nabla_\mu S^\mu = \dfrac{g_S}{m_S^2}\,\nabla_\mu J_5^\mu \quad \text{(algebraic longitudinal constraint)} \\[6pt] \textbf{Yang–Mills:}\quad & D_\nu F^{\nu\mu} = J^\mu_{\rm gauge},\qquad F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+g[A_\mu,A_\nu] \\[6pt] \textbf{Scalars:}\quad & \Box \phi - V'(\phi) = 0 \\[6pt] \textbf{Dirac (with axial coupling):}\quad & \big(i\gamma^\mu D_\mu - m_\psi - g_S \gamma^\mu\gamma^5 S_\mu\big)\psi = 0, \qquad J_5^\mu=\bar\psi\gamma^\mu\gamma^5\psi . \end{aligned}
$$

Everything below clarifies how these equations interlock, what initial data they need, and how to solve them efficiently without losing physics.

* * *

##### 4.5.2.5.3 How sectors exchange information (conservation and identities)
------------------------------------------------------------------

**Plain stepping stones.** If you push on one part of the fabric, everything else must push back just enough to keep the sum of pushes consistent. That’s what the identities do.

**Exact statements.**

*   **Bianchi identity → covariant energy balance.**  $\nabla^\mu G_{\mu\nu}=0$  implies  $\nabla^\mu T^{\rm total}_{\mu\nu}=0$ . Sectors exchange energy–momentum internally; the covariant sum vanishes on solutions.
*   **Gauge continuity.** Gauge invariance yields  $D_\mu J^\mu_{\rm gauge}=0$ . The non-propagating gauge constraints in the initial data (Gauss law) are the instant snapshot of this.
*   **Axial divergence.** Classically for massless fermions,  $\nabla_\mu J_5^\mu=0$ . When masses or (beyond-classical) anomalies are present,  $\nabla_\mu J_5^\mu\neq0$ —and precisely that non-conservation fixes the **longitudinal** component of  $S_\mu$  algebraically through  $\nabla\!\cdot\!S=(g_S/m_S^2)\nabla\!\cdot\!J_5$ . The **transverse**  $S_\mu$  propagates causally regardless.

**Stress–energy additivity.** The gravitational source is a **sum** of sector stresses. Any “improvement” by a divergence reshuffles surface flux only—bookkeeping in the ledger—leaving bulk equations and positivity intact.

* * *

##### 4.5.2.5.4 Cauchy problem: what you specify on a slice and what is constrained
-----------------------------------------------------------------------

**Plain picture.** To “press play,” you tell the system what it looks like **now** on a spacelike slice  $\Sigma_t$ . Some components are free initial data; others are tied down by constraints.

**Data and constraints.**

*   **Gravity (ADM).** Spatial metric  $h_{ij}$  and extrinsic curvature  $K_{ij}$ , subject to the Hamiltonian and momentum constraints.
*   **Yang–Mills.** Spatial potentials  $A_i$  and conjugate electric densities  $E^i=\sqrt{h}\,F^{0i}$ , obeying Gauss’s law  $D_i E^i=\sqrt{h}\,J^0_{\rm gauge}$ .
*   **Scalars.**  $\phi$  and  $\dot\phi$ .
*   **Dirac.**  $\psi$  on the slice (first order in time).
*   **Axial torsion.**  $S_i$  and  $\Pi^i\equiv H^{0i}$  as genuine data;  $S_0$  is non-dynamical, fixed by the **secondary** Proca constraint
    $`
    \partial_i\Pi^i + m_S^2 S_0 - g_S J_5^0=0,
    `$
    which follows from preserving the **primary** constraint  $\Pi^0=0$ .

**Well-posedness.** With boundary conditions declared (Dirichlet/Neumann/Robin/Sommerfeld per sector), the propagating blocks form a symmetric-hyperbolic system. If constraints hold initially, the equations keep them satisfied.

* * *

##### 4.5.2.5.5 Hyperbolicity and front speeds (principal symbols at a glance)
------------------------------------------------------------------

**Plain picture.** Treat every wave at very short wavelength: does it respect the light cone? If yes, the theory’s causal skeleton is healthy.

**Symbols and cones.**

*   **Axial torsion.** Principal symbol  $`\mathcal P^\mu{}_\nu(k)=-k^2\delta^\mu{}_\nu+k^\mu k_\nu`$  ⇒ characteristics  $`k^2=0`$  ⇒ **front speed = 1**.
*   **Yang–Mills (linear regime).** The Maxwell-like principal block is luminal; interactions are lower order.
*   **Scalar/Dirac.** Standard cones; mass shifts poles but not characteristics.
*   **Gravity (linearized).** Two spin-2 polarizations with luminal fronts in vacuum.

Thus the physical cones nest inside the metric light cone as required.

* * *

##### 4.5.2.5.6 Canonical energy for the axial sector (positivity without hand-waving)
--------------------------------------------------------------------------

**Plain picture.** A trustworthy theory never lets you build a perpetual motion machine from fields. That means the quadratic Hamiltonian is positive when written on the true physical variables.

**Calculation.** In a local inertial chart, with  $\Pi^i=H^{0i}$  and  $\Pi^0=0$ ,

$$
\mathcal H_S=\tfrac12\,\Pi^i\Pi^i+\tfrac14 H_{ij}H_{ij} +\tfrac12 m_S^2(S_0^2 + S_i S_i) + g_S S_0 J_5^0 - g_S S_i J_5^i .
$$

Use the secondary constraint to eliminate  $S_0$  and complete the square. The remaining quadratic form in  $\Pi^i,H_{ij},S_i$  is strictly positive for  $m_S^2>0$ . No negative-norm states are introduced, and no gauge fixing is needed to see it.

* * *

##### 4.5.2.5.7 Projectors and scalar resolvents (the “prism → beams” method made explicit)
-------------------------------------------------------------------------------

**Plain picture.** Split a complicated field into independent “colors,” solve one scalar kernel per color, recombine. This is faster **and** clearer than wrestling a big tensor inverse.

**Spin-1 (Helmholtz–Proca).**  
Let  $`\Pi^{\mathrm T}{}^\mu{}_\nu=\delta^\mu{}_\nu-\nabla^\mu\nabla_\nu/\Box`$ . Then

$`
S^\mu = g_S\,(\Box+m_S^2)^{-1}\,\Pi^{\mathrm T}{}^\mu{}_\nu\,J_5^\nu,\qquad \nabla\!\cdot\!S=\frac{g_S}{m_S^2}\nabla\!\cdot\!J_5.
`$

**Kernel.** In Fourier variables,  $G^R(\omega,\mathbf k)=[-(\omega+i0^+)^2+\mathbf k^2+m_S^2]^{-1}$ ; in the static limit  $G(\mathbf r)=e^{-m_S r}/(4\pi r)$ .

**When projectors commute with inverses.** In homogeneous media with compatible BCs: commute and proceed. In inhomogeneous settings: local-Fourier or Hadamard patching, then track any surface remainders in the ledger.

**Rank-2 and 2-forms.** Barnes–Rivers projectors (per spin  $2,1,0$ ) and SD/ASD splits for 2-forms supply analogous scalar-resolvent lanes. Positivity one-liners follow after Wick for quadratic audits.

* * *

##### 4.5.2.5.8 Boundary prescriptions and reciprocity (making variations honest)
---------------------------------------------------------------------

**Plain picture.** Say what’s fixed at the edge **before** solving; then no surprises appear when you vary the action.

**Axial torsion.** The boundary term in the variation is  $\int_{\partial\mathcal M}\!\sqrt{|h|}\,n_\nu H^{\nu\mu}\,\delta S_\mu$ . Choose:  
• **Dirichlet-type** (fix  $S_\mu$  components), or  
• **Neumann-type** (fix  $n_\nu H^{\nu\mu}$  and add the compensator surface term), or  
• **Sommerfeld** (outgoing waves).

**Equivalence of methods under the same BCs.** Free-space + homogeneous completion, images, or boundary-integral formulations are **physically equivalent** if they honor the same BCs; any difference is a redistribution of **boundary** flux—the ledger’s job—not a change to the bulk equations.

* * *

##### 4.5.2.5.9 Energy density and flux (bulk side of the ledger)
-----------------------------------------------------

**Plain picture.** Each sector drops non-negative “coins” into the jar. The time-rate of change of those coins equals the flux flowing through the boundary; the gravitational boundary coin (ADM) is added separately in the theorem.

**Local inertial forms.**

$$
\begin{aligned} T^{\rm YM}_{00}&=\tfrac12\mathrm{Tr}(\mathbf E^2+\mathbf B^2)\ge 0,\\ T^{(S)}_{00}&=\tfrac12(\mathbf E_S^2+\mathbf B_S^2)+\tfrac12 m_S^2(S_0^2+\mathbf S^2)\ge 0,\\ T^{(\phi)}_{00}&=\tfrac12\dot\phi^2+\tfrac12(\nabla\phi)^2+V(\phi)\ (\ge 0\text{ if }V\ge 0),\\ T^{(\psi)}_{00}&\text{ (Belinfante; listed in the appendix)}. \end{aligned}
$$

**Flux.** The axial “Poynting-like” vector  $\mathbf P_S \equiv \mathbf E_S\times\mathbf B_S$  and the mass term’s transport appear in the standard Noether current; the integrated balance on  $\Sigma_t$  is

$$
\frac{d}{dt}E_{\rm bulk}(t)= -\oint_{\partial\Sigma_t}\!\!\! d\Sigma\, \text{(total energy flux)}.
$$

The gravitational boundary energy is **not** in this flux—it is the ADM surface term added in the theorem.

* * *

##### 4.5.2.5.10 Worked archetypes (static, retarded, and boundary-driven)
--------------------------------------------------------------

**Static, spherically symmetric axial source.** For  $J_5^0(\mathbf r)$  compactly supported,

$$
S_0(\mathbf r)= g_S\!\int\! d^3r'\,\frac{e^{-m_S |\mathbf r-\mathbf r'|}}{4\pi |\mathbf r-\mathbf r'|}\,J_5^0(\mathbf r'),\qquad \mathbf S(\mathbf r)=\mathbf 0\ \text{(by symmetry)}.
$$

This yields  $E_S=\int T^{(S)}_{00}\,d^3x$  as a manifestly positive contribution to the jar.

**Retarded axial pulse.** For a compactly supported  $J_5^\mu(t,\mathbf r)$ ,

$$
S^\mu(t,\mathbf r)= g_S \int d^4x'\,G^R(t\!-\!t',\mathbf r\!-\!\mathbf r')\, \Pi^{\mathrm T\,\mu}{}_{\nu}\, J_5^\nu(t',\mathbf r') ,
$$

with Sommerfeld BCs selecting the unique outgoing solution.

**Boundary-driven cavity.** In a finite domain with Neumann data for  $n_\nu H^{\nu\mu}$ , either an image construction or a boundary-integral representation gives the same bulk  $S_\mu$ ; any difference in intermediate steps appears as redistributed boundary flux captured by the ledger.

* * *

##### 4.5.2.5.11 Gauge-slice independence (audit lane)
------------------------------------------

**Plain picture.** Changing a gauge knob should never move a physical pole or residue.

**Sketch.** Introduce Stückelberg  $S_\mu=\hat S_\mu+\partial_\mu\pi/m_S$  and  $R_\xi$  gauge  $\mathcal L_{\rm gf}=-\tfrac{1}{2\xi}(\nabla\!\cdot\!\hat S+\xi m_S\pi)^2$ . The combined propagator block factorizes; the **Nielsen identity** shows  $\partial_\xi$  acting on any gauge-invariant observable vanishes, hence poles/residues are  $\xi$ \-independent. This matches the projector/Helmholtz solution lane exactly.

* * *

##### 4.5.2.5.12 Dispersion and DC order (positivity corridor)
--------------------------------------------------

**Plain picture.** To measure “DC” behavior you first quiet the spatial ripples, **then** turn down the temporal frequency. That order is not negotiable if you want honest slopes and causal Kramers–Kronig relations.

**Rules.**

*   **Retarded convention:**  $G^R(\omega,\mathbf k)=G(\omega+i0^+,\mathbf k)$ .
*   **DC order:**  $\mathbf k\to 0$  **then**  $\omega\to 0^+$ .
*   **Herglotz positivity:**  $\Im G^R(\omega,\mathbf 0)/\omega \ge 0$  near  $\omega\to0^+$  for passive media; use subtractions where needed.
*   **Moments/sum-rules:** finite integrals of  $\omega^{-n}\Im G^R$  check consistency; massless limits are handled by a small regulator  $m\to0^+$  removed **after** the DC order is enforced.

* * *

##### 4.5.2.5.13 Decoupling and matching (heavy- $S$  corner)
-------------------------------------------------

When  $m_S^2\gg\partial^2$ , solve algebraically to leading order:

$$
S^\mu \approx \frac{g_S}{m_S^2}J_5^\mu\quad\Rightarrow\quad \Delta\mathcal L_{\rm eff} = -\frac{g_S^2}{2m_S^2}\,J_5^\mu J_{5\mu} + O(\partial^2/m_S^4).
$$

This gives a local axial current–current contact. It is the correct low-energy limit for matching to experiments sensitive to short-range spin–spin forces.

* * *

##### 4.5.2.5.14 What the MFES puts in your hands
-------------------------------------

A closed PDE system with:

*   **Named sources** and **explicit couplings** for every interaction channel.
*   **Constraint-aware Cauchy data** and **boundary prescriptions** that keep variations honest and solutions unique under the chosen BCs.
*   **Projector/Helmholtz lanes** that reduce inversions to one scalar resolvent per physical channel.
*   **Causal cones and positive energies** visible without gauge gymnastics.
*   A **bulk energy** ready to be combined with the ADM surface contribution in the energy identity.

The next development is purely mechanical from here: integrate the bulk  $T_{00}$  across all sectors, add the gravitational boundary coin (ADM), and obtain the Miller Equivalence identity that fixes total energy for any isolated solution under the stated boundary data.

### 4.5.3 Connectivity Map
**Within Chapter 4 (closely related):**
- §4.4 — UGFT action (bulk, boundary, topology) and the MGSP1 policy
- §4.6 — Stress–energy and positivity (sign-locked, per sector)
- §4.7 — The Miller Equivalence Theorem (MET) — statement & proof sketch
- §4.8 — Equivalence-first computation (MEFP) and MPSD lanes
- §4.9 — Causality, hyperbolicity, response & dispersion (MDPC)
- §4.10 — Boundary, uniqueness, topology & ledgers (MBLC + MLCP)

**External chapters (C#):**
- C2 §3 & §12
- C1 §0–4

---

## 4.6 Table of Contents and Introduction

### 4.6.1 Table of Contents (Section 4.6)
- 4.6.2 Stress–energy and positivity (sign-locked, per sector)
- 4.6.3 Connectivity Map

### 4.6.2 Stress–energy and positivity (sign-locked, per sector)
_See also:_ §4.4, §4.5, §4.7, §4.9, §4.11; C0 §0.15–0.16, C5 §5.9

6\. Stress–energy and positivity (sign-locked, per sector)
===================================================================================

> **What this section presents.** A complete, sector-by-sector construction of the stress–energy tensor under our fixed conventions, followed by pointwise and integrated **positivity** audits, precise energy–flux formulas, energy-condition checks (NEC/WEC/DEC), and the rigorous treatment of “improvement” terms as **ledger** reassignments of boundary flux. Each part starts with a picture, ascends through physical meaning, and lands in the calculus you’d actually use at a blackboard.
> Throughout, the metric signature is  $(-,+,+,+)$ ; local inertial frame (LIF) means  $g_{\mu\nu}\to \eta_{\mu\nu}$  at a point; traces and couplings are explicit; surface/flux terms are posted to the ledger.

In every part of nature one must be able to say which way the energy flows and that it never flows the wrong way. The stress–energy tensor is the instrument for this accounting. It ties the geometry of the world to the content within it. Each of it's component tells us how matter presses on space and how space responds in turn. When constructed with the correct signs, every physical sector contributes a positive share. Fields store energy, they do not create it from emptiness. It just "is" and will always be. This is not a bookkeeping rule but it is instead the expression of stability itself. If a single term could carry negative energy, the entire edifice of equilibrium would collapse. Thus each sector—gravitational, electromagnetic, scalar, or the axial twist introduced here must reveal in its local inertial frame a non-negative density and a flux consistent with the speed of light. Only then can we trust that the total balance, summed through the jar and recorded at the rim, mirrors a universe whose energies compensate but never contradict.

* * *

##### 4.6.2.6.1 Orientation: the measuring stick and the notion of “positive”
-----------------------------------------------------------------

**Picture.** Energy density is the weight you feel when you place a field configuration on the scale. To read that scale without bias, we first zero it: signature, orientation, and normalization are fixed once and for all. With the scale zeroed, “positive” means two things: (i) **pointwise** non-negativity of  $T_{00}$  in a local inertial frame for the bosonic sectors; and (ii) **integrated** lower bounds for full configurations on a Cauchy slice, with any method-dependent flux differences recorded in the ledger.

**Hilbert definition and audit lens.** For a bulk action  $S[\Phi;g]$ ,

$$
T_{\mu\nu}\equiv -\frac{2}{\sqrt{|g|}}\frac{\delta S}{\delta g^{\mu\nu}}\!,
$$

symmetric and covariantly conserved on shell (once all sectors are summed). We test positivity in a LIF, where  $T_{00}$  splits cleanly into “electric-like,” “magnetic-like,” and “mass/reservoir” pieces. For spinors we use the Belinfante-symmetrized tensor (tetrad variation, then symmetrization), and for mixed sectors we treat superpotentials as boundary reallocations.

* * *

##### 4.6.2.6.2 Yang–Mills (flows): from lines of force to a convex quadratic
-----------------------------------------------------------------

**Intuition.** A gauge field is a bundle of taut lines. Stretch them (electric), twist them (magnetic), and the energy rises like a square of the deformation. Energy flows sideways as a **Poynting** vector: tension times velocity.

**Construction.** With  $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+g[A_\mu,A_\nu]$  and  $\mathrm{Tr}(T^AT^B)=\delta^{AB}$ ,

$$
T^{\rm YM}_{\mu\nu} =\mathrm{Tr}\!\left(F_{\mu\alpha}F_{\nu}{}^{\alpha}-\tfrac14 g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\right).
$$

In a LIF,  $E_i\equiv F_{0i}$ ,  $B_i\equiv \frac12\epsilon_{ijk}F^{jk}$ , hence

$$
T^{\rm YM}_{00}=\tfrac12\,\mathrm{Tr}(\mathbf E^2+\mathbf B^2)\ge 0,\qquad (T^{\rm YM})^i{}_0=\mathrm{Tr}(\mathbf E\times\mathbf B)^i .
$$

Positivity is manifest and gauge-independent; the flux is the familiar Poynting vector.

**Energy conditions.** For any null  $k^\mu=(1,\hat{\mathbf k})$ ,

$$
T^{\rm YM}_{\mu\nu}k^\mu k^\nu=\tfrac12\,\mathrm{Tr}(\mathbf E+\hat{\mathbf k}\times\mathbf B)^2\ge0\quad(\text{NEC}).
$$

The DEC holds classically: energy flux never exceeds energy density in magnitude.

**Poynting theorem (integrated).** On a slice  $\Sigma_t$ ,

$$
\frac{d}{dt}\!\int_{\Sigma_t}\!\!T^{\rm YM}_{00} = -\oint_{\partial\Sigma_t}\!(\mathbf E\times\mathbf B)\cdot d\mathbf a +\int_{\Sigma_t}\!\!\mathrm{Tr}(\mathbf E\cdot\mathbf J_{\rm gauge}) ,
$$

showing precisely how work done on charges and boundary radiation change the jar of YM energy.

**Improvements.** Adding  $\nabla_\alpha X^{\alpha}{}_{\mu\nu}$  with  $X$  antisymmetric shifts only the surface flux; bulk positivity and the equations are untouched. We post this change to the ledger.

* * *

##### 4.6.2.6.3 Axial torsion  $S_\mu$  (twist): Proca positivity without hand-waving
-------------------------------------------------------------------------

**Intuition.** The twist is a **short-range** vector ripple. Like a string with inertia, it stores energy in field curvature ( $H$ ) and in displacement ( $m_S^2 S^2$ ). Its handshake is with handedness:  $S_\mu J_5^\mu$ .

**Hilbert tensor and LIF split.** With  $H_{\mu\nu}\equiv\nabla_\mu S_\nu-\nabla_\nu S_\mu$ ,

$$
T^{(S)}_{\mu\nu} =H_{\mu\alpha}H_{\nu}{}^{\alpha}-\tfrac14 g_{\mu\nu}H^2 +m_S^2\!\left(S_\mu S_\nu-\tfrac12 g_{\mu\nu}S^2\right).
$$

In a LIF,  $E_{S,i}\equiv H_{0i}$ ,  $B_{S,i}\equiv \tfrac12\epsilon_{ijk}H^{jk}$ ,

$$
T^{(S)}_{00}=\tfrac12(\mathbf E_S^2+\mathbf B_S^2)+\tfrac12 m_S^2(S_0^2+\mathbf S^2)\ge0,\qquad (T^{(S)})^i{}_0=(\mathbf E_S\times\mathbf B_S)^i .
$$

**Canonical derivation of positivity (Proca lemma).**  
Define  $\Pi^i=H^{0i}$  and note  $\Pi^0=0$  (primary constraint). The Hamiltonian density in a LIF is

$$
\mathcal H_S=\tfrac12\Pi^2+\tfrac14 H_{ij}^2+\tfrac12 m_S^2(S_0^2+\mathbf S^2) + g_S S_0 J_5^0 - g_S \mathbf S\!\cdot\!\mathbf J_5 .
$$

Time preservation of  $\Pi^0=0$  yields the **secondary** constraint

$$
\partial_i\Pi^i+m_S^2 S_0 - g_S J_5^0=0,
$$

fixing  $S_0$  algebraically. Eliminating  $S_0$  and completing the square leaves a strictly positive quadratic form in  $(\Pi^i,H_{ij},S_i)$  for  $m_S^2>0$ . No gauge choice is needed; no negative-norm modes exist.

**Static functional and the Yukawa kernel.** For static sources with  $J_5^i=0$ ,

$$
E_S=\int d^3x\Big[\tfrac12(\nabla S_0)^2+\tfrac12 m_S^2 S_0^2\Big] -\!g_S\!\int d^3x\ S_0 J_5^0 =\frac{g_S^2}{2}\!\int\! d^3x\,d^3x'\ J_5^0(\mathbf x)\,\frac{e^{-m_S|\mathbf x-\mathbf x'|}}{4\pi |\mathbf x-\mathbf x'|}\,J_5^0(\mathbf x')\ge0.
$$

The kernel is positive-definite; the minimum is attained at the physical  $S_0$ . Range  $m_S^{-1}$  is explicit.

**NEC/DEC.** The Proca quadratic satisfies the NEC; DEC holds classically for the axial sector (flux norm  $\le$  density).

* * *

##### 4.6.2.6.4 Scalar sector: gradients, potential, and the role of “improvement”
----------------------------------------------------------------------

**Intuition.** A scalar is a **height field** on space: change it in time (kinetic), tilt it in space (gradient), or place it on a hill/valley (potential) and you pay energy accordingly.

**Tensor and audit.**

$$
T^{(\phi)}_{\mu\nu} =\partial_\mu\phi\,\partial_\nu\phi-\tfrac12 g_{\mu\nu}(\partial\phi)^2-g_{\mu\nu}V(\phi), \qquad T^{(\phi)}_{00}=\tfrac12\dot\phi^2+\tfrac12(\nabla\phi)^2+V(\phi).
$$

If  $V(\phi)\ge 0$ , pointwise positivity is immediate. If  $V$  dips below zero, a constant shift of the vacuum energy (a ledger matter in gravity) restores a convenient baseline without altering bulk dynamics.

**Conformal improvement.** The improved tensor

$$
\Theta_{\mu\nu}=T^{(\phi)}_{\mu\nu} +\xi\!\left(g_{\mu\nu}\Box-\nabla_\mu\nabla_\nu+G_{\mu\nu}\right)\phi^2,\quad \xi=\tfrac{1}{6}\ \text{(4D)},
$$

differs from  $T$  by a divergence on shell. Bulk positivity and equations are unchanged; only boundary flux moves—recorded in the ledger.

* * *

##### 4.6.2.6.5 Dirac sector (with axial coupling): symmetry, bounds, and bookkeeping
-------------------------------------------------------------------------

**Intuition.** A spinor’s energy density is the expectation of a first-order Hamiltonian. Locally it need not be manifestly non-negative the way a square is, but in the **combined** spinor+axial system the lower bound becomes transparent once the axial longitudinal constraint is used.

**Belinfante tensor (symmetric).** With tetrads  $`e^a{}_\mu`$  and spin connection  $`\omega_{\mu ab}`$ ,

$$
T^{(\psi)}_{\mu\nu} =\frac{i}{4}\,\bar\psi\!\left(\gamma_\mu\!\!\stackrel{\leftrightarrow}{D}_{\!\nu} +\gamma_\nu\!\!\stackrel{\leftrightarrow}{D}_{\!\mu}\right)\!\psi - g_{\mu\nu}\,\mathcal L_\psi^{\rm on\,shell},\quad \mathcal L_\psi=\bar\psi(i\gamma^\alpha D_\alpha-m_\psi)\psi .
$$

The axial contact  $-g_S S_\mu J_5^\mu$  may be counted in the spinor or axial block, **but not both**. The **sum** is invariant; we choose the split that keeps quadratic positivity most transparent in a given calculation.

**LIF form and lower bounds.** In a LIF and temporal gauge for background fields,

$$
T^{(\psi)}_{00} =\frac{i}{2}\psi^\dagger\!\stackrel{\leftrightarrow}{\partial_t}\!\psi-\mathcal L_\psi^{\rm on\,shell} \sim \psi^\dagger(\boldsymbol{\alpha}\!\cdot\!\mathbf p+\beta m_\psi)\psi\ (+\ \text{gauge pieces}).
$$

While not a square, the **total** matter+axial energy is bounded below: the axial piece linear in  $J_5$  is controlled by the positive quadratic in  $S$  (previous subsection). Eliminating  $S_0$  via the secondary constraint produces an effective  $-\frac{g_S^2}{2m_S^2}J_5^0J_{5,0}$  contribution to the Hamiltonian density **together** with the Yukawa-positive field energy; the net bound follows from Cauchy–Schwarz and the kernel’s positivity.

* * *

##### 4.6.2.6.6 Interaction bookkeeping: invariance of the **sum**
------------------------------------------------------

**Intuition.** The contact  $-g_S S_\mu J_5^\mu$  is the handshake across sectors. Energy accounting must count the handshake exactly once.

**Two equivalent ledgers.**

*   **Matter-count:** keep  $T^{(S)}$  purely quadratic; count the contact inside  $T^{(\psi)}$  (through  $-g_{\mu\nu}\mathcal L_\psi$ ).
*   **Field-count:** absorb the contact into  $T^{(S)}$  by a field redefinition and add/subtract a superpotential so the metric variation stays symmetric.

Both produce the same  $T^{\rm total}_{\mu\nu}$ . Any difference appears only as a boundary flux term that the ledger records.

* * *

##### 4.6.2.6.7 Energy conditions: quick, explicit checks
---------------------------------------------

**NEC (null energy).** For any null  $k^\mu$ ,

$$
\begin{aligned} T^{\rm YM}_{\mu\nu}k^\mu k^\nu&=\tfrac12\,\mathrm{Tr}(\mathbf E+\hat{\mathbf k}\times\mathbf B)^2\ge0,\\ T^{(S)}_{\mu\nu}k^\mu k^\nu&=\tfrac12\,(\mathbf E_S+\hat{\mathbf k}\times\mathbf B_S)^2+\tfrac12 m_S^2(S_\parallel)^2\ge0,\\ T^{(\phi)}_{\mu\nu}k^\mu k^\nu&=(k\!\cdot\!\partial\phi)^2\ge0. \end{aligned}
$$

The Dirac block is subtler pointwise; the **combined** system maintains the balances needed by the gravitational equation.

**DEC (dominant).** For YM and Proca/axial sectors, the energy-flux four-vector is future-timelike or null. Scalars satisfy DEC if  $V(\phi)\ge0$ . No superluminal energy transport appears in the classical system.

* * *

##### 4.6.2.6.8 Wick-space positivity macros (fast audits you can trust)
------------------------------------------------------------

**Reason.** Quadratic bosonic forms are easiest to audit in Euclidean signature; integers in the ledger are Wick-invariant.

*   **Vectors/Proca.** The Euclidean operator  $(-\partial^2+m^2)$  is positive-definite;  $\int (\tfrac14 H^2+\tfrac12 m^2 S^2)\ge0$  is immediate.
*   **Two-forms (if present).** Decompose  $H$  into self/anti-self dual  $H_\pm$ ; then  $\|H\|^2=\|H_+\|^2+\|H_-\|^2\ge0$ .
*   **Ledger.** Pontryagin, Chern–Simons (integer level with  $\mathcal A=gA$ ), and Nieh–Yan are topological integers; Wick does not change them and they do not alter bulk positivity.

* * *

##### 4.6.2.6.9 Mixing blocks: positivity by linear algebra, cones unchanged **(fixed)**
----------------------------------------------------------------------------

**Intuition.** When quadratic forms mix multiple one-forms, do the linear algebra first, physics second. Put the matrix into a friendly shape; the cones and poles won’t move.

**Functional inner product and corrected quadratic form.**  
Let  $\langle X, Y\rangle \equiv \int_{\Sigma}\!\sqrt{h}\, X\cdot Y$  denote the  $L^2$  pairing on the slice (with the appropriate index contractions suppressed for readability). For two fields  $A$  and  $B$  with a symmetric quadratic form, write

$$
\boxed{\; \mathcal Q[A,B] =\frac12\,\Big\langle \begin{pmatrix} A \\[2pt] B \end{pmatrix}, \begin{pmatrix} K_{AA} & K_{AB} \\ K_{AB}^\dagger & K_{BB} \end{pmatrix} \begin{pmatrix} A \\[2pt] B \end{pmatrix} \Big\rangle . \;}
$$

Here  $K_{BA}=K_{AB}^\dagger$  is the adjoint with respect to  $\langle\cdot,\cdot\rangle$ . This corrects (and replaces) the earlier schematic inline expression.

**Sylvester/Cholesky route.** If the block kernel is positive (e.g., Sylvester’s criterion on leading principal minors holds), there exists a Cholesky factorization

$$
\begin{pmatrix} K_{AA} & K_{AB} \\ K_{AB}^\dagger & K_{BB} \end{pmatrix} = R^\dagger R,
$$

with  $R$  upper-triangular (as an operator matrix). The local, invertible field redefinition

$$
\begin{pmatrix} A \\ B \end{pmatrix} \mapsto R^{-1}\!\begin{pmatrix} A \\ B \end{pmatrix}
$$

canonically normalizes the quadratic form while preserving light cones and pole locations (physical content is unchanged).

* * *

##### 4.6.2.6.10 Integrated energy and flux balance on a Cauchy slice
--------------------------------------------------------

**Bulk jar.**

$$
E_{\rm bulk}(t)\equiv \int_{\Sigma_t}\! N\sqrt{h}\;T^{0}{}_{0,\rm total}.
$$

Using  $\nabla_\mu T^{\mu}{}_{0}=0$  and Stokes,

$$
\frac{d}{dt}E_{\rm bulk}(t) = -\oint_{\partial\Sigma_t}\! \big[\,\text{YM Poynting} + \text{axial Poynting} + \text{scalar/Dirac flux}\,\big]\cdot d\mathbf a .
$$

**Important:** the **gravitational** boundary energy is **not** included here; it appears as the ADM surface term and is added **on top** of  $E_{\rm bulk}$  in the Miller identity. Any re-shuffling of flux by improvements or by alternative boundary-solving methods is recorded as a ledger move—never as a change in bulk equations or in positivity.

* * *

##### 4.6.2.6.11 Worked vignettes (expanding intuition with calculus)
---------------------------------------------------------

### (a) Short-range axial halo around a polarized lump

Take a localized static  $J_5^0$  with total axial “charge”  $Q_5=\int J_5^0$ . The solution is

$$
S_0(\mathbf r)=g_S\!\int\! d^3r'\,\frac{e^{-m_S|\mathbf r-\mathbf r'|}}{4\pi |\mathbf r-\mathbf r'|}\,J_5^0(\mathbf r') ,\qquad \mathbf S=0 \ (\text{spherical symmetry}).
$$

The stored energy

$$
E_S=\frac{g_S^2}{2}\!\int\! d^3x\,d^3x'\ J_5^0(\mathbf x)\,\frac{e^{-m_S|\mathbf x-\mathbf x'|}}{4\pi |\mathbf x-\mathbf x'|}\,J_5^0(\mathbf x')\ge0
$$

grows  $\propto Q_5^2$  at fixed size for  $m_S R\!\ll\!1$ , and localizes into a shell for  $m_S R\!\gg\!1$ .

### (b) Plane-wave energy flow for the axial sector

For  $S_\mu(x)=\Re\{\varepsilon_\mu e^{ik\cdot x}\}$  with  $k^2=m_S^2$ , the time-average satisfies

$$
\langle T^{(S)}_{00}\rangle=\tfrac12\omega^2 |\boldsymbol{\varepsilon}_\perp|^2+\tfrac12 m_S^2 |\varepsilon_0|^2+\tfrac12 m_S^2 |\boldsymbol{\varepsilon}_\perp|^2,\qquad \langle\mathbf S_E\rangle=\langle\mathbf E_S\times \mathbf B_S\rangle=\omega\,\mathbf k\,\tfrac12|\boldsymbol{\varepsilon}_\perp|^2,
$$

showing subluminal group speed  $v_g=|\mathbf k|/\omega<1$  with a luminal **front** (set by the principal symbol).

### (c) Mixed one-forms: diagonalization without moving physics **(fixed)**

For two coupled vectors  $A_\mu$  and  $B_\mu$  with quadratic functional  $\mathcal Q[A,B]$  defined with the  $L^2$  pairing  $\langle\cdot,\cdot\rangle$ ,

$$
\mathcal Q[A,B] =\frac12\,\Big\langle \begin{pmatrix} A \\[2pt] B \end{pmatrix}, \begin{pmatrix} K_{AA} & K_{AB} \\ K_{AB}^\dagger & K_{BB} \end{pmatrix} \begin{pmatrix} A \\[2pt] B \end{pmatrix} \Big\rangle .
$$

If the operator matrix is positive, a Cholesky factorization  $K=R^\dagger R$  exists, and the canonical redefinition  $(A,B)\mapsto R^{-1}(A,B)$  renders the form manifestly positive; **cones and poles are unchanged** because  $R$  is local and invertible.

* * *

##### 4.6.2.6.12 What this section delivers to the energy theorem
-----------------------------------------------------

*   **Explicit, sign-locked stress–energy** for each sector with transparent LIF decompositions.
*   **Pointwise** positivity for bosons, and **integrated** lower bounds for the coupled spinor+axial system.
*   **Energy-condition** checks (NEC/DEC/WEC) suitable for quick diagnostics.
*   **Improvement/ledger** rules that keep the **sum**  $T^{\rm total}_{\mu\nu}$  invariant while cleanly tracking boundary flux.
*   A slice energy  $E_{\rm bulk}$  whose time change is exactly the outward flux and which will, in the Miller identity, be added to the gravitational **ADM** rim coin to give total energy.

With the stress–energy now fully constructed and audited, the next move is automatic: assemble the bulk jar from **all** sectors, add the gravitational boundary coin, and state and prove the energy equality that powers the remainder of the chapter.

### 4.6.3 Connectivity Map
**Within Chapter 4 (closely related):**
- §4.4 — UGFT action (bulk, boundary, topology) and the MGSP1 policy
- §4.5 — Miller Field Equation Set (MFES) — full classical system
- §4.7 — The Miller Equivalence Theorem (MET) — statement & proof sketch
- §4.9 — Causality, hyperbolicity, response & dispersion (MDPC)
- §4.11 — Spectral standardization — the Miller Transform (MT)

**External chapters (C#):**
- C0 §0.15–0.16
- C5 §5.9

---

## 4.7 Table of Contents and Introduction

### 4.7.1 Table of Contents (Section 4.7)
- 4.7.2 The Miller Equivalence Theorem (MET) — statement & proof sketch
- 4.7.3 Connectivity Map

### 4.7.2 The Miller Equivalence Theorem (MET) — statement & proof sketch
_See also:_ §4.5, §4.6, §4.9, §4.10, §4.11; C2 §9, C0 §0.3 & §0.12, C5 §5.1

7\. The Miller Equivalence Theorem (MET) — statement & proof sketch
====================================================================================

> **What this section presents.** A rigorous energy identity for the full UGFT dynamics, written and proved in two complementary lanes:
> 
> *   **Hamiltonian/ADM lane:** constraints + surface terms;
> *   **Covariant/Noether lane:** conserved current = bulk piece + boundary superpotential.
>     
> 
> Each lane is carried from intuition to exact calculus. We specify the minimal hypotheses (falloff, boundary pairing, constraint satisfaction, ledger discipline), show why projector/basis changes, IBP “improvements,” and gauge-slice choices do **not** change the result, and make the role of **boundary flux** explicit. Worked micro-examples illustrate how the identity is used without re-deriving earlier chapters.

The true worth of a theory is shown when distinct lines of reasoning converge on the same quantity. The Miller Equivalence Theorem embodies this principle in precise mathematical form: whether one tallies the energy through the densities that fill space or through the flux that passes a distant boundary, the total is identical. This equality is not a coincidence of algebra; It is a reflection of nature’s own balance saying what leaves one region must enter another, and nothing vanishes unrecorded. The proof isn't mysterious at all. The equations of motion make the divergence of the total stress vanish, and the geometry of spacetime translates that local statement into a global conservation. What we call “jar” and “rim” are just two ways of counting the same substance. Thus, the theorem confirms that the language of fields and the language of boundaries are consistent descriptions of one reality. It is the reality that the bookkeeper’s ledger and the geometer’s integral both tell the same story when the mathematics has been done with care.

* * *

##### 4.7.2.7.1 Intuition first: coins in the jar, one coin on the rim
----------------------------------------------------------

Start with the picture we will make exact. Take any time-slice  $\Sigma_t$ . Inside the slice sits the **jar**: the integral of the local energy density from **all** bulk sectors,

$$
E_{\rm jar}(t)\;\equiv\;\int_{\Sigma_t} N\sqrt{h}\;T^{0}{}_{0,\rm total}.
$$

At the boundary  $\partial\Sigma_t$  sits gravity’s **rim coin**: the ADM surface energy computed with our fixed ADM normalization and boundary pairing. The **Miller Equivalence Theorem** asserts that for isolated data, the **total energy** equals jar + rim, and that this equality is immune to every algebraic reshuffle we legitimately perform (basis/projectors, integrations by parts, EOM-proportional tweaks) because those reshuffles only move entries in the **ledger** (boundary bookkeeping), never the bulk physics.

* * *

##### 4.7.2.7.2 The theorem (sign-locked, unambiguous statement)
----------------------------------------------------

Let  $\Sigma_t$  be a Cauchy slice with induced metric  $h_{ij}$ , lapse  $N$ , and outward unit normal  $u^\mu$  on  $\partial\Sigma_t$ . Assume the falloffs and boundary pairing below. Then:

$$
\boxed{\; E_{\rm total}(t) = \underbrace{\int_{\Sigma_t}\! N\sqrt{h}\; T^{0}{}_{0,\rm total}}_{\displaystyle E_{\rm jar}(t)} \;+\;\underbrace{E_{\rm grav}^{\rm ADM}[\partial\Sigma_t]}_{\displaystyle \text{rim coin}} \;=\; c^2\,M_{\rm ADM}\;. \;}
$$

Notes on the equality:

*    $`T^{0}{}_{0,\rm total}`$  is the **sum** from all bulk sectors fixed earlier (YM, scalars, Dirac, axial torsion  $S_\mu$ , …) in our sign conventions.
*    $E_{\rm grav}^{\rm ADM}$  is the gravitational surface term obtained from the ADM/Regge–Teitelboim evaluation of the canonical generator for time translations with the **GHY** pairing already in the action.
*   Any addition of a total divergence or EOM-proportional “improvement” to a bulk Lagrangian modifies **only** the boundary posting in the ledger (the rim piece), leaving the boxed identity unchanged.

* * *

##### 4.7.2.7.3 Minimal hypotheses (exactly what we use and nothing more)
-------------------------------------------------------------

1.  **Asymptotic behavior.** As  $r\to\infty$ ,  $h_{ij}=\delta_{ij}+O(1/r)$ ,  $\partial h=O(1/r^2)$ ; Yang–Mills  $F=O(1/r^2)$ ; scalars decay at least  $O(1/r)$ ; spinor bilinears integrable; axial torsion  $S_\mu=O\!\left(e^{-m_S r}/r\right)$  (short range).
2.  **Boundary pairing.** The metric variation is well-posed by including **GHY**. For non-gravitational sectors, BCs (Dirichlet/Neumann/Robin/Sommerfeld) are **declared** before variation, with any needed surface compensators placed in the ledger.
3.  **Constraints hold.** Hamiltonian/momentum constraints (and Gauss constraints for YM) are satisfied on  $\Sigma_t$ .
4.  **Ledger discipline.** Topological integers (Pontryagin, CS at integer level, Nieh–Yan/Holst) and IBP differences are **ledger-only**; they never replace bulk kinetics.

_(Positivity is not an assumption of MET; it is a separate fact we already established per sector, making the “jar” aesthetically non-negative.)_

* * *

##### 4.7.2.7.4 Proof lane A — Hamiltonian/ADM: constraints + surface = energy
------------------------------------------------------------------

**Idea.** In a 3+1 split, the canonical generator for time translations consists of bulk **constraints** plus a **surface** term. On solutions, the constraints vanish **as generators**, but their variation ties the gravitational bulk piece to the matter content. The net result is the identity: total energy = jar + rim.

### (A1) Canonical decomposition (with GHY already in place)

With our locks, the gravitational Lagrangian density reads

$$
\mathcal L_{\rm grav}=\frac{1}{16\pi G}\,N\sqrt{h}\,\big({}^{(3)}\!R+K_{ij}K^{ij}-K^2\big)\;+\;\partial_t(\cdots)\;+\;\nabla_i(\cdots),
$$

so the Hamiltonian takes the standard form

$$
H_{\rm grav}[N,N^i]=\int_{\Sigma_t}\!\big(N\,\mathcal H_{\rm grav}+N^i \mathcal H_{i,\rm grav}\big)\;+\;E_{\rm ADM}[N,N^i].
$$

Adding the non-gravitational sectors yields

$$
H_{\rm total}[N,N^i]=\int_{\Sigma_t}\!\big(N\,\mathcal H_{\rm tot}+N^i \mathcal H_{i,\rm tot}\big)\;+\;E_{\rm ADM}.
$$

### (A2) Lapse variation and the constraint identity

Varying the total Hamiltonian with respect to the lapse  $N$  gives the (weak) Hamiltonian constraint,

$$
\mathcal H_{\rm grav}+\mathcal H_{\rm matter} = 0 \quad\Rightarrow\quad \mathcal H_{\rm grav} =-\,\mathcal H_{\rm matter}.
$$

With our sign locks, the matter Hamiltonian density equals the **jar density**:

$$
\mathcal H_{\rm matter}= N\sqrt{h}\;T^{0}{}_{0,\rm total}.
$$

Thus on shell,

$$
\mathcal H_{\rm grav}= -\,N\sqrt{h}\;T^{0}{}_{0,\rm total}.
$$

### (A3) Evaluate the generator for a unit time translation

For  $(N\to 1,\,N^i\to 0)$  at infinity,

$$
\begin{aligned} E_{\rm total} =H_{\rm total}\big|_{\text{on shell}} &= \int_{\Sigma_t}\!(\mathcal H_{\rm grav}+\mathcal H_{\rm matter})\;+\;E_{\rm ADM} \\ &= \int_{\Sigma_t}\!\big(-N\sqrt{h}T^{0}{}_{0,\rm total}+N\sqrt{h}T^{0}{}_{0,\rm total}\big)\;+\;E_{\rm ADM}\\ &= \underbrace{\int_{\Sigma_t}\! N\sqrt{h}\,T^{0}{}_{0,\rm total}}_{E_{\rm jar}(t)} \;+\; E_{\rm ADM}. \end{aligned}
$$

The bulk cancellation is the **mechanism** that isolates the jar and leaves the rim coin explicit.

### (A4) Why IBP/improvements don’t touch the identity

Adding a total divergence to any bulk Lagrangian shifts  $\mathcal H$  by a total spatial divergence plus a total time derivative. Both contribute only to **surface** posts (the ledger); the bulk constraint identity is unchanged. Therefore the combination “jar + rim” is invariant under IBP moves and EOM-proportional improvements.

* * *

##### 4.7.2.7.5 Proof lane B — Covariant/Noether: current = bulk + boundary
---------------------------------------------------------------

**Idea.** Use diffeomorphism invariance. The Noether current for time translations decomposes into a bulk piece proportional to  $T^\mu{}_\nu\xi^\nu$  plus the divergence of a superpotential. Integrating over  $\Sigma_t$  converts the divergence into the ADM surface term.

### (B1) Noether current and superpotential

For  $\xi^\mu$  the unit asymptotic time-translation field, the on-shell current has the structure

$$
J^\mu[\xi]=\sqrt{|g|}\,T^{\mu}{}_{\nu}\,\xi^\nu\;+\;\nabla_\nu Q^{\mu\nu}[\xi].
$$

Here  $Q^{\mu\nu}$  is the (GHY-normalized) gravitational superpotential consistent with our boundary pairing.

### (B2) Integrate over the slice

Using Gauss:

$$
\int_{\Sigma_t}\! J^0[\xi] =\int_{\Sigma_t}\!N\sqrt{h}\;T^{0}{}_{0}\;+\;\oint_{\partial\Sigma_t}\!Q^{0i}[\xi]\,d\Sigma_i.
$$

### (B3) Identify the charge

The left side is the Noether charge for time translations—i.e. the **total energy**. The boundary integral equals  $E_{\rm ADM}$  with our locks. Hence

$$
E_{\rm total} =\int_{\Sigma_t}\! N\sqrt{h}\;T^{0}{}_{0,\rm total} \;+\;E_{\rm ADM}.
$$

As before, adding a total divergence to the Lagrangian shifts  $Q^{\mu\nu}$  by a superpotential difference: a **ledger** move that leaves the combination unchanged.

* * *

##### 4.7.2.7.6 Flux balance, radiative situations, and “who pays at infinity”
------------------------------------------------------------------

The instantaneous **jar** changes by exactly the outward energy flux through  $\partial\Sigma_t$ :

$$
\frac{d}{dt}\,E_{\rm jar}(t) = -\oint_{\partial\Sigma_t}\!\big[\text{YM Poynting} + \text{axial Poynting} + \text{scalar/Dirac flux}\big]\cdot d\mathbf a .
$$

For truly isolated systems, the ADM rim coin is time-independent; in radiative spacetimes one swaps the ADM surface at spatial infinity for the Bondi mass at null infinity. The **ledger** keeps this straight: energy carried out to infinity appears as a change in the boundary posting; the bulk identity on each finite slice remains “jar + rim.”

* * *

##### 4.7.2.7.7 Invariances (what cannot change MET)
----------------------------------------

*   **Basis/projectors.** Helicity, Barnes–Rivers, SD/ASD splits diagonalize kinetics but do not change the stress or the ADM formula.
*   **Gauge slice & Stückelberg.**  $R_\xi$  choices and Stückelberg splits leave physical poles/residues invariant; MET depends on the diffeo/Noether charge, not on gauge bookkeeping.
*   **Integrations by parts / improvements.** These transfer terms between bulk integrals and the boundary superpotential. The **sum** is invariant because the ledger keeps the surface piece explicit.
*   **Topological integers.** Pontryagin/CS/Nieh–Yan/Holst are ledger entries by policy; they never replace bulk kinetics and are Wick-invariant—no effect on MET.

* * *

##### 4.7.2.7.8 Micro-examples (see-through uses of MET)
--------------------------------------------

### (a) Short-range axial halo (static, compact  $J_5^0$ )

With  $J_5^0$  localized and time-independent, the unique solution has  $S_0$  given by a Yukawa fold and  $\mathbf S=0$  by symmetry. The **jar** is

$$
E_{\rm jar}=\int d^3x\ \Big[\tfrac12(\nabla S_0)^2+\tfrac12 m_S^2 S_0^2\Big] =\frac{g_S^2}{2}\!\int\! d^3x\,d^3x'\ J_5^0(\mathbf x)\, \frac{e^{-m_S|\mathbf x-\mathbf x'|}}{4\pi |\mathbf x-\mathbf x'|}\,J_5^0(\mathbf x')\ \ge 0.
$$

No radiation, so the instantaneous ADM posting is constant; **MET** reads  $E_{\rm total}=E_{\rm jar}+E_{\rm ADM}$ .

### (b) Finite wall, quasilocal version

If  $\Sigma_t$  ends on a timelike wall  $\mathcal B$ , replace  $E_{\rm ADM}$  with the **Brown–York** quasilocal energy on  $\mathcal B$  (which belongs in the ledger alongside the GHY term). The identity keeps the same form: jar plus rim (now quasilocal) equals total energy in the chosen region.

### (c) Asymptotically AdS

Include holographic counterterms (ledger entries) to define the rim coin; the jar piece is unchanged. MET holds verbatim with the AdS-renormalized boundary posting.

* * *

##### 4.7.2.7.9 Edge-case cautions (so you can spot pitfalls)
-------------------------------------------------

*   **Under-declared BCs.** If you do not declare BCs before varying, surface terms can masquerade as bulk contributions; MET then appears to “fail” only because the ledger was not set up.
*   **Order-of-limits.** For DC/IR questions, enforce the corridor  $\mathbf k\to 0$  then  $\omega\to0^+$  before reading slopes; this affects **flux** evaluations but not the static MET identity.
*   **Non-isolated systems.** With external work sources (e.g., time-dependent boundary controls), the rim coin changes accordingly; the identity remains instantaneous but the time-evolution gains a **work** term in the ledger.

* * *

##### 4.7.2.7.10 What MET gives you in practice
-----------------------------------

1.  **A one-line audit**: compute  $E_{\rm jar}$  from the fields you solved, add the ledger’s rim coin, and you have  $E_{\rm total}$ .
2.  **A debugging oracle**: two equivalent derivations that disagree must be disagreeing on a **boundary** post; the ledger tells you which IBP or method choice moved it.
3.  **A falsifiability handle**: measured boundary energy changes must equal jar changes + the posted rim change, with the DC/retarded order respected.

_From here we can push into explicit solves and response checks knowing that our accounting is locked: local energy lives in the jar, gravity’s contribution lives on the rim, and—together—they tell the whole truth._

### 4.7.3 Connectivity Map
**Within Chapter 4 (closely related):**
- §4.5 — Miller Field Equation Set (MFES) — full classical system
- §4.6 — Stress–energy and positivity (sign-locked, per sector)
- §4.9 — Causality, hyperbolicity, response & dispersion (MDPC)
- §4.10 — Boundary, uniqueness, topology & ledgers (MBLC + MLCP)
- §4.11 — Spectral standardization — the Miller Transform (MT)

**External chapters (C#):**
- C2 §9
- C0 §0.3 & §0.12
- C5 §5.1

---

## 4.8 Table of Contents and Introduction

### 4.8.1 Table of Contents (Section 4.8)
- 4.8.2 Equivalence-first computation (MEFP) and MPSD lanes
- 4.8.3 Connectivity Map

### 4.8.2 Equivalence-first computation (MEFP) and MPSD lanes
_See also:_ §4.5, §4.9, §4.10, §4.11, §4.13; C5 §5.16–5.21, §5.33

8\. Equivalence-first computation (MEFP) and MPSD lanes
========================================================================

> **What this section presents.** A complete, working methodology for solving the UGFT field equations that is fast, auditable, and mathematically sharp. We convert “big, coupled tensor problems” into a small number of **scalar resolvents** plus **boundary posts** that we keep in a ledger. The story begins with pictures and ends with operator identities, commutation lemmas, symbol calculus, reciprocity/uniqueness at boundaries, dispersion/positivity corridors, and discrete (numerical) realizations. Nothing here restates earlier chapters; we only teach you **how to compute** correctly and efficiently.

Calculation should follow the joints of the phenomenon, not the joints of our notation. The equivalence‑first scheme accomplishes this by sifting fields into the parts that transmit influence and the parts that constrain. The MPSD lanes then treat each transmitting part as a single scalar problem; whichever formulation one starts from, the recomposed answer carries the same residues, the same characteristic cone, and the same energy. Because the boundary rule is fixed at the outset, method changes leave the interior untouched, and any redistribution appears only as a boundary record in the ledger. This economy makes causality and sign transparent at every step and allows different workers, using different tools, to reach the same number without prior arrangement.

* * *

##### 4.8.2.1 What “equivalence” is, operationally—and the invariants we refuse to touch
------------------------------------------------------------------------------

**Plain picture.** Imagine a messy white beam (a coupled field). Pass it through a prism (a projector basis). It emerges as colored beams (physical channels). You focus each beam with one lens (a scalar inverse) and then recombine. If two prisms yield the same colors and brightness on your screen, the prisms are **equivalent**.

**Physics meaning.** Two computational lanes are **equivalent** when they preserve, on shell:

*   the **characteristic cones** (principal symbol),
*   the **pole structure** and **residues** (propagator near physical poles),
*   the **observables** (stress, flux, conserved charges),
*   the **ledger** posting (boundary and topological data) up to explicit reallocation at the edge.

Permitted moves that guarantee equivalence:

1.  **Basis changes** (projectors, helicity, SD/ASD, Cholesky canonicalization);
2.  **Integrations by parts** (IBP) with declared BCs, with boundary terms ledgered;
3.  **Gauge-slice choices** (including Stückelberg and  $R_\xi$ ), with physical poles/residues staying invariant;
4.  **EOM-proportional terms** added/subtracted from the Lagrangian—these vanish on shell and only reshape the boundary superpotential.

Everything else—hidden sign flips, unconstrained boundary leaks, or order-of-limits violations—fails the equivalence test and will show up as a broken ledger or a moved pole.

* * *

##### 4.8.2.2 Lane A — Choose a basis that behaves (projectors and canonicalization)
--------------------------------------------------------------------------

We first bring the quadratic form to blocks where both **cones** and **signs** can be read at a glance.

##### 4.8.2.2.1 One-forms (vectors): Helmholtz/Hodge split with boundary

**Intuition.** Any vector field is “gradient + divergence-free + harmonic.” The third piece is global and lives at the edge.

**Calculus.** On a domain  $\Omega\subset \mathbb R^3$  with smooth boundary and chosen BCs, the Hodge decomposition reads

$$
\mathbf V = \nabla \varphi \;\oplus\; \mathbf V_{\rm div\,0}\;\oplus\;\mathbf V_{\rm harm},
$$

with  $\nabla\!\cdot\!\mathbf V_{\rm div\,0}=0$  and  $\nabla\times \mathbf V_{\rm harm}=\nabla\!\cdot\!\mathbf V_{\rm harm}=0$ . The harmonic subspace depends on BCs and contributes only boundary data (ledger). In covariant notation,

$$
\Pi^{\mathrm L}{}^\mu{}_\nu \equiv \frac{\nabla^\mu\nabla_\nu}{\Box},\qquad \Pi^{\mathrm T}{}^\mu{}_\nu \equiv \delta^\mu{}_\nu - \Pi^{\mathrm L}{}^\mu{}_\nu,
$$

are idempotent projectors onto longitudinal/transverse subspaces **modulo** boundary harmonics.

**Commutation with inverses.** For constant-coefficient operators  $\mathcal D=\Box+m^2$  under homogeneous LTI BCs,

$$
\Pi^{\mathrm T}\,\mathcal D^{-1}=\mathcal D^{-1}\,\Pi^{\mathrm T}.
$$

_Sketch._ In Fourier variables,  $\Pi^{\mathrm T}(k)$  is rational in  $k$  and commutes with  $\mathcal D(k)$ . Non-LTI coefficients admit a parametrix  $G_0$  with  $[\Pi^{\mathrm T},G_0]$  supported at  $\partial\Omega$ ; we ledger that remainder.

##### 4.8.2.2.2 Rank-2 (symmetric) tensors: Barnes–Rivers in a local frame

On a local inertial patch (or exactly in flat space), decompose

$$
\mathbb 1_{(2)} = P^{(2)} \oplus P^{(1)} \oplus P^{(0s)} \oplus P^{(0w)} \oplus P^{(0sw)} \oplus P^{(0ws)} ,
$$

which isolates spin–2, spin–1, and spin–0 channels. A quadratic operator  $K$  becomes  $K=\sum_s \kappa_s P^{(s)}$  plus gauge-null directions. You invert **per spin**:  $K^{-1}=\sum_s \kappa_s^{-1}P^{(s)}$  on the physical subspace. In curved backgrounds, use frames and patch; the principal symbol and residues (our invariants) are unaffected by this localization.

##### 4.8.2.2.3 Two-forms: self/anti-self-dual (SD/ASD) as a positivity lens

Wick to Euclidean, set  $P_\pm=\tfrac12(1\pm *)$ . Any quadratic form  $\langle H,H\rangle$  becomes  $\|H_+\|^2+\|H_-\|^2$ . Rotate back after the audit; ledger integers are Wick-invariant, so nothing physical is lost.

##### 4.8.2.2.4 Mixed one-forms: Sylvester/Cholesky brings clarity before physics

For a block quadratic functional

$$
\mathcal Q[A,B] = \tfrac12 \Big\langle \begin{pmatrix} A \\ B \end{pmatrix}, \begin{pmatrix} K_{AA} & K_{AB} \\ K_{AB}^\dagger & K_{BB} \end{pmatrix} \begin{pmatrix} A \\ B \end{pmatrix} \Big\rangle, \qquad K=K^\dagger>0,
$$

Cholesky  $`K=R^\dagger R`$  and  $`(A,B)\mapsto R^{-1}(A,B)`$  yields a **unit** quadratic form. Because  $R$  is local and invertible, **cones** and **poles** are unchanged; boundary cross-terms turn into superpotentials we post to the ledger.

* * *

##### 4.8.2.3 Lane B — Project → scalarize → solve (the MPSD dictionary in action)
------------------------------------------------------------------------

We now transform “tensor inverses” into **one scalar inverse per channel**.

##### 4.8.2.3.1 Spin-1 (Proca-type) channels exactly as formulas you run

Take any source  $J^\mu$ . After Helmholtz,

$$
X^\mu = (\text{longitudinal algebraic})\ \oplus\ X^\mu_\perp,\qquad (\Box+m^2)\,X_\perp^\mu= \Pi^{\mathrm T\,\mu}{}_\nu\,J^\nu .
$$

Hence

$$
X_\perp^\mu = (\Box+m^2)^{-1}\,\Pi^{\mathrm T\,\mu}{}_\nu\,J^\nu .
$$

The answer is a **single scalar resolvent** composed with a projector. For the axial field, set  $m=m_S$  and  $J^\mu=g_S J_5^\mu$ ; the longitudinal piece is fixed by  $\nabla\!\cdot\!X=(1/m^2)\,\nabla\!\cdot\!J$ .

**Kernels you actually use.**

$$
G^R(\omega,\mathbf k)=\frac{1}{-(\omega+i0^+)^2+\mathbf k^2+m^2},\qquad G^{\rm static}(\mathbf r)=\frac{e^{-m r}}{4\pi r}.
$$

##### 4.8.2.3 Rank-2: per-spin inverses without tears

If  $K=\sum_s \kappa_s P^{(s)}$  (with gauge-null handled separately),

$$
K^{-1}=\sum_s \kappa_s^{-1}\,P^{(s)}.
$$

Residues are checked one spin at a time; positivity is a per-spin statement. This is the clean way to see “no ghost” without chasing components.

##### 4.8.2.3.3 Two-forms: split, solve, recombine

After Wick,  $H=H_+\oplus H_-$  and the inverses are  $(-\partial^2+m^2_\pm)^{-1}$  channelwise. Back in Lorentzian, SD/ASD diagonalization remains the right lens for residues and cones.

##### 4.8.2.3.4 Mixed vectors: Schur complement = legal “integrate out”

For

$$
\mathbb K=\begin{pmatrix}K_{AA}&K_{AB}\\K_{BA}&K_{BB}\end{pmatrix},
$$

with  $K_{BB}$  invertible on the chosen BCs,

$$
K_{AA}^{\rm eff}=K_{AA}-K_{AB}K_{BB}^{-1}K_{BA}.
$$

**Symbol calculus** gives  $\sigma(K_{AA}^{\rm eff})=\sigma(K_{AA})-\sigma(K_{AB})\sigma(K_{BB})^{-1}\sigma(K_{BA})$ . Hence cones/poles of  $A$  are those of the effective operator. You then **project → scalarize** on  $K_{AA}^{\rm eff}$  exactly as above.

* * *

##### 4.8.2.4 Lane C — Boundary & ledger corridor (declare BCs first, compute once)
-------------------------------------------------------------------------

**Why the order matters.** Variation produces surface terms; unless BCs are fixed in advance and compensators are inserted, the Euler–Lagrange process is not a function and algebra will quietly leak to the boundary.

##### 4.8.2.4.1 Variational surface terms → BC menus, rigorously

*   **Spin-1 (including axial).**  $`\delta S`$  carries  $`\int_{\partial\Omega} n_\nu H^{\nu\mu}\,\delta S_\mu`$ .  
    Choices: **Dirichlet** (fix tangential  $S$ ), **Neumann** (fix  $n_\nu H^{\nu\mu}$ ), **Robin** (linear combo), **Sommerfeld** (radiation). A compensator on  $\partial\Omega$  makes  $\delta S$  clean.
*   **Yang–Mills.** Fix the appropriate tangential potential or the normal flux; add the matching surface piece. Sommerfeld for outgoing waves.
*   **Scalar.** Fix  $\phi$  or  $n\!\cdot\!\partial\phi$ ; the complementary choice is the compensator.

**Function spaces.** Use  $H(\mathrm{curl})$  and  $H(\mathrm{div})$  for vector traces; the trace theorems ensure  $(n\times S)$  and  $(n\!\cdot\!H)$  are well-defined boundary data, so the above BCs are not folklore—they are functional identities.

##### 4.8.2.4.2 Reciprocity & uniqueness: Green–Betti + Rellich = only one answer

*   **Green–Betti.** For second-order systems,  $\int_\Omega (u\,\mathcal L v - v\,\mathcal L u)=\int_{\partial\Omega}(u\,\mathcal B v - v\,\mathcal B u)$ . This equates (i) free-space+homogeneous completion, (ii) images, (iii) boundary integrals—**under the same BCs**.
*   **Rellich uniqueness.** With Sommerfeld radiation, a radiating solution that carries no flux at infinity is zero. Hence no hidden homogeneous piece contaminates the solution.

##### 4.8.2.4.3 Posting rules (what moves to the ledger)

*   **IBP/improvements:** total divergences and superpotentials move **only** surface posts.
*   **Topological integers:** Pontryagin/CS (with  $\mathcal A=gA$  so the level is integer) and Nieh–Yan/Holst are integers recorded at the edge; they never replace kinetic terms.

* * *

##### 4.8.2.5 Lane D — Dispersion & positivity corridor (retarded, DC, Herglotz)
----------------------------------------------------------------------

**Why we enforce this.** Causality + passivity implies analytic structure + positivity. Read DC improperly, and you will manufacture negative slopes and violate physics.

##### 4.8.2.5.1 Retarded convention and spectral measure

Use  $\omega\to\omega+i0^+$  for all Green functions. For scalar channels,

$$
G^R(\omega,\mathbf 0)=\int_0^\infty \frac{\rho(\mu)}{\mu-(\omega+i0^+)^2}\,d\mu,
$$

with  $\rho(\mu)\ge 0$  (spectral measure). This is the Herglotz representation; it encodes positivity before any numerics.

##### 4.8.2.5.2 DC order:  $\mathbf k\to0$  then  $\omega\to0^+$ 

The slope

$$
\lim_{\omega\to0^+}\lim_{\mathbf k\to 0} \frac{\Im G^R(\omega,\mathbf k)}{\omega}\ \ge\ 0
$$

is the passivity test. Interchange of limits can spoil it; we forbid that.

##### 4.8.2.5.3 Kramers–Kronig with subtractions; moments/sum-rules

Principal-value integrals with enough subtractions render K–K finite. Moments

$$
\int_0^\infty \frac{\Im G^R(\omega,0)}{\omega^{2n+1}}\,d\omega
$$

give quick internal consistency checks: incorrect signs or wrong DC order light up here.

* * *

##### 4.8.2.6 Micro-workflows you can copy-paste (now with error bars and asymptotics)
----------------------------------------------------------------------------

### Card A — Static axial field from a compact polarized source

**Input:** compact  $J_5^0(\mathbf r)$ , BC:  $S\to 0$  at infinity.  
**Run:**  $(-\nabla^2+m_S^2)S_0=g_S J_5^0$  with  $S_i=0$  by symmetry.  
**Closed form:**  $S_0(\mathbf r)=g_S\,G*J_5^0$ ,  $G=e^{-m_S r}/(4\pi r)$ .  
**Energy:**  $E_S=\tfrac12\!\int[(\nabla S_0)^2+m_S^2 S_0^2]$ .  
**Asymptotics:**  $S_0(r)\sim g_S Q_5\,e^{-m_S r}/(4\pi r)$ .  
**Error bar (truncation):**  $\|S_0-S_0^{(R)}\|_{L^\infty(\mathbb R^3\setminus B_R)}\lesssim C\,e^{-m_S R}/R$ .

### Card B — Retarded axial pulse (strict corridor)

**Input:** compact  $J_5^\mu(t,\mathbf r)$ , Sommerfeld BC.  
**Run:**  $S_\perp^\mu=g_S\,G^R * \Pi^{\mathrm T} J_5^\mu$ ,  $S_{\parallel}$  algebraic.  
**Check:** enforce  $\mathbf k\to0$  then  $\omega\to0^+$ ; Herglotz slope  $\ge 0$ .  
**Flux:** ledger posts the radiated energy through a far sphere.

### Card C — Two mixed vectors with SPD kernel

**Input:**  $K=K^\dagger>0$ .  
**Run:** Cholesky  $K=R^\dagger R$ , redefine  $(A,B)\mapsto R^{-1}(A,B)$ , then Helmholtz on each, then scalar resolvents.  
**Residues:** unchanged (local, invertible map).  
**Boundary:** any cross-term created by  $R$  is a superpotential and goes to the ledger.

### Card D — Rank-2 per-spin inversion

**Input:**  $K_{\mu\nu,\rho\sigma}(k)$  on a patch.  
**Run:** project to  $P^{(2)},P^{(1)},P^{(0s)},P^{(0w)}$ , invert  $\kappa_s$  on each block, recompose.  
**Health:** compute residues at physical poles; negative residue → stop (ghost).

* * *

##### 4.8.2.7 Lemmas and proofs you’ll actually cite
------------------------------------------

### (L1) Projector–inverse commutation (vector case), with boundary remainder

For  $\mathcal D=\Box+m^2$  and homogeneous LTI BCs on  $\Omega$ ,

$$
\Pi^{\mathrm T}\mathcal D^{-1}-\mathcal D^{-1}\Pi^{\mathrm T}=\mathcal R_{\partial\Omega},
$$

where  $\mathcal R_{\partial\Omega}$  is a first-order boundary operator supported on  $\partial\Omega$ .  
_Sketch._ Fourier-diagonalize in the interior; by Green’s identities the mismatch localizes at the boundary. We post  $\mathcal R_{\partial\Omega}$  to the ledger.

### (L2) Schur complement preserves cones/poles

If  $K_{BB}$  is elliptic/hyperbolic and invertible under the BCs,

$$
\sigma(K_{AA}^{\rm eff})=\sigma(K_{AA})-\sigma(K_{AB})\sigma(K_{BB})^{-1}\sigma(K_{BA}).
$$

Hence characteristics of  $K_{AA}^{\rm eff}$  coincide with those of the full system projected to  $A$ ; poles are those zeros of  $\kappa_s$  in the effective block.

### (L3) Cholesky canonicalization preserves physics

With  $K=R^\dagger R$ , the map  $X\mapsto RX$  preserves principal symbols, poles, and residues. Any change to surface terms is a superpotential—ledger-only.

* * *

##### 4.8.2.8 Discrete posture (how to do all this on a computer without breaking physics)
--------------------------------------------------------------------------------

**Transforms.** Use the **Miller Transform** locks: MT-c (continuous), MT-d (unitary DFT), MT-1S (single-frequency estimator consistent with MT-d on-grid).

**Spaces.** Discretize vectors in  $H(\mathrm{curl})$  (edge elements) and  $H(\mathrm{div})$  (face elements); this respects tangential/normal traces so BCs are real, not approximate. For scalars use  $H^1$  (nodal).

**Constraints.** Enforce divergence constraints weakly via mixed formulations (e.g., a Lagrange multiplier for the longitudinal piece) or exactly via Helmholtz splitting on the mesh.

**Screened Poisson/Yukawa.** Use standard SPD solvers (conjugate gradients with algebraic multigrid). Mass-lumping yields diagonally dominant mass matrices; positivity of the discrete energy is then pointwise checkable.

**Retarded kernels.** Use causal stepping (e.g., leapfrog) or convolution quadrature; never impose artificial damping to “fix” stability—if you need it, a corridor or BC is wrong.

**DC order in code.** To measure DC slopes, compute  $G^R(\omega,\mathbf 0)$  at small  $\omega$  on a fixed mesh; only then refine  $\mathbf k$  to zero on a larger domain. Reversing steps is a corridor violation.

* * *

##### 4.8.2.9 Pitfalls (and why MEFP keeps you out of them)
-------------------------------------------------

*   **Undeclared BCs.** IBP leaks to the boundary; variations cease to be functionals. Remedy: declare BCs _first_, add compensators, and post every surface term.
*   **Projectors on curved backgrounds.** Apply in frames on patches; non-commutation localizes at boundaries and is ledgered (never faked as bulk).
*   **Mixing with wrong signs.** If Cholesky fails, the kernel isn’t SPD—there is a ghost. Stop and fix the kinetic form before projecting.
*   **Order-of-limits.** Swapping  $\mathbf k\to 0$  and  $\omega\to 0^+$  can produce negative slopes from a perfectly passive system. Corridor discipline prevents this.
*   **Numerical shortcuts that break physics.** “Small artificial damping” hides, it doesn’t heal. If you need it, a BC or discretization space is mismatched to the physics.

* * *

##### 4.8.2.10 What MEFP + MPSD buys you in practice
------------------------------------------

*   **Speed with proof.** Every inversion reduces to **one scalar resolvent per channel**; residues and cones are visible; signs are audited.
*   **Transparent boundaries.** Reciprocity and Rellich guarantee uniqueness; any method difference appears only as a **ledger** post.
*   **Robust dispersion.** Retarded convention, DC order, and Herglotz positivity make low-frequency behavior reliable.
*   **Drop-in reuse.** The same cards/lemmas solve axial torsion problems, YM mixings, rank-2 inversions, and two-form audits with superficial edits only.

_From here, we can move straight into the worked solves and the falsifiability pack. The heavy algebra has been domesticated: prisms split the beam, scalar lenses focus each color, the ledger tracks the edges, and the corridor guards causality and positivity._

### 4.8.3 Connectivity Map
**Within Chapter 4 (closely related):**
- §4.5 — Miller Field Equation Set (MFES) — full classical system
- §4.9 — Causality, hyperbolicity, response & dispersion (MDPC)
- §4.10 — Boundary, uniqueness, topology & ledgers (MBLC + MLCP)
- §4.11 — Spectral standardization — the Miller Transform (MT)
- §4.13 — Legacy & intermediate forms

**External chapters (C#):**
- C5 §5.16–5.21, §5.33

---

