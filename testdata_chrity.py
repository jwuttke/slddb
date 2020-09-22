"""
Material Data from Christy Kinane's table for testing database.
"""

from slddb import SLDDB
from slddb.dbconfig import DB_FILE

data=[   ['Si', 2.33, 0.0],
         ['Ag', 10.49, 0.0],
         ['Cr', 7.14, 0.0],
         ['Co', 8.9, 1.8],
         ['CoO', 6.4, 0.0],
         ['SiO2', 2.648, 0.0, 'Native Oxyde'],
         ['Ni ', 8.908, 0.6],
         ['Ta', 16.65, 0.0],
         ['Ru', 12.37, 0.0],
         ['MgO', 3.6, 0.0],
         ['Co20Fe60B20', 5.629, 1.68],
         ['Co40Fe40B20', 5.724, 1.6],
         ['Co60Fe20B20', 5.821, 1.52],
         ['Fe ', 7.874, 2.2],
         ['B', 2.46, 0.0],
         ['Mg', 1.738, 0.0],
         ['Ti', 4.507, 0.0],
         ['Pd', 12.023, 0.0],
         ['PdO', 8.3, 0.0],
         ['NiO', 6.7, 0.0],
         ['BiFe0.5Mn0.5O3', 8.3, 0.0],
         ['Sr', 2.63, 0.0],
         ['SrTiO3', 5.175, 0.0, 'STO'],
         ['V', 6.11, 0.0],
         ['VCr', 6.584, 0.0],
         ['Si', 2.33, 0.0],
         ['SiO2', 2.2, 0.0, 'fused SiO2 (Quartz)'],
         ['Mg', 1.738, 0.0],
         ['Ti', 4.507, 0.0],
         ['Pd', 12.023, 0.0],
         ['PdO', 8.3, 0.0],
         ['MgO', 3.6, 0.0],
         ['TiO', 4.95, 0.0],
         ['MgH2', 1.45, 0.0],
         ['TiH2', 3.75, 0.0],
         ['VH', 5.55, 0.0],
         ['CrH', 6.426, 0.0],
         ['Al', 2.7, 0.0],
         ['V4Cr6', 6.688, 0.0],
         ['V6Cr4', 6.484, 0.0],
         ['V8Cr2', 6.291, 0.0],
         ['GaAs', 5.3176, 0.0],
         ['VH2CrH8', 6.907, 0.0],
         ['VH4CrH6', 6.688, 0.0],
         ['VH6CrH4', 6.484, 0.0],
         ['VH8CrH2', 6.291, 0.0],
         ['Eu', 5.244, 0.0],
         ['Co0.5Fe0.5Si', 2.884, 1.0],
         ['Nb', 8.57, 0.0],
         ['Ho', 8.795, 0.0],
         ['IrMn', 11.23476, 0.0],
         ['Ir', 22.65, 0.0],
         ['Mn', 7.47, 4.0],
         ['Ni2MnGa', 8.0, 0.0],
         ['C60', 1.65, 0.0],
         ['Ir80Mn20', 16.10465, 0.0],
         ['CoF2', 4.43, 0.0],
         ['FeF2', 4.09, 0.0],
         ['NiF2', 4.72, 0.0],
         ['Rh', 12.45, 0.0],
         ['FeRh', 9.64685, 0.0],
         ['Al2O3', 3.98, 0.0],
         ['Li', 0.535, 0.0],
         ['Bi2Se3', 6.0457, 0.0],
         ['Bi', 9.78, 0.0],
         ['Se', 4.819, 0.0],
         ['C60', 1.65, 0.0],
         ['Gd', 7.901, 0.0],
         ['Co80Gd20', 8.68049, 0.0],
         ['D20', 1.107, 0.0],
         ['Ta2O5', 8.2, 0.0],
         ['Ge', 5.323, 0.0],
         ['Bi2Se3', 6.0457, 0.0],
         ['GaAs', 5.3176, 0.0],
         ['Co28Fe28B14Ta30', 7.04477, 0.0],
         ['EuO', 8.19, 0.0],
         ['Au', 19.3, 0.0],
         ['IrMn3', 8.97351, 0.0],
         ['Pt', 21.09, 0.0],
         ['Ge', 5.323, 0.0],
         ['FeCo', 8.35562, 2.0],
         ['Cr0.24Bi1.76Se3', 5.98009, 0.0],
         ['U', 19.05, 0.0],
         ['UO2', 10.97, 0.0],
         ['Ga', 5.904, 0.0],
         ['As', 5.727, 0.0],
         ['GaAs', 5.3176, 0.0],
         ['C ', 2.267, 0.0],
         ['Sn', 7.31, 0.0],
         ['Fe4N', 7.213, 0.0],
         ['Gd0.47Co0.53', 8.44107, 0.0],
         ['Gd', 7.901, 0.0],
         ['Fe20Ni80', 8.68003, 0.92],
         ['Fe2O3', 5.242, 0.0],
         ['Y', 4.472, 0.0],
         ['Y3Fe5O12', 5.11, 0.0, 'YIG'],
         ['Fe3O4', 5.17, 0.0],
         ['FeO', 5.745, 0.0],
         ['Gd3Ga5O12', 7.08, 0.0, 'GGG'],
         ['Ga', 5.904, 0.0],
         ['Y3Al5O12', 4.46, 0.0, 'YAG'],
         ['Er', 9.066, 0.0],
         ['Tb', 8.219, 0.0],
         ['Cu', 8.92, 0.0],
         ['La0.3Al0.3O0.9Sr0.7Al0.7Ta0.7O4.2', 6.79, 0.0, 'LSAT'],
         ['Y1Ba2Cu3O7', 6.3, 0.0, 'YBCO'],
         ['La0.7Ca0.3MnO3', 6.05, 0.0, 'LCMO'],
         ['W', 19.25, 0.0],
         ['TiO2', 4.23, 0.0],
         ['C58H70N2O2S4', 1.24, 0.0, 'dye'],
         ['He[4]', 0.145, 0.0, 'T=1K'],
         ['He[3]', 0.08185, 0.0, 'T=1K'],
         ['He[4]', 0.187, 0.0, 'solid'],
         ['C', 3.51, 0.0, 'diamod'],
         ['C', 2.26, 0.0, 'graphite'],
         ['C[12]', 3.51, 0.0, 'Isotope (Diamond)'],
         ['C[13]', 3.51, 0.0, 'Isotope (Diamond)'],
         ['Mn3NiN', 6.72, 0.3],
         ['V', 6.11, 0.0],
         ['H2O', 1.0, 0.0],
         ['NbO', 7.3, 0.0],
         ['NbO2', 5.9, 0.0],
         ['Nb2O5', 4.6, 0.0],
         ['MnNiGa', 10.26, 4.6],
         ['PbZr0.2Ti0.8O3', 7.8, 0.0],
         ['Zr', 6.49, 0.0],
         ['Pb', 11.34, 0.0],
         ['La0.7Sr0.3MnO3', 6.4, 0.0, 'LSMO'],
         ['Lu', 9.841, 0.0],
         ['Lu2O3', 9.42, 0.0],
         ['Hg', 14.19, 0.0],
         ['Co2FeAl', 6.12, 0.0],
         ['FePt', 15.2, 0.0, '(L10)'],
         ['IrO2', 11.66, 0.0],
         ['LaNiO3', 7.22, 0.0],
         ['La', 6.146, 0.0],
         ['Pb', 11.34, 0.0],
         ['NaNbO3', 4.575, 0.0],
         ['Na', 0.968, 0.0],
         ['C2H6O', 0.7893, 0.0],
         ['C12H26', 0.75, 0.0, 'dodecane'],
         ['In', 7.31, 0.0],
         ['InAs', 5.67, 0.0],
         ['EuS', 5.75, 0.0],
         ['S', 1.96, 0.0],
         ['Te', 6.24, 0.0],
         ['MnTe', 6.0, 0.0],
         ['Bi2Te3', 7.7, 0.0],
         ['CrSe', 6.74, 0.0]]


if __name__=="__main__":
    db=SLDDB(DB_FILE)
    for item in data:
        if len(item)>3:
            db.add_material(item[0], item[0],
                            description="Christy Kinane - %s"%item[3],
                            density=item[1],
                            mu=item[2])
        else:
            db.add_material(item[0], item[0],
                            description="Christy Kinane",
                            density=item[1],
                            mu=item[2])
