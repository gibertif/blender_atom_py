import numpy as _np

class atom:
    def __init__(self,extra_prop=0):
        self.name='X'
        self.pos=_np.zeros(3) # [0.,0.,0.]
        self.element='X'
        self.prop=[]
        for k in range(extra_prop):
            self.prop.append(0.)

class snapshot:
    def __init__(self,atoms,extra_prop=0):
        self.idx=0

        self.atoms=atoms
        
        self.frame=[]
        for st in range(atoms):
            self.frame.append(atom(extra_prop))
            
    def __getitem__(self,index):
        return self.frame[index]

    def __setitem__(self,index,value):
        self.frame[index]=value

    def __iter__(self):
        return self
    
    def __next__(self): 
        self.idx += 1
        try:
            return self.frame[self.idx-1]
        except IndexError:
            self.idx = 0
            raise StopIteration  # Done iterating

    def __len__(self):
        return self.atoms



class trajectory:
    def __init__(self,steps,atoms,extra_prop=0):
        self.idx=0



        self.steps=steps

        self.trj=[]
        for st in range(steps):
            self.trj.append(snapshot(atoms,extra_prop))
            
    def __getitem__(self,index):
        return self.trj[index]

    def __setitem__(self,index,value):
        self.trj[index]=value

    def __iter__(self):
        return self
    
    def __next__(self): 
        self.idx += 1
        try:
            return self.trj[self.idx-1]
        except IndexError:
            self.idx = 0
            raise StopIteration  # Done iterating

    def __len__(self):
        return self.steps



