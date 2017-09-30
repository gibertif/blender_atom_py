# blender_atom_py

## Workflow:

1. Load a trajectory.  Create a trj objects with position, serial and name. check!
2. Create the topology: define color and radius of a sphere for each atoms. If necessary, construct the bonds. chack!
3. Create a material for each elements in the trajectory.

## ROADMAP:

* Load one snapshot, render it with VdW and ball and stick representation.
* Load a trajectory, display and animate it.
* Do the one-click, load, color and animation


## TODO:

* Add an additional field to _trajectory_ so that we can tune color and transparency as a function of time.
* Implement how to read a xyz
* Class that read a topology (json file from blender-chemical).
* Transform a trajectory in time series in blender.
* Ball representation.
* Ball and stick representation.

