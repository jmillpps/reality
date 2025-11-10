# Chapter 4 (Sections 9-14)

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

**Propagation of singularities.** For normally hyperbolic operators, the wavefront set  $\mathrm{WF}(G^R)$  lies on the **bicharacteristic flow** generated by the Hamiltonian  $H(x,k)=\tfrac12 g^{\mu\nu}k_\mu k_\nu$ . This says: singular support rides null geodesics. The Hadamard form  $U\delta(\sigma)+V\theta(-\sigma)$  is the local expression of that transport;  $U$  obeys a transport equation along null geodesics,  $V$  solves an inhomogeneous recursion. We use this only to justify local causal support and to patch parametrices—no quantum inputs are needed.

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

For  $`P^\mu{}_\nu=\nabla_\alpha\nabla^\alpha\delta^\mu{}_\nu-\nabla^\mu\nabla_\nu`$ ,  
 $`\sigma(P)^\mu{}_\nu(x,k)=-k^2\delta^\mu{}_\nu + k^\mu k_\nu`$ .  
Eigenvalues vanish iff  $`k^2=0`$ . Hence the characteristic cone is the light cone, and the front is luminal.

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
    $`
    \gamma_t V=(n\times V)|_{\partial\Omega}\in H^{-1/2}(\mathrm{div}_{\partial\Omega}),\quad \gamma_n V=(n\!\cdot V)|_{\partial\Omega}\in H^{-1/2}(\partial\Omega),
    `$
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
    $`
    \nu_G=\frac{1}{8\pi^2}\int_{\mathcal M}\mathrm{Tr}(F\wedge F)\in \mathbb Z.
    `$
*   **Chern–Simons on a 3-manifold.** Write  $\mathcal A\equiv g A$ . Then
    $`
    S_{CS}=\frac{k}{4\pi g^2}\int_{\partial\mathcal M}\!\mathrm{Tr}\Big(\mathcal A\wedge d\mathcal A+\tfrac{2}{3}\mathcal A\wedge\mathcal A\wedge\mathcal A\Big),\quad k\in\mathbb Z,
    `$
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
     $`\displaystyle \int |f|^2=\int |\tilde f|^2`$  (time) and  $`\displaystyle \int |f|^2=\int |\tilde f|^2`$  (space–time), with no stray factors.
*   **Derivative dictionary:**  
     $`\partial_t \leftrightarrow i\omega,\ \nabla \leftrightarrow -i\mathbf k,\ \Box \leftrightarrow (-\omega^2+\mathbf k^2)`$ .
*   **Convolution/product:** a convolution in  $t$  (or in  $x$ ) becomes pointwise multiplication, times the same MT-c scale, so you never juggle inconsistent  $`2\pi`$  factors.

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

