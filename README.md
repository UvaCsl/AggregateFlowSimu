# Image-based Flow Simulation of Platelet Aggregates

This code is associated to the submission for peer review publication of "Image-based Flow Simulation of Platelet Aggregates under Different Shear Rates". 

This repository present an image-based computational model simulating blood flow through and around platelet aggregates. The microstructure of aggregates was captured by two different modalities of microscopy images of *in vitro* whole blood perfusion experiments in microfluidic chambers coated with collagen. One set of images captured the geometry of the aggregate outline, while the other employed platelet labelling to infer the internal density. The platelet aggregates were modelled as a porous medium, the permeability of which was calculated with the Kozeny-Carman equation. The simulation is implemented in FreeFEM language (very similar to C++) using the finite element method. The code is adapted from [GitHub Pages](https://github.com/mbarzegary/navier-stokes-solver).
