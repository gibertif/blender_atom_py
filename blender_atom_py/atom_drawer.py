import bpy
import atom_materials as ama
import atom_io as aio
import atom_topology as at
import atom_meshes as ame

class drawer:

    def __init__(self):
        self.zero=0
        self.origin = (0,0,0)
        self.obj=[]
        bpy.data.scenes["Scene"].render.fps=26       


    def draw_snapshot(self,filename):
        trj = aio.trajectory(filename)
        topology = at.topology()


    def animate_objects(self,trajectory):
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


    def animate_all(self,filename,draw_bonds=True):
        trj = aio.trajectory(filename)
        topology = at.topology()
        if draw_bonds:
            t.construct_topology()











