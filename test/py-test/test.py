import sys
sys.path.append("../../")
import blender_atom_py as bap
import numpy as np 

xyz_io = bap.io.atom_io.xyz('test.xyz')
trj = xyz_io.read()

top=bap.atom_objects.atom_topology.topology()
el=top.create_elements(trj[0])
print(el)
bd=top.create_bonds(trj[0])
print(bd)


#for k in trj:
#    for at in k:
#        print(at.prop)
