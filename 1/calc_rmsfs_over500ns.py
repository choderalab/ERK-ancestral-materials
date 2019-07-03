from glob import glob
import mdtraj as md
import numpy as np

rmsfs = []
for i,traj in enumerate(sorted(glob('run0-*.h5'))):
    
    traj = md.load(traj)
    traj = traj.atom_slice(traj.top.select('name CA'))
    traj = traj.superpose(traj)
    if len(traj) > 1000:
        traj = traj[1000:]
    else:
        continue    
    avg_xyz = np.mean(traj.xyz[:, :, :], axis=0)
    rmsf = np.sqrt(3*np.mean((traj.xyz[:, :, :] - avg_xyz)**2, axis=(0,2)))
    rmsfs.append(rmsf)
    print(0,i)
    
np.save('../rmsfs0_over500ns', rmsfs)    

rmsfs = []
for i,traj in enumerate(sorted(glob('run1-*.h5'))):
    
    traj = md.load(traj)
    traj = traj.atom_slice(traj.top.select('name CA'))
    traj = traj.superpose(traj)
    if len(traj) > 1000:
        traj = traj[1000:]
    else:
        continue    
    avg_xyz = np.mean(traj.xyz[:, :, :], axis=0)
    rmsf = np.sqrt(3*np.mean((traj.xyz[:, :, :] - avg_xyz)**2, axis=(0,2)))
    rmsfs.append(rmsf)
    print(1,i)
    
np.save('../rmsfs1_over500ns', rmsfs)    

rmsfs = []
for i,traj in enumerate(sorted(glob('run2-*.h5'))):
    
    traj = md.load(traj)
    traj = traj.atom_slice(traj.top.select('name CA'))
    traj = traj.superpose(traj)
    if len(traj) > 1000:
        traj = traj[1000:]
    else:
        continue    
    avg_xyz = np.mean(traj.xyz[:, :, :], axis=0)
    rmsf = np.sqrt(3*np.mean((traj.xyz[:, :, :] - avg_xyz)**2, axis=(0,2)))
    rmsfs.append(rmsf)
    print(2,i)
    
np.save('../rmsfs2_over500ns', rmsfs)    

rmsfs = []
for i,traj in enumerate(sorted(glob('run3-*.h5'))):
    
    traj = md.load(traj)
    traj = traj.atom_slice(traj.top.select('name CA'))
    traj = traj.superpose(traj)
    if len(traj) > 1000:
        traj = traj[1000:]
    else:
        continue    
    avg_xyz = np.mean(traj.xyz[:, :, :], axis=0)
    rmsf = np.sqrt(3*np.mean((traj.xyz[:, :, :] - avg_xyz)**2, axis=(0,2)))
    rmsfs.append(rmsf)
    print(3,i)
    
np.save('../rmsfs3_over500ns', rmsfs)    
