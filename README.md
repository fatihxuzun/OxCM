# OxCM Contour Method Solver
![logo](https://raw.githubusercontent.com/fffatttihhh/oxCM/main/oxCM_logo.png)

This project presents oxCM contour method solver, structured on the legacy version of the FEniCS open-source computing platform, that provides a standardized way of solution to the linear elastic numerical model for the calculation of residual stresses corresponding to the measured displacements, that appear because of the changes in the boundary conditions after non-contact cutting, by a single line command in the availability of a domain composed of tetrahedral mesh and experimentally collected and processed profilometry data. For more information see the citing paper given below and contact with the authors of this paper.

## Dependencies
* dolfin
* numpy
* scipy
* click

## Installation
dolfin is the computational environment of FEniCS available in the latest stable release of legacy FEniCS that should be installed using the instructions given in this link:

https://fenicsproject.org/download/archive/

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tested versions of numpy, scipy and click:

```bash
pip install numpy==1.24.1
pip install scipy==1.9.3
pip install click==8.1.3
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install oxCM:

```bash
pip install git+https://github.com/fatihxuzun/OxCM.git
```

## OxCM Command Line Interface
oxCM command line interface (CLI) relies on 5 parameters:

1. --degree, an integer value that define degree of function space

2. --young, a float value that define Young's modulus

3. --poisson, a float value that define Poisson's ratio

4. --mesh, a string value that define the mesh file in 'xml' format

5. --data, a string value that define the data file in any plain text file format

## OxCM Input Files
Mesh file and data file should be located in the user created project folder:

/myProjectFolder$

## Usage
Running OxCM command line interface (CLI) using training files:

```bash
oxCM --degree 1 --young 200e3 --poisson 0.29 --mesh 'myMesh.xml' --data 'myData.txt'
```

## Outputs
Outputs of the OxCM are ParaWiev plots of displacement, elastic strain and stress with a log file of CLI parameters:

* Displacement.vtu
* ElasticStrain.vtu
* Stress.vtu
* Parameters.log

The OxCM saves outputs to the results folder located in the project folder:

/myProjectFolder/results$

## Scientific Usage
This project has been developed as a part of the study that aims to understand the influence of processing conditions on the accuracy of the contour method residual stress quantifications. Please cite:

doi link to the paper
