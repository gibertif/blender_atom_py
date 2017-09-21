# Coloring and Size scheme
# Number, Name, Symbol, (RGB color), radius 

ELEMENTS_DEFAULT = (
( 1,      "Hydrogen",        "H", (  1.0,   1.0,   1.0), 0.32),
( 2,        "Helium",       "He", ( 0.85,   1.0,   1.0), 0.93),
( 3,       "Lithium",       "Li", (  0.8,  0.50,   1.0), 1.23),
( 4,     "Beryllium",       "Be", ( 0.76,   1.0,   0.0), 0.90),
( 5,         "Boron",        "B", (  1.0,  0.70,  0.70), 0.82),
( 6,        "Carbon",        "C", ( 0.56,  0.56,  0.56), 0.77),
( 7,      "Nitrogen",        "N", ( 0.18,  0.31,  0.97), 0.75),
( 8,        "Oxygen",        "O", (  1.0,  0.05,  0.05), 0.73),
( 9,      "Fluorine",        "F", ( 0.56,  0.87,  0.31), 0.72),
(10,          "Neon",       "Ne", ( 0.70,  0.89,  0.96), 0.71),
(11,        "Sodium",       "Na", ( 0.67,  0.36,  0.94), 1.54),
(12,     "Magnesium",       "Mg", ( 0.54,   1.0,   0.0), 1.36),
(13,     "Aluminium",       "Al", ( 0.74,  0.65,  0.65), 1.18),
(14,       "Silicon",       "Si", ( 0.94,  0.78,  0.62), 1.11),
(15,    "Phosphorus",        "P", (  1.0,  0.50,   0.0), 1.06),
(16,        "Sulfur",        "S", (  1.0,   1.0,  0.18), 1.02),
(17,      "Chlorine",       "Cl", ( 0.12,  0.94,  0.12), 0.99),
(18,         "Argon",       "Ar", ( 0.50,  0.81,  0.89), 0.98),
(19,     "Potassium",        "K", ( 0.56,  0.25,  0.83), 2.03),
(20,       "Calcium",       "Ca", ( 0.23,   1.0,   0.0), 1.74),
(21,      "Scandium",       "Sc", ( 0.90,  0.90,  0.90), 1.44),
(22,      "Titanium",       "Ti", ( 0.74,  0.76,  0.78), 1.32),
(23,      "Vanadium",        "V", ( 0.65,  0.65,  0.67), 1.22),
(24,      "Chromium",       "Cr", ( 0.54,   0.6,  0.78), 1.18),
(25,     "Manganese",       "Mn", ( 0.61,  0.47,  0.78), 1.17),
(26,          "Iron",       "Fe", ( 0.87,   0.4,   0.2), 1.17),
(27,        "Cobalt",       "Co", ( 0.94,  0.56,  0.62), 1.16),
(28,        "Nickel",       "Ni", ( 0.31,  0.81,  0.31), 1.15),
(29,        "Copper",       "Cu", ( 0.78,  0.50,   0.2), 1.17),
(30,          "Zinc",       "Zn", ( 0.49,  0.50,  0.69), 1.25),
(31,       "Gallium",       "Ga", ( 0.76,  0.56,  0.56), 1.26),
(32,     "Germanium",       "Ge", (  0.4,  0.56,  0.56), 1.22),
(33,       "Arsenic",       "As", ( 0.74,  0.50,  0.89), 1.20),
(34,      "Selenium",       "Se", (  1.0,  0.63,   0.0), 1.16),
(35,       "Bromine",       "Br", ( 0.65,  0.16,  0.16), 1.14),
(36,       "Krypton",       "Kr", ( 0.36,  0.72,  0.81), 1.31),
(37,      "Rubidium",       "Rb", ( 0.43,  0.18,  0.69), 2.16),
(38,     "Strontium",       "Sr", (  0.0,   1.0,   0.0), 1.91),
(39,       "Yttrium",        "Y", ( 0.58,   1.0,   1.0), 1.62),
(40,     "Zirconium",       "Zr", ( 0.58,  0.87,  0.87), 1.45),
(41,       "Niobium",       "Nb", ( 0.45,  0.76,  0.78), 1.34),
(42,    "Molybdenum",       "Mo", ( 0.32,  0.70,  0.70), 1.30),
(43,    "Technetium",       "Tc", ( 0.23,  0.61,  0.61), 1.27),
(44,     "Ruthenium",       "Ru", ( 0.14,  0.56,  0.56), 1.25),
(45,       "Rhodium",       "Rh", ( 0.03,  0.49,  0.54), 1.25),
(46,     "Palladium",       "Pd", (  0.0,  0.41,  0.52), 1.28),
(47,        "Silver",       "Ag", ( 0.75,  0.75,  0.75), 1.34),
(48,       "Cadmium",       "Cd", (  1.0,  0.85,  0.56), 1.48),
(49,        "Indium",       "In", ( 0.65,  0.45,  0.45), 1.44),
(50,           "Tin",       "Sn", (  0.4,  0.50,  0.50), 1.41),
(51,      "Antimony",       "Sb", ( 0.61,  0.38,  0.70), 1.40),
(52,     "Tellurium",       "Te", ( 0.83,  0.47,   0.0), 1.36),
(53,        "Iodine",        "I", ( 0.58,   0.0,  0.58), 1.33),
(54,         "Xenon",       "Xe", ( 0.25,  0.61,  0.69), 1.31),
(55,       "Caesium",       "Cs", ( 0.34,  0.09,  0.56), 2.35),
(56,        "Barium",       "Ba", (  0.0,  0.78,   0.0), 1.98),
(57,     "Lanthanum",       "La", ( 0.43,  0.83,   1.0), 1.69),
(58,        "Cerium",       "Ce", (  1.0,   1.0,  0.78), 1.65),
(59,  "Praseodymium",       "Pr", ( 0.85,   1.0,  0.78), 1.65),
(60,     "Neodymium",       "Nd", ( 0.78,   1.0,  0.78), 1.64),
(61,    "Promethium",       "Pm", ( 0.63,   1.0,  0.78), 1.63),
(62,      "Samarium",       "Sm", ( 0.56,   1.0,  0.78), 1.62),
(63,      "Europium",       "Eu", ( 0.38,   1.0,  0.78), 1.85),
(64,    "Gadolinium",       "Gd", ( 0.27,   1.0,  0.78), 1.61),
(65,       "Terbium",       "Tb", ( 0.18,   1.0,  0.78), 1.59),
(66,    "Dysprosium",       "Dy", ( 0.12,   1.0,  0.78), 1.59),
(67,       "Holmium",       "Ho", (  0.0,   1.0,  0.61), 1.58),
(68,        "Erbium",       "Er", (  0.0,  0.90,  0.45), 1.57),
(69,       "Thulium",       "Tm", (  0.0,  0.83,  0.32), 1.56),
(70,     "Ytterbium",       "Yb", (  0.0,  0.74,  0.21), 1.74),
(71,      "Lutetium",       "Lu", (  0.0,  0.67,  0.14), 1.56),
(72,       "Hafnium",       "Hf", ( 0.30,  0.76,   1.0), 1.44),
(73,      "Tantalum",       "Ta", ( 0.30,  0.65,   1.0), 1.34),
(74,      "Tungsten",        "W", ( 0.12,  0.58,  0.83), 1.30),
(75,       "Rhenium",       "Re", ( 0.14,  0.49,  0.67), 1.28),
(76,        "Osmium",       "Os", ( 0.14,   0.4,  0.58), 1.26),
(77,       "Iridium",       "Ir", ( 0.09,  0.32,  0.52), 1.27),
(78,     "Platinium",       "Pt", ( 0.81,  0.81,  0.87), 1.30),
(79,          "Gold",       "Au", (  1.0,  0.81,  0.13), 1.34),
(80,       "Mercury",       "Hg", ( 0.72,  0.72,  0.81), 1.49),
(81,      "Thallium",       "Tl", ( 0.65,  0.32,  0.30), 1.48),
(82,          "Lead",       "Pb", ( 0.34,  0.34,  0.38), 1.47),
(83,       "Bismuth",       "Bi", ( 0.61,  0.30,  0.70), 1.46),
(84,      "Polonium",       "Po", ( 0.67,  0.36,   0.0), 1.46),
(85,      "Astatine",       "At", ( 0.45,  0.30,  0.27), 1.45),
(86,         "Radon",       "Rn", ( 0.25,  0.50,  0.58), 1.00),
(87,      "Francium",       "Fr", ( 0.25,   0.0,   0.4), 1.00),
(88,        "Radium",       "Ra", (  0.0,  0.49,   0.0), 1.00),
(89,      "Actinium",       "Ac", ( 0.43,  0.67,  0.98), 1.00),
(90,       "Thorium",       "Th", (  0.0,  0.72,   1.0), 1.65),
(91,  "Protactinium",       "Pa", (  0.0,  0.63,   1.0), 1.00),
(92,       "Uranium",        "U", (  0.0,  0.56,   1.0), 1.42),
(93,     "Neptunium",       "Np", (  0.0,  0.50,   1.0), 1.00),
(94,     "Plutonium",       "Pu", (  0.0,  0.41,   1.0), 1.00),
(95,     "Americium",       "Am", ( 0.32,  0.36,  0.94), 1.00),
(96,        "Curium",       "Cm", ( 0.47,  0.36,  0.89), 1.00),
(97,     "Berkelium",       "Bk", ( 0.54,  0.30,  0.89), 1.00),
(98,   "Californium",       "Cf", ( 0.63,  0.21,  0.83), 1.00),
(99,   "Einsteinium",       "Es", ( 0.70,  0.12,  0.83), 1.00),
(100,       "Fermium",       "Fm", ( 0.70,  0.12,  0.72), 1.00),
(101,   "Mendelevium",       "Md", ( 0.70,  0.05,  0.65), 1.00),
(102,      "Nobelium",       "No", ( 0.74,  0.05,  0.52), 1.00),
(103,    "Lawrencium",       "Lr", ( 0.78,   0.0,   0.4), 1.00),
(104,       "Vacancy",      "Vac", (  0.5,   0.5,   0.5), 1.00),
(105,       "Default",  "Default", (  1.0,   1.0,   1.0), 1.00),
(106,         "Stick",    "Stick", (  0.5,   0.5,   0.5), 1.00),
)
