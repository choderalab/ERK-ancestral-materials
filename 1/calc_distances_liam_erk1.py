from glob import glob
import mdtraj as md
import numpy as np

# ERK2 numbering 
# For key catalytic residues mentioned in the manu

# E69-F166 
# K52-E69
# D165-K52

# For spines
# Regulatory spine:
# I84-L73
# L73-F166
# F166-H145
# H145-D208

# Catalytic spine:
# V37-A50
# A50-L154
# L153-L155 
# L153-M106 
# L155-M106
# M106-I215
# I215-M219

# ERK1 WT - 0-index - subtract 3 from ERK2 WT 0-indexed
contacts = [[64,161], [47,64], [160,47], [79,68], [68,161], [161,140], [140,203], [32,45], [45,149], [148,150], [148,101], [150,101], [101,210], [210,214]]

distances = []
for i,traj in enumerate(sorted(glob('run0-*.h5'))):               
    traj = md.load(traj)                                         
    distance = md.compute_contacts(traj, contacts=contacts)
    distances.append(distance)
    print(0,i)

np.save('../distances0_liam', distances)
