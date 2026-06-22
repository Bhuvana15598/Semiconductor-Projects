import numpy as np
import matplotlib.pyplot as plt

# Material parameters: GaN and AlN
GaN = {
    "a0":   0.3189,   # lattice constant (nm)
    "P_sp": -0.029,   # spontaneous polarization (C/m²)
    "e31":  -0.49,    # piezoelectric coefficient (C/m²)
    "e33":   0.73,    # piezoelectric coefficient (C/m²)
    "C13": 103,       # elastic constant (GPa)
    "C33": 405,        # elastic constant (GPa)
    "Eg" : 3.44       # eV

}

AlN = {
    "a0":   0.3112,
    "P_sp": -0.081,
    "e31":  -0.60,
    "e33":   1.46,
    "C13": 108,
    "C33": 373,
    "Eg" : 6.28   
}

# Step A: Linear interpolation (Vegard's law)

def algan_parameter(x, value_GaN, value_AlN):
    result = x * value_AlN + (1 - x) * value_GaN
    return result

# Step B: Get all AlGaN properties for Al fraction x

def get_algan_properties(x):
    algan = {}
    for key in GaN:
        algan[key] = algan_parameter(x, GaN[key], AlN[key])
    return algan

# Step C: Piezoelectric polarization of strained AlGaN

def piezoelectric_polarization(algan_props, a_GaN):
    a = algan_props["a0"]      # relaxed AlGaN lattice constant
    e31 = algan_props["e31"]
    e33 = algan_props["e33"]
    C13 = algan_props["C13"]
    C33 = algan_props["C33"]

    # in-plane strain
    strain = (a_GaN - a) / a

    # piezoelectric polarization
    Ppz = 2 * strain * (e31 - e33 * (C13 / C33))

    return Ppz

# Step D: Total polarization sheet charge density

def sheet_charge_density(x):
    algan_props = get_algan_properties(x)

    Psp_algan = algan_props["P_sp"]
    Psp_gan = GaN["P_sp"]

    Ppz_algan = piezoelectric_polarization(algan_props, GaN["a0"])

    # polarization discontinuity
    sigma = (Psp_algan - Psp_gan) + Ppz_algan

    return abs(sigma)

# Calculating Conduction band (This is the new addition)

def conduction_band_offset(x):

    Eg_algan = algan_parameter(
        x,
        GaN["Eg"],
        AlN["Eg"]
    )

    delta_Eg = Eg_algan - GaN["Eg"]

    delta_Ec = 0.70 * delta_Eg

    return delta_Ec

# Step E: Calculate 2DEG density

q = 1.602e-19  # electron charge (C)

def sheet_carrier_density(x):
    sigma = sheet_charge_density(x)

    # carriers/m²
    ns_m2 = sigma / q

    # convert to cm^-2
    ns_cm2 = ns_m2 / 1e4

    return ns_cm2

# Generate data


x_values = np.linspace(0.0, 0.40, 41)

sigma_values = [sheet_charge_density(x) for x in x_values]
ns_values = [sheet_carrier_density(x) for x in x_values]


# Print sample values


print("Al Fraction    Sheet Charge (C/m²)    2DEG Density (cm⁻²)")
print("-" * 55)

for x in [0.15, 0.20, 0.25, 0.30]:
    sigma = sheet_charge_density(x)
    ns = sheet_carrier_density(x)

    print(f"{x:8.2f}      {sigma:10.4f}         {ns:.3e}")

    x = 0.30

delta_Ec = conduction_band_offset(x)

print(f"x = {x:.2f}")
print(f"Conduction Band Offset = {delta_Ec:.3f} eV")


# Graph 1: Polarization Components


Psp_diff_values = []
Ppz_values = []
sigma_total_values = []

for x in x_values:
    props = get_algan_properties(x)

    Psp_diff = abs(props["P_sp"] - GaN["P_sp"])
    Ppz = abs(piezoelectric_polarization(props, GaN["a0"]))
    sigma = abs(Psp_diff + Ppz)

    Psp_diff_values.append(Psp_diff)
    Ppz_values.append(Ppz)
    sigma_total_values.append(sigma)

plt.figure(figsize=(8,5))

plt.plot(x_values, Psp_diff_values, marker='o',
         label='Spontaneous Polarization')

plt.plot(x_values, Ppz_values, marker='s',
         label='Piezoelectric Polarization')

plt.plot(x_values, sigma_total_values, marker='^',
         linewidth=2,
         label='Total Sheet Charge Density')

plt.xlabel('Al mole fraction (x)')
plt.ylabel('Polarization (C/m²)')
plt.title('Polarization Contributions in AlGaN/GaN')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# Graph 2: 2DEG Density


plt.figure(figsize=(8,5))

plt.plot(x_values, ns_values,
         marker='o',
         linewidth=2)

plt.xlabel('Al mole fraction (x)')
plt.ylabel('2DEG Density (cm$^{-2}$)')
plt.title('2DEG Density vs Al Fraction')

plt.ticklabel_format(style='sci',
                     axis='y',
                     scilimits=(0,0))

plt.grid(True)
plt.tight_layout()
plt.show()

# Graph 3: Band Diagram


x_al = 0.30

# Conduction band offset
delta_Ec = conduction_band_offset(x_al)

# Polarization charge density
sigma = sheet_charge_density(x_al)

# Permittivity of AlGaN
eps0 = 8.854e-12          # F/m
eps_r = 9.0               # approximate AlGaN dielectric constant
eps = eps_r * eps0

# Controlled band bending
bend_amount = 0.6   # eV across barrier

# Electric field in AlGaN
E_field = sigma / eps     # V/m

# Barrier thickness
t_barrier_nm = 20
t_barrier_m = t_barrier_nm * 1e-9

# Position axis
x1 = np.linspace(0, t_barrier_nm, 200)      # AlGaN
x2 = np.linspace(t_barrier_nm, 100, 300)    # GaN

# Band bending in AlGaN
Ec_algan = delta_Ec - bend_amount * (x1 / t_barrier_nm)
#Ec_algan = delta_Ec - E_field * (x1 * 1e-9)

# Shift so interface energy matches GaN reference
Ec_algan = Ec_algan - Ec_algan[-1]

# Simple triangular well in GaN
Ec_gan = -0.15 * np.exp(-(x2 - t_barrier_nm)/10)    
# Ec_gan = Ec_algan[-1] - 0.15 * np.exp(-(x2 - t_barrier_nm)/10)

# Plot
plt.figure(figsize=(9,5))

plt.plot(x1, Ec_algan, linewidth=3, label='AlGaN')
plt.plot(x2, Ec_gan, linewidth=3, label='GaN')

plt.axvline(t_barrier_nm,
            linestyle='--',
            color='black',
            label='Interface')

plt.xlabel("Position (nm)")
plt.ylabel("Conduction Band Energy (eV)")
plt.title(f"Band Bending in AlGaN/GaN HEMT (x = {x_al:.2f})")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
