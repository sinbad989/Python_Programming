[TOC]

# Prologue : an atomistic view of electrical resistance

Understanding the flow of of current through a very small object that has only one energy level in the energy range of interest doesn't require significant background in quantum mechanics. What requires quantum mechanics is in understanding where the energy levels come from and in the description of large conductors with multiple energy levels. 



To start, we have to understand the factor that influence the current-voltage relation of a really small object. 

**Top-down:**

the conductance G (inverse of resistance) of a large macroscopic conductor is directly proportional to its cross-sectional area *A* and inversely proportional to its length *L*, as given by the Ohm's law:


$$
G = \sigma A/L
$$
To measure conductivity of anything we need to attach two large contact pads to it, across which a battery can be connected. 

- no one knew how to attach contact pads to a small molecule till the late twentieth century, and so no one knew what the conductance of a really small object was

**Bottom-up**: 

But now, we are able to measure the conductance of small objects.

Traditional top-down approach tend to obscure the physics of very small conductors 



Generic structure used: a simple version of a "nanotransistors"

- it is consist of a semiconducting channel separated by an insulator layer from the metallic gate 
  - the regions marked source and drain are the two contact pads, assumed to be highly conducting 
- The resistance of the channel determines the current that flows from the source to the drain when a voltage $V_D$ is applied between them. The voltage $V_G$ on the gate is used to control the electron density in the channel and hence its resistance. 



The nanotransistor discussed is actually the essence of any field effect transistor (FET) although the details differ from one version to another. 

- the channel length have progressively reduced in 1960 (from ~10 $\mu​$m) to 2000 (from ~0.1 $\mu​$m), allowing circuit designers to pack $(100)^2​$ = 10000 times more transistors (and hence more computing power) into a chip of a given surface

  > This increase in packing density is at the heart of the computer revolution 

**How much longer can the downscaling continue?**

Regardless of what form future electronics devices take, we will have to learn how to model and describe the electronic properties of device structure that are engineered on an atomic scale



## Outline 



**(1.1)**  Energy level diagram

to model the flow of current, the first step is to draw an equilibrium energy level diagram and locate the electrochemical potential $\mu$ (also called the Fermi level or Fermi energy) set by the source and drain contacts.

**(1.2)**  What makes electron flow? 

current flows when an external device such as a battery maintains the two contacts at different electrochemical potentials $\mu_1$ and $\mu_2$, driving the channel into a non-equilibrium state

- current through a really small device with only one energy level in the range of interest is easily calculated, and depends on the quality of the contacts 

**(1.3)** The quantum conductance

- what is not obvious is that there is a maximum conductance for a channel with one level, which is a fundamental constant related to the charge on an electron and Planck's constant

$$
G_0 = \frac{q^2}{h} = 38.7 \mu S
$$

  	Small channels typically have two levels (one spin up and one spin down) at the same energy 	(degenerate level) making maximum conductance equal to $2G_0$. The point is that there is an upper limit to the conductance that can be achieved even with the most perfect contacts. 

**(1.4)** Potential Profile

in this section, the important role played by charging and electrostatics in determining the shape of the current-voltage (I-V) characteristics, and how this aspect is coupled with the equations for quantum transport. 

> Once this aspect has been incorporated we have all the basic physics needed to describe a one-level channel that is coupled "well" to the contacts.

**(1.5)** Coulomb blockade

If the channel is weakly coupled, there is additional physics that will be discussed 

**(1.6)** Towards Ohm's Laws

How the one-level description is extended to larger devices with multiple energy levels, eventually leading to Ohm's law. It is this extension to larger devices that requires the advanced concepts of quantum statistical mechanics that constitute the subject matter of the rest of the this book. 

## 1.1 Energy Level Diagram

The first step in understanding the operation of any inhomogeneous device structure is to draw an *equilibrium* energy level diagram (sometimes called the *band diagram*) assuming that there is no voltage applied between the source and the drain. 

> Electrons in a semiconductor occupy a set of energy levels that form bands. 



**Negative differential resistance (NDR)**: a decrease in the current with an increase in the voltage

**Fermi function:** 

if the source and drain regions are coupled to the channel then electrons will flow out of the device bringing them all in equilibrium with a common electrochemical potential $\mu$. In this equilibrium state, the average number of electrons in any energy level is typically not an integer, but is given by the Fermi function: 
$$
f_0(E-\mu) = \frac{1}{1+exp[(E-\mu)/k_BT]}
$$
Energy levels far below $\mu$ are always full so that $f_0 = 1$, while energy levels far above $\mu$ are always empty with $f_0 = 0$. 

The average number of electrons lies between 0 and 1: $0 \leq f_0 \leq 1$. 

> Note: this number cannot exceed one because the exclusion principle forbids more than one electron per level. 

**n-type operation:**

**p-type operation:** 

## 1.2 What makes electron flow? 

Conduction depends on the availability of states around $E=\mu$; **it does not matter if they are empty or filled.** To understand why, consider what makes an electron flow from the source to the drain. 



The batter between contacts lowers the energy levels in the drain with respect to the source contact and maintains them at distinct electrochemical potentials separated by $qV_D$
$$
\mu_1 - \mu_2 = q V_D
$$
giving rise to two different Fermi functions: 
$$
f_1(E) \equiv \frac{1}{1+exp[(E-\mu_1)/k_B T]} = f_0(E-\mu_1) \\
f_2(E) \equiv \frac{1}{1+exp[(E-\mu_2)/k_B T]} = f_0(E-\mu_2)
$$
**The contact seeks to bring the channel into equilibrium with itself.** The source keeps pumping electrons into it, hoping to establish equilibrium. But equilibrium is never achieved as the drain keeps pulling electrons out in its bid to establish equilibrium with itself. This **sends the channel into an non-equilibrium state** *intermediate between what the source would like to see and what the drain would like to see.* 



**Rate equations for a one-level model:**

Consider a simple one-level system, biased such that its energy $ \varepsilon ​$ lies between the electrochemical potentials in the two contacts. 

Net flux across the left junction: 
$$
I_1 = \frac{q\gamma_1}{\hbar}(f_1 - N)
$$
Net flux across the right junction: 
$$
I_2 = \frac{q\gamma_1}{\hbar}(f_2 - N)
$$
The rate constants $\frac{\gamma_1}{\hbar}. \frac{\gamma_2}{\hbar}$ are the rates at which an electron placed initially in the level $\varepsilon$ will escape into the source and drain contacts respectively. 

 **Current in a one-level model:**

At steady state there is no flux into or out of the channel $I_1 + I_2 = 0$, so that we obtain the reasonable result: 
$$
N = \frac{\gamma_1 f_1 + \gamma_2 f_2}{\gamma_1  + \gamma_2}
$$
N is the weighted average of what contacts 1 and 2 would like to see. Inserting this equation to the net flux of the steady-state current: 
$$
\begin{align*}
I &= I_1=\frac{q\gamma_1}{\hbar}(f_1 - N) \\
&= \frac{q\gamma_1}{\hbar}\bigg(f_1 -\frac{\gamma_1 f_1 + \gamma_2 f_2}{\gamma_1  + \gamma_2} \bigg) \\
I &=\frac{q}{\hbar} \frac{\gamma_1\gamma_2}{\gamma_1  + \gamma_2} [f_1(\varepsilon) - f_2(\varepsilon)]
\end{align*}
$$

>  This is the current per spin. We should multiply it by two if there are two spin states with the same energy.

This results illustrate certain basic facts about the process of current flow: 

**Cases of no current flow: **

case 1: $f_1(\varepsilon)  = f_2(\varepsilon)  ​$

- same fermi functions

case 2: $f_1 (\varepsilon) = f_2(\varepsilon)  = 1​$

- when the level is way below both electrochemical potentials 

case 3: $f_1 (\varepsilon) = f_2 (\varepsilon) = 0 $

- a level that is way above both potentials $\mu_1$ and $\mu_2$

**Case with current flow:**

It is only when the level lies within a few $k_B T​$ of the potentials $\mu_1 , \mu_2​$ that we have $f_1(\varepsilon) \neq f_1(\varepsilon) ​$ and current flows. 

> Current flow is thus the result of the "difference in agenda" between the contacts. 
>
> - the current is in the direction opposite to that of the flux of electrons, since electrons have negative charge. 

We can reason from here why the process of conduction requires the presence of state around $E =\mu$ but does not matter if its empty or filled. 

- with empty states, e are first injected by the negative contacts and subsequently collected by the positive contact. 
- for filled states, e are first collected by the positive contacts and subsequently refilled by the negative contact. 

> Either way, we have a current flowing in the external circuit of the same direction. 



## 1.3 The quantum of conductance 

> Consider a device with a small voltage applied across it causing a splitting of the source and drain potentials. 

We can write the current through this device and simplify it by assuming $\mu_1 > \varepsilon > \mu_2$ and the temperature is low enough that $f_1(\varepsilon) \equiv f_0 (\varepsilon - \mu_1 ) \approx 1$ and $f_2(\varepsilon) \equiv f_0 (\varepsilon - \mu_2 ) \approx 0$: 
$$
I = \frac{q}{\hbar} \frac{\gamma_1 \gamma_2}{\gamma_1 + \gamma_2} = \frac{q\gamma_1}{\hbar} \text{ if } \gamma_1=\gamma_2
$$
 

This suggests that we could pump unlimited current through this one-level device by increasing $\gamma_1$, that is by coupling it more and more strongly to the contacts. 

- one seminal results of mesoscopic physics is that the maximum conductance of a one-level device is equal to $G_0$

**WHAT HAVE WE MISSED?** 

What we have missed is the **broadening** of the level that inevitably accompanies any process of coupling to it. This causes part of the energy level to spread outside the energy range between $\mu_1$ and $\mu_2$ where current flows. 

- the actual current is then reduced below what we expect from (eq. 12) by a factor $(\mu_1 - \mu_2)/C\gamma_1$ representing the fraction of the level that lies in the window between $\mu_1$ and $\mu_2$, where $C \gamma_1$ is the effective width of the level, C being a numerical constant. Since $\mu_1 - \mu_2 = qV_D$, we see from equation 12, 
  $$
  I =  \frac{q\gamma_1}{2\hbar} \frac{qV_D}{C\gamma_1} = \frac{q^2 V_D}{2\hbar C} \rightarrow G = \frac{I}{V_D} = \frac{q^2}{2\hbar C}
  $$
  The conductance approaches a constant value independent of the strength of the coupling to the constants in this case. But what is C? How do we obtain the value of C? 

   

- We will now, carry out calculations so as to obtain a better estimate for C.

Broadening is closely related to the density of state (DOS). Note that before we couple the channel to the source and drain, the DOS $D(E)$ have one sharp level in the channel and continuous distribution of states in the contacts. 

On coupling, these states "spill over": the channel loses part of its state as it spreads into the contacts, but also gain part of the contact state that spread into the channel. This results to a more diffuse structure from its initial sharp structure. 

> Integrated over all energy, the level can still hold only one electron. In chapter 8, we will see that there is a "sum rule" that requires the loss to be exactly offset by the gain.



The broadened DOS could in principle have any shape, but in the simplest situation it is described by a Lorentzian function centered around $E = \varepsilon$ (whose integral over all energy is equal to one): 
$$
D_{\varepsilon}(E) = \frac{\gamma/2\pi}{(E-\varepsilon)^2 + (\gamma/2)^2}
$$
where the broadening $\gamma$ turns out that $\gamma = \gamma_1 + \gamma_2$, where $\gamma_1, \gamma_2$ are the escape rates. 

Note: in general the lineshape need not be Lorentzian and this is usually reflected in an energy-dependent broadening $\gamma(E)$. 

**Bottom line:**  the coupling to the contacts broadens a single discrete energy level into a continuous density of states given by equation 14.

We can include this effect by modifying our expression for the current: 
$$
\begin{align}

I &=\frac{q}{\hbar} \frac{\gamma_1\gamma_2}{\gamma_1  + \gamma_2} [f_1(\varepsilon) - f_2(\varepsilon)] \rightarrow I =\frac{q}{\hbar}\int_{-\infin}^{+\infin} dE D_{\varepsilon}(E) \frac{\gamma_1\gamma_2}{\gamma_1  + \gamma_2} [f_1(E) - f_2(E)]
\end{align}
$$

>  Note: the change of variable in the Fermi function from channel energy $\varepsilon $ to a continuous energy $E$

At low temperatures, we can write: 
$$
f_1(E)-f_2(E)=\begin{cases}
    &1,& \text{ if }\text{ } \mu_1 >E>\mu_2\\
    &0,              & \text{otherwise}
\end{cases}
$$
so that the current is given by 
$$
I =\frac{q}{\hbar} \frac{\gamma_1\gamma_2}{\gamma_1  + \gamma_2} \int_{-\mu_2}^{+\mu_1} dE D_{\varepsilon}(E)
$$
If the bias is small enough, we can assume that DOS to be constant over the range $\mu_1 >E>\mu_2$, we can rewrite the equation above as, 
$$
\begin{align*}
I &=\frac{q}{\hbar} \frac{\gamma_1\gamma_2}{\gamma_1  + \gamma_2} \int_{\mu_2}^{\mu_1} dE D_{\varepsilon}(E) \\
&= \frac{q}{\hbar} \frac{\gamma_1\gamma_2}{\gamma_1  + \gamma_2} D_{\varepsilon}(E) \int_{\mu_2}^{\mu_1} dE \\
&= \frac{q}{\hbar} \frac{\gamma_1\gamma_2}{\gamma_1  + \gamma_2} D_{\varepsilon}(E) (\mu_1 -\mu_2) \\
&=  \frac{q}{\hbar} \frac{\gamma_1\gamma_2}{\gamma_1  + \gamma_2}\frac{\gamma/2\pi} {(\mu-\varepsilon)^2 + (\gamma/2)^2} (\mu_1 -\mu_2) \\
I &=  \frac{q}{\hbar} \frac{\gamma_1\gamma_2}{\gamma_1  + \gamma_2}\frac{(\gamma_1 +\gamma_2)/2\pi} {(\mu-\varepsilon)^2 + ((\gamma_1 +\gamma_2)/2)^2} (\mu_1 -\mu_2) \\
\end{align*}
$$
Where $\mu$ is the average of $\mu_1, \mu_2$. 

The maximum current is obtained if the energy level $\varepsilon$ coincides with $\mu$. Noting that $\mu_1 - \mu_2 = qV_D$. 
$$
\begin{align*}

I &=  \frac{q}{\hbar} \frac{\gamma_1\gamma_2}{\gamma_1  + \gamma_2}\frac{(\gamma_1 +\gamma_2)/2\pi} {(\mu-\varepsilon)^2 + ((\gamma_1 +\gamma_2)/2)^2} (\mu_1 -\mu_2) \\
&= \frac{q}{\hbar} \frac{\gamma_1\gamma_2}{\gamma_1  + \gamma_2}\frac{(\gamma_1 +\gamma_2)/2\pi} { ((\gamma_1 +\gamma_2)/2)^2} qV_D \\
&= \frac{q}{\hbar} \frac{\gamma_1\gamma_2}{2\pi }\frac{4} { (\gamma_1 +\gamma_2)^2} qV_D \\
I &= \frac{q^2}{h} V_D\frac{4\gamma_1\gamma_2} { (\gamma_1 +\gamma_2)^2}  \\
\end{align*}
$$


If $\gamma_1 = \gamma_2 $, we can derive the maximum conductance:
$$
\begin{align*}

I &= \frac{q^2}{h} V_D\frac{4\gamma_1\gamma_2} { (\gamma_1 +\gamma_2)^2}  \\
\frac{I}{V_D} &= \frac{q^2}{h} \frac{4\gamma_1^2} { 4\gamma_1^2)} \\
G=\frac{I}{V_D} &=\frac{q^2}{h} 
\end{align*}
$$
Our revised expression for the current extends our earlier results to include the effect of broadening. Similarly, we can extend the expression for the number of electrons: 
$$
N = \frac{\gamma_1 f_1(\varepsilon) + \gamma_2 f_2(\varepsilon)}{\gamma_1  + \gamma_2} \rightarrow N = \int_{-\infin}^{+\infin} dE D_{\varepsilon}(E)\frac{\gamma_1 f_1(\varepsilon) + \gamma_2 f_2(\varepsilon)}{\gamma_1  + \gamma_2}
$$

## 1.4 Potential Profile 

**How do we calculate the potential inside the channel?** 

If the channel were an insulator, we could solve the Laplace's equation: 
$$
\nabla \cdot (\varepsilon_r \nabla V) = 0
$$
subject to the boundary conditions that $V = 0$ (source electrode), $V = V_G $ (gate electrode), and $V= V_D$ (drain electrode). 

