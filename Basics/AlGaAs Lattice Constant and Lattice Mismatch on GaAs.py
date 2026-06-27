# Project 2: Lattice Constant and Lattice Mismatch of AlGaAs on GaAs


import numpy as np
import matplotlib.pyplot as plt


# Step 1: Define Al mole fraction range

x = np.linspace(0, 1.0, 100)


# Step 2: Lattice constants of binary endpoints (Angstrom, 300 K)

a_GaAs = 5.6533   # Angstrom
a_AlAs = 5.6611   # Angstrom


# Step 3: Vegard's law interpolation

a_AlGaAs = x * a_AlAs + (1 - x) * a_GaAs


# Step 4: Lattice mismatch relative to GaAs substrate

mismatch_percent = (a_AlGaAs - a_GaAs) / a_GaAs * 100  # in %


# Step 5: Plot both lattice constant and mismatch (two panels)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(x, a_AlGaAs, color='tab:green', linewidth=2, marker='o', markersize=3)
axes[0].set_title("Lattice Constant of AlGaAs vs Al Fraction")
axes[0].set_xlabel("Al mole fraction (x)")
axes[0].set_ylabel("Lattice constant (Å)")
axes[0].grid(True)

axes[1].plot(x, mismatch_percent, color='tab:red', linewidth=2, marker='s', markersize=3)
axes[1].set_title("Lattice Mismatch vs GaAs Substrate")
axes[1].set_xlabel("Al mole fraction (x)")
axes[1].set_ylabel("Mismatch (%)")
axes[1].grid(True)

plt.tight_layout()
plt.savefig("02_algaas_lattice_mismatch.png", dpi=150)
plt.show()


# Step 6: Print sample values

print("Al fraction (x) | Lattice const (Å) | Mismatch (%)")
for xi in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
    a_i = xi * a_AlAs + (1 - xi) * a_GaAs
    mismatch_i = (a_i - a_GaAs) / a_GaAs * 100
    print(f"     {xi:.2f}        |      {a_i:.4f}       |    {mismatch_i:.4f}")
