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

# ERK2 55N - 0-indexed (mutant is at 53 in 0-index - add 1 to those 53 and over compared to WT)
contacts = [[68,165], [50,68], [164,50], [83,72], [72,165], [165,144], [144,207], [35,48], [48,153], [152,154], [152,105], [154,105], [105,214], [214,218]]

distances = []
for i,traj in enumerate(sorted(glob('run3-*.h5'))):               
    traj = md.load(traj)                                         
    distance = md.compute_contacts(traj, contacts=contacts)
    distances.append(distance)
    print(3,i)
 
np.save('../distances3_liam', distances)
