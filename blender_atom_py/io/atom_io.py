from .. import atom_objects
import numpy as np

class xyz:
    
    def __init__(self,filename):
        self.filename=filename
        self.steps=self._get_steps()
        self.natoms=self._get_atoms()
        self.extra_fields=self._get_fields()-4
        
    def read(self):
        """Read filename in XYZ format and return lists of atoms and coordinates.
        If opt_prop is set to yes, then also the descriptor are readed (velocities for instance)
        The function return atoms_name,atoms_coordinates and eventually properties
        """
        trj=atom_objects.atomic_structure.trajectory(self.steps,self.natoms,self.extra_fields)

        fin=open(self.filename,'r')
        for it in range(self.steps):
            line=fin.readline()
            line=fin.readline()
            for at in range(self.natoms):
                line=fin.readline()
                trj[it][at].serial=at
                trj[it][at].name=line.split()[0]
                trj[it][at].element=line.split()[0]
                trj[it][at].pos[0]=line.split()[1]
                trj[it][at].pos[1]=line.split()[2]
                trj[it][at].pos[2]=line.split()[3]
                for prop in range(self.extra_fields):
                    trj[it][at].prop[prop]=line.split()[4+prop]

        return trj

        fin.close()


    def _rewind(self):
        with open(self.filename,'r') as fi:
            fi.seek(0,0)

    def _get_steps(self):
        self._rewind()
        steps=0
        for line in open(self.filename,'r'):
            if len(line.split())==1:
                steps=steps+1
        self._rewind()
        return steps
    
    def _get_atoms(self):
        self._rewind()
        with open(self.filename,'r') as fi:
            natoms=int(fi.readline().split()[0])
        self._rewind()
        return natoms
    
    def _get_fields(self):
        self._rewind()
        with open(self.filename,'r') as fi:
            fi.readline()
            fi.readline()
            fields=len(fi.readline().split())
        self._rewind()
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
