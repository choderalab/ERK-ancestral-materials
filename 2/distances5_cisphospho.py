from glob import glob
import mdtraj as md
import numpy as np

# crystal structure numbering
contact_residues = [103, 84, 73, 166, 168, 186, 185, 183, 188, 147, 149, 151]

# erk2-insertion (at 54) simulation numbering - subtract 2, then add 1 to all residues above 54
contact_residues = np.array(contact_residues)
contact_residues = contact_residues - 2
contact_residues_ = []
for residue in contact_residues:
    if residue >= 54:
        residue_ = residue + 1
    else:
        residue_ = residue    
    contact_residues_.append(residue_)
contact_residues = np.array(contact_residues_)           

contacts = []
for i in range(len(contact_residues)):
    for j in range(i+1,len(contact_residues)):
        contacts.append([contact_residues[i], contact_residues[j]])

distances = []
for i,traj in enumerate(sorted(glob('run5-*.h5'))): 
    traj = md.load(traj)
    distance = md.compute_contacts(traj, contacts=contacts)
    distances.append(distance)
    print(5,i)

np.save('../distances5_cisphospho', distances)
