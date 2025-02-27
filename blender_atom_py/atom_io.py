import numpy as np

class trajectory:
    def __init__(self,steps,natoms):
        self.idx=0
        self.steps=steps
        self.natoms=natoms
        self.fields=0
        self.traj=np.rec.array(np.zeros((self.steps,self.natoms),dtype=[('serial',int),('name','U4'),('pos',float,3)]))
    
    def __iter__(self):
        return self
    
    def __next__(self): # Python 3: def __next__(self)
        self.idx += 1
        try:
            return self.traj[self.idx-1]
        except IndexError:
            self.idx = 0
            raise StopIteration  # Done iterating.

    def __getitem__(self,index):
            return self.traj[index]


class xyz(trajectory):
    def __init__(self,filename):
        """Read filename in XYZ format and return lists of atoms and coordinates.
        If opt_prop is set to yes, then also the descriptor are readed (velocities for instance)
        The function return atoms_name,atoms_coordinates and eventually properties
        """
        steps=self._get_steps(filename)
        natoms=self._get_atoms(filename)

#        trajectory.__init__(self,steps,natoms)
        self.trajectory=trajectory(steps,natoms)

        fin=open(filename,'r')
        for it in range(steps):
            line=fin.readline()
            line=fin.readline()
            for at in range(natoms):
                line=fin.readline()
                self.trajectory.traj[it,at].serial=at
                self.trajectory.traj[it,at].name=line.split()[0]
                self.trajectory.traj[it,at].pos[0]=line.split()[1]
                self.trajectory.traj[it,at].pos[1]=line.split()[2]
                self.trajectory.traj[it,at].pos[2]=line.split()[3]

        fin.close()

    def _rewind(self,filename):
        with open(filename,'r') as fi:
            fi.seek(0,0)

    def _get_steps(self,filename):
        self._rewind(filename)
        steps=0
        for line in open(filename,'r'):
            if len(line.split())==1:
                steps=steps+1
        self._rewind(filename)
        return steps
    
    def _get_atoms(self,filename):
        self._rewind(filename)
        with open(filename,'r') as fi:
            natoms=int(fi.readline().split()[0])
        self._rewind(filename)
        return natoms
    
    def _get_fields(self,filename):
        self._rewind(filename)
        with open(filename,'r') as fi:
            fi.readline()
            fi.readline()
            fields=len(fi.readline().split())
        self._rewind(filename)
        return fields



#
#    def read_lammps_snapshot(filename, opt_prop = 'no'):
#    
#        """Read filename in lammps format and return lists of atoms and coordinates.
#        If opt_prop is set to yes, then also the descriptor are readed (velocities for instance)
#        The function return atoms_name,atoms_coordinates,cell_vectors and eventually properties
#        """
#    
#        filename.readline()                       # comment: timestep
#        current_step = int(filename.readline())   # current step
#        filename.readline()                       # comment:number of atoms
#        n_atoms = int(filename.readline())
#        filename.readline()                       # comment: box boundary
#        temp_cell = filename.readline()     # cellx, lower and upper boundaries
#        lx_l,lx_u = temp_cell.split()
#        temp_cell = filename.readline()     # celly, lower and upper boundaries
#        ly_l,ly_u = temp_cell.split()
#        temp_cell = filename.readline()     # cellz, lower and upper boundaries
#        lz_l,lz_u = temp_cell.split()
#        line = filename.readline()  # comment containing the description of the fields
#    
#        cell = []
#        cell.append(math.fabs(float(lx_u)) + math.fabs(float(lx_l)))
#        cell.append(math.fabs(float(ly_u)) + math.fabs(float(ly_l)))
#        cell.append(math.fabs(float(lz_u)) + math.fabs(float(lz_l)))
#    
#    
#        if opt_prop != 'no':
#            atoms = []
#            coordinates = []
#            prop = []
#            for at in range(0,n_atoms):
#                line = filename.readline()                       # comment: timestep
#                arr_line = line.split()
#                atoms.append(arr_line[0])
#                coordinates.append([float(arr_line[1]),float(arr_line[2]),float(arr_line[3])])
#                array_prop = []
#                for word in range(4,len(arr_line)):
#                    array_prop.append(arr_line[word])
#                    prop.append(array_prop)
#            return atoms,coordinates,cell,prop
#        else:
#            atoms = []
#            coordinates = []
#            for at in range(0,n_atoms):
#                line = filename.readline()
#                arr_line = line.split()
#                atoms.append(arr_line[0])
#                coordinates.append([float(arr_line[1]),float(arr_line[2]),float(arr_line[3])])
#            return atoms,coordinates,cell
#    
