from dolfin import *
import numpy as np
from scipy import interpolate as sc
import click

@click.command()
@click.option('--degree', type=int, nargs=1, default=1)
@click.option('--young', type=float, nargs=1)
@click.option('--poisson', type=float, nargs=1)
@click.option('--mesh', type=str, nargs=1)
@click.option('--data', type=str, nargs=1)
def parameters(degree, young, poisson, mesh, data):
    return [degree, young, poisson, mesh, data]

dg = parameters(standalone_mode=False)[0]
E = parameters(standalone_mode=False)[1]
n = parameters(standalone_mode=False)[2]
meshRead = parameters(standalone_mode=False)[3]
dataRead = parameters(standalone_mode=False)[4]

# Read mesh file
mesh = Mesh(meshRead)

# Finite element function space
Vtemp = FunctionSpace(mesh, "CG", dg) # dg determines the number of dof points

# Extract coordinates of function space
fCoord = Vtemp.tabulate_dof_coordinates()

fCtemp = np.transpose(fCoord)

P1_z = round(np.min(fCtemp[2]),1)
P2_z = round(np.max(fCtemp[2]),1)

fInd = []
for i in range(len(fCoord)):
    if round(fCoord[i][2],1) == P2_z:
        fInd.append(i)

# Interpolate experimental data to the xy-plane located at P2_z
def readData(d):
    for i in range(len(d)):
        d[i] = d[i].split('\n')
        d[i] = d[i][0].split('\t')
        dTemp = []
        for j in range(3):
            dTemp.append(float(d[i][j]))
        d[i] = dTemp
    return d

ru = open(dataRead, "r")
uExp = ru.readlines()
uExp = readData(uExp)
ru.close()

uExp = np.transpose(uExp)

x = np.linspace(np.min(uExp[0]), np.max(uExp[0])) 
y = np.linspace(np.min(uExp[1]), np.max(uExp[1]))
xx, yy = np.meshgrid(x, y)

zz = sc.griddata((uExp[0], uExp[1]), uExp[2], (xx, yy), method='cubic')

#fInt = sc.interp2d(x, y, zz, kind='cubic')
fInt = sc.RegularGridInterpolator((x, y), zz, method='cubic')

# alternative interpolation that include smoothing the data (under development)
#fInt = sc.SmoothBivariateSpline(uExp[0], uExp[1], uExp[2], s=None)

fix_x = np.mean(x) - np.mean(fCtemp[0])
fix_y = np.mean(y) - np.mean(fCtemp[1])

uDof = []
for i in fInd:
    uDof.append(fInt(fCoord[i][0] + fix_x, fCoord[i][1] + fix_y))

# Linear elastic model
G = E/(2.0*(1.0 + n))

C = np.array([[(1.0/E),(-n/E),(-n/E),0.0,0.0,0.0],
              [(-n/E),(1.0/E),(-n/E),0.0,0.0,0.0],
              [(-n/E),(-n/E),(1.0/E),0.0,0.0,0.0],
              [0.0,0.0,0.0,(1.0/G),0.0,0.0],
              [0.0,0.0,0.0,0.0,(1.0/G),0.0],
              [0.0,0.0,0.0,0.0,0.0,(1.0/G)]])

C = np.linalg.inv(C)
C = C.tolist()
C = as_matrix(C)

def totalStrain(u):
    return 0.5*(grad(u) + grad(u).T)

def elasticStrain(e):
    return as_vector([(e[0,0]),
                      (e[1,1]),
                      (e[2,2]),
                      (e[0,1])*2,
                      (e[0,2])*2,
                      (e[1,2])*2])

def plotElasticStrain(e):
    return e 

def Stress(s):
    return as_tensor([[s[0], s[3], s[4]],
                      [s[3], s[1], s[5]],
                      [s[4], s[5], s[2]]])    

def sigma(u):
    return Stress(dot(C, elasticStrain(totalStrain(u))))

# Function space
V = VectorFunctionSpace(mesh, "CG", dg)
v = TestFunction(V)
uv = TrialFunction(V)

f = Constant((0, 0, 0))

Work = inner(sigma(uv), totalStrain(v))*dx
a = lhs(Work)
L = rhs(Work) + inner(f, v)*dx

u = Function(V, name="Displacement")

# Boundary conditions
bc = []
for i in range(len(fInd)):
    bcLine = 'def cnt_boundary' + str(i) + '(co): return round(co[0],3) == round(fCoord[' + str(fInd[i]) + '][0],3) and round(co[1],3) == round(fCoord[' + str(fInd[i]) + '][1],3) and round(co[2],3) == round(P2_z,3)'
    exec(bcLine.splitlines()[0])
    bcLine = 'bc = bc + [DirichletBC(V.sub(2), Constant((' + str(-uDof[i][0]) + ')), cnt_boundary' + str(i) + ', method="pointwise"' + ')]'
    bc.append(exec(bcLine.splitlines()[0]))

def base_boundary(co):
    return (-1e-1 + P1_z) < round(co[2],3) < (1e-1 + P1_z)
bcSymmetry = DirichletBC(V.sub(2), Constant((0.)), base_boundary, method='pointwise')

bc.append(bcSymmetry)

# Solve
solve(a == L, u, bc, solver_parameters={"linear_solver": "mumps"})

# Create Paraview results
uPlot = project(u, solver_type="mumps")
pvd_file = File ("results/U" + ".pvd")
pvd_file << uPlot

sPlot = project(sigma(u), solver_type="mumps")
pvd_file = File ("results/Stress" + ".pvd")
pvd_file << sPlot

esPlot = project(plotElasticStrain(totalStrain(u)), solver_type="mumps")
pvd_file = File ("results/ElasticStrain" + ".pvd")
pvd_file << esPlot