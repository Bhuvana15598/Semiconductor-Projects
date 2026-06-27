Goal:
1. Compute and plot the direct bandgap of AlGaAs as a function of aluminum composition x, using the standard empirical interpolation formula (valid in the direct-gap regime, x < 0.45).

Reference formula (widely used, e.g. Adachi / Vurgaftman & Meyer):
    Eg(x) = 1.424 + 1.247*x   [eV]   for 0 <= x < 0.45  (direct gap, Gamma valley)

Beyond x ~ 0.45, AlGaAs becomes an indirect-gap semiconductor (X valley minimum drops below the Gamma valley). 

Plot:

<img width="800" height="500" alt="AlGaAs Bandgap vs Al Fraction" src="https://github.com/user-attachments/assets/014f989c-15e2-4f0a-867d-fe452c211162" />

<img width="312" height="136" alt="image" src="https://github.com/user-attachments/assets/e4ffa7ae-5d1d-449f-b8ec-82c23d647537" />



In this plot bandgap increases linearly from 1.424 eV (pure GaAs) to ~1.99 eV at x = 0.45. Beyond this composition, AlGaAs becomes an indirect-gap semiconductor (not modeled here).
