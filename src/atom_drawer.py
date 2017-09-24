import bpy
import atom_materials as am
import atom_io as aio
import atom_topology as at


class drawer:

    def __init__(self):
        self.zero=0
        self.origin = (0,0,0)
        self.obj=[]
        bpy.data.scenes["Scene"].render.fps=16       
        
    def clean_mesh():
        bpy.ops.object.select_by_type(type="MESH")
        bpy.ops.object.delete()
        self.obj=[]
    
#    def scale_atoms(self,scale=1):
#
#    def scale_bonds(self,scale=1):
#
    def create_objects(self,snapshot,topology):
        self.obj=[]
        for at in snapshot:
            p=at.pos
            bpy.ops.mesh.primitive_uv_sphere_add(location=p,size=0.1)
            bpy.context.object.name=str(at.name)+str(at.serial)
            self.obj.append(bpy.context.object)


        if topology.bonds:
            for bond in topology.bonds:


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
        self.clean_mesh()
        trj = aio.trajectory(filename)
        topology = at.topology()
        if draw_bonds:
            t.construct_topology()











