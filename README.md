# Image-based Flow Simulation of Platelet Aggregates

This code is associated to the submission for peer review publication of "[Image-based Flow Simulation of Platelet Aggregates under Different Shear Rates](https://www.biorxiv.org/content/10.1101/2023.02.22.529480v2)". 

This repository present an image-based computational model simulating blood flow through and around platelet aggregates. The microstructure of aggregates was captured by two different modalities of microscopy images of *in vitro* whole blood perfusion experiments in microfluidic chambers coated with collagen. One set of images captured the geometry of the aggregate outline, while the other employed platelet labelling to infer the internal density. The platelet aggregates were modelled as a porous medium, the permeability of which was calculated with the Kozeny-Carman equation. 

The simulation is implemented in FreeFEM language (very similar to C++) using the finite element method. The code is adapted from [navier-stokes-solver](https://github.com/mbarzegary/navier-stokes-solver).

## Repository structure

This repository consists of the following files/directories:

* `mesh/`: directory cotains image-based mesh files including aggregates meshes (under 800, 1600, 4000 1/s WSRs) and CFD mesh
* `data/`: directory cotains input data including intensity, volume fraction, permeability coefficient and permeability on aggregate mesh (1600 1/s WSR) and CFD mesh
* `transfer.py`: process the experimental image data (read the fluorescence intensity and transform the czi format to vtk format)
* `interpolation.edp`: interpolation the input data from aggregate mesh to CFD mesh
* `ns_3d.edp`: 3D Navier-Stokes model including Brinkman term 
* `run.sl`: batch script for high performance computing
