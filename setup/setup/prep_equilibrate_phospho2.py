import time
import progressbar
from simtk import openmm, unit
from simtk.openmm import app
import mdtraj as md
import numpy as np
import argparse

#
# Simulation parameters
#

#pdb_filename = 'PRC2.pdb'

parser = argparse.ArgumentParser()
parser.add_argument('pdb_filename', type=str)
args = parser.parse_args()
pdb_filename = args.pdb_filename

water_model = 'tip3p'
solvent_padding = 10.0 * unit.angstroms
solvent_numAdded = 20959

ffxml_filenames = ['ff99SBildn.xml', 'tip3p_standard.xml', 'phosaa10.xml']

pressure = 1.0 * unit.atmospheres
barostat_period = 50
temperature = 300 * unit.kelvin
equilibration_collision_rate = 20.0 / unit.picoseconds
production_collision_rate = 1.0 / unit.picoseconds
timestep = 2.0 * unit.femtoseconds
nsteps = 500 # 1 ps
niterations = 10000 # 10 ns

#minimization_tolerance = 10.0 * unit.kilojoules_per_mole / unit.nanometers
#minimization_steps = 20
nonbondedMethod = app.PME
cutoff = 0.9 * unit.nanometers
constraints = app.HBonds
rigidWater = True
removeCMMotion = False

solvated_pdb_filename = 'solvated.pdb'
minimized_pdb_filename = 'minimized.pdb'
equilibrated_pdb_filename = 'equilibrated.pdb'

system_xml_filename = 'system.xml'
integrator_xml_filename = 'integrator.xml'
state_xml_filename = 'state.xml'

#
#
#       

print('Loading %s' % pdb_filename)
pdb = app.PDBFile(pdb_filename)

print("Loading forcefield: %s" % ffxml_filenames)
forcefield = app.ForceField(*ffxml_filenames)

#print("Adding hydrogens...")
modeller = app.Modeller(pdb.topology, pdb.positions)
# the phosphorylated tyrosine is loaded in with 2 wrong extra bonds 
modeller.delete([list(list(modeller.topology.residues())[181].bonds())[3], list(list(modeller.topology.residues())[181].bonds())[22]])
#modeller.addHydrogens(variants=variants)
#modeller.addExtraParticles(forcefield)

print('Adding solvent...')
#modeller.addSolvent(forcefield, model=water_model, padding=solvent_padding)
modeller.addSolvent(forcefield, model=water_model, numAdded=solvent_numAdded)
print('System has %d atoms' % modeller.topology.getNumAtoms())

print('Writing initial solvated system to %s' % solvated_pdb_filename)
with open(solvated_pdb_filename, 'w') as outfile:
    app.PDBFile.writeFile(modeller.topology, modeller.positions, file=outfile, keepIds=True)

# Create the system
print('Creating OpenMM System...')
system = forcefield.createSystem(modeller.topology, nonbondedMethod=nonbondedMethod, cutoff=cutoff, constraints=constraints, rigidWater=rigidWater, removeCMMotion=removeCMMotion)

# Add a barostat
print('Adding barostat...')
barostat = openmm.MonteCarloBarostat(pressure, temperature, barostat_period)
system.addForce(barostat)

# Minimize
print('Minimizing energy...')
integrator = openmm.LangevinIntegrator(temperature, equilibration_collision_rate, timestep)
context = openmm.Context(system, integrator)
context.setPositions(modeller.positions)
print('  initial : %8.3f kcal/mol' % (context.getState(getEnergy=True).getPotentialEnergy()/unit.kilocalories_per_mole))
#openmm.LocalEnergyMinimizer.minimize(context, minimization_tolerance, minimization_steps)
openmm.LocalEnergyMinimizer.minimize(context)
print('  final   : %8.3f kcal/mol' % (context.getState(getEnergy=True).getPotentialEnergy()/unit.kilocalories_per_mole))
with open(minimized_pdb_filename, 'w') as outfile:
    app.PDBFile.writeFile(modeller.topology, context.getState(getPositions=True,enforcePeriodicBox=True).getPositions(), file=outfile, keepIds=True)

# Equilibrate
print('Equilibrating...')
initial_time = time.time()
for iteration in progressbar.progressbar(range(niterations)):
    integrator.step(nsteps)
elapsed_time = (time.time() - initial_time) * unit.seconds
simulation_time = niterations * nsteps * timestep
print('    Equilibration took %.3f s for %.3f ns (%8.3f ns/day)' % (elapsed_time / unit.seconds, simulation_time / unit.nanoseconds, simulation_time / elapsed_time * unit.day / unit.nanoseconds))
with open(equilibrated_pdb_filename, 'w') as outfile:
    app.PDBFile.writeFile(modeller.topology, context.getState(getPositions=True,enforcePeriodicBox=True).getPositions(), file=outfile, keepIds=True)
print('  final   : %8.3f kcal/mol' % (context.getState(getEnergy=True).getPotentialEnergy()/unit.kilocalories_per_mole))

# Serialize state
print('Serializing state to %s' % state_xml_filename)
state = context.getState(getPositions=True, getVelocities=True, getEnergy=True, getForces=True)
with open(state_xml_filename, 'w') as outfile:
    xml = openmm.XmlSerializer.serialize(state)
    outfile.write(xml)

# Serialize system
print('Serializing system to %s' % system_xml_filename)
system.setDefaultPeriodicBoxVectors(*state.getPeriodicBoxVectors())
with open(system_xml_filename, 'w') as outfile:
    xml = openmm.XmlSerializer.serialize(system)
    outfile.write(xml)

# Serialize integrator
print('Serializing integrator to %s' % integrator_xml_filename)
integrator = openmm.LangevinIntegrator(temperature, production_collision_rate, timestep)
with open(integrator_xml_filename, 'w') as outfile:
    xml = openmm.XmlSerializer.serialize(integrator)
    outfile.write(xml)    
