Goal:
1. Compute the lattice constant of Al(x)Ga(1-x)As using Vegard's law (linear interpolation between AlAs and GaAs), then compute the lattice mismatch when this AlGaAs layer is grown on a GaAs substrate.

Vegard's law:
    a_AlGaAs(x) = x * a_AlAs + (1 - x) * a_GaAs

Lattice mismatch (strain source for the heterostructure):
    mismatch(x) = (a_AlGaAs(x) - a_GaAs) / a_GaAs

Note: AlAs and GaAs are almost perfectly lattice-matched (~0.1% mismatch at x=1), which is *exactly* why AlGaAs/GaAs is the classic "nearly strain-free" heterostructure 

Plot:

<img width="1200" height="500" alt="AlGaAs Lattice Constant   Mismatch" src="https://github.com/user-attachments/assets/5dbbc45c-4f37-4f85-96da-6c8ff5c732c8" />


<img width="476" height="155" alt="image" src="https://github.com/user-attachments/assets/32b4a90b-3600-4cd0-bea0-f6fe6271a791" />


Lattice constant rises gently with x; mismatch stays below 0.14% even at x = 1.
The key takeaway is AlGaAs/GaAs is almost strain-free
