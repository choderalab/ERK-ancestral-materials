from glob import glob
import mdtraj as md
import numpy as np

# crystal structure numbering
contact_residues = [103, 84, 73, 166, 168, 186, 185, 183, 188, 147, 149, 151]

# erk2 simulation numbering - subtract 2
contact_residues = np.array(contact_residues)
contact_residues = contact_residues - 2

contacts = []
for i in range(len(contact_residues)):
    for j in range(i+1,len(contact_residues)):
        contacts.append([contact_residues[i], contact_residues[j]])

distances = []
for i,traj in enumerate(sorted(glob('run2-*.h5'))): 
    traj = md.load(traj)
    distance = md.compute_contacts(traj, contacts=contacts)
    distances.append(distance)
    print(2,i)

np.save('../distances2_cisphospho', distances)
