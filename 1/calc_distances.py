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

distances = []
for i,traj in enumerate(sorted(glob('run0-*.h5'))):               
    traj = md.load(traj)                                         
    distance = md.compute_contacts(traj, contacts=[[64,47]])
    distances.append(distance)
    print(0,i)
 
np.save('../distances0', distances)

distances = []
for i,traj in enumerate(sorted(glob('run1-*.h5'))):               
    traj = md.load(traj)                                         
    distance = md.compute_contacts(traj, contacts=[[65,47]])
    distances.append(distance)
    print(1,i)
 
np.save('../distances1', distances)

distances = []
for i,traj in enumerate(sorted(glob('run2-*.h5'))):               
    traj = md.load(traj)                                         
    distance = md.compute_contacts(traj, contacts=[[67,50]])
    distances.append(distance)
    print(2,i)
 
np.save('../distances2', distances)

distances = []
for i,traj in enumerate(sorted(glob('run3-*.h5'))):               
    traj = md.load(traj)                                         
    distance = md.compute_contacts(traj, contacts=[[68,50]])
    distances.append(distance)
    print(3,i)
 
np.save('../distances3', distances)
 
