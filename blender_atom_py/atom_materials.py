import bpy

class materials:

#    def __init__(self,object_list):
#        for obj in object_list:
#            print(obj)

    def _makeMaterial(name, color, specular, alpha):
        mat = bpy.data.materials.new(name)
        mat.diffuse_color = color
        mat.diffuse_shader = "LAMBERT"
        mat.diffuse_intensity = 1.0
        mat.specular_color = specular
        mat.specular_shader = "COOKTORR"
        mat.specular_intensity = 0.5
        mat.alpha = alpha
        mat.ambient = 1
        return mat
    
    def _setMaterial(ob, mat):
        me = ob.data
        me.materials.append(mat)
    
    
    
