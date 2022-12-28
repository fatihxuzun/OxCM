# The oxCM Contour Method Solver

![logo](https://raw.githubusercontent.com/fffatttihhh/oxCM/main/logo.png)


## Dependencies

dolfin

numpy

scipy

click


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install oxCM.

```bash
pip install oxCM
```

## Usage
oxCM needs 5 imputs

--degree, an integer value that define degree of function space

--young, a float value that define Young's modulus

--poisson, a float value that define Poisson's ratio

--mesh, a string value that define the mesh file in 'xml' format

--data, a string value that define the data file in any plain text file format

Place mesh file and data file in the project folder

/myProjectFolder$

Run oxCM command line interface

```bash
oxCM --degree 1 --young 200e3 --poisson 0.3 --mesh 'myMesh.xml' --data 'myData.txt'
```
The oxCM saves outputs in 'vtu' format to the results folder

/myProjectFolder/results$

## Scientific Usage
This project has been developed as a part of the study that aims to understand the influence of processing conditions on the accuracy of the contour method residual stress quantifications. Please cite:

doi link to the paper
