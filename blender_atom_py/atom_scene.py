import bpy 
import numpy 


class shape:

    def __init__(self,material,obj):
        self.material=material
        self.object=obj


class scene:

    def __init__(self,steps,atoms):
        self.idx=0
        self.shapes=[]

    def __iter__(self):
        return self
    
    def __next__(self): # Python 3: def __next__(self)
        self.idx += 1
        try:
            return self.shapes[self.idx-1]
        except IndexError:
            self.idx = 0
            raise StopIteration  # Done iterating.
        
    def __getitem__(self,index):
        return self.shapes[index]





