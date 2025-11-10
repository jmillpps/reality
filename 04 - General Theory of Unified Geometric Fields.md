# Chapter 4

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
     $\Pi^{\rm T}{}^\mu{}_\nu=\delta^\mu{}_\nu-\nabla^\mu\nabla_\nu/\Box$ ,  
     $S^\mu = g_S(\Box+m_S^2)^{-1}\,\Pi^{\rm T}{}^\mu{}_\nu J_5^\nu$ ,  
     $\nabla_\mu S^\mu=(g_S/m_S^2)\nabla_\mu J_5^\mu$  (algebraic longitudinal).
*   **Rank‑2 (Barnes–Rivers).**  
    Decompose  $h_{\mu\nu}$  with projectors  $P^{(2)},P^{(1)},P^{(0\text{s})},P^{(0\text{w})}$ ; invert per spin with residues checked in the chosen basis.
*   **Two‑forms (SD/ASD).**  
     $H_\pm=\tfrac12(H\pm i*H)$ ; in Euclidean signature, positivity is one line because  $*^2=+1$  on 2‑forms.
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
*   The **Gibbons–Hawking–York (GHY)** term makes the variational problem well-posed if we hold the induced metric fixed at the boundary ( $ \delta h_{ij}=0$ )—without it, varying  $R$  produces a total divergence that spoils the Euler–Lagrange story.

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

**Geometry you actually need.** In curved space we use a tetrad  $e^a{}_\mu$  and a spin connection  $\omega_\mu{}^{ab}$ . The gamma matrices are flat-space objects  $\{\gamma^a,\gamma^b\}=2\eta^{ab}$ , and  $\gamma^\mu=e^\mu{}_a\gamma^a$ . The covariant derivative acting on a spinor is

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
    $$
    \partial_i\Pi^i + m_S^2 S_0 - g_S J_5^0=0,
    $$
    which follows from preserving the **primary** constraint  $\Pi^0=0$ .

**Well-posedness.** With boundary conditions declared (Dirichlet/Neumann/Robin/Sommerfeld per sector), the propagating blocks form a symmetric-hyperbolic system. If constraints hold initially, the equations keep them satisfied.

* * *

##### 4.5.2.5.5 Hyperbolicity and front speeds (principal symbols at a glance)
------------------------------------------------------------------

**Plain picture.** Treat every wave at very short wavelength: does it respect the light cone? If yes, the theory’s causal skeleton is healthy.

**Symbols and cones.**

*   **Axial torsion.** Principal symbol  $\mathcal P^\mu{}_\nu(k)=-k^2\delta^\mu{}_\nu+k^\mu k_\nu$  ⇒ characteristics  $k^2=0$  ⇒ **front speed = 1**.
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
Let  $\Pi^{\mathrm T}{}^\mu{}_\nu=\delta^\mu{}_\nu-\nabla^\mu\nabla_\nu/\Box$ . Then

$$
S^\mu = g_S\,(\Box+m_S^2)^{-1}\,\Pi^{\mathrm T}{}^\mu{}_\nu\,J_5^\nu,\qquad \nabla\!\cdot\!S=\frac{g_S}{m_S^2}\nabla\!\cdot\!J_5.
$$

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

**Belinfante tensor (symmetric).** With tetrads  $e^a{}_\mu$  and spin connection  $\omega_{\mu ab}$ ,

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

*    $T^{0}{}_{0,\rm total}$  is the **sum** from all bulk sectors fixed earlier (YM, scalars, Dirac, axial torsion  $S_\mu$ , …) in our sign conventions.
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

##### 4.8.2.8.1 What “equivalence” is, operationally—and the invariants we refuse to touch
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

##### 4.8.2.8.2 Lane A — Choose a basis that behaves (projectors and canonicalization)
--------------------------------------------------------------------------

We first bring the quadratic form to blocks where both **cones** and **signs** can be read at a glance.

### 8.2.1 One-forms (vectors): Helmholtz/Hodge split with boundary

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

### 8.2.2 Rank-2 (symmetric) tensors: Barnes–Rivers in a local frame

On a local inertial patch (or exactly in flat space), decompose

$$
\mathbb 1_{(2)} = P^{(2)} \oplus P^{(1)} \oplus P^{(0s)} \oplus P^{(0w)} \oplus P^{(0sw)} \oplus P^{(0ws)} ,
$$

which isolates spin–2, spin–1, and spin–0 channels. A quadratic operator  $K$  becomes  $K=\sum_s \kappa_s P^{(s)}$  plus gauge-null directions. You invert **per spin**:  $K^{-1}=\sum_s \kappa_s^{-1}P^{(s)}$  on the physical subspace. In curved backgrounds, use frames and patch; the principal symbol and residues (our invariants) are unaffected by this localization.

### 8.2.3 Two-forms: self/anti-self-dual (SD/ASD) as a positivity lens

Wick to Euclidean, set  $P_\pm=\tfrac12(1\pm *)$ . Any quadratic form  $\langle H,H\rangle$  becomes  $\|H_+\|^2+\|H_-\|^2$ . Rotate back after the audit; ledger integers are Wick-invariant, so nothing physical is lost.

### 8.2.4 Mixed one-forms: Sylvester/Cholesky brings clarity before physics

For a block quadratic functional

$$
\mathcal Q[A,B] = \tfrac12 \Big\langle \begin{pmatrix} A \\ B \end{pmatrix}, \begin{pmatrix} K_{AA} & K_{AB} \\ K_{AB}^\dagger & K_{BB} \end{pmatrix} \begin{pmatrix} A \\ B \end{pmatrix} \Big\rangle, \qquad K=K^\dagger>0,
$$

Cholesky  $K=R^\dagger R$  and  $ (A,B)\mapsto R^{-1}(A,B)$  yields a **unit** quadratic form. Because  $R$  is local and invertible, **cones** and **poles** are unchanged; boundary cross-terms turn into superpotentials we post to the ledger.

* * *

##### 4.8.2.8.3 Lane B — Project → scalarize → solve (the MPSD dictionary in action)
------------------------------------------------------------------------

We now transform “tensor inverses” into **one scalar inverse per channel**.

### 8.3.1 Spin-1 (Proca-type) channels exactly as formulas you run

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

### 8.3.2 Rank-2: per-spin inverses without tears

If  $K=\sum_s \kappa_s P^{(s)}$  (with gauge-null handled separately),

$$
K^{-1}=\sum_s \kappa_s^{-1}\,P^{(s)}.
$$

Residues are checked one spin at a time; positivity is a per-spin statement. This is the clean way to see “no ghost” without chasing components.

### 8.3.3 Two-forms: split, solve, recombine

After Wick,  $H=H_+\oplus H_-$  and the inverses are  $(-\partial^2+m^2_\pm)^{-1}$  channelwise. Back in Lorentzian, SD/ASD diagonalization remains the right lens for residues and cones.

### 8.3.4 Mixed vectors: Schur complement = legal “integrate out”

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

##### 4.8.2.8.4 Lane C — Boundary & ledger corridor (declare BCs first, compute once)
-------------------------------------------------------------------------

**Why the order matters.** Variation produces surface terms; unless BCs are fixed in advance and compensators are inserted, the Euler–Lagrange process is not a function and algebra will quietly leak to the boundary.

### 8.4.1 Variational surface terms → BC menus, rigorously

*   **Spin-1 (including axial).**  $\delta S$  carries  $ \int_{\partial\Omega} n_\nu H^{\nu\mu}\,\delta S_\mu$ .  
    Choices: **Dirichlet** (fix tangential  $S$ ), **Neumann** (fix  $n_\nu H^{\nu\mu}$ ), **Robin** (linear combo), **Sommerfeld** (radiation). A compensator on  $\partial\Omega$  makes  $\delta S$  clean.
*   **Yang–Mills.** Fix the appropriate tangential potential or the normal flux; add the matching surface piece. Sommerfeld for outgoing waves.
*   **Scalar.** Fix  $\phi$  or  $n\!\cdot\!\partial\phi$ ; the complementary choice is the compensator.

**Function spaces.** Use  $H(\mathrm{curl})$  and  $H(\mathrm{div})$  for vector traces; the trace theorems ensure  $(n\times S)$  and  $(n\!\cdot\!H)$  are well-defined boundary data, so the above BCs are not folklore—they are functional identities.

### 8.4.2 Reciprocity & uniqueness: Green–Betti + Rellich = only one answer

*   **Green–Betti.** For second-order systems,  $\int_\Omega (u\,\mathcal L v - v\,\mathcal L u)=\int_{\partial\Omega}(u\,\mathcal B v - v\,\mathcal B u)$ . This equates (i) free-space+homogeneous completion, (ii) images, (iii) boundary integrals—**under the same BCs**.
*   **Rellich uniqueness.** With Sommerfeld radiation, a radiating solution that carries no flux at infinity is zero. Hence no hidden homogeneous piece contaminates the solution.

### 8.4.3 Posting rules (what moves to the ledger)

*   **IBP/improvements:** total divergences and superpotentials move **only** surface posts.
*   **Topological integers:** Pontryagin/CS (with  $\mathcal A=gA$  so the level is integer) and Nieh–Yan/Holst are integers recorded at the edge; they never replace kinetic terms.

* * *

##### 4.8.2.8.5 Lane D — Dispersion & positivity corridor (retarded, DC, Herglotz)
----------------------------------------------------------------------

**Why we enforce this.** Causality + passivity implies analytic structure + positivity. Read DC improperly, and you will manufacture negative slopes and violate physics.

### 8.5.1 Retarded convention and spectral measure

Use  $\omega\to\omega+i0^+$  for all Green functions. For scalar channels,

$$
G^R(\omega,\mathbf 0)=\int_0^\infty \frac{\rho(\mu)}{\mu-(\omega+i0^+)^2}\,d\mu,
$$

with  $\rho(\mu)\ge 0$  (spectral measure). This is the Herglotz representation; it encodes positivity before any numerics.

### 8.5.2 DC order:  $\mathbf k\to0$  then  $\omega\to0^+$ 

The slope

$$
\lim_{\omega\to0^+}\lim_{\mathbf k\to 0} \frac{\Im G^R(\omega,\mathbf k)}{\omega}\ \ge\ 0
$$

is the passivity test. Interchange of limits can spoil it; we forbid that.

### 8.5.3 Kramers–Kronig with subtractions; moments/sum-rules

Principal-value integrals with enough subtractions render K–K finite. Moments

$$
\int_0^\infty \frac{\Im G^R(\omega,0)}{\omega^{2n+1}}\,d\omega
$$

give quick internal consistency checks: incorrect signs or wrong DC order light up here.

* * *

##### 4.8.2.8.6 Micro-workflows you can copy-paste (now with error bars and asymptotics)
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

##### 4.8.2.8.7 Lemmas and proofs you’ll actually cite
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

##### 4.8.2.8.8 Discrete posture (how to do all this on a computer without breaking physics)
--------------------------------------------------------------------------------

**Transforms.** Use the **Miller Transform** locks: MT-c (continuous), MT-d (unitary DFT), MT-1S (single-frequency estimator consistent with MT-d on-grid).

**Spaces.** Discretize vectors in  $H(\mathrm{curl})$  (edge elements) and  $H(\mathrm{div})$  (face elements); this respects tangential/normal traces so BCs are real, not approximate. For scalars use  $H^1$  (nodal).

**Constraints.** Enforce divergence constraints weakly via mixed formulations (e.g., a Lagrange multiplier for the longitudinal piece) or exactly via Helmholtz splitting on the mesh.

**Screened Poisson/Yukawa.** Use standard SPD solvers (conjugate gradients with algebraic multigrid). Mass-lumping yields diagonally dominant mass matrices; positivity of the discrete energy is then pointwise checkable.

**Retarded kernels.** Use causal stepping (e.g., leapfrog) or convolution quadrature; never impose artificial damping to “fix” stability—if you need it, a corridor or BC is wrong.

**DC order in code.** To measure DC slopes, compute  $G^R(\omega,\mathbf 0)$  at small  $\omega$  on a fixed mesh; only then refine  $\mathbf k$  to zero on a larger domain. Reversing steps is a corridor violation.

* * *

##### 4.8.2.8.9 Pitfalls (and why MEFP keeps you out of them)
-------------------------------------------------

*   **Undeclared BCs.** IBP leaks to the boundary; variations cease to be functionals. Remedy: declare BCs _first_, add compensators, and post every surface term.
*   **Projectors on curved backgrounds.** Apply in frames on patches; non-commutation localizes at boundaries and is ledgered (never faked as bulk).
*   **Mixing with wrong signs.** If Cholesky fails, the kernel isn’t SPD—there is a ghost. Stop and fix the kinetic form before projecting.
*   **Order-of-limits.** Swapping  $\mathbf k\to 0$  and  $\omega\to 0^+$  can produce negative slopes from a perfectly passive system. Corridor discipline prevents this.
*   **Numerical shortcuts that break physics.** “Small artificial damping” hides, it doesn’t heal. If you need it, a BC or discretization space is mismatched to the physics.

* * *

##### 4.8.2.8.10 What MEFP + MPSD buys you in practice
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

## 4.9 Table of Contents and Introduction

### 4.9.1 Table of Contents (Section 4.9)
- 4.9.2 Causality, hyperbolicity, response & dispersion (MDPC)
- 4.9.3 Connectivity Map

### 4.9.2 Causality, hyperbolicity, response & dispersion (MDPC)
_See also:_ §4.11, §4.12, §4.14; C0 §0.8–0.9 & §0.14, C5 §5.36–5.47, C1 §1.7

9\. Causality, hyperbolicity, response & dispersion (MDPC) — deeply developed
=============================================================================

> **What this section presents.** A fully operational theory of _how_ disturbances move and _how_ the system answers a drive. We start with handholds a careful non-expert can grasp (front vs group; why the order of limits matters), then climb to the exact tools experts use: principal symbols and symmetrizers, retarded kernels and their support, Herglotz/Nevanlinna positivity for matrix responses, Schur complements for mixed channels, Hadamard/parametrix structure on curved backgrounds, and boundary radiation/uniqueness. Each subsection is a walk-through: picture → invariant you must preserve → derivation you can check line-by-line.

Causality means simply this: no influence propagates faster than light. The structure of space‑time fixes this limit. If two events can be joined by the worldline of a material body (a timelike connection), their order is the same for all observers: the cause is earlier, the effect later. If the separation is spacelike, no signal can connect the events, and their order may differ for different observers without contradiction. Thus the constant (c) is not merely a property of light, but a property of space‑time itself: it is the upper bound for every physical propagation.

Also, when we find that our equations describe not only what happens here but also what seems to echo elsewhere without any mediating influence, we are reminded that the picture we call a “system” is only a convenience. The world is not neatly divisible into independent parts; the division is an act of bookkeeping. In the old mechanics, completeness meant that every cause was contained within the system itself. In the deeper view, completeness lives not in the separate accounts but in the ledger that records their balance. What we take for action at a distance may only be the balancing of that universal ledger—a reconciliation of entries already written into the fabric of spacetime. Causality then is not broken; it is simply expressed in a wider currency, where correlations are the transactions and conservation of information is the law that never fails.

* * *

##### 4.9.2.9.1 Orientation: what counts as “healthy propagation”
-----------------------------------------------------

**Plain picture.** Tap once. Nothing anywhere reacts _before_ a light signal could arrive. When a well-prepared pulse comes, its _crest_ may lag (group speed  $<1$ ), but the _very first ripple_ (the _front_) hugs the light cone. If you specify the present carefully on a slice, the equations determine the future and the past uniquely (hyperbolicity). If you drive the system with a time-harmonic source, the frequency response is analytic in the upper half-plane and its low-frequency slope is non-negative (passivity).

**Three invariants to protect:**

1.  **Characteristic cone** (from the principal symbol): sets the _front_.
2.  **Green/normal hyperbolicity** with energy estimates: ensures well-posedness.
3.  **Herglotz positivity + Kramers–Kronig** for responses: encodes causality/passivity at  $\omega\to0^+$ .

We will read all three off each channel and for _any_ mixing we collapse to with Schur complements.

* * *

##### 4.9.2.9.2 Front, signal, and group: one tap → three velocities
--------------------------------------------------------

**From picture to calculus.** For a linear PDE  $\mathcal L u=f$ , the **front** rides on the _characteristics_ of  $\sigma(\mathcal L)(x,k)$ , the principal symbol: solve  $\det \sigma(\mathcal L)(x,k)=0$ . The **group** velocity comes from the actual dispersion  $\omega(\mathbf k)$ :  $v_g=\partial\omega/\partial|\mathbf k|$ . The **signal** speed (how a wavepacket’s envelope moves) interpolates and depends on bandwidth; the _front_ is the only relativistically sacred one.

**Stationary-phase sketch (flat patch).** Let  $u(t,\mathbf x)=\int e^{i(\mathbf k\cdot\mathbf x-\omega t)}\hat u_0(\mathbf k)\,d^3\!k$ .

*   If the phase has no stationary point inside  $|\mathbf x|<t$ , the contribution is exponentially small; if a stationary point exists with  $\omega=\omega(\mathbf k)$ , a packet travels with  $v_g$ .
*   When the phase can never be stationary because  $\omega$  is analytic in  $\Im\omega>0$  and the integration contour can be pulled upward for  $t<|\mathbf x|$ , the _front_ is barred from advancing: it sits on  $|\mathbf x|=t$ .

This stationary-phase/contour dance is the frequency-domain face of the principal-symbol story below.

* * *

##### 4.9.2.9.3 Hyperbolicity: existence, uniqueness, and domain of dependence
------------------------------------------------------------------

**Definition (what we use).**

*   A scalar second-order  $P$  is **normally hyperbolic** if  $\sigma(P)(x,k)=-g^{\mu\nu}k_\mu k_\nu$ . On globally hyperbolic backgrounds, advanced/retarded Green functions exist and have causal support.
*   A constrained first-order system (e.g., Proca with algebraic longitudinal; YM with Gauss law) is **Green hyperbolic** if the _reduced_ dynamics on the physical subspace is normally hyperbolic and constraints propagate.

**Axial spin-1 (transverse block).** Write the equation on  $\Pi^{\mathrm T}\!S$ :

$$
(\Box+m_S^2)\,S_\perp^\mu= \Pi^{\mathrm T\,\mu}{}_\nu\,J_5^\nu,\qquad \Pi^{\mathrm T\,\mu}{}_\nu=\delta^\mu{}_\nu-\frac{\nabla^\mu\nabla_\nu}{\Box}.
$$

Principal symbol:  $\sigma(\Box+m_S^2)=-(k^2)+m_S^2$  times the identity on the transverse subspace. **Characteristics**  $k^2=0$  ⇒ luminal _front_. The longitudinal  $S_\parallel$  is algebraic (no wave operator), pinned by  $\nabla\!\cdot\!S=(g_S/m_S^2)\nabla\!\cdot\!J_5$ .

**Energy estimate (template you can reuse).** Multiply the PDE by a time derivative of the field, integrate by parts on  $\Sigma_t$ , and use the stress–flux identity to get

$$
\|u(t)\|_{H^1(\Sigma_t)}^2 +\int_{t_0}^t\!\!\!\text{Flux}_{\partial\Sigma_\tau}\,d\tau \ \le\ C\Big(\|u(t_0)\|_{H^1(\Sigma_{t_0})}^2+\int_{t_0}^t\!\!\!\|f(\tau)\|_{L^2}^2 d\tau\Big).
$$

This gives uniqueness and continuous dependence on data—precisely what “well-posed” means for us. The same estimate holds blockwise for YM transverse modes and scalars.

**Constraint propagation (Proca).** Let  $\Gamma\equiv\partial_i\Pi^i+m_S^2 S_0-g_S J_5^0$ . Using the equations,  $\partial_t\Gamma=0$  modulo sources ⇒ if  $\Gamma=0$  at  $t_0$ , it stays zero. Hence only transverse DOF carry time evolution.

* * *

##### 4.9.2.9.4 Retarded kernels: support, tails, and the front
---------------------------------------------------

**Spin-1 (mass  $m$ ) in  $3+1$ .** On the transverse subspace,

$$
G^R(\omega,\mathbf k)=\frac{1}{-(\omega+i0^+)^2+\mathbf k^2+m^2}.
$$

Fourier inversion gives the _causal_ kernel with support on and inside the light cone:

$$
G^R(t,\mathbf r)=\theta(t)\,\bigg[\underbrace{\frac{\delta(t-r)}{4\pi r}}_{\text{front at }t=r} -\underbrace{\frac{m}{4\pi}\frac{J_1\!\left(m\sqrt{t^2-r^2}\right)}{\sqrt{t^2-r^2}}\,\theta(t-r)}_{\text{sub-luminal body}}\bigg].
$$
*   The  $\delta(t-r)$  term is the _front_.
*   The Bessel tail decays for  $t>r$  and is exponentially small when  $m\sqrt{t^2-r^2}\gg1$ .
*   Static limit:  $G(\mathbf r)=e^{-m r}/(4\pi r)$ .

**Curved background (Hadamard form, local statement).** In a convex normal neighborhood, every Green function has

$$
G^R(x,x')=U(x,x')\,\delta(\sigma)+V(x,x')\,\theta(-\sigma),
$$

with  $\sigma$  the signed squared geodesic distance.  $U$  transports the _front_ along null geodesics;  $V$  carries the tail inside the cone. This local statement is enough to control causal support and to glue parametrix patches globally.

* * *

##### 4.9.2.9.5 Response as a Herglotz/Nevanlinna function: positivity from passivity
-------------------------------------------------------------------------

**From power balance to inequalities.** Drive a channel  $X$  with a source  $J$ . The work delivered on  $[t_0,t_1]$  is

$$
W=\int_{t_0}^{t_1}\!\! dt\ \big[J(t)\cdot \dot X(t)\big] =\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}\ i\omega\, \tilde J(-\omega)^\dagger\,\tilde\chi^R(\omega)\,\tilde J(\omega).
$$

Passivity demands  $W\ge 0$  for any real  $J$ . With the _retarded_ prescription ( $\omega\to\omega+i0^+$ ) and the **DC corridor** (below), this implies

*   **Scalar case:**  $\displaystyle \lim_{\omega\to0^+}\frac{1}{\omega}\Im \chi^R(\omega,\mathbf 0)\ \ge\ 0.$ 
*   **Matrix case:** for any test vector  $v$ ,
    
$$
\lim_{\omega\to0^+}\frac{1}{\omega}\,v^\dagger \Im \boldsymbol\chi^R(\omega,\mathbf 0)\,v\ \ge\ 0,
$$

i.e., the Hermitian matrix  $\Im \boldsymbol\chi^R(\omega,\mathbf 0)/\omega$  is positive semidefinite as  $\omega\downarrow0$ .

**Analyticity/Kramers–Kronig.** Causality → analyticity in  $\Im\omega>0$  → the subtracted K–K relation

$$
\Re \chi^R(\omega)=\chi_\infty+\frac{2}{\pi}\,\mathcal P\!\int_0^\infty\! d\omega'\,\frac{\omega'\,\Im\chi^R(\omega')}{\omega'^2-\omega^2}.
$$

The sign of  $\Im\chi^R/\omega$  near  $0^+$  fixes the low-frequency slope of  $\Re\chi^R$ .

* * *

##### 4.9.2.9.6 The DC corridor (and why reversing the limits lies)
-------------------------------------------------------

**Rule.** Always take  $\mathbf k\to0$  **then**  $\omega\to0^+$ .

**Demonstration (one line, one lie).** For the scalar resolvent

$$
\chi^R(\omega,\mathbf k)=\frac{1}{-(\omega+i0^+)^2+\mathbf k^2+m^2},
$$
 
$$
\lim_{\omega\to0^+}\lim_{\mathbf k\to0}\frac{\Im\chi^R(\omega,\mathbf k)}{\omega} =\frac{\pi}{2m}\quad(\ge0),
$$

because  $\Im[(x+i0)^{-1}]=-\pi\delta(x)$  captures weight at threshold. The _reversed_ order yields 0 and misses the dissipative spectral weight—a false negative. In mixed matrices, the reversed order can flip signs and create spurious “active” behavior. The corridor forbids that.

**Regulators.** For massless channels, introduce  $m\to0^+$  and remove it _after_ the corridor limits; this preserves passivity and the correct infrared sum rules.

* * *

##### 4.9.2.9.7 Spectral measures, moments, and quick sum rules
---------------------------------------------------

**Scalar Herglotz representation at  $\mathbf k=0$ .**

$$
\chi^R(\omega)=\chi_0 + \int_0^\infty \frac{d\rho(\mu)}{\mu-(\omega+i0^+)^2},\qquad d\rho(\mu)\ge 0.
$$
*   **High-frequency:**  $\chi^R(\omega)=\chi_0 + \omega^{-2}\!\int d\rho(\mu)+O(\omega^{-4})$ . Wrong  $\omega^{-2}$  coefficient ⇒ normalization/corridor error.
*   **Moments:**  $\int \mu^n\, d\rho(\mu)$  control derivatives of  $\Re\chi^R$  at  $\omega=0$ . Matrix versions replace  $d\rho$  by a PSD matrix measure.

These are fast internal checks: a handful of frequencies can flag a sign or order mistake without a full inversion.

* * *

##### 4.9.2.9.8 Boundaries, radiation, and uniqueness: who pays at infinity
---------------------------------------------------------------

**Sommerfeld & Rellich.** Impose the outgoing condition; then the only homogeneous solution with zero far-field flux is the zero solution (Rellich). Hence the retarded solution is **unique**, and any method (images, boundary integrals, free-space + homogeneous) that honors the same BCs gives the same bulk field. Differences are ledger posts—bookkeeping at the surface.

**Flux identity (any sector).**

$$
\frac{d}{dt}\int_{\Sigma_t}\! N\sqrt{h}\,T^{0}{}_{0} = -\oint_{\partial\Sigma_t}\!\text{(Poynting-like)}\cdot d\mathbf a \ +\ \int_{\Sigma_t}\! J\cdot \dot X,
$$

so the far boundary “cashier” always balances the jar: radiation out equals jar decrease minus source work.

* * *

##### 4.9.2.9.9 Mixed channels: matrix positivity and Schur complements
-----------------------------------------------------------

**Matrix Herglotz at DC.** For the block response  $\boldsymbol\chi^R(\omega,\mathbf 0)$ ,

$$
\frac{1}{\omega}\,\Im \boldsymbol\chi^R(\omega,\mathbf 0)\ \succeq\ 0\quad(\omega\downarrow0).
$$

**Stability under Schur reduction.** If you integrate out block  $B$ ,

$$
\chi_{AA}^{R,\rm eff} =\chi_{AA}^R-\chi_{AB}^R(\chi_{BB}^R)^{-1}\chi_{BA}^R,
$$

then

$$
\frac{1}{\omega}\,\Im \chi_{AA}^{R,\rm eff}(\omega,\mathbf 0)\ \succeq\ 0,
$$

provided  $\Im \chi_{BB}^R/\omega\succeq0$ . _Proof sketch._ The Schur complement of a PSD block of a Hermitian matrix is PSD; apply this to the block-matrix  $\Im\boldsymbol\chi^R/\omega$ .

This guarantees passivity survives the legal “integrate-out” we use in effective descriptions.

* * *

##### 4.9.2.9.10 Microlocal viewpoint (how singularities travel)
---------------------------------------------------

**Purpose.** Beyond kernels: how do _fronts_ (singularities) move on curved backgrounds?

**Propagation of singularities.** For normally hyperbolic operators, the wavefront set  $\operatorname{WF}(G^R)$  lies on the **bicharacteristic flow** generated by the Hamiltonian  $H(x,k)=\tfrac12 g^{\mu\nu}k_\mu k_\nu$ . This says: singular support rides null geodesics. The Hadamard form  $U\delta(\sigma)+V\theta(-\sigma)$  is the local expression of that transport;  $U$  obeys a transport equation along null geodesics,  $V$  solves an inhomogeneous recursion. We use this only to justify local causal support and to patch parametrices—no quantum inputs are needed.

* * *

##### 4.9.2.9.11 Numerics that don’t cheat causality
----------------------------------------

**Spaces that honor traces.** Use  $H(\mathrm{curl})$ / $H(\mathrm{div})$ \-conforming elements for vector channels so tangential/normal traces are _exactly_ represented. This makes boundary flux—our ledger entry—numerically faithful.

**CFL from the cone.** Derive the time step from the principal symbol’s light cone, not from ad-hoc damping. If a scheme is unstable at that CFL, a boundary or corridor rule is being violated.

**Causal convolution.** For retarded kernels compute with convolution quadrature (CQ). CQ preserves analyticity in  $\Im\omega>0$  and causal support by construction.

**DC measurement protocol.** Fix  $\mathbf k=0$  (large domain), measure  $\Im \chi^R(\omega,0)/\omega$  as  $\omega\downarrow0$ . Only after that, relax  $\mathbf k$  toward zero on a larger domain. Reversing order is a corridor breach and will flip slopes spuriously.

* * *

##### 4.9.2.9.12 Lemmas with proofs (short, load-bearing, reusable)
-------------------------------------------------------

### Lemma 9.1 (Luminal front for spin-1 transverse block)

For  $P^\mu{}_\nu=\nabla_\alpha\nabla^\alpha\delta^\mu{}_\nu-\nabla^\mu\nabla_\nu$ ,  
 $\sigma(P)^\mu{}_\nu(x,k)=-k^2\delta^\mu{}_\nu + k^\mu k_\nu$ .  
Eigenvalues vanish iff  $k^2=0$ . Hence the characteristic cone is the light cone, and the front is luminal. □

### Lemma 9.2 (Energy estimate ⇒ well-posedness)

Let  $P$  be normally/Green hyperbolic with compatible BCs. Then there exists  $C>0$  such that

$$
\|u(t)\|_{H^1}^2\le C\Big(\|u(t_0)\|_{H^1}^2+\int_{t_0}^t\!\!\|f(\tau)\|_{L^2}^2d\tau\Big).
$$

_Proof._ Multiply  $Pu=f$  by  $\partial_t u$ , integrate on  $\Sigma_t$ , use the divergence theorem to convert space derivatives to flux through  $\partial\Sigma_t$ , absorb the flux by BCs (or ledger it), and Grönwall. □

### Lemma 9.3 (Matrix Herglotz at DC)

For any test  $v$ ,

$$
\lim_{\omega\to0^+}\frac{1}{\omega}\,v^\dagger \Im \boldsymbol\chi^R(\omega,0)\,v\ \ge\ 0.
$$

_Proof._ Passivity:  $\int J\cdot \dot X\,dt\ge 0$  for  $X=\boldsymbol\chi^R * J$ . Choose  $J(t)=\Re\{v\,e^{-i\omega t}\,\eta(t)\}$  with a smooth window  $\eta\to1$ ; send the window to 1 after taking  $\omega\to0^+$ . Fourier algebra gives the inequality. □

### Lemma 9.4 (Corridor necessity)

For  $\chi^R=( -(\omega+i0)^2+\mathbf k^2+m^2)^{-1}$ ,

$$
\lim_{\omega\to0^+}\lim_{\mathbf k\to0}\frac{\Im\chi^R}{\omega}=\frac{\pi}{2m}\neq \lim_{\mathbf k\to0}\lim_{\omega\to0^+}\frac{\Im\chi^R}{\omega}=0.
$$

_Proof._ Use  $\Im(1/(x+i0))=-\pi\delta(x)$  and take limits carefully. □

### Lemma 9.5 (Schur complement preserves DC positivity)

If  $\Im \boldsymbol\chi^R/\omega\succeq 0$  and  $\chi_{BB}$  is invertible,

$$
\frac{1}{\omega}\,\Im\big(\chi_{AA}-\chi_{AB}\chi_{BB}^{-1}\chi_{BA}\big)\ \succeq\ 0.
$$

_Proof._ Write  $\Im \boldsymbol\chi^R/\omega$  as a Hermitian PSD block matrix; PSD ⇒ PSD Schur complement. □

* * *

##### 4.9.2.9.13 What MDPC secures for every computation that follows
---------------------------------------------------------

*   **Causal support** (luminal _fronts_, subluminal _groups_) established from principal symbols/Hadamard form.
*   **Well-posedness** via energy estimates; constraints propagate; domain of dependence is physical.
*   **Retarded responses** analytic in  $\Im\omega>0$ ; **Herglotz/K–K** structure pins low-frequency behavior.
*   A strict **DC corridor** that forbids false negatives/positives in passivity tests.
*   **Matrix positivity** that survives block reduction (Schur), ensuring effective descriptions don’t smuggle in activity.
*   **Boundary radiation** and uniqueness locked by Sommerfeld/Rellich, with all method differences transparently posted to the **ledger**.

_With MDPC in hand, every solve downstream—static, pulsed, mixed, or boundary-driven—arrives with a stamped health card: cone-respecting, energy-controlled, and dispersion-honest._

### 4.9.3 Connectivity Map
**Within Chapter 4 (closely related):**
- §4.11 — Spectral standardization — the Miller Transform (MT)
- §4.12 — Sanity limits & effective descriptions
- §4.14 — Health, gauge-slice independence, and audits

**External chapters (C#):**
- C0 §0.8–0.9 & §0.14
- C5 §5.36–5.47
- C1 §1.7

---

## 4.10 Table of Contents and Introduction

### 4.10.1 Table of Contents (Section 4.10)
- 4.10.2 Boundary, uniqueness, topology & ledgers (MBLC + MLCP)
- 4.10.3 Connectivity Map

### 4.10.2 Boundary, uniqueness, topology & ledgers (MBLC + MLCP)
_See also:_ §4.4, §4.5, §4.7, §4.9; C3 §3.14, §3.37, §3.45, C0 §0.12

10\. Boundary, uniqueness, topology & ledgers (MBLC + MLCP)
==============================================================================

> **What this section presents.** A complete framework that makes edge behavior mathematically clean, solutions unique, and global integers explicit—while **never** altering bulk dynamics. We build two pillars:
> 
> *   **MBLC (Boundary–Ledger Corridor):** declare boundary conditions **before** varying; derive the precise surface terms; show method-independence and radiation uniqueness; and formalize how every integration-by-parts (IBP) or “improvement” is posted, line by line, to a **ledger** as surface flux or integer data.
> *   **MLCP (Ledger–Ceiling Principle):** track topology (Pontryagin, Chern–Simons with explicit coupling normalization, Nieh–Yan/Holst, flux quanta) as ledger-only; implement the **duality guard** so we propagate exactly one representative when dual descriptions exist; and prove Wick invariance of the recorded integers.
>     
> 
> We proceed from picture → functional setup → variation and BC menus → uniqueness/radiation → method-independence → DtN/Calderón maps → quasilocal/ADM energy posting → topology and duality → worked templates → lemmas and short proofs. Everything here is forward-only; nothing from earlier chapters is repeated.

* * *

In speaking of fields one must first speak of their boundary. The differential equations do not determine a single world by themselves; it is the condition at the boundary that selects the physical one. If the outgoing condition is chosen, the radiating solution is unique; any other construction that respects the same condition yields the same interior field, for their difference would carry no power to infinity. Rearrangements of the formulas by integration—useful for calculation—change only the surface term and never the interior law; such terms belong to a ledger at the boundary and account for the exchange of energy with the exterior. The topology of the region, expressed by integer indices, also resides in this ledger: it classifies the global arrangement but does not add forces to the local dynamics. Where two descriptions are mathematically equivalent, one should not count both; a single representative together with the boundary record suffices. In this way the theory keeps faith with causality and conservation: the geometry restricts what may propagate, the boundary fixes what does, and the ledger preserves the equality between what leaves and what remains.

##### 4.10.2.10.1 Orientation: edges, receipts, and how the ledger keeps us honest
---------------------------------------------------------------------

**Plain picture.** Think of the bulk calculus as your **cart** and the boundary as the **cashier**. You can rearrange items inside the cart (IBP, basis changes) or place some on the counter (boundary terms); the **total** you pay doesn’t change, but the **receipt** does. The **ledger** is that receipt: every surface flux and integer sits there, separated from bulk dynamics.

**Working rule.** _Declare BCs first; vary second._ If BCs are not fixed at the outset, the variational derivative is not a map into field equations—it’s a distribution with unposted surface pieces. MBLC enforces the correct order: BCs → compensators → variation → field equations + clean boundary posts.

* * *

##### 4.10.2.10.2 Functional stage: trace spaces and what it means to “fix the boundary”
---------------------------------------------------------------------------

The boundary menus we use are not slogans; they are theorems about traces.

*   **Scalars.**  $\phi\in H^1(\Omega)$  admits the trace  $\gamma\phi=\phi|_{\partial\Omega}\in H^{1/2}(\partial\Omega)$  and a normal-derivative trace in  $H^{-1/2}(\partial\Omega)$  once the PDE is imposed. Dirichlet, Neumann, and Robin BCs are thus well-defined as constraints on  $H^{1/2}$  and  $H^{-1/2}$  data.
*   **One-forms (vectors).** The right spaces are  $H(\mathrm{curl};\Omega)=\{V\in L^2: \nabla\times V\in L^2\}$  and  $H(\mathrm{div};\Omega)=\{V\in L^2: \nabla\!\cdot V\in L^2\}$ . Tangential and normal traces,
    $$
    \gamma_t V=(n\times V)|_{\partial\Omega}\in H^{-1/2}(\mathrm{div}_{\partial\Omega}),\quad \gamma_n V=(n\!\cdot V)|_{\partial\Omega}\in H^{-1/2}(\partial\Omega),
    $$
    are continuous maps. This is what makes “fix tangential field” or “fix normal flux” _mathematical statements_ rather than wishes.
*   **Tensors.** For YM or symmetric tensors in divergence form, the boundary operator appearing in Green–Betti identities is of the tangential/normal-flux type; we treat it via surface differential forms and the induced metric  $h$ .

**Takeaway.** We can talk about Dirichlet/Neumann/Robin/Sommerfeld BCs with complete functional precision, and the compensator terms that make variations well-posed are not ad hoc—they are dictated by these trace theorems.

* * *

##### 4.10.2.10.3 Variational calculus with BC menus (sector by sector)
----------------------------------------------------------

We write **only** the boundary contributions from the variation and the compatible menus; bulk EOM are assumed known already.

### 10.2.1 Scalar  $\phi$ 

From

$$
S_\phi=\int_\Omega\!\sqrt{|g|}\,\Big(-\tfrac12(\nabla\phi)^2 - V(\phi)\Big),
$$

integration by parts yields

$$
\delta S_\phi=\int_\Omega\!\sqrt{|g|}\,(\Box\phi-V'(\phi))\,\delta\phi\ +\ \underbrace{\int_{\partial\Omega}\!\sqrt{|h|}\;(n\!\cdot\nabla\phi)\,\delta\phi}_{\text{surface}}.
$$

**BC menus (choose one):**

*   **Dirichlet:**  $\gamma\phi=f$ . Variation vanishes on  $\partial\Omega$ ; no compensator needed.
*   **Neumann:**  $\gamma_n(\nabla\phi)=g$ . Add surface compensator  $S_\partial=-\int_{\partial\Omega}\!\sqrt{|h|}\,\phi\,n\!\cdot\!\nabla\phi$  so that  $\delta S_\phi+\delta S_\partial$  has no free  $\delta\phi$  on  $\partial\Omega$ .
*   **Robin:**  $a\,\gamma\phi+b\,\gamma_n(\nabla\phi)=r$ . Add  $S_\partial=-\tfrac12\!\int_{\partial\Omega}\!\sqrt{|h|}\,(a\phi^2 + 2b\,\phi\,n\!\cdot\!\nabla\phi)$  to enforce the linear relation.
*   **Sommerfeld (radiative):**  $(\partial_t+\partial_r)\phi=0$  asymptotically (or its geometric avatar). No compensator; uniqueness follows from Rellich (§10.4).

### 10.2.2 Yang–Mills  $A_\mu$  (boundary form)

With  $\mathrm{Tr}(F^2)$  convention,

$$
\delta S_{\rm YM}=-\int_\Omega\!\sqrt{|g|}\,\mathrm{Tr}(D_\mu F^{\mu\nu}\,\delta A_\nu) + \underbrace{\int_{\partial\Omega}\!\sqrt{|h|}\,\mathrm{Tr}(n_\mu F^{\mu\nu}\,\delta A_\nu)}_{\text{surface}}.
$$

**BC menus:**

*   **Dirichlet-type:** fix  $\gamma_t A$  (gauge-invariant tangential representative). Works with a gauge that keeps  $A$  tangential data invariant.
*   **Neumann-type:** fix normal flux  $\gamma_n(F)^\nu=n_\mu F^{\mu\nu}$ . Add the standard flux compensator to kill the surface term.
*   **Sommerfeld:** outgoing radiation for asymptotic problems; uniqueness by Rellich.

These menus are compatible with gauge covariance of **data** (not necessarily of  $A$  itself), and the compensator terms keep the variation stationary.

### 10.2.3 Axial torsion  $S_\mu$  (Proca-type 1-form)

With  $H_{\mu\nu}=\nabla_\mu S_\nu-\nabla_\nu S_\mu$ ,

$$
\delta S_S=\int_\Omega\!\sqrt{|g|}\,(\nabla_\nu H^{\nu\mu}+m_S^2 S^\mu-g_S J_5^\mu)\,\delta S_\mu +\ \underbrace{\int_{\partial\Omega}\!\sqrt{|h|}\,n_\nu H^{\nu\mu}\,\delta S_\mu}_{\text{surface}}.
$$

**BC menus:**

*   **Dirichlet-type:** fix  $\gamma_t S$  (tangential components).
*   **Neumann-type:** fix  $\gamma_n(H)^\mu=n_\nu H^{\nu\mu}$  and add its compensator.
*   **Sommerfeld:** outgoing wave for the transverse (propagating) piece; longitudinal is algebraic and needs no independent BC.

### 10.2.4 Metric  $g_{\mu\nu}$  (Dirichlet on induced metric)

The Einstein–Hilbert variation produces a boundary piece exactly canceled by **GHY** for Dirichlet metric data,

$$
S_{\rm GHY}=\frac{1}{8\pi G}\int_{\partial\Omega}\!\sqrt{|h|}\,K,
$$

so metric variations are well-posed. This is the unique boundary partner for Dirichlet  $h_{ij}$ ; at finite walls one can switch to Brown–York quasilocal energy with the same pairing logic.

* * *

##### 4.10.2.10.4 Uniqueness for radiating problems (Rellich) and why Sommerfeld is sufficient
---------------------------------------------------------------------------------

**Sommerfeld condition (flat, large  $r$ ).**

$$
(\partial_r+\partial_t)\Psi = o(r^{-1})\quad\text{as } r\to\infty,
$$

for the radiating degree(s)  $\Psi$ . The precise tensorial generalization uses the physical transverse content.

**Rellich lemma (content for second-order radiators).** If a solution of the homogeneous problem satisfies the Sommerfeld condition and carries **zero** net flux through spheres at infinity, it is identically zero. Therefore, the radiative solution is **unique**.

**Curved version (local).** In asymptotically simple spacetimes, replace  $\partial_r+\partial_t$  by the null–geodesic transport on the conformal boundary. The same uniqueness holds in the outgoing sector.

**Consequences.** Once the BC is fixed, different constructive methods (free-space + homogeneous completion, method of images, boundary integrals) cannot disagree on the **bulk** solution—any difference is a redistribution of boundary posts (ledger).

* * *

##### 4.10.2.10.5 Method-independence by Green–Betti reciprocity
---------------------------------------------------

For linear, second-order systems  $\mathcal L u=f$ , the Green–Betti identity reads

$$
\int_\Omega\! (u\,\mathcal L v - v\,\mathcal L u) =\int_{\partial\Omega}\! \big(u\,\mathcal B v - v\,\mathcal B u\big),
$$

where  $\mathcal B$  is the boundary flux operator (e.g., normal derivative for scalars,  $n\!\cdot\!F$  for YM,  $n\!\cdot\!H$  for Proca). Take  $u$  and  $v$  as two solutions constructed by different methods but obeying **the same BCs**. The RHS vanishes; the LHS implies  $\mathcal L(u-v)=0$ . By Rellich (for outgoing) or Lax–Milgram (for elliptic static),  $u-v=0$  in the bulk. Any residual difference is a boundary superpotential—posted in the ledger.

**Practical meaning.** You are free to choose the most convenient construction—no physical statement hangs on that choice as long as BCs are identical.

* * *

##### 4.10.2.10.6 Dirichlet↔Neumann maps and Calderón projectors (boundary as an operator)
-----------------------------------------------------------------------------

**Dirichlet-to-Neumann (DtN).** Fix boundary data  $d=\gamma u$ . Solve  $\mathcal L u=f$  and return the flux  $n=\mathcal B u$ . The map  $\Lambda: d\mapsto n$  is elliptic/Fredholm for our classes of problems (with the appropriate function spaces). Its inverse (NtD) exists modulo finite-dimensional harmonic kernels (which are ledger entries).

**Calderón projector.** The pair  $(d,n)$  must lie on a constraint subspace: the Calderón projector  $C$  extracts the admissible traces of a solution. Impedance (Robin) BCs are precisely **graphs** of DtN (or NtD) with a positive real part—useful for proving boundary passivity and energy balance.

**Quasilocal energy.** For gravity, the Brown–York quasilocal stress tensor yields a boundary energy that is a functional of  $h_{ij}$  and its DtN data (extrinsic curvature). Its difference from ADM at infinity is a **ledger equivalence**: same physics, different post.

* * *

##### 4.10.2.10.7 Posting rules: IBP/improvements and energy balance are ledger-only moves
-----------------------------------------------------------------------------

**IBP/improvement.** If you change a bulk Lagrangian by a divergence,

$$
\mathcal L\to \mathcal L + \nabla_\mu W^\mu,
$$

the action changes by a surface term

$$
S\to S+\int_{\partial\Omega}\!\sqrt{|h|}\,n_\mu W^\mu.
$$

Field equations—and hence bulk physics—are unchanged. Only the **ledger** (surface post) moves.

**Slice energy and flux.** On a Cauchy slice  $\Sigma_t$ ,

$$
\frac{d}{dt}\int_{\Sigma_t}\! N\sqrt{h}\,T^{0}{}_{0} = -\oint_{\partial\Sigma_t}\!\text{(Poynting-like)}\cdot d\mathbf a\ +\ \int_{\Sigma_t}\! J\cdot \dot X.
$$

The _gravitational_ boundary energy is **not** in this flux; it is the ADM/Brown–York “rim coin,” posted once in the ledger and added to the bulk jar in the energy identity.

**Method differences.** Free-space + homogeneous vs images vs boundary-integral rearranges the flux **between** boundary panels; the **bulk** field and the **total** energy stay fixed. The ledger records the partition explicitly.

* * *

##### 4.10.2.10.8 MLCP: integers, dualities, and the ceiling on what can (and cannot) move
-----------------------------------------------------------------------------

**Principle.** In  $4$ D,  $p\!\ge\!3$  forms carry **no local propagating DOF**. Treat them as **ledger-only**: track their flux integers; never replace bulk kinetics with them. When dualities exist, propagate **one** representative and enforce the relation; do not double count.

### 10.7.1 Integer classes with explicit coupling normalization

*   **Pontryagin (gauge):**
    $$
    \nu_G=\frac{1}{8\pi^2}\int_{\mathcal M}\mathrm{Tr}(F\wedge F)\in \mathbb Z.
    $$
*   **Chern–Simons on a 3-manifold.** Write  $\mathcal A\equiv g A$ . Then
    $$
    S_{CS}=\frac{k}{4\pi g^2}\int_{\partial\mathcal M}\!\mathrm{Tr}\Big(\mathcal A\wedge d\mathcal A+\tfrac{2}{3}\mathcal A\wedge\mathcal A\wedge\mathcal A\Big),\quad k\in\mathbb Z,
    $$
    so the **level  $k$ ** remains manifestly integer regardless of the coupling convention.
*   **Nieh–Yan/Holst (torsion/gravity).** Built from torsion and curvature; integer-valued on closed manifolds; in our policy they are **ledger-only** (do not replace bulk kinetics).

**Wick invariance.** These integers are independent of the Lorentzian/Euclidean choice; they do not enter positivity audits nor modify principal symbols.

### 10.7.2 Duality guard: one field propagates; the other is a constraint

For a 2-form  $B$  with  $H=dB$  and a pseudoscalar  $\theta$  with  $H=*d\theta$ ,

$$
S_{\rm guard}=\int_{\mathcal M}\Lambda\wedge(H - *d\theta),
$$

enforces the identity. Choose to **propagate  $\theta$ **, eliminate  $B$  via the constraint, and leave  $\int H$  as a **ledger integer**.

**Why it matters.** Letting both propagate creates two copies of the same physics and double counts energy. Guarding the duality keeps the jar honest and the MET identity intact.

### 10.7.3 Relative cohomology and boundaries

On  $(\mathcal M,\partial\mathcal M)$ , relative classes  $[F]\in H^2(\mathcal M,\partial\mathcal M)$  naturally pair with boundary cycles; flux quantization  $\int_{S^2}F=2\pi n$  splits between interior and boundary per Stokes:

$$
\int_{\Sigma} dA=\int_{\partial\Sigma} A.
$$

The right-hand side is a **boundary** posting; the integer sits in the ledger.

### 10.7.4 Structural caveats (recorded, not propagated)

Freed–Witten constraints, Spin $^c$  requirements, or similar bundle restrictions needed to couple fermions are **metadata** in the ledger. They do not replace any bulk kinetic term in UGFT.

* * *

##### 4.10.2.10.9 Worked templates (boundary + topology patterns you can reuse)
------------------------------------------------------------------

### Template A — Finite cavity for  $S_\mu$  (Neumann walls, no radiation)

*   **BC:**  $n_\nu H^{\nu\mu}=0$  on  $\partial\Omega$ .
*   **Solve:** Helmholtz on the transverse subspace with homogeneous completion to match zero flux. Uniqueness is immediate (no outgoing channel).
*   **Energy:** entirely in the **jar**; ledger shows zero surface power.

### Template B — Interface with impedance (Robin)

*   **BC:**  $(n\!\cdot\!H)+\alpha\,(n\times S)=0$  (a DtN graph).
*   **Solve:** assemble DtN on each side and match via a Calderón projector.
*   **Ledger:** the interface posts a surface power term  $P_{\rm surf}=\int (n\!\cdot\!H)\cdot S_t$ , recorded explicitly; the **bulk** is identical across methods.

### Template C — Asymptotic radiation

*   **BC:** Sommerfeld for the radiating channel(s).
*   **Solve:** retarded kernel; uniqueness via Rellich.
*   **Ledger:** jar decreases at the rate of radiated power; gravitational rim coin (ADM/Bondi) is posted separately and added to the total per MET.

### Template D — 2-form ↔ axion dualization with guard

*   **Guard:** add  $\Lambda\wedge(H-*d\theta)$ .
*   **Propagate:**  $\theta$  only.
*   **Eliminate:**  $H=*d\theta$ , keep  $\int H$  as integer.
*   **Ledger:** integer recorded; no bulk kinetic replaced; Wick invariant.

* * *

##### 4.10.2.10.10 Lemmas and short proofs (load-bearing and reusable)
--------------------------------------------------------

**Lemma 10.1 (Method-independence).**  
_Statement._ Two solutions constructed by different methods but obeying identical BCs coincide in the **bulk**.  
_Proof._ Use Green–Betti with identical BCs to show the difference solves the homogeneous problem with zero boundary data; by Rellich/Lax–Milgram, the difference is zero. □

**Lemma 10.2 (Rellich uniqueness for radiators).**  
_Statement._ Under Sommerfeld BC, a homogeneous radiating solution with zero far-field flux is zero.  
_Sketch._ Multiply the equation by the complex conjugate, integrate over a large sphere, use the Sommerfeld condition to show the boundary integral is non-negative and vanishes only for the trivial field. □

**Lemma 10.3 (IBP/improvement ⇒ ledger post).**  
_Statement._  $\mathcal L\mapsto \mathcal L+\nabla\!\cdot W$  changes  $S$  by  $\int_{\partial\mathcal M}\sqrt{|h|}\,n\!\cdot\!W$ ; bulk EOM are unchanged. □

**Lemma 10.4 (Duality guard avoids double counting).**  
_Statement._ With  $S_{\rm guard}=\int \Lambda\wedge(H-*d\theta)$  and  $\theta$  chosen as the propagating field, the solution space modulo constraint equals that of  $\theta$  alone; energies match; any difference is a boundary 3-form (ledger). □

**Lemma 10.5 (Wick invariance of integers).**  
_Statement._ Characteristic-class integrals (Pontryagin, CS with integer level, Nieh–Yan) are invariant under Wick rotation; they do not enter positivity checks nor change bulk EOM. □

* * *

##### 4.10.2.10.11 Numerical posture (edges that compute like the math)
----------------------------------------------------------

*   **Trace-conforming spaces.** Use  $H^1$  (scalars) and  $H(\mathrm{curl})/H(\mathrm{div})$  (vectors) so tangential/normal traces exist _exactly_. This makes Dirichlet/Neumann/Robin menus exact in code—no hidden “penalty” physics.
*   **DtN/NtD assembly.** Form boundary operators with boundary element or hybridized FEM; implement the Calderón projector directly to enforce method-independence.
*   **Radiation honesty.** Prefer Sommerfeld or exact non-reflecting BCs; if using PML, treat its loss as a **ledger sink** (not bulk dissipation) and keep it separate in energy accounting.
*   **Ledger table.** Print a run-time “receipt” listing each boundary piece: which operator, which panel, what flux/integer. This makes the MET book-keeping one glance away.

* * *

##### 4.10.2.10.12 What MBLC + MLCP lock down for the rest of the chapter
------------------------------------------------------------

*   **Variations are functions,** not leaky distributions: edges declared; compensators in place; surface terms visible and posted.
*   **Uniqueness by design:** Green–Betti + Rellich make constructive method choices invisible to the bulk; only the ledger can differ—and it tells you _how_.
*   **One accounting line:** IBP/improvements move only the surface post; the **sum** (bulk jar + gravitational rim) is invariant.
*   **Topology handled once,** forever: integers logged as integers, dualities guarded so only one representative propagates, Wick-invariant and never masquerading as dynamics.
*   **Numerics that mirror analysis:** functional traces honored, DtN maps available, radiation honest, and the ledger printed as a receipt.

_From here, every edge and integer in the remaining derivations is already domesticated. The cart holds the bulk dynamics; the cashier prints the boundary receipt; the total you pay—the physical content—never depends on how you rearranged items before checkout._

### 4.10.3 Connectivity Map
**Within Chapter 4 (closely related):**
- §4.4 — UGFT action (bulk, boundary, topology) and the MGSP1 policy
- §4.5 — Miller Field Equation Set (MFES) — full classical system
- §4.7 — The Miller Equivalence Theorem (MET) — statement & proof sketch
- §4.9 — Causality, hyperbolicity, response & dispersion (MDPC)

**External chapters (C#):**
- C3 §3.14, §3.37, §3.45
- C0 §0.12

---

## 4.11 Table of Contents and Introduction

### 4.11.1 Table of Contents (Section 4.11)
- 4.11.2 Spectral standardization — the Miller Transform (MT)
- 4.11.3 Connectivity Map

### 4.11.2 Spectral standardization — the Miller Transform (MT)
_See also:_ §4.8, §4.9, §4.12, §4.14; C5 §5.34–5.37, C0 §0.8

11\. Spectral standardization — the Miller Transform (MT)
============================================================================

> **What this section presents.** A single, rigorous spectral “grammar” that every later calculation obeys—analytical and numerical—so constants, signs, and limits never drift. We start with intuitive stakes (why a single ruler matters) and then build the **continuous** pair (MT-c), the **discrete** pair (MT-d), and a **single-shot** estimator (MT-1S). We prove how causality appears as analyticity (**retarded** shift), why Parseval/Plancherel is exact (unitarity), how derivatives and projectors become clean multipliers, how DC/IR limits are taken (the **corridor**), and how to measure them in practice (windows, leakage, error bars). Every identity below is chosen so you can carry it straight to the blackboard or into code.

A physical law should not depend on our manner of description; a fixed spectral chart secures this. The Miller Transform provides such a chart. With one phase rule and unitary normalization, differentiation in time and space becomes multiplication by (i\omega) and (-i\mathbf{k}), and the equality of energy in time and in frequency (Parseval) is exact rather than conventional. Causality is expressed by taking the boundary value from the upper half‑plane, (\omega!\to!\omega+i0^+); this is the analytic image of the light cone. The relations between real and imaginary parts of a response (Kramers–Kronig) then follow as a necessity. For slow processes one first suppresses spatial variation and only then lets the frequency tend to zero; reversing this order fabricates influences that cannot carry signals. With this chart, Green functions, boundary integrals, and numerical schemes write the same interior law. It adds nothing and removes nothing; it prevents ambiguity, so that what is conserved in nature is also conserved in our description.

* * *

##### 4.11.2.11.1 Why one spectral ruler is non-negotiable
---------------------------------------------

**Plain picture.** Two carpenters can both be precise and still disagree if their tape measures are different. In spectral work a hidden  $2\pi$  or sign flip in the exponential is that mismatched tape. Fixing the “ruler” once—and never touching it again—means every stress, kernel, residue, and DC slope computed by different people matches digit-for-digit.

**Design goals.**

1.  **Unitary** transforms (no energy scaling creep).
2.  **Phase**  $e^{\,i(\omega t-\mathbf k\!\cdot\!\mathbf x)}$  so  $\partial_t\!\to\!i\omega$  and  $\nabla\!\to\!-i\mathbf k$ .
3.  **Retarded** shift  $\omega\!\to\!\omega+i0^+$  built in, so causality/MDPC is automatic.
4.  **Matrix-friendly** conventions (projectors, Schur complements, Cholesky) act algebraically.
5.  **Discrete harmony:** DFT equals the continuous transform on-grid; a **single-shot** probe reads any off-grid  $\Omega$  consistently.

* * *

##### 4.11.2.11.2 MT-c (continuous, unitary) and the consequences you use every day
----------------------------------------------------------------------

**Definition (time).**

$$
\boxed{ \tilde f(\omega)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\!dt\ e^{+i\omega t}\,f(t),\qquad f(t)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\!d\omega\ e^{-i\omega t}\,\tilde f(\omega). }
$$

**Space–time (3+1).**

$$
\boxed{ \tilde f(\omega,\mathbf k)=\frac{1}{(2\pi)^{2}}\!\int dt\,d^3x\ e^{\,i(\omega t-\mathbf k\cdot\mathbf x)}\, f(t,\mathbf x),\ f=\frac{1}{(2\pi)^{2}}\!\int d\omega\,d^3k\ e^{-i(\omega t-\mathbf k\cdot\mathbf x)}\, \tilde f. }
$$

**Immediate payoffs.**

*   **Plancherel/Parseval (exact):**  
     $\displaystyle \int |f|^2=\int |\tilde f|^2$  (time) and  $\displaystyle \int |f|^2=\int |\tilde f|^2$  (space–time), with no stray factors.
*   **Derivative dictionary:**  
     $\partial_t \leftrightarrow i\omega,\ \nabla \leftrightarrow -i\mathbf k,\ \Box \leftrightarrow (-\omega^2+\mathbf k^2)$ .
*   **Convolution/product:** a convolution in  $t$  (or in  $x$ ) becomes pointwise multiplication, times the same MT-c scale, so you never juggle inconsistent  $2\pi$  factors.

**Retarded prescription = analyticity.**  
Causality (support only for  $t\ge 0$ ) is the statement “ $\tilde f$  extends analytically to  $\Im\omega>0$  and is the boundary value from above.” We encode this by **always** reading

$$
G^R(\omega,\mathbf k)=G(\omega+i0^+,\mathbf k)
$$

and using Sokhotski–Plemelj:

$$
\frac{1}{x\pm i0^+}=\mathcal P\!\big(\tfrac{1}{x}\big)\mp i\pi\,\delta(x).
$$

This identity underwrites Kramers–Kronig, the Herglotz slope, and every “no pre-echo” conclusion in MDPC.

**Static kernels (with the right constants).** For  $r=|\mathbf r|$ ,

$$
\int \frac{d^3k}{(2\pi)^3}\,\frac{e^{\,i\mathbf k\cdot\mathbf r}}{\mathbf k^2+m^2}=\frac{e^{-m r}}{4\pi r},\qquad \int \frac{d^3k}{(2\pi)^3}\,\frac{e^{\,i\mathbf k\cdot\mathbf r}}{\mathbf k^2}=\frac{1}{4\pi r}.
$$

These two identities guarantee that every screened/unscreened inversion you perform elsewhere reproduces the Yukawa/Coulomb kernels with **no** “mystery constants.”

* * *

##### 4.11.2.11.3 Causality as Hardy-space analyticity (why the retarded shift is right)
---------------------------------------------------------------------------

**Layman step.** “No effect before the cause” means the impulse response  $h(t)$  vanishes for  $t<0$ . The Fourier transform of such a function is the boundary trace of something analytic above the real axis. That analytic continuation is the **retarded** Green/susceptibility.

**Expert step.** The Paley–Wiener/Hardy theorem:  $h\in L^2(\mathbb R)$  with  $\operatorname{supp}h\subseteq[0,\infty)$  iff its transform is the non-tangential boundary value of a function in the Hardy space  $H^2(\mathbb C_+)$ . The MT-c normalization keeps this correspondence unitary:

$$
\|h\|_{L^2}=\|\tilde h\|_{L^2}=\|\tilde h\|_{H^2(\mathbb C_+)}.
$$

Consequently, the _only_ consistent way to read causal responses is by  $\omega\!\to\!\omega+i0^+$ . Any “principal-value only” shortcut erases dissipation and breaks passivity checks.

* * *

##### 4.11.2.11.4 MT-d (discrete, unitary): how to keep numerics honest
----------------------------------------------------------

**DFT pair (unitary).** For  $t_n=n\Delta t$  and  $\omega_k=\frac{2\pi}{N\Delta t}k$ ,

$$
\boxed{ \tilde f_k=\frac{1}{\sqrt{N}}\sum_{n=0}^{N-1} e^{+i\frac{2\pi kn}{N}} f_n,\qquad f_n=\frac{1}{\sqrt{N}}\sum_{k=0}^{N-1} e^{-i\frac{2\pi kn}{N}} \tilde f_k. }
$$

**Consequences.**

*   **Exact Parseval on the grid:**  $\sum_n|f_n|^2=\sum_k|\tilde f_k|^2.$ 
*   **Finite-difference symbols:** centered  $\partial_t$  has symbol  $\frac{i}{\Delta t}\sin(\omega\Delta t)$ ;  $-\partial_t^2$  has  $\frac{4}{\Delta t^2}\sin^2(\omega\Delta t/2)$ . CFL is read from these against the metric cone.
*   **Nyquist and aliasing:**  $\omega_{\max}=\pi/\Delta t$ ; everything above folds. Windows (below) mitigate leakage but never beat Nyquist.

**Windows and leakage (with calibration).** Use smooth windows  $w_n$  (Hann, Blackman–Harris, flat-top) and preserve unitarity: scale  $w_n$  so  $\sum_n w_n^2=N$ . Correct amplitude by the **coherent gain**  $G_c=\frac{1}{N}\sum_n w_n$ . Side-lobe roll-off  $O(\omega^{-p})$  determines how fast off-bin energy decays—pick  $p$  by the accuracy you need.

* * *

##### 4.11.2.11.5 MT-1S (single-shot): probe one  $\Omega$  without building a spectrum
--------------------------------------------------------------------------

**Why this exists.** Many corridor checks and admittance measurements need  $\tilde f(\Omega)$  at a _few_  $\Omega$  (often near  $0^+$ ). Rebuilding the entire DFT is unnecessary and adds leakage we then have to undo.

**Definition (time series).**

$$
\boxed{ \widetilde f_{\text{1S}}(\Omega)=\frac{\Delta t}{\sqrt{2\pi}}\sum_{n=0}^{N-1} w_n\, f_n\, e^{-i\Omega t_n}. }
$$
*   **On-grid:** if  $\Omega=\omega_k$  and  $w\equiv1$ , MT-1S equals MT-d exactly.
*   **Off-grid:** MT-1S is a Riemann approximation to MT-c; bias is  $O(N^{-2})$  for  $C^1$  windows and vanishes as  $N\to\infty$ .
*   **Near DC:** choose a frequency ladder  $\Omega_j\downarrow0^+$  and fit  $\Im\widetilde f_{\text{1S}}(\Omega_j)/\Omega_j$  to a constant +  $O(\Omega_j^2)$ . That constant is the Herglotz slope.

* * *

##### 4.11.2.11.6 Operators, projectors, and kernels in MT coordinates
---------------------------------------------------------

**Vector/tensor calculus (once, for all uses).**

$$
\partial_t\to i\omega,\quad \nabla\to -i\mathbf k,\quad \nabla\!\cdot\to -i\,\mathbf k\!\cdot,\quad \nabla\times\to +i\,\mathbf k\times .
$$

**Helmholtz projectors.**

$$
\Pi^{\mathrm L}(\mathbf k)=\frac{\mathbf k\mathbf k^\top}{\mathbf k^2},\qquad \Pi^{\mathrm T}(\mathbf k)=\mathbb 1-\Pi^{\mathrm L}(\mathbf k).
$$

They are orthogonal projectors with respect to the MT inner product; energy decomposes per channel without cross-terms.

**Scalar resolvents (Proca/Helmholtz).**

$$
(\Box+m^2)^{-1}\ \Longleftrightarrow\ \frac{1}{-(\omega+i0^+)^2+\mathbf k^2+m^2}.
$$

**Hankel shortcut (radial).**

$$
\int \frac{d^3k}{(2\pi)^3} e^{\,i\mathbf k\cdot\mathbf r} F(k) =\frac{1}{2\pi^2 r}\int_0^\infty dk\,k\,\sin(kr)\,F(k),
$$

a workhorse for spherically symmetric sources.

* * *

##### 4.11.2.11.7 Kramers–Kronig and Herglotz in this normalization (no hidden minus signs)
------------------------------------------------------------------------------

**Kubo/response in MT-c.** With a source  $J$  and readout  $X$ ,

$$
\tilde X(\omega)=\boldsymbol\chi^R(\omega)\,\tilde J(\omega),\qquad W=\int dt\,J\cdot \dot X =\int\frac{d\omega}{2\pi}\ i\omega\,\tilde J(-\omega)^\dagger \boldsymbol\chi^R(\omega)\tilde J(\omega).
$$

**Passivity ⇒ Herglotz.**  $W\ge 0$  for any real  $J$  forces

$$
\lim_{\omega\to0^+}\frac{1}{\omega}\,\Im \boldsymbol\chi^R(\omega,0)\ \succeq\ 0,
$$

exactly the matrix inequality we test in MDPC. (Scalar case: non-negative slope for  $\Im\chi^R/\omega$  at  $0^+$ .)

**Kramers–Kronig (subtracted).**

$$
\Re \chi^R(\omega)=\chi_\infty+\frac{2}{\pi}\,\mathcal P\!\int_0^\infty\! d\omega'\,\frac{\omega'\,\Im\chi^R(\omega')}{\omega'^2-\omega^2}.
$$

The  $\omega\to0^+$  slope matches the Herglotz inequality, so analytic dispersive structure and passivity line up in this convention.

* * *

##### 4.11.2.11.8 DC/IR corridor inside MT (and why reversing it lies)
---------------------------------------------------------

**Rule (never break it).** Evaluate  $\lim_{\omega\to0^+}\lim_{\mathbf k\to0}$ , not the reverse.

**Exhibit (scalar resolvent).**

$$
\chi^R(\omega,\mathbf k)=\frac{1}{-(\omega+i0^+)^2+\mathbf k^2+m^2}.
$$

Then

$$
\lim_{\omega\to0^+}\lim_{\mathbf k\to0}\frac{\Im \chi^R(\omega,\mathbf k)}{\omega}=\frac{\pi}{2m}\quad(\ge 0),
$$

but reversing limits yields  $0$ , erasing the spectral weight at threshold. For matrices this reversal can fabricate **negative** slopes (fake activity). MT-1S is built to respect the correct order in code.

**Regulators for massless channels.** Introduce  $m\to 0^+$ , execute the corridor, then remove  $m$ . This preserves Herglotz positivity and the right sum rules.

* * *

##### 4.11.2.11.9 Error-controlled numerics: windows, leakage, and slope estimation
----------------------------------------------------------------------

**Window math in two lines.** Let  $w_n$  be a real, even window with  $\sum_n w_n^2=N$ . The windowed DFT obeys Parseval exactly and modifies amplitudes by  $G_c$ . Side-lobes decay like  $O(\omega^{-p})$ . Choose  $p$  and record length  $N$  so the leakage error is below your tolerance at the nearest out-of-bin frequency.

**DC slope protocol (practical).**

1.  Keep  $\mathbf k=0$  (or the smallest grid mode).
2.  Compute  $\Im \chi^R_{\text{1S}}(\omega_j)/\omega_j$  at a monotone ladder  $\omega_j\downarrow0^+$ .
3.  Fit versus  $\omega_j^2$  and extrapolate to  $0^+$ .
4.  Quote two error bars: (i) the fit residual; (ii) the window-moment bound. If either is large, increase  $N$  or use a steeper window.

**CFL from the cone.** For time marching, derive the step from the principal symbol  $(-\,\omega^2+\mathbf k^2)$  and the maximum discrete group speed; adding ad-hoc damping to “stabilize” is a sign your BCs or corridor are wrong.

* * *

##### 4.11.2.11.10 Micro-workflows (ready cards)
----------------------------------

### MT-A — Retarded susceptibility from an impulse response

**Input:**  $h(t)$  for  $t\in[0,T]$ .  
**Compute:**  $\tilde\chi^R(\omega)=\tfrac{1}{\sqrt{2\pi}}\int_0^T e^{+i\omega t}\,w(t)h(t)\,dt.$   
**Stabilize:** subtract a linear polynomial in  $\omega$  and enforce K–K on the residual.  
**Check:** small- $\omega$  slope  $\Im\tilde\chi^R/\omega\ge0$ .

### MT-B — Static Yukawa field from a density

**Input:**  $J(\mathbf x)$  compact.  
**Compute (Fourier):**  $\tilde J(\mathbf k)=(2\pi)^{-3/2}\!\int e^{-i\mathbf k\cdot\mathbf x}J$ .  
**Invert:**  $S_0(\mathbf x)=g_S\int \frac{d^3k}{(2\pi)^3}\ \frac{e^{\,i\mathbf k\cdot\mathbf x}}{\mathbf k^2+m_S^2}\,\tilde J(\mathbf k)$ .  
**Result:**  $S_0=g_S\,G*J$  with  $G=e^{-m_S r}/(4\pi r)$ .

### MT-C — Mixed channels with canonicalization

**Input:** block kernel  $K(\omega,\mathbf k)=K^\dagger>0.$   
**Run:** Cholesky  $K=R^\dagger R$ , define  $\widehat X=RX$ , diagonalize per channel in  $(\omega,\mathbf k)$ , apply scalar resolvents, transform back.  
**Check:** residues  $\ge 0$ ;  $\Im\boldsymbol\chi^R/\omega\succeq0$  near  $0^+$ .

* * *

##### 4.11.2.11.11 Subtleties you’ll meet—and their antidotes
------------------------------------------------

*   **Hidden  $2\pi$  factors.** Antidote: never mix MT-c with a non-unitary DFT; MT-d is unitary and matches MT-c on-grid.
*   **Wrong exponential sign.** Antidote: verify  $\partial_t\to i\omega$  and  $\nabla\to -i\mathbf k$ . If this fails, your Kubo sign and Poynting directions will flip.
*   **Even transforms for causal kernels.** Antidote: never replace  $e^{i\omega t}$  with cosines; they lose phase and hide dissipation. Use retarded MT-c with  $+i0^+$ .
*   **DC order violation.** Antidote: measure with MT-1S on a frequency ladder at  $\mathbf k=0$ ; only after that refine  $\mathbf k\to0$ .
*   **Window bias.** Antidote: correct by coherent gain and, if measuring slopes, by the first window moment; quote the remaining bias as an error bar.

* * *

##### 4.11.2.11.12 Two compact proofs (load-bearing)
---------------------------------------

**Lemma 11.1 (Plancherel for MT-c).**  
The operator  $\mathcal F:f\mapsto \tilde f$  with the MT-c constants is unitary on  $L^2$ .  
_Proof sketch._ Compute  $ \langle \tilde f,\tilde g\rangle = \int \frac{d\omega}{2\pi}\int\! dt\,dt'\ e^{i\omega(t-t') } f(t)\overline{g(t')} = \int dt\, f(t)\overline{g(t)}$  using  $\int \frac{d\omega}{2\pi} e^{i\omega(t-t')}=\delta(t-t')$ . □

**Lemma 11.2 (Herglotz slope via passivity).**  
For causal  $\boldsymbol\chi^R$ ,  $\lim_{\omega\to0^+}\frac{1}{\omega}\Im\boldsymbol\chi^R(\omega,0)\succeq0$ .  
_Proof sketch._ For any real  $J$  with compact support,  $W=\int J\cdot\dot X\ge0$ . In frequency space (MT-c),  $W=\int \frac{d\omega}{2\pi} i\omega \tilde J^\dagger \boldsymbol\chi^R \tilde J$ . Take  $J$  narrowband near  $\omega$  and send  $\omega\to0^+$  with the retarded prescription; the inequality follows for all test vectors, hence matrix PSD. □

* * *

##### 4.11.2.11.13 What MT locks for the remainder
-------------------------------------

*   **One spectral ruler** across analysis and code; exact Parseval and fixed phase remove every “mysterious factor.”
*   **Causality baked in:** the retarded shift turns support in time into analyticity in  $\omega$ ; K–K and Herglotz become corollaries, not add-ons.
*   **Frictionless algebra:** derivatives, projectors, Schur complements, and per-spin decompositions are clean multipliers; residues read straight off.
*   **Honest DC:** the corridor is explicit and measurable (MT-1S ladder); massless regulators are orderly and removable.
*   **Reproducibility:** continuous ↔ discrete harmony; windowed estimates with controlled bias; error bars that mean something.

_With MT fixed, every spectral quantity that appears later—retarded kernels, per-channel residues, DC slopes, boundary admittances—lands on a common grid. There are no loose constants to chase, no sign caves to fall into, and no hidden limit swaps. The rest of the chapter can compute at speed and at depth in the same, shared language._

### 4.11.3 Connectivity Map
**Within Chapter 4 (closely related):**
- §4.8 — Equivalence-first computation (MEFP) and MPSD lanes
- §4.9 — Causality, hyperbolicity, response & dispersion (MDPC)
- §4.12 — Sanity limits & effective descriptions
- §4.14 — Health, gauge-slice independence, and audits

**External chapters (C#):**
- C5 §5.34–5.37
- C0 §0.8

---

## 4.12 Table of Contents and Introduction

### 4.12.1 Table of Contents (Section 4.12)
- 4.12.2 Sanity limits & effective descriptions
- 4.12.3 Connectivity Map

### 4.12.2 Sanity limits & effective descriptions
_See also:_ §4.4, §4.9, §4.10, §4.11, §4.14; C2 §25, C5 §5.33

12\. Sanity limits & effective descriptions
=================================================================

> **What this section presents.** A careful, execution-ready way to _simplify without lying_. We will (i) integrate out the short-range axial field  $S_\mu$  and obtain a **local**, **causal**, **positive** effective theory with **quantified errors**; (ii) derive the **quasi-static, spin-structured potential** in a form that exposes the tensor anatomy and contact piece; (iii) build a **low-frequency retarded constitutive law** that preserves the Herglotz/passivity inequalities order-by-order; (iv) cross the **ultra-light/IR** corner by obeying the order of limits; (v) show how **boundaries** survive elimination through a Dirichlet-to-Neumann (DtN) operator that lives in the ledger; and (vi) give **remainder bounds** and **drop-in cards** you can actually run. Nothing below repeats earlier sections; we take the tools and push them to their operational frontiers.

Every physical theory is only an approximation to a more complete picture, valid within a certain range of scales. When the details become too fine to observe, nature allows us to replace them by smoother laws without deceit. The heavy field that oscillates too rapidly may be removed, leaving behind a quiet influence—an effective term that still honors energy, causality, and the speed of light. What matters is that this reduction is carried out with respect for the order of cause and effect: one must eliminate the hidden motion without letting its echo run ahead of time. In this way the complicated network of interactions simplifies to a local description, yet the essential invariants—the fronts of propagation, the positive flow of energy, and the balance recorded at the boundaries—remain untouched. The art of physics is not in writing ever longer equations, but in knowing when a part of the system can be trusted to keep its own account while the larger world proceeds according to the same unbroken rules.

* * *

##### 4.12.2.12.1 What “effective” means here—and what it must never break
-------------------------------------------------------------

**Plain picture.** Step back from fine grain: keep only the silhouette that matters at your resolution. In mathematics: replace a nonlocal, wave-carrying field by a finite tower of **local operators** whose coefficients encode the forgotten micro-structure. Three invariants must survive:

1.  **Causality**: all kernels are **retarded**; no pre-echo.
2.  **Positivity**: quadratic energy and low-frequency dissipation remain **non-negative**.
3.  **Boundary honesty**: any surface term generated by IBP or elimination becomes a **ledger** post; bulk equations are not altered.

Everything below is designed so these invariants are visible at each step.

* * *

##### 4.12.2.12.2 Heavy-torsion regime (integrate out  $S_\mu$  without losing causality)
----------------------------------------------------------------------------

We integrate out  $S_\mu$  when  $|\partial|\ll m_S$ . The key is to expand the **retarded** resolvent, not a formal algebraic inverse, so causality is preserved by construction.

### 12.1.1 Retarded inversion, then the Neumann series (operator level)

Project to the physical channel and invert:

$$
S^\mu_\perp = g_S\,(\Box+m_S^2)^{-1}\,\Pi^{\mathrm T\,\mu}{}_{\nu}\,J_5^\nu,\qquad \Pi^{\mathrm T}=\mathbb 1-\frac{\nabla\nabla}{\Box}.
$$

For  $|\partial|\ll m_S$ ,

$$
(\Box+m_S^2)^{-1} =\frac{1}{m_S^2}\sum_{n=0}^{\infty}\!\left(-\frac{\Box}{m_S^2}\right)^{n},
$$

where each  $\Box$  acts **inside** a retarded convolution. Truncating at  $n=N$  leaves a **causal** law.

### 12.1.2 Local action by completing the square (classical tree matching)

At the quadratic level,

$$
\mathcal L_S=-\tfrac14 H^2+\tfrac12 m_S^2 S^2 - g_S S\!\cdot\!J_5 = -\tfrac14 H^2+\tfrac12 m_S^2\Big(S-\tfrac{g_S}{m_S^2}J_5\Big)^2 - \frac{g_S^2}{2m_S^2}J_5^2.
$$

Eliminating  $S$  (on shell) yields the _nonlocal_ functional

$$
\Delta S_{\rm eff}=-\frac{g_S^2}{2}\int J_{5\mu}\,(\Box+m_S^2)^{-1} \Pi^{\mathrm T\,\mu}{}_{\nu}\,J_5^\nu,
$$

whose **local** derivative expansion is

  $$
\boxed{\; \Delta\mathcal L_{\rm eff} =-\frac{g_S^2}{2m_S^2}\,J_{5}^2 -\frac{g_S^2}{2m_S^4}\,J_{5\mu}\,\Box J_5^\mu -\frac{g_S^2}{2m_S^6}\,J_{5\mu}\,\Box^2J_5^\mu +\cdots\ . \;}
$$

The first term is the axial contact; higher terms are derivative-suppressed and inherit **retarded** support from the parent resolvent.

### 12.1.3 Positivity and characteristics after truncation

*   **Positivity.** The exact kernel is positive (Proca energy). At small  $\omega$ ,  $\Im\chi^R(\omega,0)/\omega\ge 0$ . Expanding a **retarded** kernel preserves this inequality: every truncated constitutive law remains **passive**. The contact piece  $-\frac{g_S^2}{2m_S^2}J_5^2$  adds a non-negative contribution to the jar once  $S$  is eliminated.
*   **Characteristics.** The principal symbol of any finite truncation is that of  $\Box$ : the **light cone**. No superluminal front appears.

### 12.1.4 Quantified error

If  $|\omega|,|\mathbf k|\le \Lambda\ll m_S$ ,

$$
\Big\|S_\perp-\sum_{n=0}^{N}\frac{g_S}{m_S^{2+2n}}\Pi^{\mathrm T}(-\Box)^{n}J_5\Big\| \ \le\ C\left(\frac{\Lambda}{m_S}\right)^{2N+2}\frac{g_S}{m_S^2}\,\|J_5\|.
$$

Report  $\epsilon=\Lambda/m_S$  and the retained order  $2N$ .

**Ledger note.** Elimination generates a surface superpotential; post it to the ledger (bulk equations and energy identity are unchanged).

* * *

##### 4.12.2.12.3 Quasi-static spin physics (the tensor anatomy exposed)
-----------------------------------------------------------

Slow time dependence lets us read the shape of the interaction transparently. The cleanest route keeps the tensor projector explicit.

### 12.2.1 Exact momentum-space kernel with the transverse projector

For localized spin densities  $S^i_{1,2}$  and separation  $\mathbf r$ ,

  $$
\boxed{\; V(\mathbf r)=g_S^2\!\int\!\frac{d^3k}{(2\pi)^3}\ e^{i\mathbf k\cdot\mathbf r}\, \frac{\delta^{ij}-\dfrac{k^ik^j}{\mathbf k^2+m_S^2}}{\mathbf k^2+m_S^2}\ S_1^i S_2^j . \;}
$$

This integrand is the **transverse projector** divided by the massive denominator; it guarantees correct short- and long-distance limits without guessing.

### 12.2.2 Real-space derivative representation (exact and computable)

Use the identity  $\mathcal F^{-1}[k_ik_j f(\mathbf k)]=-\partial_i\partial_j\,\mathcal F^{-1}[f]$ . Let

$$
G(r)=\frac{e^{-m_S r}}{4\pi r},\qquad F(r)=\mathcal F^{-1}\!\left[\frac{1}{(\mathbf k^2+m_S^2)^2}\right]=\frac{e^{-m_S r}}{8\pi m_S}.
$$

Then

$$
\frac{\delta^{ij}}{\mathbf k^2+m_S^2}\ \mapsto\ \delta^{ij}\,G,\qquad \frac{k^ik^j}{(\mathbf k^2+m_S^2)^2}\ \mapsto\ -\,\partial_i\partial_j\,F,
$$

and

$$
V(\mathbf r)=g_S^2\Big[\ \delta^{ij}G(\mathbf r)\ +\ \partial_i\partial_j F(\mathbf r)\ \Big]\,S_1^i S_2^j.
$$

Compute  $\partial_i\partial_j$  in terms of radial derivatives:

$$
\partial_i\partial_j \Phi(r) =\Big(\delta_{ij}-\hat r_i\hat r_j\Big)\frac{\Phi'(r)}{r} +\hat r_i\hat r_j\,\Phi''(r).
$$

With  $F'=-\frac{e^{-m_S r}}{8\pi}$ ,  $F''=\frac{m_S e^{-m_S r}}{8\pi}$ , we obtain the closed form

  $$
\boxed{\; \begin{aligned} V(\mathbf r) &=\frac{g_S^2\,e^{-m_S r}}{4\pi}\bigg[ \underbrace{\frac{1}{r}}_{\text{isotropic}}\ (\mathbf S_1\!\cdot\!\mathbf S_2) +\underbrace{\Big(-\frac{1}{2}\frac{1}{r^3} -\frac{1}{2}\frac{m_S}{r^2}\Big)}_{\text{transverse}}\ \Big(\mathbf S_1\!\cdot\!\mathbf S_2 - (\mathbf S_1\!\cdot\!\hat{\mathbf r})(\mathbf S_2\!\cdot\!\hat{\mathbf r})\Big)\\[2pt] &\qquad\qquad\qquad +\underbrace{\frac{m_S}{8\pi}\,e^{-m_S r}\,\delta^{(3)}(\mathbf r)\ \times \text{(finite renorm.)}}_{\text{contact completion}} \bigg], \end{aligned} \;}
$$

which you can equivalently recast in the standard dipole tensor basis

$$
V(\mathbf r)=\frac{g_S^2 e^{-m_S r}}{4\pi r}\Big[ (\mathbf S_1\!\cdot\!\mathbf S_2)\,A(m_S r) +\big(3(\mathbf S_1\!\cdot\!\hat{\mathbf r})(\mathbf S_2\!\cdot\!\hat{\mathbf r})-\mathbf S_1\!\cdot\!\mathbf S_2\big)\,B(m_S r) \Big],
$$

with  $A,B$  smooth and **positive**, determined from the radial coefficients above; their far- and near-zone expansions are immediate:

$$
\begin{aligned} m_S r\gg1:&\quad A\to 1,\qquad B\sim \frac{1+m_S r}{(m_S r)^2},\\ m_S r\ll1:&\quad A\to1,\qquad B\to \frac{1}{r^2}\quad(\text{dipole}),\quad V_{\rm contact}\propto (\mathbf S_1\!\cdot\!\mathbf S_2)\,\delta^{(3)}(\mathbf r). \end{aligned}
$$

**Macroscopic averaging.** For unpolarized matter,  $\langle S^i\rangle=0$ ,  $\langle S^i S^j\rangle\propto\delta^{ij}$  so the tensor part averages away and the leading static force is suppressed. Polarized media (ferromagnets, spin-polarized gases, polarized beams) are the natural falsifiability arena.

* * *

##### 4.12.2.12.4 Low-frequency dynamics: a retarded, short-memory law
---------------------------------------------------------

Now let the drive be slow in time. The right object is a **retarded** constitutive relation with a finite number of derivatives, chosen so passivity survives order-by-order.

### 12.3.1 Start from the convolution everyone agrees on

$$
S^\mu_\perp(t,\mathbf x) =g_S\int dt'\,d^3x'\,G^R_{m_S}(t\!-\!t',\mathbf x\!-\!\mathbf x')\, \Pi^{\mathrm T\,\mu}{}_{\nu}J_5^\nu(t',\mathbf x').
$$

Expand under the integral using the **retarded** operator identity:

  $$
\boxed{\; S^\mu_\perp =\frac{g_S}{m_S^2}\,\Pi^{\mathrm T\,\mu}{}_{\nu}J_5^\nu -\frac{g_S}{m_S^4}\,\Pi^{\mathrm T\,\mu}{}_{\nu}(\partial_t^2-\nabla^2)J_5^\nu +\frac{g_S}{m_S^6}\,\Pi^{\mathrm T\,\mu}{}_{\nu}(\partial_t^2-\nabla^2)^2J_5^\nu +\cdots . \;}
$$

### 12.3.2 Passivity check in one line (Herglotz at  $\omega\to0^+$ )

For  $\mathbf k=0$ ,

$$
\tilde S^\mu_\perp = g_S\Big[\frac{1}{m_S^2}+\frac{\omega^2}{m_S^4}+\frac{\omega^4}{m_S^6}+\cdots\Big]\Pi^{\mathrm T\,\mu}{}_{\nu}\,\tilde J_5^\nu,
$$

so

$$
\lim_{\omega\to0^+}\frac{1}{\omega}\Im \chi^R(\omega,0)\ \ge\ 0
$$

holds term-by-term: the truncated law remains **passive**. The group speed is subluminal; the **front** remains luminal (principal symbol unchanged).

### 12.3.3 Band of validity and reporting

With  $\varepsilon\!=\!\max(|\omega|,|\mathbf k|)/m_S$ , truncation at  $2N$  derivatives has error  $O(\varepsilon^{2N+2})$ . Always report  $(N,\varepsilon)$ ; causality and positivity stay locked.

* * *

##### 4.12.2.12.5 Ultra-light/IR lane (how to pass through zero mass without ghosts)
-----------------------------------------------------------------------

The massless corner is honest only if you respect **both** the regulator and the **DC corridor**.

*   Keep  $m_S>0$  until you have taken  $\mathbf k\to0$  and then  $\omega\to0^+$ ; only **then** send  $m_S\to 0^+$ .
*   The static kernel goes  $e^{-m_S r}/(4\pi r)\to 1/(4\pi r)$ . The retarded kernel keeps causal support; the luminal front does not change.
*   Swapping any limit creates spurious negative slopes in  $\Im\chi^R/\omega$  and breaks passivity numerically; we forbid that.

* * *

##### 4.12.2.12.6 Near–far matching (multipoles with mass, no double counting)
-----------------------------------------------------------------

For a compact source of size  $R$  with slow time dependence, match _adiabatic_ near-zone solutions to _retarded Yukawa_ far-zone tails:

$$
S_0(t,\mathbf r)\ \sim\ \sum_{\ell=0}^\infty \frac{e^{-m_S r}}{r^{\ell+1}}\ \mathcal M_\ell(t-r;\,m_S),\qquad r\gg R,
$$

with  $\mathcal M_\ell$  the retarded multipole moments of  $J_5$ . Choose a matching radius  $r_\star$  with  $R\ll r_\star \ll m_S^{-1}+\lambda$  (time scale  $\lambda$ ); impose continuity of  $S$  and outward flux. No overlap, no gaps, no double counting.

* * *

##### 4.12.2.12.7 What doesn’t move in the gravitational sector
--------------------------------------------------

Eliminating  $S$  at low energies trades field energy for a **local contact** in the jar; the metric dynamics and the gravitational rim coin do not change. Axial backreaction is suppressed by

$$
\frac{E_S}{E_{\rm matter}}\ \sim\ \frac{g_S^2}{m_S^2}\,\frac{\langle J_5^2\rangle}{\rho c^2}\ \ll\ 1
$$

for unpolarized macroscopic matter. The energy identity (bulk jar + rim coin) remains exact.

* * *

##### 4.12.2.12.8 Boundaries after elimination: DtN appears (and lives in the ledger)
------------------------------------------------------------------------

Integrating out fields in bounded domains induces **boundary** operators. They do _not_ alter bulk equations; they change the **ledger**.

*   If  $S$  is eliminated, the induced boundary quadratic is
    $$
    S_{\partial,{\rm eff}} =\frac{g_S^2}{2}\int_{\partial\Omega}\!\! d\Sigma\,d\Sigma'\, J_{5a}(x)\,\Lambda^{ab}_{m_S}(x,x')\,J_{5b}(x'),
    $$
    where  $\Lambda$  is the DtN (Steklov-Poincaré) operator for  $(-\nabla^2+m_S^2)^{-1}$  restricted to  $\partial\Omega$ .  $\Lambda$  is **positive** and decays on the scale  $m_S^{-1}$ .
*   Solve-then-eliminate or eliminate-then-solve yield the _same bulk field_: Green–Betti reciprocity and Rellich uniqueness guarantee **method independence**; only the ledger line changes.

* * *

##### 4.12.2.12.9 Remainder bounds (you can quote them without apology)
----------------------------------------------------------

Let  $\Lambda$  bound the frequency–wavenumber support of  $J_5$ .

1.  **Local EFT (order  $2N$ )**:
    $$
    \big\|S_\perp - S_\perp^{(2N)}\big\|_{L^2(\Sigma)} \le C \left(\frac{\Lambda}{m_S}\right)^{2N+2}\frac{g_S}{m_S^2}\,\|J_5\|_{L^2(\Sigma)}.
    $$
2.  **Spin potential (supports of diameter  $R$ )**:
    $$
    \left|V(\mathbf r)-V_{\text{tensor Yukawa}}\right| \le \frac{g_S^2}{4\pi}\,e^{-m_S r}\,\frac{R^2}{r^3}\,C_{\rm ang},\qquad r\gg R.
    $$
3.  **Low- $\omega$  constitutive law (order  $2N$ )**:
    $$
    \|\tilde S_\perp - \tilde S_\perp^{(2N)}\| \le C' \left(\frac{|\omega|+|\mathbf k|}{m_S}\right)^{2N+2} \frac{g_S}{m_S^2}\,\|\tilde J_5\|.
    $$

Constants  $C,C',C_{\rm ang}$  depend on smoothness and geometry but **not** on  $m_S$ .

* * *

##### 4.12.2.12.10 Micro-workflows (drop-in cards)
------------------------------------

### Card 12-A — Local EFT through  $1/m_S^4$ 

**Given:**  $\Lambda\ll m_S$ .  
**Do:**  $S_\perp=\frac{g_S}{m_S^2}\Pi^{\mathrm T}J_5-\frac{g_S}{m_S^4}\Pi^{\mathrm T}\Box J_5$ .  
**Error:**  $\lesssim(\Lambda/m_S)^4\cdot (g_S/m_S^2)\|J_5\|$ .  
**Post:** add  $-\frac{g_S^2}{2m_S^2}J_5^2$  to the jar; move the superpotential to the ledger.

### Card 12-B — Spin–spin force between polarized bodies

**Given:** spins  $S_{1,2}(\mathbf x)$ , separation  $\mathbf r$ .  
**Do:** evaluate  $V(\mathbf r)$  via the projector integral; reduce with the  $\partial_i\partial_j F$  formula.  
**Asymptotics:** use far/near-zone expansions; include the contact piece if supports overlap.  
**Note:** for unpolarized ensembles the leading force averages out.

### Card 12-C — Slow-time admittance

**Given:**  $|\omega|\le\omega_\*\ll m_S$ .  
**Do:**  $S_\perp=\frac{g_S}{m_S^2}\Pi^{\mathrm T}\!\left(1-\frac{\partial_t^2}{m_S^2}+\cdots\right)J_5$ .  
**Check:**  $\Im \chi^R(\omega,0)/\omega\ge0$  as  $\omega\downarrow0$ ; report  $\varepsilon=\omega_\*/m_S$ .

### Card 12-D — Ultra-light regulator lane

**Do:** keep  $m_S>0$ , take  $\mathbf k\to0$  then  $\omega\to0^+$ , then  $m_S\to0^+$ .  
**Warn:** any other order falsifies passivity numerically.

### Card 12-E — Boundary-mediated interaction after elimination

**Given:** domain  $\Omega$ , Neumann wall for the axial sector.  
**Do:** assemble DtN  $\Lambda_{m_S}$ , compute  $S_{\partial,{\rm eff}}=\frac{g_S^2}{2}J_5\Lambda J_5$ .  
**Ledger:** post as boundary power; bulk equations unchanged.

* * *

##### 4.12.2.12.11 What you leave this section with
--------------------------------------

*   A **local, causal EFT** for heavy torsion: coefficients explicit; Herglotz/passivity and front speed preserved; **errors quantified**.
*   A **quasi-static tensor potential** with clear angular structure, contact completion, and near/far asymptotics—good enough to design falsifiability experiments.
*   A **retarded short-memory law** for slow dynamics whose DC slope stays **non-negative** order-by-order.
*   An **IR pathway** that honors the DC corridor and avoids spurious negatives when  $m_S$  is tiny.
*   A **boundary-aware** elimination procedure: DtN operators appear in the **ledger** only; bulk physics is invariant.
*   **Validity cards** and **remainder bounds** so you can tell any reader not just _what_ you threw away, but _how much_—with causality, positivity, and boundary honesty intact.

### 4.12.3 Connectivity Map
**Within Chapter 4 (closely related):**
- §4.4 — UGFT action (bulk, boundary, topology) and the MGSP1 policy
- §4.9 — Causality, hyperbolicity, response & dispersion (MDPC)
- §4.10 — Boundary, uniqueness, topology & ledgers (MBLC + MLCP)
- §4.11 — Spectral standardization — the Miller Transform (MT)
- §4.14 — Health, gauge-slice independence, and audits

**External chapters (C#):**
- C2 §25
- C5 §5.33

---

## 4.13 Table of Contents and Introduction

### 4.13.1 Table of Contents (Section 4.13)
- 4.13.2 Legacy & intermediate forms
- 4.13.3 Connectivity Map

### 4.13.2 Legacy & intermediate forms
_See also:_ §4.8, §4.10, §4.11, §4.14; C5 §5.46–5.49, C3 §3.19

13\. Legacy & intermediate forms — explicit catalog (traceable, expanded)
=========================================================================

> **What this section presents.** A _conversion manual_. Many readers arrive with well-worn calculational lanes—harmonic gauge for gravity, Coulomb/Lorenz for vector fields, Stückelberg+ $R_\xi$  for massive vectors, images vs boundary integrals at edges, BRST, Euclidean SD/ASD splits, non-unitary Fourier pairs, etc. None of those lanes are “wrong”; they’re just different alphabets. Here we give a line-by-line **translator** from each alphabet into the **equivalence-first** grammar used in this chapter. For each lane:
> 
> 1.  we articulate the **contract** the lane silently assumes (what is being held fixed; what is being solved for);
> 2.  we write the **map** into our projectors/Schur/Calderón/retarded framework;
> 3.  we list the **invariants** that must not change (cones, poles/residues, bulk energy, boundary post);
> 4.  we state a **checksum**—a one-screen calculation that certifies the map; and
> 5.  we note the exact **ledger** move (if any) created by the translation.
>     
> 
> This is not a restatement of earlier results; it is a **truth table** that lets two experts, working in different styles, prove to each other they are computing the _same_ physics.

The development of physics is a conversation between generations of thought, each using its own symbols to speak about the same world. One should not discard the older languages, for within them lie the proofs of our present understanding. What matters is that the translation from one dialect to another leaves the essential structure unchanged: the geometry that governs propagation, the energy that measures the effort of nature, and the boundary record that ensures conservation. When the same phenomenon is written once in tensor form, once in potentials, and again in projectors or spectral kernels, the task of the theorist is not to choose a favorite grammar but to verify that each recounts the same event in spacetime. In this way the apparent diversity of form becomes a test of coherence, and the ledger of physical invariants—the cones, the residues, the flux through the boundary—serves as the common signature by which all formulations may be reconciled.

* * *

##### 4.13.2.13.1 Reading the translator: a three-layer recipe
-------------------------------------------------

**Plain picture.** Imagine two cameras pointed at the same scene. One shoots RAW with a wide color gamut; the other shoots a compressed format. If both are calibrated, a color card placed in the scene _proves_ the mapping. Our “color card” consists of four invariants that never move:

*   **Cone:** the characteristic polynomial of the principal symbol (front speed).
*   **Pole/residue:** the location and sign of physical poles in any Green/response function.
*   **Bulk energy (“jar”):** the slice integral of  $T_{00}$  in our sign locks.
*   **Boundary post (“ledger”):** the surface energy/flux/integers the variation leaves behind.

**Workflow.** For each legacy lane:

1.  **State the lane’s contract.** What gauge/constraint choice is implicit? What boundary data are being fixed? Which Green function is used (retarded/advanced/time-ordered)?
2.  **Apply the map.** Replace ad-hoc manipulations by projectors (Helmholtz, BR), Schur complements, Cholesky canonicalization, Calderón operators, and the retarded prescription. Keep track of any IBP superpotentials.
3.  **Run the checksum.** Compute: (i) the principal symbol; (ii) the residue at each physical pole in the projected block; (iii) one slice energy; (iv) one boundary flux. Any mismatch means a contract was misread.

All that follows is just this recipe specialized to the most common alphabets.

* * *

##### 4.13.2.13.2 Massive spin-1 sector (axial-vector template): Stückelberg/ $R_\xi$  ↔ Helmholtz/retarded
----------------------------------------------------------------------------------------------

### Contract (what the legacy lane really fixes)

*   **Field split.**  $S_\mu=\hat S_\mu+\partial_\mu \pi/m$ .
*   **Gauge choice.** Gauge-fixing functional  $G=\nabla\!\cdot\!\hat S+\xi m \pi$ ,  $\mathcal L_{\rm gf}=-(2\xi)^{-1}G^2$ .
*   **Propagator.** Time-ordered or Feynman (not retarded) by default in many notes; boundary data often implicit (no Sommerfeld declaration).

### Map (turn gauges into a projector statement)

1.  **Project to physics.** Multiply any propagator or equation by  $\Pi^{\mathrm T}$  on both index pairs. The algebraic longitudinal content disappears from poles:
    $$
    \Pi^{\mathrm T} D^{(\xi)} \Pi^{\mathrm T}\ =\ \frac{-\,\Pi^{\mathrm T}}{k^2-m^2+i0}\quad (\text{retarded: }+i0\to +i0^+ \text{ in }\omega).
    $$
2.  **Source remap.** Replace  $J^\mu$  everywhere by  $\Pi^{\mathrm T}{}^\mu{}_\nu\,J^\nu$ . The longitudinal equation  $\nabla\!\cdot\!S=(g_S/m^2)\nabla\!\cdot\!J$  is algebraic; keep it out of the propagating block.
3.  **Time arrow.** If the legacy calculation used time-ordered Green’s functions, switch to **retarded** by  $\omega\to\omega+i0^+$  before applying Kramers–Kronig/Herglotz checks.

### Invariants & ledger

*   **Poles/residues.** Simple pole at  $k^2=m^2$  with **positive** residue on  $\Pi^{\mathrm T}$ ; independent of  $\xi$  (Nielsen identity).
*   **Cone.** Principal symbol  $-k^2\delta^\mu{}_\nu+k^\mu k_\nu$  → luminal front.
*   **Ledger.** Gauge-fixing adds only superpotentials (surface terms) to the action; post them, do not adjust bulk  $T_{00}$ .

### Checksum (one minute)

Pick any conserved plane-wave source  $J^\mu\propto \varepsilon^\mu e^{-ik\cdot x}$  with  $k\!\cdot\!\varepsilon=0$ . Compute

$$
\lim_{k^2\to m^2}(k^2-m^2)\,\Pi^{\mathrm T} D^{(\xi)} \Pi^{\mathrm T}
$$

and verify it equals  $-\Pi^{\mathrm T}$  for all  $\xi$ . Then check the local inertial  $T_{00}$  of the resulting field is non-negative.

* * *

##### 4.13.2.13.3 Linearized gravity: harmonic/de Donder ↔ Barnes–Rivers (spin-by-spin)
--------------------------------------------------------------------------

### Contract

*   **Gauge.**  $\partial^\mu \bar h_{\mu\nu}=0$  with  $\bar h_{\mu\nu}=h_{\mu\nu}-\frac12 \eta_{\mu\nu}h$ .
*   **Green.** Free-space inverse of  $\Box$  in that gauge; boundary behavior often implicit.

### Map

1.  **Local patch → BR basis.** In Fourier, decompose  $h_{\mu\nu}$  into  $P^{(2)},P^{(1)},P^{(0s)},P^{(0w)}$  blocks.
2.  **Invert per spin.** Only the  $P^{(2)}$  block carries the radiative pole; all others are algebraic/gauge or constrained.
3.  **Back to real space.** Recompose  $h_{\mu\nu}$  and evaluate radiation zone fields with  $P^{(2)}$  only (TT content).

### Invariants & ledger

*   **Poles/residues.** Positive residue in the spin-2 block; no physical poles in spin-1/0 blocks.
*   **Cone.** Luminal front.
*   **Ledger.** Any “improved” stress in the legacy lane differs by divergences → boundary flux only. ADM/Brown–York is the single gravitational ledger post.

### Checksum

Compute the far-zone energy flux from de Donder and from  $P^{(2)}$ ; they must match. If they don’t, an improvement term wasn’t posted to the ledger or a normalization drifted.

* * *

##### 4.13.2.13.4 Yang–Mills: Lorenz/Coulomb/BRST ↔ Helmholtz + physical currents
--------------------------------------------------------------------

### Contract

*   **Lorenz:**  $\nabla^\mu A_\mu=0$ , ghosts present in the path integral.
*   **Coulomb:**  $\nabla\!\cdot\!\mathbf A=0$ , scalar potential instantaneous; transverse waves propagate.
*   **BRST:** Ward identities ensure gauge-independent observables.

### Map

1.  **Helmholtz split.**  $\mathbf A=\mathbf A_\perp+\nabla \phi$ , with  $\mathbf A_\perp=\Pi^{\mathrm T}\mathbf A$ .
2.  **Currents.** Replace  $J^\mu\to \Pi^{\mathrm T}J^\mu$  in propagation; Gauss law solved as a constraint for  $\phi$ .
3.  **Spectral checks.** Work with retarded  $\chi^R_{T}(\omega,\mathbf k)$  on the transverse subspace; apply Herglotz and K–K.

### Invariants & ledger

*   **Poles/residues.** Same transverse spectral density in Lorenz/Coulomb/projector lanes.
*   **Cone.** Luminal fronts.
*   **Ledger.** Gauge-fixing superpotentials and IBP remainders → surface posts.

### Checksum

Measure (analytically or numerically)  $\Im \chi^R_T(\omega,0)/\omega$  near  $0^+$  in both lanes; the slope must agree and be  $\ge0$ .

* * *

##### 4.13.2.13.5 Two-forms: raw  $H^2$  ↔ SD/ASD diagonalization (positivity reveal)
------------------------------------------------------------------------

### Contract

*   **Legacy habit.** Keep  $H_{\mu\nu\rho}H^{\mu\nu\rho}$  in Lorentzian and inspect components—positivity is opaque.

### Map

1.  **Wick to Euclidean.** Decompose  $H=H_+\oplus H_-$  with  $P_\pm=\frac12(1\pm *)$ .
2.  **Read positivity.** The quadratic action becomes  $\|H_+\|^2+\|H_-\|^2\ge0$ .
3.  **Rotate back.** Propagators, cones, and residues are unchanged; only the _audit_ changed basis.

### Invariants & ledger

*   **Poles/residues/cone.** Identical across representations.
*   **Ledger.** If topological terms are present (e.g.,  $\int B\wedge F$ ), they are integers and ledger-only.

### Checksum

Compute the quadratic form for a test configuration in both representations; equality is exact. Any mismatch is a sign/normalization slip.

* * *

##### 4.13.2.13.6 Mixed one-forms: ad-hoc rotations ↔ Sylvester/Cholesky + projector
-----------------------------------------------------------------------

### Contract

*   **Legacy habit.** “Complete the square” by eye; rotate fields with a non-systematic orthogonal matrix.

### Map

1.  **Build the kernel.** Quadratic form  $Q=\frac12 X^\top K X$  with symmetric  $K$ .
2.  **Test positivity.** Sylvester’s criterion (all leading principal minors positive) or compute **Cholesky**  $K=R^\top R$ .
3.  **Canonicalize.** Redefine  $X\mapsto R^{-1}X$  → unit SPD quadratic form.
4.  **Project.** Apply Helmholtz/BR projectors channelwise; invert scalar resolvents; recombine.

### Invariants & ledger

*   **Poles/cones/residues.** Unchanged by  $R$  (local, invertible); they must be read _after_ canonicalization.
*   **Ledger.** Cross-terms converted to superpotentials; record them at the boundary.

### Checksum

Compare dispersion curves and DC slopes before/after canonicalization; they must be identical in magnitude and sign.

* * *

##### 4.13.2.13.7 Fourier conventions: non-unitary/exponential flips ↔ MT (unitary, retarded)
--------------------------------------------------------------------------------

### Contract

*   **Legacy habits.** Mixed  $2\pi$  conventions; sometimes cosine transforms for “even” kernels; time-ordered analyticity.

### Map

1.  **Phase fix.** Demand  $\partial_t\to i\omega$ ,  $\nabla\to -i\mathbf k$ . Flip signs if needed.
2.  **Scale to unitarity.** Rescale transforms so Parseval is exact (no invisible energy factors).
3.  **Retarded.** Replace “PV only” by  $+i0^+$ . Restore the imaginary part that carries dissipation.

### Invariants & ledger

*   **Herglotz/K–K.** Must hold after the map; if not, the ruler is still wrong.
*   **Ledger.** None—this is a convention change.

### Checksum

Inverse-transform the Yukawa denominator; you must land on  $e^{-mr}/4\pi r$  with no leftover constants.

* * *

##### 4.13.2.13.8 Boundaries: free-space+homogeneous, images, boundary integrals, DtN (one bulk)
-----------------------------------------------------------------------------------

### Contract

*   **Method choice.** Pick one construction and silently assume it is “the” solution; BCs not always spelled out.

### Map

1.  **Declare BCs first.** Without BCs, none of the methods are determinate.
2.  **Green–Betti.** Show that two methods with the _same BCs_ differ by a solution of the homogeneous problem with zero boundary data.
3.  **Rellich.** Under radiation BCs, the homogeneous complement is zero → **same bulk field**.
4.  **DtN perspective.** Boundary integral/DtN make the boundary operator  $\Lambda$  explicit; images/free-space+homogeneous implicitly compute the same  $\Lambda$ .

### Invariants & ledger

*   **Bulk field.** Identical across methods.
*   **Ledger.** Panel-wise flux partition can differ; the _sum_ of outward power is the same and must be posted.

### Checksum

Compute total outward power across the boundary; methods must agree. Differences per panel are bookkeeping (ledger).

* * *

##### 4.13.2.13.9 Covariant vs 3+1/ADM: Noether/Komar ↔ ADM rim + jar split
--------------------------------------------------------------

### Contract

*   **Covariant lane.** Conserved charges from Killing vectors/Noether currents; boundary terms often implicit.
*   **3+1 lane.** Lapse/shift/extrinsic curvature; explicit Hamiltonian constraint and surface energy.

### Map

1.  **Identify the charge.** Noether/Komar time-translation charge equals the ADM surface term when GHY pairing is used.
2.  **Jar–rim split.** The covariant stress slice integral equals the ADM bulk constraint piece; remaining surface term is the **rim**.

### Invariants & ledger

*   **Total energy.** Same number: jar  $+$  rim equals the Noether/ADM charge.
*   **Ledger.** Surface term is the only gravitational ledger line.

### Checksum

Compute the total energy for a simple static metric in both languages; equality is exact.

* * *

##### 4.13.2.13.10 Path integral vs canonical: time-ordered correlators ↔ retarded response
-----------------------------------------------------------------------------

### Contract

*   **Path integral.** Two-point functions are time-ordered; analytic continuation to retarded is sometimes left implicit.
*   **Canonical/response.** Retarded susceptibility is primary; DC order enforced.

### Map

1.  **Reconstruct retarded.**  $\chi^R(\omega)=G^{\rm TO}(\omega+i0)-G^{\rm TO}(\omega-i0)$  up to standard factors.
2.  **Project.** Apply projectors to isolate physical channels; read poles/residues.
3.  **DC corridor.** Enforce  $\mathbf k\to0$  first,  $\omega\to0^+$  second.

### Invariants & ledger

*   **Spectral measure.** Källén–Lehmann ↔ Herglotz; same positive spectral weight.
*   **Ledger.** None.

### Checksum

Compare the low- $\omega$  slope of  $\Im \chi^R/\omega$  reconstructed from the path integral with the canonical MDPC check.

* * *

##### 4.13.2.13.11 Wick rotations: Euclidean audits ↔ Lorentzian dynamics (sign hygiene)
---------------------------------------------------------------------------

### Contract

*   **Legacy habits.** Different sign choices for vectors/2-forms; sometimes positivity checked directly in Lorentzian.

### Map

1.  **One Wick rule.** Rotate with a single, fixed convention so that bosonic quadratics become positive in Euclidean space.
2.  **Audit there.** Do positivity one-liners (e.g., SD/ASD for 2-forms), then rotate back.

### Invariants & ledger

*   **Poles/residues.** Unchanged after rotating back.
*   **Ledger.** Integer topology is Wick-invariant; remains in the ledger.

### Checksum

Pick a quadratic form and verify positivity in Euclidean; propagate poles back to Lorentzian unchanged.

* * *

##### 4.13.2.13.12 Distributions, regulators, DC order: PV →  $+i0^+$ ,  $m\to0^+$  after the corridor
-----------------------------------------------------------------------------------------

### Contract

*   **Legacy habits.** PV integrals without imaginary parts; setting masses to zero first.

### Map

1.  **Restore the imaginary part.** Use  $(x\pm i0)^{-1}=\mathrm{PV}(1/x)\mp i\pi\delta(x)$ .
2.  **Corridor discipline.**  $\mathbf k\to0$  then  $\omega\to0^+$  before massless limits.
3.  **Regulators.** Keep  $m\to0^+$  until the end.

### Invariants & ledger

*   **Passivity.** Herglotz slope  $\ge0$  after the map; K–K holds.
*   **Ledger.** None.

### Checksum

Evaluate  $\lim_{\omega\to0^+}\lim_{\mathbf k\to0} \Im \chi^R/\omega$  for a simple kernel; reversing limits must fail, confirming the need for the corridor.

* * *

##### 4.13.2.13.13 “Diff” table (five tests that certify equivalence)
--------------------------------------------------------

1.  **Cone diff.** Compare characteristic polynomials; must match (front speed unchanged).
2.  **Pole diff.** Compare physical pole positions; must be identical.
3.  **Residue diff.** Compare residues on physical projectors; must be positive and equal.
4.  **Jar–rim diff.** Compare  $E_{\rm bulk}$  and the boundary post; sum must match across lanes.
5.  **Flux diff.** Compare total outward power; per-panel differences are ledger posts only.

If any diff fails, the translation missed a contract item (BCs, gauge parameter, Fourier ruler, or an improvement term not posted).

* * *

##### 4.13.2.13.14 Translation cards (drop-in mini-workflows)
------------------------------------------------

### Card T-1 —  $R_\xi$  massive vector → projector lane

*   **Input.**  $D_{\mu\nu}^{(\xi)}(k), J^\nu(k)$ .
*   **Do.**  $S_\mu=\Pi^{\mathrm T}{}_\mu{}^\alpha D_{\alpha\beta}^{(\xi)} \Pi^{\mathrm T}{}^\beta{}_\nu J^\nu$ .
*   **Check.** Residue at  $k^2=m^2$  independent of  $\xi$ ; compute  $T_{00}\ge0$ .

### Card T-2 — de Donder GR → BR per-spin

*   **Input.**  $\bar h_{\mu\nu}$ .
*   **Do.** Project to  $P^{(2)}$ , invert  $\kappa_2$ , reconstruct radiative field.
*   **Check.** Far-zone energy flux equals the de Donder result.

### Card T-3 — Coulomb YM → transverse response

*   **Input.**  $\mathbf A=(\mathbf A_\perp,\nabla\phi)$ .
*   **Do.** Propagate  $\mathbf A_\perp$  with retarded kernel; solve  $\phi$  from Gauss law.
*   **Check.**  $\Im \chi_T^R/\omega\ge0$  near  $0^+$ .

### Card T-4 — Images vs boundary integral vs DtN

*   **Input.** One boundary problem, three solutions.
*   **Do.** Compare interior fields and total outward power.
*   **Check.** Identical bulk; equal power sums; any panel differences go to the ledger.

### Card T-5 — Non-unitary Fourier → MT

*   **Input.** Legacy transform pair.
*   **Do.** Rescale to MT; fix exponential sign; adopt  $+i0^+$ .
*   **Check.** Parseval exact; Yukawa constant  $e^{-mr}/4\pi r$  on inversion.

* * *

##### 4.13.2.13.15 What this catalog gives you (and how to use it)
-----------------------------------------------------

*   A **deterministic translator** from any familiar lane into the equivalence-first workflow—no hand-waving, no “trust me.”
*   A list of **invariants** that must survive intact and the **exact** ledger entries that may shift.
*   **Checksums** you can run in minutes to certify that two derivations, written in different alphabets, are in fact the _same computation_.
*   A set of **cards** you can paste into your own notes to keep future work aligned—especially useful when collaborating across subfields with different dialects.

_Bring whatever lane you learned. This catalog tells you precisely how to dock it into our projector-, Schur-, Calderón-, and retarded-based grammar, and how to prove—rather than merely claim—that nothing physical moved._

## Response:
14\. Health, gauge-slice independence, and audits — fully expanded
==================================================================

> **What this section presents.** A complete, execution-ready **health protocol** for the theory and for any calculation performed with it. We convert the usual intuition—“no ghosts, causal, well-posed, gauge-independent, energy-positive”—into a set of **mechanical audits** you can run line-by-line: quadratic and spectral checks for ghosts; principal-symbol and symmetrizer checks for hyperbolicity; Dirac-constraint closure and DOF counts; **Nielsen/BRST** checks for gauge-slice independence; boundary well-posedness and uniqueness; **Herglotz/Kramers–Kronig** checks for dispersion; and reproducible **numerical** tests. Each audit begins in plain language, climbs to the exact criteria a working theorist uses, and ends with a short “pass/fail” **card**. No earlier text is restated; this is the **inspection manual**.

### 4.13.3 Connectivity Map
**Within Chapter 4 (closely related):**
- §4.8 — Equivalence-first computation (MEFP) and MPSD lanes
- §4.10 — Boundary, uniqueness, topology & ledgers (MBLC + MLCP)
- §4.11 — Spectral standardization — the Miller Transform (MT)
- §4.14 — Health, gauge-slice independence, and audits

**External chapters (C#):**
- C5 §5.46–5.49
- C3 §3.19

---

## 4.14 Table of Contents and Introduction

### 4.14.1 Table of Contents (Section 4.14)
- 4.14.2 Health, gauge-slice independence, and audits
- 4.14.3 Connectivity Map

### 4.14.2 Health, gauge-slice independence, and audits
_See also:_ §4.1, §4.2, §4.3, §4.4, §4.5, §4.6, §4.7, §4.8, §4.9, §4.10, §4.11, §4.12, §4.13; C1 §0–1.7, C2 §27, C5 §5.52

14\. Health, gauge-slice independence, and audits
==================================================================

> **What this section presents.** A complete, execution-ready **health protocol** for the theory and for any calculation performed with it. We convert the usual intuition—“no ghosts, causal, well-posed, gauge-independent, energy-positive”—into a set of **mechanical audits** you can run line-by-line: quadratic and spectral checks for ghosts; principal-symbol and symmetrizer checks for hyperbolicity; Dirac-constraint closure and DOF counts; **Nielsen/BRST** checks for gauge-slice independence; boundary well-posedness and uniqueness; **Herglotz/Kramers–Kronig** checks for dispersion; and reproducible **numerical** tests. Each audit begins in plain language, climbs to the exact criteria a working theorist uses, and ends with a short “pass/fail” **card**. No earlier text is restated; this is the **inspection manual**.

Nature speaks in many tempos; we hear clearly only those for which our instruments are tuned. A careful reduction silences the fast voices yet leaves their trace as modest corrections that neither outrun light nor mint energy from nothing. The effective law is then a courtesy of scale, not a new metaphysics: it carries the same geometry of propagation and the same accounting at the boundary. Thus one may compute with fewer symbols and no deception, provided the ledger records the terms that were traded away.

On the other hand, reliability shows itself under cross‑examination. We ask whether any mode bears negative energy; whether disturbances remain inside the cone; whether a reshuffling of gauge or coordinates leaves the numbers we observe unchanged. Constraints must close, the boundary must fix a unique solution, and the response must display causality as analyticity rather than slogan. When these trials are passed, the formal apparatus ceases to be scaffolding and becomes part of the object: prediction no longer depends on description, and the ledger balances without appeal to taste.

* * *

##### 4.14.2.14.1 Why we audit (and what “healthy” means here)
-------------------------------------------------

**Plain picture.** A bridge is safe when its cables are in tension (not buckling), its pillars stand on solid ground, and its load path is clear to the river (nowhere does water dam up). A field theory is safe when (i) **no ghosts** sit hidden in its quadratic form, (ii) its PDEs are **hyperbolic** so initial data determine evolution in their causal domain, (iii) its energy and responses are **positive** in the right senses, (iv) **constraints** close and count the right number of degrees of freedom, (v) **gauge slices** don’t move physical poles/residues, and (vi) **boundaries** and **radiation** are well-posed and unique. Our audits verify exactly these points.

**One promise.** Every test below is **basis-agnostic**: it gives the same answer in any projector, gauge, or legacy lane—provided you respect the ledger (surface posts) and the dispersion corridor (space first, time second at DC).

* * *

##### 4.14.2.14.2 The Stops: a one-screen pipeline you can actually run
----------------------------------------------------------

**STOP-0 — Locks check.** Verify you are using the agreed ruler (signature, phase, unitary Fourier, retarded shift), and that BCs are declared **before** varying.

**STOP-1 — Ghost audit (quadratic level).**  
(1a) Canonical quadratic energy density non-negative in a local inertial frame;  
(1b) Euclidean positivity (bosons) after Wick;  
(1c) Projector-residue test: residues at physical poles are **positive**.

**STOP-2 — Constraint closure & DOF count.**  
Run the Dirac algorithm: primary → secondary constraints; classify first/second class; count DOF  $= \tfrac12(\text{phase-space dim} - 2 \times \#\text{first} - \#\text{second})$ .

**STOP-3 — Hyperbolicity.**  
Principal symbol  $\sigma(\mathcal L)(x,k)$  has Lorentzian type; find a symmetrizer; produce an energy estimate (domain of dependence).

**STOP-4 — Gauge-slice independence.**  
Nielsen/BRST test: physical poles and residues do **not** depend on the slice parameter (e.g.,  $\xi$ ); projector forms agree with Stückelberg/ $R_\xi$  on the transverse/physical block.

**STOP-5 — Boundary/uniqueness.**  
Variational surface terms cancelled by compensators; DtN map elliptic/Fredholm; Rellich uniqueness with Sommerfeld for radiators. Differences among methods recorded **only** as ledger posts.

**STOP-6 — Dispersion/passivity (DC corridor).**  
Retarded analyticity; Herglotz slope  $\Im\chi^R(\omega,0)/\omega \ge 0$  as  $\omega\!\downarrow\!0^+$ ; Kramers–Kronig satisfied (with subtractions if needed); **space** → **time** order at DC never violated.

**STOP-7 — Numerical reproducibility.**  
Unitary DFT, trace-conforming spaces at edges, CFL from the cone, and MT-1S ladder for DC slopes; include ledger receipts (surface power) in outputs.

Every subsection below gives the nuts-and-bolts for one STOP, followed by an audit **card**.

* * *

##### 4.14.2.14.3 STOP-1 — Ghost audit (quadratic and spectral)
--------------------------------------------------

**Plain picture.** A ghost is a mode whose energy switches sign—the theoretical analogy of a cable in compression where only tension is safe.

**(A) Canonical positivity in a local inertial chart.**  
Write the quadratic Hamiltonian density  $\mathcal H^{(2)}$ . For each propagating channel, complete the square on canonical pairs; verify  $\mathcal H^{(2)}\ge 0$ .  
_Axial spin-1 template:_ with  $\Pi^i\!=\!H^{0i}$ ,  $S_0$  algebraic, the reduced quadratic form in  $(\Pi^i,H_{ij},S_i)$  is positive for  $m_S^2>0$ .

**(B) Euclidean positivity (bosons).**  
Wick rotate and check  $S_E^{(2)}=\int (\tfrac14H^2+\tfrac12 m^2 S^2)\ge 0$ . For 2-forms, SD/ASD split gives  $\|H_+\|^2+\|H_-\|^2$ .

**(C) Projector-residue test.**  
In Fourier variables, decompose onto physical projectors  $P$ . The residue matrix  $\operatorname{Res}_{k^2=m^2} G(k)$  restricted to  $P$  must be **positive semidefinite**. For a massive spin-1,  $\operatorname{Res} = -\Pi^{\mathrm T}$  (our sign locks make “minus” the positive kinetic convention in the action); inner products give positive numbers.

**Audit card GHOST-1.**

*   Build  $\mathcal H^{(2)}$  and check squares  $\ge 0$ .
*   Wick and check SD/ASD positivity.
*   Compute one projector residue at a physical pole; verify positive eigenvalues.  
    **Pass** if all three hold.

* * *

##### 4.14.2.14.4 STOP-2 — Constraint closure and degrees of freedom
-------------------------------------------------------

**Plain picture.** Constraints are rules of the game. They must close, and the headcount of movers on the board must match the theory’s promise.

**Dirac ladder (minimal recipe).**

1.  Compute canonical momenta; list **primary** constraints.
2.  Enforce time-preservation  $\dot\phi\approx 0$  to get **secondary** constraints.
3.  Classify: Poisson brackets show first-class (gauge) vs second-class (algebraic).
4.  DOF count:  $\frac12(\dim \Gamma - 2n_{\rm 1st} - n_{\rm 2nd})$ .

**Axial spin-1 (worked logic).**  
Primary:  $\Pi^0=0$ . Preserving it:  $\partial_i\Pi^i+m_S^2 S_0-g_S J_5^0=0$  (secondary). Both are **second-class**; eliminating  $S_0$  leaves  $3$  DOF (the transverse polarizations). Brackets close; no tertiary constraints.

**Audit card DOF-1.**

*   List constraints; compute their bracket matrix.
*   Rank shows second-class for axial sector; no first-class here.
*   Count DOF = 3.  
    **Pass** if the rank/DOF match.

* * *

##### 4.14.2.14.5 STOP-3 — Hyperbolicity (principal symbol, symmetrizer, estimate)
---------------------------------------------------------------------

**Plain picture.** Well-posedness is the right to predict tomorrow from today within the light cone.

**(A) Principal symbol.**  
Extract the highest-derivative block  $\sigma(\mathcal L)(x,k)$ . Healthy channels give  $\det\sigma = 0$  only on  $k^2=0$  (light cone).

**(B) Symmetrizer & energy estimate.**  
Find  $H(x)$  such that  $H\sigma$  is symmetric and positive (on the physical subspace). Derive

$$
\|u(t)\|_{H^1(\Sigma_t)}^2 + \int_{t_0}^t \!\!\text{Flux}\, d\tau \le C\Big(\|u(t_0)\|_{H^1}^2 + \int_{t_0}^t \!\!\|f\|_{L^2}^2\Big).
$$

This delivers uniqueness and domain of dependence.

**(C) Front speed.**  
Characteristics from  $\det\sigma=0$  give **luminal** fronts; group speeds can be subluminal (massive channels).

**Audit card HYP-1.**

*   Compute  $\sigma$ ; verify Lorentzian type and light-cone characteristics.
*   Produce a symmetrizer (explicit on the projector block).
*   State the energy estimate with declared BCs.  
    **Pass** when all three exist.

* * *

##### 4.14.2.14.6 STOP-4 — Gauge-slice independence (Nielsen/BRST)
-----------------------------------------------------

**Plain picture.** Changing a gauge knob should move only scaffolding, never the building.

**Nielsen identity (pole position).**  
Let  $G^{-1}(k,\xi)$  denote the 1PI two-point function in a gauge family  $\xi$ . Then

$$
\frac{\partial}{\partial\xi} G^{-1}(k,\xi) = \mathcal N(k,\xi)\, G^{-1}(k,\xi)
$$

for some regular  $\mathcal N$ . At a **physical pole**  $k^2=m^2$ ,  $G^{-1}=0$  so  $\partial_\xi G^{-1}=0$ : the pole **does not move** with  $\xi$ . On the projector-restricted block, the **residue** is likewise  $\xi$ \-independent.

**BRST Ward identity (observables).**  
Gauge-invariant observables commute with the BRST charge; their correlators obey slice-independence. In linear response this means: on the physical projector,  $\chi^R$  is  $\xi$ \-independent.

**Audit card GAUGE-1.**

*   Differentiate  $G^{-1}$  with respect to  $\xi$ ; evaluate at a physical pole; show zero.
*   Numerically/analytically verify residue equality across gauges.  
    **Pass** when both hold.

* * *

##### 4.14.2.14.7 STOP-5 — Boundary well-posedness & uniqueness (and the ledger)
-------------------------------------------------------------------

**Plain picture.** The variation has **no loose ends** at the edge; the radiating solution is **unique**; method choices differ only by what the receipt prints.

**(A) Variational surface terms.**  
Compute the surface term  $\int_{\partial\Omega}(\cdots)\,\delta\Phi$ . Choose **one** BC menu (Dirichlet/Neumann/Robin/Sommerfeld) and add the compensating surface functional so  $\delta S$  has no boundary remainder.

**(B) DtN/Calderón.**  
Boundary operators are Fredholm/elliptic on the trace spaces; this certifies well-posedness.

**(C) Rellich uniqueness.**  
With Sommerfeld radiation, the only homogeneous radiating solution with zero far-field flux is the trivial one; the radiating field is unique.

**Ledger.** Any integration-by-parts or method difference (images vs BIE vs free-space + homogeneous) **only** reshuffles boundary flux; we post it to the ledger.

**Audit card BOUND-1.**

*   Show the surface term is cancelled for the chosen BCs.
*   Exhibit DtN positivity/Fredholmness.
*   State Rellich uniqueness.  
    **Pass** when all three are documented.

* * *

##### 4.14.2.14.8 STOP-6 — Dispersion/passivity with the DC corridor
-------------------------------------------------------

**Plain picture.** A passive system never outputs more energy than it absorbs; this appears as **non-negative** low-frequency dissipation.

**(A) Retarded analyticity.**  
All response functions are boundary values from  $\Im\omega>0$ . Use the retarded prescription  $\omega\!\to\!\omega+i0^+$ .

**(B) Herglotz positivity.**  
For any probe  $v$ ,

$$
\lim_{\omega\to0^+}\frac{1}{\omega}\,v^\dagger \Im \boldsymbol\chi^R(\omega,\mathbf 0) v\ \ge\ 0.
$$

**(C) Kramers–Kronig (with subtractions).**  
Check the real part via the dispersive integral; low-frequency slope must be consistent with (B).

**(D) Corridor discipline.**  
Evaluate **space first**, then **time**:  $\mathbf k\!\to\!0$  followed by  $\omega\!\to\!0^+$ . Reversing the order can flip signs and fake activity.

**Audit card DISP-1.**

*   Confirm retarded analyticity and the K–K relation (with stated subtractions).
*   Compute the DC slope with the corridor; verify  $\ge 0$  (matrix PSD).  
    **Pass** when both are satisfied.

* * *

##### 4.14.2.14.9 STOP-7 — Numerical audits (reproducibility and receipts)
-------------------------------------------------------------

**Plain picture.** A result is reproducible when a second team—using different meshes but the same ruler—gets the same numbers within predicted error bars.

**(A) Spectral ruler.**  
Use the unitary DFT (MT-d); for off-grid frequencies use MT-1S; report window gains/moments.

**(B) Spaces & CFL.**  
Use trace-conforming spaces for edges ( $H^1$  for scalars;  $H(\mathrm{curl})$ / $H(\mathrm{div})$  for 1-forms). Derive the time step from the cone, not from ad-hoc damping.

**(C) DC protocol.**  
Fix  $\mathbf k\!=\!0$ ; measure  $\Im\chi^R/\omega$  at a ladder  $\omega_j\!\downarrow\!0^+$ ; only then refine  $\mathbf k\!\to\!0$ .

**(D) Ledger receipt.**  
Log outward power per boundary panel and the total; post the total as the boundary entry added to the jar in energy identities.

**Audit card NUM-1.**

*   Unitary MT pair confirmed; MT-1S used near DC with error bars.
*   Spaces and CFL documented; no “stability by damping.”
*   Ledger power printed.  
    **Pass** when these appear in the run report.

* * *

##### 4.14.2.14.10 Typical failure modes (and how to repair them)
---------------------------------------------------

*   **Hidden ghost.** Symptom: a negative residue or an indefinite canonical quadratic form. _Fix:_ canonicalize via Cholesky; ensure signs of kinetic terms match the locks; re-evaluate residues on projector blocks.
*   **Not hyperbolic.** Symptom: no energy estimate; ill-posed growth. _Fix:_ re-express equations in symmetric-hyperbolic form; check BC compatibility.
*   **Gauge drift.** Symptom: pole locations shift with  $\xi$ . _Fix:_ compute Nielsen derivative; project to physical block; remove unprojected longitudinal contamination.
*   **Boundary leak.** Symptom: variation has a surface remainder; method results disagree. _Fix:_ declare BCs; add compensator; enforce Rellich; reconcile methods via DtN; ledger the difference.
*   **Dispersion lie.** Symptom:  $\Im\chi^R/\omega<0$  at DC. _Fix:_ restore  $+i0^+$ ; enforce corridor; check window/fit bias; if persistent, a ghost or sign error exists upstream.
*   **Numerical “stabilization”.** Symptom: adding damping “helps.” _Fix:_ remove damping; fix CFL or BCs; ensure the cone and spaces are respected.

* * *

##### 4.14.2.14.11 Micro-audits (cards you can paste into any derivation)
------------------------------------------------------------

### Card A — Projector-residue positivity (ghost check)

1.  Compute the physical projector  $P$ .
2.  Extract  $\operatorname{Res}_{\text{pole}}(G)$  on  $P$ .
3.  Check eigenvalues  $\ge 0$ .  
    **Pass** if yes.

### Card B — Dirac ladder (DOF)

1.  List primary constraints;
2.  Time-preserve → secondary;
3.  Classify;
4.  Count DOF.  
    **Pass** if count matches the theory’s promise.

### Card C — Principal symbol and symmetrizer

1.   $\sigma(\mathcal L)(x,k)$ ;
2.  Find  $H$  s.t.  $H\sigma$  symmetric, positive;
3.  State energy estimate.  
    **Pass** if all exist.

### Card D — Nielsen identity at a pole

1.  Differentiate  $G^{-1}(k,\xi)$  w.r.t.  $\xi$ ;
2.  Evaluate at  $k^2=m^2$ ;
3.  Show zero.  
    **Pass** if pole doesn’t move.

### Card E — DC corridor, Herglotz slope

1.  Compute  $\chi^R(\omega,\mathbf k)$  retarded;
2.  Take  $\mathbf k\to0$ , then  $\omega\to0^+$ ;
3.  Verify  $\Im\chi^R/\omega\ge 0$ .  
    **Pass** if PSD.

### Card F — Boundary well-posedness

1.  Display the surface term and compensator;
2.  Provide DtN/Fredholm statement;
3.  Rellich uniqueness (if radiating).  
    **Pass** when all three appear.

* * *

##### 4.14.2.14.12 Short proofs you can cite (load-bearing, tool-agnostic)
-------------------------------------------------------------

**Lemma (Residue positivity ⇒ no ghost).**  
If the projector-restricted residue matrix at a simple pole is PSD and the canonical quadratic form is positive in a LIF, the mode carries positive energy; no negative-norm state exists.

**Lemma (Nielsen).**  
 $\partial_\xi G^{-1}(k,\xi)=\mathcal N G^{-1}$  implies  $\partial_\xi k_{\rm pole}^2=0$  when  $G^{-1}(k_{\rm pole},\xi)=0$ ; residues on the physical block are  $\xi$ \-independent.

**Lemma (Rellich).**  
With Sommerfeld radiation, a homogeneous solution with zero net far-field flux is trivial—uniqueness of radiating solutions.

**Lemma (Herglotz).**  
For a causal, passive response,  $\Im \chi^R(\omega,0)/\omega\ge 0$  as  $\omega\to0^+$ ; the matrix version is PSD for all probes  $v$ .

**Lemma (Symmetrizer ⇒ domain of dependence).**  
If there exists  $H$  s.t.  $H\sigma$  is symmetric and positive on the physical subspace, then there is an energy estimate with boundary flux; hence well-posedness and causal support.

* * *

##### 4.14.2.14.13 The audit “passport” (what to staple to any calculation)
--------------------------------------------------------------

When you finish a derivation or a solve, attach a **one-page passport**:

1.  **Locks & BCs:** phase/sign convention; BC menu; compensator cited.
2.  **Ghost check:** canonical positivity; projector residue table.
3.  **Constraints:** list and DOF count.
4.  **Hyperbolicity:** principal symbol; symmetrizer; energy estimate.
5.  **Gauge independence:** slice parameter(s); Nielsen/BRST note.
6.  **Dispersion:** retarded prescription; DC corridor; Herglotz/K–K check.
7.  **Boundary:** DtN/Fredholm note; Rellich; ledger receipt (power/integers).
8.  **Numerics (if any):** MT pair; spaces; CFL; window; error bars.

If each line reads **PASS**, the calculation is not only correct—it is **auditable** by anyone adopting the same ruler.

* * *

**What you gain.** With these audits, every piece of the theory—and every result you state—comes with a **warranty card**: ghosts excluded, cones respected, slices irrelevant, edges accounted for, and DC behavior honest. The entire chapter becomes not just a proposal but a **certified system**.

### 4.14.3 Connectivity Map
**Within Chapter 4 (closely related):**
- §4.1 — Introduction — from textbook physics to UGFT
- §4.2 — Eponyms
- §4.3 — Classical starting point — standard actions & EOM
- §4.4 — UGFT action (bulk, boundary, topology) and the MGSP1 policy
- §4.5 — Miller Field Equation Set (MFES) — full classical system
- §4.6 — Stress–energy and positivity (sign-locked, per sector)
- §4.7 — The Miller Equivalence Theorem (MET) — statement & proof sketch
- §4.8 — Equivalence-first computation (MEFP) and MPSD lanes
- §4.9 — Causality, hyperbolicity, response & dispersion (MDPC)
- §4.10 — Boundary, uniqueness, topology & ledgers (MBLC + MLCP)
- §4.11 — Spectral standardization — the Miller Transform (MT)
- §4.12 — Sanity limits & effective descriptions
- §4.13 — Legacy & intermediate forms

**External chapters (C#):**
- C1 §0–1.7
- C2 §27
- C5 §5.52

---

