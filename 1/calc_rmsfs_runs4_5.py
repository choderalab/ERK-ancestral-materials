from glob import glob
import mdtraj as md
import numpy as np

rmsfs = []
for i,traj in enumerate(sorted(glob('run4-*.h5'))):
    
    traj = md.load(traj)
    traj = traj.atom_slice(traj.top.select('name CA'))
    traj = traj.superpose(traj)
    if len(traj) > 100:
        traj = traj[100:]
    else:
        continue    
    avg_xyz = np.mean(traj.xyz[:, :, :], axis=0)
    rmsf = np.sqrt(3*np.mean((traj.xyz[:, :, :] - avg_xyz)**2, axis=(0,2)))
    rmsfs.append(rmsf)
    print(0,i)
    
np.save('../rmsfs4', rmsfs)    

rmsfs = []
for i,traj in enumerate(sorted(glob('run5-*.h5'))):
    
    traj = md.load(traj)
    traj = traj.atom_slice(traj.top.select('name CA'))
    traj = traj.superpose(traj)
    if len(traj) > 100:
        traj = traj[100:]
    else:
        continue    
    avg_xyz = np.mean(traj.xyz[:, :, :], axis=0)
    rmsf = np.sqrt(3*np.mean((traj.xyz[:, :, :] - avg_xyz)**2, axis=(0,2)))
    rmsfs.append(rmsf)
    print(1,i)
    
np.save('../rmsfs5', rmsfs)    
