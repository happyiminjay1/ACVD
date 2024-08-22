from pyvista import examples
import os
import pyacvd
import pyvista

cow = pyvista.PolyData('/home/minjay/3DObjectTracking/M3T/examples/config/mug.obj')
clus = pyacvd.Clustering(cow)

clus.subdivide(2)
clus.cluster(4000)

# remesh
remesh = clus.create_mesh()

remesh.save('./new_mug2.ply')
