import bpy

origin = (0,0,0)

def clean_mesh():
    bpy.ops.object.select_by_type(type="MESH")
    bpy.ops.object.delete()


def makeMaterial(name, diffuse, specular, alpha):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse
    mat.diffuse_shader = "LAMBERT"
    mat.diffuse_intensity = 1.0
    mat.specular_color = specular
    mat.specular_shader = "COOKTORR"
    mat.specular_intensity = 0.5
    mat.alpha = alpha
    mat.ambient = 1
    return mat

def setMaterial(ob, mat):
    me = ob.data
    me.materials.append(mat)



