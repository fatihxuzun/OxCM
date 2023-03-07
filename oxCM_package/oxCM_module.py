import click
import os
import shutil
import time

@click.command()
@click.option('--degree', type=int, nargs=1, default=1)
@click.option('--young', type=float, nargs=1)
@click.option('--poisson', type=float, nargs=1)
@click.option('--mesh', type=str, nargs=1)
@click.option('--data', type=str, nargs=1)
def parameters(degree, young, poisson, mesh, data):
    return [degree, young, poisson, mesh, data]

p0 = parameters(standalone_mode=False)[0]
p1 = parameters(standalone_mode=False)[1]
p2 = parameters(standalone_mode=False)[2]
p3 = parameters(standalone_mode=False)[3]
p4 = parameters(standalone_mode=False)[4]

filePath = os.path.dirname(__file__)

paramList = "--degree " + str(p0) + " --young " + str(p1) + " --poisson " + str(p2) + " --mesh " + str(p3) + " --data " + str(p4)

# Create or update "/results/" folder
isdir = os.path.isdir('results')

if isdir == True:
    shutil.rmtree('results')
    print('"/results/" folder is updated in the project folder' + '\n')
else:
    print('"/results/" folder is created in the project folder' + '\n')

os.mkdir('results')

# Create log file of parameters
wlog = open("results/parameters.log", "w")

wlog.write("Degree of Function Space: " + str(p0) + '\n')
wlog.write("Young's Modulus: " + str(p1) + '\n')
wlog.write("Poisson's Ratio: " + str(p2) + '\n')
wlog.write("Mesh File: " + str(p3) + '\n')
wlog.write("Data File: " + str(p4))

wlog.close()

print('Parameters are saved to "parameters.log" file located in "/results/" folder' + '\n')

# Initiate solver
def oxCM():
    time_ = time.time()

    os.system("python3 " +  filePath + "/oxCM_solver.py " + paramList) 

    time_ = round(time.time() - time_, 1)

    print('\n' + 'Time Elapsed: ' + str(time_) + ' sec' + '\n')

    print('Please backup the results located in "/results/" folder' + '\n')
