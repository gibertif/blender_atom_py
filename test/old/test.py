import bpy 
import numpy as np
import sys
sys.path.append('../src')
import utilities as u 
import atoms_io as aio

#bpy.ops.mesh.primitive_uv_sphere_add(location=u.origin)
#u.setMaterial(bpy.context.object, red)

steps=0
for line in open('traj.xyz','r'):
    if len(line.split())==1:
        natoms=int(line.split()[0])
        steps=steps+1

print(steps,natoms)

traj=np.zeros((steps,natoms),dtype=[
    ('step',int),
    ('name','U4'),
    ('pos',float,3),
    ])

with open('traj.xyz','r') as fi:
    fi.seek(0,0)

it=-1
for line in open('traj.xyz','r'):
    if len(line.split())==1:
        it=it+1
        jump_next=True
        continue
    if jump_next:
        jump_next=False
        at=0
        continue
    else:
        traj['step'][it,at]=it
        traj['name'][it,at]=line.split()[0]
        traj['pos'][it,at,0]=line.split()[1]
        traj['pos'][it,at,1]=line.split()[2]
        traj['pos'][it,at,2]=line.split()[3]
        at=at+1


red = u.makeMaterial("Red",(1,0,0),(1,1,1),1)
white = u.makeMaterial("White",(1,1,1),(1,1,1),1)

obj=[]
for st in traj[0]:
    p=(st['pos'])
    obj.append(bpy.ops.mesh.primitive_uv_sphere_add(location=p))
    if 'O' in st['name']:
        u.setMaterial(bpy.context.object, red)
    if 'H' in st['name']:
        u.setMaterial(bpy.context.object, white)


step=0
for st in traj:
    step=step+1
    print(step)
    bpy.context.scene.frame_set(step)
    for at in st:
        p=(at['pos'])
        bpy.ops.mesh.primitive_uv_sphere_add(location=p)
        if 'O' in at['name']:
            u.setMaterial(bpy.context.object, red)
        if 'H' in at['name']:
            u.setMaterial(bpy.context.object, white)

