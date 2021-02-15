"""
Molar mass calculator by Redline Software
-----------------------------------------
Not for illegal or test/exam cheating use.
Redline Software does not take any responsibility for bugs and/or incorrect results. Use at your own risk.

2021 Redline Software
"""

from string import digits

element_names = {
    # Data from the Periodic Table
    "H": "Hydrogen",
    "He": "Helium",
    "Li": "Lithium",
    "Be": "Beryllium",
    "B": "Boron",
    "C": "Carbon",
    "N": "Nitrogen",
    "O": "Oxygen",
    "F": "Fluorine",
    "Ne": "Neon",
    "Na": "Sodium",
    "Mg": "Magnesium",
    "Al": "Aluminium",
    "Si": "Silicon",
    "P": "Phosphorus",
    "S": "Sulfur",
    "Cl": "Chlorine",
    "Ar": "Argon",
    "K": "Potassium",
    "Ca": "Calcium",
    "Sc": "Scandium",
    "Ti": "Titanium",
    "V": "Vanadium",
    "Cr": "Chromium",
    "Mn": "Manganese",
    "Fe": "Iron",
    "Co": "Cobalt",
    "Ni": "Nickel",
    "Cu": "Copper",
    "Zn": "Zinc",
    "Ga": "Gallium",
    "Ge": "Germanium",
    "As": "Arsenic",
    "Se": "Selenium",
    "Br": "Bromine",
    "Kr": "Krypton",
    "Rb": "Rubidium",
    "Sr": "Strontium",
    "Y": "Yttrium",
    "Zr": "Zirconium",
    "Nb": "Niobium",
    "Mo": "Molybdenum",
    "Tc": "Technetium",
    "Ru": "Ruthenium",
    "Rh": "Rhodium",
    "Pd": "Palladium",
    "Ag": "Silver",
    "Cd": "Cadmium",
    "In": "Indium",
    "Sn": "Tin",
    "Sb": "Antimony",
    "Te": "Tellurium",
    "I": "Iodine",
    "Xe": "Xenon",
    "Cs": "Caesium",
    "Ba": "Barium",
    "La": "Lanthanum",
    "Hf": "Hafnium",
    "Ta": "Tantalum",
    "W": "Tungsten",
    "Re": "Rhenium",
    "Os": "Osmium",
    "Ir": "Iridium",
    "Pt": "Platinum",
    "Au": "Gold",
    "Hg": "Mercury",
    "Tl": "Thallium",
    "Pb": "Lead",
    "Bi": "Bismuth",
    "Po": "Polonium",
    "At": "Astatine",
    "Rn": "Radon",
    "Fr": "Francium",
    "Ra": "Radium",
    "Ac": "Actinium",
    "Rf": "Rutherfordium",
    "Db": "Dubnium",
    "Sg": "Seaborgium",
    "Bh": "Bohrium",
    "Hs": "Hassium",
    "Mt": "Meitnerium",
    "Ce": "Cerium",
    "Pr": "Praseodymium",
    "Nd": "Neodymium",
    "Pm": "Promethium",
    "Sm": "Samarium",
    "Eu": "Europium",
    "Gd": "Gadolinium",
    "Tb": "Terbium",
    "Dy": "Dysprosium",
    "Ho": "Holmium",
    "Er": "Erbium",
    "Tm": "Thulium",
    "Yb": "Ytterbium",
    "Lu": "Lutetium",
    "Th": "Thorium",
    "Pa": "Protactinium",
    "U": "Uranium",
    "Np": "Neptunium",
    "Pu": "Plutonium",
    "Am": "Americium",
    "Cm": "Curium",
    "Bk": "Berkelium",
    "Cf": "Californium",
    "Es": "Einsteinium",
    "Fm": "Fermium",
    "Md": "Mendelevium",
    "No": "Nobelium",
    "Lr": "Lawrencium"
}

atom_weights = {
    # Data from the Periodic Table
    "H": 1.01,
    "He": 4.00,
    "Li": 6.94,
    "Be": 9.01,
    "B": 10.01,
    "C": 12.01,
    "N": 14.01,
    "O": 16.00,
    "F": 18.99,
    "Ne": 4.00,
    "Na": 22.99,
    "Mg": 24.30,
    "Al": 26.98,
    "Si": 28.09,
    "P": 30.97,
    "S": 32.06,
    "Cl": 35.45,
    "Ar": 39.95,
    "K": 39.10,
    "Ca": 40.08,
    "Sc": 44.96,
    "Ti": 47.90,
    "V": 50.94,
    "Cr": 52.00,
    "Mn": 54.94,
    "Fe": 55.85,
    "Co": 58.93,
    "Ni": 58.71,
    "Cu": 63.46,
    "Zn": 65.37,
    "Ga": 69.72,
    "Ge": 72.59,
    "As": 74.92,
    "Se": 78.96,
    "Br": 79.9,
    "Kr": 83.8,
    "Rb": 85.47,
    "Sr": 87.62,
    "Y": 88.90,
    "Zr": 91.22,
    "Nb": 92.91,
    "Mo": 95.94,
    "Tc": 99.00,
    "Ru": 101.07,
    "Rh": 102.9,
    "Pd": 106.4,
    "Ag": 107.88,
    "Cd": 112.40,
    "In": 114.82,
    "Sn": 118.69,
    "Sb": 121.75,
    "Te": 127.60,
    "I": 126.90,
    "Xe": 131.30,
    "Cs": 132.90,
    "Ba": 137.35,
    "La": 138.90,
    "Hf": 178.49,
    "Ta": 180.95,
    "W": 183.85,
    "Re": 186.20,
    "Os": 190.20,
    "Ir": 192.20,
    "Pt": 195.10,
    "Au": 196.99,
    "Hg": 200.59,
    "Tl": 204.37,
    "Pb": 207.19,
    "Bi": 208.98,
    "Po": 209,
    "At": 210,
    "Rn": 222,
    "Fr": 223,
    "Ra": 226,
    "Ac": 227,
    "Rf": 261,
    "Db": 262,
    "Sg": 263,
    "Bh": 262,
    "Hs": 265,
    "Mt": 268,
    "Ce": 140.12,
    "Pr": 140.90,
    "Nd": 144.24,
    "Pm": 147,
    "Sm": 150.36,
    "Eu": 151.95,
    "Gd": 157.25,
    "Tb": 158.92,
    "Dy": 162.50,
    "Ho": 164.93,
    "Er": 167.26,
    "Tm": 168.94,
    "Yb": 173.04,
    "Lu": 174.97,
    "Th": 232.04,
    "Pa": 231,
    "U": 238.03,
    "Np": 237,
    "Pu": 242,
    "Am": 243,
    "Cm": 247,
    "Bk": 247,
    "Cf": 249,
    "Es": 254,
    "Fm": 253,
    "Md": 256,
    "No": 254,
    "Lr": 257
}

molar_mass = 0

def add_element_mass():
    global molar_mass, element, multiplier
    if multiplier == "":
        multiplier = 1
    element_mass = atom_weights[element] * int(multiplier)
    molar_mass += element_mass
    print("%s x %s: %.2f g/mol" %(multiplier, element_names[element], element_mass))
    element = ""
    multiplier = ""

formula = input("Enter formula: ")
element = ""
multiplier = ""
for i, c in enumerate(formula):
    if c in digits:
        multiplier += c
        if i + 1 < len(formula):
            if not formula[i + 1] in digits:
                add_element_mass()
        else:
            add_element_mass()
    else:
        element += c
        if element in atom_weights.keys():
            if i + 1 < len(formula):
                if not element + formula[i + 1] in atom_weights.keys() and formula[i + 1] not in digits:
                    add_element_mass()
            else:
                add_element_mass()


print("Molar mass is: %.2f" %molar_mass)

