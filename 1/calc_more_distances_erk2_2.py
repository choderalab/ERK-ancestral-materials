from glob import glob
import mdtraj as md
import numpy as np
import itertools

# translated to 0-indexes:

# ERK1 WT: E64 - K47
# ERK1 74N: E65 - K47
# ERK2 WT: E67 - K50
# ERK2 55N: E68 - K50
# ERK2 Q102M: E67 - K50
# ERK2 55N Q102M: E68 - K50

# distances = []
# for i,traj in enumerate(sorted(glob('run2-*.h5'))):               
#     traj = md.load(traj)                                         
#     distance = md.compute_contacts(traj, contacts=[list(x) for x in list(itertools.combinations(np.arange(40,78), 2))])
#     distances.append(distance)
#     print(2,i)
# 
# np.save('../distances2_more', distances)

distances = []
for i,traj in enumerate(sorted(glob('run3-*.h5'))):               
    traj = md.load(traj)                                         
    distance = md.compute_contacts(traj, contacts=[list(x) for x in list(itertools.combinations(np.arange(40,79), 2))])
    distances.append(distance)
    print(3,i)

np.save('../distances3_more', distances)
 
