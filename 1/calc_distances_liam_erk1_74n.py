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

# ERK1 74N - 0-index - insertion is at 51 - compared to WS all indexes 51 and above +1
contacts = [[64,162], [47,65], [161,47], [80,69], [69,162], [162,141], [141,204], [32,45], [45,150], [149,151], [149,102], [151,102], [102,211], [211,215]]

distances = []
for i,traj in enumerate(sorted(glob('run1-*.h5'))):               
    traj = md.load(traj)                                         
    distance = md.compute_contacts(traj, contacts=contacts)
    distances.append(distance)
    print(1,i)

np.save('../distances1_liam', distances)
