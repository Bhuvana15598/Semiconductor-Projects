# Project 1: Bandgap of Al(x)Ga(1-x)As as a function of Al mole fraction

import numpy as np
import matplotlib.pyplot as plt


# Step 1: Define Al mole fraction range (direct-gap regime only)

x = np.linspace(0, 0.45, 100)


# Step 2: Empirical direct bandgap formula for AlGaAs

Eg_GaAs = 1.424  # eV, bandgap of pure GaAs at 300 K
slope = 1.247    # eV, empirical bowing/slope coefficient (direct gap branch)

Eg = Eg_GaAs + slope * x


# Step 3: Plot

plt.figure(figsize=(8, 5))
plt.plot(x, Eg, marker='o', markersize=3, linewidth=2, color='tab:blue')
plt.title("Direct Bandgap of AlGaAs vs Al Mole Fraction")
plt.xlabel("Al mole fraction (x)")
plt.ylabel("Bandgap $E_g$ (eV)")
plt.grid(True)
plt.tight_layout()
plt.savefig("01_algaas_bandgap.png", dpi=150)
plt.show()


# Step 4: Print a few sample values

print("Al fraction (x) | Bandgap Eg (eV)")
for xi in [0.0, 0.1, 0.2, 0.3, 0.4]:
    Eg_i = Eg_GaAs + slope * xi
    print(f"     {xi:.2f}        |     {Eg_i:.4f}")
