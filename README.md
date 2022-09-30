# RuPyks

Experimental Rubiks cube program

## To do

- [x] Create structure to represent Rubics Cube [RC] state
- [x] Create function(s) to change RC state
- [x] Create visualization of RC state
- [ ] Implement ways to track changes to RC state
- [ ] Create functions to check the status and solving progress
- [ ] Create function(s)/method(s) to solve RC
    - stepwise (e. g. LBL)
    - automatic, ML?

## RC Structure

The Cube is represented by a 3 by 3 by 3 numpy ndarray in a 3D right hand cartesian coordinate system: X axis in the direction of array columns (second dimension, "left to right"), Y axis in the direction of the array's third dimension, "front to back"), Z axis in the reverse direction of array rows (first dimension, "bottom to top"). A 

Based on folded cube:

[![](https://ruwix.com/pics/western-color-scheme-rubiks-cube.jpg)](https://ruwix.com/the-rubiks-cube/japanese-western-color-schemes/)

Each face is represented by a 3 by 3 numpy array. Furthermore, a numpy ndarry (3, 3, 3) represents the general structure to track the position of each little cube, where structure[0] is the front face and everything if viewed from the front.

## Coding principles

Topic | URL
--- | ---
Structure | https://docs.python-guide.org/writing/structure/
Structure dos and don'ts | https://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application/3419951#3419951
Boilerplate template | https://pypi.org/project/python_boilerplate_template/
