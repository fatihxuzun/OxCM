# OxCM Contour Method Solver
![logo](https://raw.githubusercontent.com/fffatttihhh/OxCM/main/OxCM_logo.png)

This project presents the OxCM contour method solver, structured on the legacy version of the FEniCS open-source computing platform, that provides a standardized way of solution to the linear elastic numerical model for the calculation of residual stresses corresponding to out-of-plane displacements, that appear as a result of the changes in the boundary conditions after non-contact cutting, by a single line command in the availability of a domain composed of tetrahedral mesh and experimentally collected and processed profilometry data. For more information see the citing paper given below and contact with the authors of this paper.

## Dependencies
* dolfin
* numpy
* scipy
* click

## Installation
Dolfin is the computational environment of legacy version of FEniCS that should be installed with its dependencies using the instructions given in this link:

https://fenicsproject.org/download/archive/

The latest version of the OxCM contour method solver was tested by Docker Desktop 4.40.0:

https://docs.docker.com/desktop/


Install the Docker Desktop on Windows, MAC with Intel chip or MAC with Apple silicon and pull official ubuntu image:

```bash
docker pull ubuntu
```

Go to your shared folder and initiate the container:

```bash
docker run -ti -v $(pwd):/home ubuntu
```

Note the <container_name> from 'Docker -> Containers' and exit the running container:

```bash
exit
```

Start the container from 'Docker -> Containers' and initiate the same container: 

```bash
docker exec -it <container-name> /bin/bash
```

Install prerequisites:

```bash
apt-get update
apt-get install sudo
apt-get install pip
apt-get install git
apt-get install python3-click
apt-get install python3-venv
```

Install FEniCS on Ubuntu:

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:fenics-packages/fenics
sudo apt update
sudo apt install fenics
```

Create python3 environment for FEniCS installation:

```bash
python3 -m venv --system-site-packages oxcm
source oxcm/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install OxCM:

```bash
pip install git+https://github.com/fatihxuzun/OxCM.git
```

## OxCM Command Line Interface
OxCM command line interface (CLI) relies on 5 parameters:

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
OxCM --degree 1 --young 200e3 --poisson 0.29 --mesh 'myMesh.xml' --data 'myData.txt'
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
This solver has been developed as a part of the study that aims to understand the influence of processing conditions and geometric irregularities on the accuracy of the contour method residual stress quantifications. Please cite:

Uzun, F., Korsunsky, A.M. The OxCM contour method solver for residual stress evaluation. Engineering with Computers (2024). https://doi.org/10.1007/s00366-024-01959-3

## Publications
Uzun, F., Korsunsky, A.M. Reconstruction of residual stresses in additively manufactured Inconel 718 bridge structures using contour method. Int J Adv Manuf Technol 137, 4573–4582 (2025). https://doi.org/10.1007/s00170-025-15417-x
