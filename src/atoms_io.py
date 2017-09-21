# TODO 
# -function to write a xyz 
# -function to write a lammps
# -function to write a lammps-data
# -investigate if we can read .dcd

import math

def read_xyz_snapshot(filename,opt_prop = 'no'):
    """Read filename in XYZ format and return lists of atoms and coordinates.
    If opt_prop is set to yes, then also the descriptor are readed (velocities for instance)
    The function return atoms_name,atoms_coordinates and eventually properties
    """
    if opt_prop != 'no':
        atoms = []
        coordinates = []
        prop = []
        n_atoms = int(filename.readline())   
        title = filename.readline()
        for at in range(0,n_atoms):
            line = filename.readline()
            arr_line = line.split()
            atoms.append(arr_line[0])
            coordinates.append([float(arr_line[1]),float(arr_line[2]),float(arr_line[3])])
            array_prop = []
            for word in range(4,len(arr_line)):
                array_prop.append(arr_line[word])
                prop.append(array_prop)
        return atoms,coordinates,prop
    else:
        atoms = []
        coordinates = []
        n_atoms = int(filename.readline())
        title = filename.readline()
        for at in range(0,n_atoms):
            line = filename.readline()
            arr_line = line.split()
            atoms.append(arr_line[0])
            coordinates.append([float(arr_line[1]),float(arr_line[2]),float(arr_line[3])])
        return atoms,coordinates


def read_lammps_snapshot(filename, opt_prop = 'no'):

    """Read filename in lammps format and return lists of atoms and coordinates.
    If opt_prop is set to yes, then also the descriptor are readed (velocities for instance)
    The function return atoms_name,atoms_coordinates,cell_vectors and eventually properties
    """

    filename.readline()                       # comment: timestep
    current_step = int(filename.readline())   # current step
    filename.readline()                       # comment:number of atoms
    n_atoms = int(filename.readline())
    filename.readline()                       # comment: box boundary
    temp_cell = filename.readline()     # cellx, lower and upper boundaries
    lx_l,lx_u = temp_cell.split()
    temp_cell = filename.readline()     # celly, lower and upper boundaries
    ly_l,ly_u = temp_cell.split()
    temp_cell = filename.readline()     # cellz, lower and upper boundaries
    lz_l,lz_u = temp_cell.split()
    line = filename.readline()  # comment containing the description of the fields

    cell = []
    cell.append(math.fabs(float(lx_u)) + math.fabs(float(lx_l)))
    cell.append(math.fabs(float(ly_u)) + math.fabs(float(ly_l)))
    cell.append(math.fabs(float(lz_u)) + math.fabs(float(lz_l)))


    if opt_prop != 'no':
        atoms = []
        coordinates = []
        prop = []
        for at in range(0,n_atoms):
            line = filename.readline()                       # comment: timestep
            arr_line = line.split()
            atoms.append(arr_line[0])
            coordinates.append([float(arr_line[1]),float(arr_line[2]),float(arr_line[3])])
            array_prop = []
            for word in range(4,len(arr_line)):
                array_prop.append(arr_line[word])
                prop.append(array_prop)
        return atoms,coordinates,cell,prop
    else:
        atoms = []
        coordinates = []
        for at in range(0,n_atoms):
            line = filename.readline()
            arr_line = line.split()
            atoms.append(arr_line[0])
            coordinates.append([float(arr_line[1]),float(arr_line[2]),float(arr_line[3])])
        return atoms,coordinates,cell

