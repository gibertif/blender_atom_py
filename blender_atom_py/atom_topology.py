import itertools as it
import numpy as np
import json

class topology:

    def read_topology(self,filename):
        import json
        with open(filename,'r') as fl:
            data=json.load(fl)
        return data

    def create_elements(self,snapshot):
        unique,count = np.unique(snapshot.name,return_counts=True)

        for element in unique:
            color=self.standard[element]["color"]
            radius=self.standard[element]["radius"]
            self.elements = np.append(self.elements,[color,radius])


    def create_bonds(self,snapshot):
        for el1 in it.permutations(snapshot,2):
            vec_d = el1[0].pos - el1[1].pos
            dist = np.sqrt(np.dot(vec_d,vec_d))
            if dist < self.standard[el1[0].name]["radius"]+self.standard[el1[1].name]["radius"]:
                self.bonds=np.append(self.bonds,[[el1[0].serial,el1[1].serial],1,self.standard["bond"]["radius"]])

    def clear_bonds(self):
        if self.bonds:
            self.bonds=np.rec.array(np.zeros(0,dtype=[('atoms',int,(2)),('order',int)]))

    def add_bond(self,bond):
        self.bonds=np.append(self.bonds,[[bond.atoms[0],bond.atoms[1]],bond.order])

    def clear_bond(self,index):
        self.bonds=np.delete(self.bonds,index)

    def __init__(self):
        self.elements=np.rec.array(np.zeros(0,dtype=[('color',float,(3)),('radius',float)]))
        self.bonds=np.rec.array(np.zeros(0,dtype=[('atoms',int,(2)),('order',int),('radius',float)]))
        self.standard = {
                "Ac": {"color": [0.439216, 0.670588, 0.980392], "radius": 1.114285},
                "Ag": {"color": [0.752941, 0.752941, 0.752941], "radius": 0.914285},
                "Al": {"color": [0.74902, 0.65098, 0.65098], "radius": 0.714285},
                "Am": {"color": [0.329412, 0.360784, 0.94902], "radius": 1.0},
                "Ar": {"color": [0.501961, 0.819608, 0.890196], "radius": 0.4057145},
                "As": {"color": [0.741176, 0.501961, 0.890196], "radius": 0.657145},
                "Au": {"color": [1, 0.819608, 0.137255], "radius": 0.77143},
                "B": {"color": [1, 0.709804, 0.709804], "radius": 0.4857145},
                "Ba": {"color": [0, 0.788235, 0], "radius": 1.22857},
                "Be": {"color": [0.760784, 1, 0], "radius": 0.6},
                "Bi": {"color": [0.619608, 0.309804, 0.709804], "radius": 0.914285},
                "Br": {"color": [0.65098, 0.160784, 0.160784], "radius": 0.657145},
                "C": {"color": [0.564706, 0.564706, 0.564706], "radius": 0.4},
                "Ca": {"color": [0.239216, 1, 0], "radius": 1.02857},
                "Cd": {"color": [1, 0.85098, 0.560784], "radius": 0.885715},
                "Ce": {"color": [1, 1, 0.780392], "radius": 1.057145},
                "Cl": {"color": [0.121569, 0.941176, 0.121569], "radius": 0.57143},
                "Co": {"color": [0.941176, 0.564706, 0.627451], "radius": 0.77143},
                "Cr": {"color": [0.541176, 0.6, 0.780392], "radius": 0.8},
                "Cs": {"color": [0.341176, 0.0901961, 0.560784], "radius": 1.485715},
                "Cu": {"color": [0.784314, 0.501961, 0.2], "radius": 0.77143},
                "Dy": {"color": [0.121569, 1, 0.780392], "radius": 1.0},
                "Er": {"color": [0, 0.901961, 0.458824], "radius": 1.0},
                "Eu": {"color": [0.380392, 1, 0.780392], "radius": 1.057145},
                "F": {"color": [0.564706, 0.878431, 0.313725], "radius": 0.2857145},
                "Fe": {"color": [0.878431, 0.4, 0.2], "radius": 0.8},
                "Ga": {"color": [0.760784, 0.560784, 0.560784], "radius": 0.742855},
                "Gd": {"color": [0.270588, 1, 0.780392], "radius": 1.02857},
                "Ge": {"color": [0.4, 0.560784, 0.560784], "radius": 0.714285},
                "H": {"color": [1, 1, 1], "radius": 1.092857},
                "Hf": {"color": [0.301961, 0.760784, 1], "radius": 0.885715},
                "Hg": {"color": [0.721569, 0.721569, 0.815686], "radius": 0.857145},
                "Ho": {"color": [0, 1, 0.611765], "radius": 1.0},
                "I": {"color": [0.580392, 0, 0.580392], "radius": 0.8},
                "In": {"color": [0.65098, 0.458824, 0.45098], "radius": 0.885715},
                "Ir": {"color": [0.0901961, 0.329412, 0.529412], "radius": 0.77143},
                "K": {"color": [0.560784, 0.25098, 0.831373], "radius": 1.257145},
                "La": {"color": [0.439216, 0.831373, 1], "radius": 1.114285},
                "Li": {"color": [0.8, 0.501961, 1], "radius": 0.82857},
                "Lu": {"color": [0, 0.670588, 0.141176], "radius": 1.0},
                "Mg": {"color": [0.541176, 1, 0], "radius": 0.857145},
                "Mn": {"color": [0.611765, 0.478431, 0.780392], "radius": 0.8},
                "Mo": {"color": [0.329412, 0.709804, 0.709804], "radius": 0.82857},
                "N": {"color": [0.188235, 0.313725, 0.972549], "radius": 0.3714285},
                "Na": {"color": [0.670588, 0.360784, 0.94902], "radius": 1.02857},
                "Nb": {"color": [0.45098, 0.760784, 0.788235], "radius": 0.82857},
                "Nd": {"color": [0.780392, 1, 0.780392], "radius": 1.057145},
                "Ni": {"color": [0.313725, 0.815686, 0.313725], "radius": 0.77143},
                "Np": {"color": [0, 0.501961, 1], "radius": 1.0},
                "O": {"color": [1, 0.0509804, 0.0509804], "radius": 1.522857},
                "Os": {"color": [0.14902, 0.4, 0.588235], "radius": 0.742855},
                "P": {"color": [1, 0.501961, 0], "radius": 0.57143},
                "Pa": {"color": [0, 0.631373, 1], "radius": 1.02857},
                "Pb": {"color": [0.341176, 0.34902, 0.380392], "radius": 1.02857},
                "Pd": {"color": [0, 0.411765, 0.521569], "radius": 0.8},
                "Pm": {"color": [0.639216, 1, 0.780392], "radius": 1.057145},
                "Po": {"color": [0.670588, 0.360784, 0], "radius": 1.085715},
                "Pr": {"color": [0.85098, 1, 0.780392], "radius": 1.057145},
                "Pt": {"color": [0.815686, 0.815686, 0.878431], "radius": 0.77143},
                "Pu": {"color": [0, 0.419608, 1], "radius": 1.0},
                "Ra": {"color": [0, 0.490196, 0], "radius": 1.22857},
                "Rb": {"color": [0.439216, 0.180392, 0.690196], "radius": 1.342855},
                "Re": {"color": [0.14902, 0.490196, 0.670588], "radius": 0.77143},
                "Rh": {"color": [0.0392157, 0.490196, 0.54902], "radius": 0.77143},
                "Ru": {"color": [0.141176, 0.560784, 0.560784], "radius": 0.742855},
                "S": {"color": [1, 1, 0.188235], "radius": 0.57143},
                "Sb": {"color": [0.619608, 0.388235, 0.709804], "radius": 0.82857},
                "Sc": {"color": [0.901961, 0.901961, 0.901961], "radius": 0.914285},
                "Se": {"color": [1, 0.631373, 0], "radius": 0.657145},
                "Si": {"color": [0.941176, 0.784314, 0.627451], "radius": 0.62857},
                "Sm": {"color": [0.560784, 1, 0.780392], "radius": 1.057145},
                "Sn": {"color": [0.4, 0.501961, 0.501961], "radius": 0.82857},
                "Sr": {"color": [0, 1, 0], "radius": 1.142855},
                "Ta": {"color": [0.301961, 0.65098, 1], "radius": 0.82857},
                "Tb": {"color": [0.188235, 1, 0.780392], "radius": 1.0},
                "Tc": {"color": [0.231373, 0.619608, 0.619608], "radius": 0.77143},
                "Te": {"color": [0.831373, 0.478431, 0], "radius": 0.8},
                "Th": {"color": [0, 0.729412, 1], "radius": 1.02857},
                "Ti": {"color": [0.74902, 0.760784, 0.780392], "radius": 0.8},
                "Tl": {"color": [0.65098, 0.329412, 0.301961], "radius": 1.085715},
                "Tm": {"color": [0, 0.831373, 0.321569], "radius": 1.0},
                "U": {"color": [0, 0.560784, 1], "radius": 1.0},
                "V": {"color": [0.65098, 0.65098, 0.670588], "radius": 0.77143},
                "W": {"color": [0.129412, 0.580392, 0.839216], "radius": 0.77143},
                "Y": {"color": [0.580392, 1, 1], "radius": 1.02857},
                "Yb": {"color": [0, 0.74902, 0.219608], "radius": 1.0},
                "Zn": {"color": [0.490196, 0.501961, 0.690196], "radius": 0.77143},
                "Zr": {"color": [0.580392, 0.878431, 0.878431], "radius": 0.885715},
                "undefined": {"color": [0, 0, 0], "radius": 0.405},
                "bond": {"color": [0.05, 0.05, 0.05], "radius": 0.103}
                }

