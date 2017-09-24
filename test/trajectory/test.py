import numpy as np
import sys
sys.path.append('../../src')


import bpy 
import atom_materials as am
import atoms_io as aio

trj = aio.trajectory('unwrapped.xyz')

print(trj.steps)

red = u.makeMaterial("Hydogen",(1,0,0),(1,1,1),1)
white = u.makeMaterial("Red",(1,1,1),(1,1,1),1)

obj=[]
for at in trj[0]:
    p=at.pos
    bpy.ops.mesh.primitive_uv_sphere_add(location=p,size=0.1)
    bpy.context.object.name=str(at.name)+str(at.serial)
    obj.append(bpy.context.object)
    if 'O' in at.name:
        am.setMaterial(bpy.context.object, red)
    if 'H' in at.name:
        am.setMaterial(bpy.context.object, white)


bpy.data.scenes["Scene"].render.fps=16

for st in range(0,trj.steps):
    f = bpy.data.scenes["Scene"].render.fps * st  # stub
    for at in trj[st]:
            p=(at.pos)
            s=at.serial
            obj[s].location=p
            obj[s].keyframe_insert(data_path="location", frame=f)
    
    for fc in obj[s].animation_data.action.fcurves: # stub
        for kp in fc.keyframe_points:
            kp.handle_left_type = 'VECTOR'
            kp.handle_right_type = 'VECTOR'
        fc.update()
            
