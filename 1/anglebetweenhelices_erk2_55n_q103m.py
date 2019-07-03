import numpy
from glob import glob
import mdtraj as md
import numpy as np

# functions
def calc_helix_axes(coords):
  # Do lsq fitting of x, y and z values for each helix
  coord1 = coords[0]
  coord2 = coords[1]
  if (len(coord1) > 0 and len(coord2) > 0):
    coord1 = numpy.asarray(coord1)
    coord2 = numpy.asarray(coord2)
    count1 = len(coord1)
    count2 = len(coord2)

    start1 = []
    end1 = []
    vect1 = []
    start2 = []
    end2 = []
    vect2 = []

    (s,e) = lsq(range(count1),coord1[:,0])
    start1.append(s)
    end1.append(e)
    (s,e) = lsq(range(count1),coord1[:,1])
    start1.append(s)
    end1.append(e)
    (s,e) = lsq(range(count1),coord1[:,2])
    start1.append(s)
    end1.append(e)

    vect1.append(end1[0] - start1[0])
    vect1.append(end1[1] - start1[1])
    vect1.append(end1[2] - start1[2])

    (s,e) = lsq(range(count2),coord2[:,0])
    start2.append(s)
    end2.append(e)
    (s,e) = lsq(range(count2),coord2[:,1])
    start2.append(s)
    end2.append(e)
    (s,e) = lsq(range(count2),coord2[:,2])
    start2.append(s)
    end2.append(e)

    vect2.append(end2[0] - start2[0])
    vect2.append(end2[1] - start2[1])
    vect2.append(end2[2] - start2[2])

    start1 = numpy.asarray(start1)
    start2 = numpy.asarray(start2)
    vect1 = numpy.asarray(vect1)
    vect2 = numpy.asarray(vect2)

    ang1_2 = angle(vect1,vect2)
    dist1_2 = distance(start1,vect1,start2,vect2)

    return ang1_2, dist1_2

  else:
    print("Missing coordinates for one or both helices.  Check your input.")

def lsq(x,y):
  slope,intcpt =  numpy.polyfit(x,y,1,full=False)
  first_point = slope*x[0]+intcpt
  last_point = slope*x[-1]+intcpt
  return first_point,last_point

def angle(v1,v2):
  ang = numpy.arccos(numpy.dot(v1,v2)/(magvect(v1)*magvect(v2)))
  ang = ang*180/numpy.pi
  return ang  
  
def magvect(v):
  magnitude = numpy.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])
  return magnitude
 
def distance(start1,v1,start2,v2):
  cross_prod = numpy.cross(v1,v2)
  mx = magvect(cross_prod)
  norm = cross_prod/mx
  diff = start1 - start2
  dist = numpy.fabs(numpy.dot(norm,diff))
  return dist
  
# end functions

# ERK2 55N-Q103M - +1 to residue indexes

angles = []
for i,traj in enumerate(sorted(glob('run5-*.h5'))): 
    print(i)
    traj = md.load(traj)
    traj = traj.atom_slice(traj.top.select('name C or name O'))
    coord1 = traj.atom_slice(traj.top.select('resid >= 58 and resid <= 74')).xyz
    coord2 = traj.atom_slice(traj.top.select('resid >= 120 and resid <= 140')).xyz
    angles_ = []
    for j in range(len(traj)):
        angles_.append(calc_helix_axes([coord1[j], coord2[j]])[0])
    angles.append(angles_)
    
np.save('../angles_erk2_55n_q103m', angles)    
