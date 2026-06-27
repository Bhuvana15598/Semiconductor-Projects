# Project 3: Conduction & Valence Band Offsets at the AlGaAs/GaAs Heterojunction

import numpy as np
import matplotlib.pyplot as plt


# Step 1: Define Al mole fraction range (direct-gap regime)

x = np.linspace(0, 0.45, 100)


# Step 2: Bandgap of AlGaAs and GaAs (from Project 0a formula)

Eg_GaAs = 1.424          # eV
slope = 1.247            # eV
Eg_AlGaAs = Eg_GaAs + slope * x


# Step 3: Total bandgap difference

dEg = Eg_AlGaAs - Eg_GaAs


# Step 4: Apply 60:40 band offset rule

dEc = 0.6 * dEg   # conduction band offset
dEv = 0.4 * dEg   # valence band offset


# Step 5: Plot

plt.figure(figsize=(8, 5))
plt.plot(x, dEc, label="Conduction Band Offset ($\\Delta E_c$)",
         marker='o', markersize=3, linewidth=2, color='tab:blue')
plt.plot(x, dEv, label="Valence Band Offset ($\\Delta E_v$)",
         marker='s', markersize=3, linewidth=2, color='tab:orange')
plt.title("Band Offsets at AlGaAs/GaAs Heterojunction (60:40 rule)")
plt.xlabel("Al mole fraction (x)")
plt.ylabel("Band offset (eV)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("03_algaas_band_offsets.png", dpi=150)
plt.show()


# Step 6: Print sample values

print("Al fraction (x) | dEg (eV) | dEc (eV) | dEv (eV)")
for xi in [0.0, 0.1, 0.2, 0.3, 0.4]:
    Eg_i = Eg_GaAs + slope * xi
    dEg_i = Eg_i - Eg_GaAs
    dEc_i = 0.6 * dEg_i
    dEv_i = 0.4 * dEg_i
    print(f"     {xi:.2f}        |  {dEg_i:.4f}  |  {dEc_i:.4f}  |  {dEv_i:.4f}")
