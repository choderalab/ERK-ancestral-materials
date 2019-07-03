import numpy as np
import mdtraj as md
import multiprocessing
from glob import glob

# change system here
trajs = sorted(glob('../11730/run3-*.h5'))

def get_contact_map(traj):
    
    traj = md.load(traj)
    
    # cut first 50 ns
    if len(traj) <= 100:
        return None
    
    traj = traj[100:]

    distances, residue_pairs = md.compute_contacts(traj)
    contact_map = md.geometry.squareform(distances, residue_pairs)
    contact_map_bool = contact_map < 0.4
    contact_map_bool_float = contact_map_bool.astype('float')
    contact_map = np.mean(contact_map_bool_float, axis=0)

    return contact_map

pool = multiprocessing.Pool(10)

contact_maps = pool.map(get_contact_map, trajs)

contact_map = np.mean([x for x in contact_maps if x is not None], axis=0)

### change system here
np.save('contact_map_erk2_55n', contact_map)

for i,map in enumerate(contact_maps):
    np.save('cont_maps_erk2_55n/%d' % i, map)
