import bpy

# TO FINISH THE SHAPEFACTORY CREATION 

class shapefactory:
    factories={}
    def addfactory(id, shapefactory):
        shapefactory.factories.put[id] = shapefactory
    addfactory = staticmethod(addfactory)
    # A Template Method:
    def createshape(id):
        if id not in shapefactory.factories:
            shapefactory.factories[id] = eval(id + '.factory()')
        return shapefactory.factories[id].create()
    createshape = staticmethod(createshape)

    class shape(object): pass

    class sphere(shape):
        def draw(self,pos,size):
            bpy.ops.mesh.primitive_uv_sphere_add(location=pos,size=size)
            bpy.context.object.name=str(at.name)+str(at.serial)
 
        class factory:
            def create(self): return circle()

    class Square(Shape):
        def draw(self):
            print("Square.draw")
        def erase(self):
            print("Square.erase")
        class Factory:
            def create(self): return Square()


class objects:
    def __init__(self):
        self.zero=0
        self.origin = (0,0,0)
        self.obj=[]
        bpy.data.scenes["Scene"].render.fps=16       
        
    def clean_mesh(self):
        bpy.ops.object.select_by_type(type="MESH")
        bpy.ops.object.delete()
        self.obj=[]

    def create_spheres(self,snapshot):
        for at in snapshot:
            p=at.pos
            bpy.ops.mesh.primitive_uv_sphere_add(location=p,size=0.1)
            bpy.context.object.name=str(at.name)+str(at.serial)
            self.obj.append(bpy.context.object)


    def create_cylinders(self,snapshot,bonds):
        for bd in bonds:
            p1 = snapshot[bd.atoms[0]].pos
            p2 = snapshot[bd.atoms[1]].pos
            diff = [c2 - c1 for c2, c1 in zip(p1, p2)]
            cent = [(c2 + c1) / 2 for c2, c1 in zip(p1,p2)]
            
            mag = sum([(c2 - c1) ** 2
                for c1, c2 in zip(p1,p2)]) ** 0.5

                # Euler rotation calculation
                
            v_axis = Vector(diff).normalized()
            v_obj = Vector((0, 0, 1))
            v_rot = v_obj.cross(v_axis)
            
            # This check prevents gimbal lock (ie. weird behavior when v_axis is
            # close to (0, 0, 1))
            if v_rot.length > 0.01:
                v_rot = v_rot.normalized()
                axis_angle = [acos(v_obj.dot(v_axis))] + list(v_rot)
            else:
                v_rot = Vector((1, 0, 0))
                axis_angle = [0] * 4

            if bd.order != 1:
                print("Improper number of bonds! Defaulting to 1.")
                bd.order = 1
                

#            bpy.ops.mesh.primitive_cylinder_add(location=p,size=0.1)
#            bpy.context.object.name=str(at.name)+str(at.serial)
#            self.obj.append(bpy.context.object)


