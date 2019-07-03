from glob import glob
import mdtraj as md
import numpy as np

# translated to 0-indexes:

# ERK1 WT: E64 - K47
# ERK1 74N: E65 - K47
# ERK2 WT: E67 - K50
# ERK2 55N: E68 - K50
# ERK2 Q102M: E67 - K50
# ERK2 55N Q102M: E68 - K50

contacts = np.load('erk1_mut_1000dist.npy')

distances = []
for i,traj in enumerate(sorted(glob('run1-*.h5'))):               
    traj = md.load(traj)                                         
    distance = md.compute_contacts(traj, contacts=contacts)
    distances.append(distance)
    print(1,i)
 
np.save('../distances1_1k', distances)
