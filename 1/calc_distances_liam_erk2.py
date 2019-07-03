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

# ERK2 WT - 0-indexed
contacts = [[67,164], [50,67], [163,50], [82,71], [71,164], [164,143], [143,206], [35,48], [48,152], [151,153], [151,104], [153,104], [104,213], [213,217]]

distances = []
for i,traj in enumerate(sorted(glob('run2-*.h5'))):               
    traj = md.load(traj)                                         
    distance = md.compute_contacts(traj, contacts=contacts)
    distances.append(distance)
    print(2,i)

np.save('../distances2_liam', distances)
