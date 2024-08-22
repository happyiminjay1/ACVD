from pyvista import examples
import os
import pyacvd
import pyvista

dir_path = './'

dir_path_o = './obj3900_note_v3.ply'

sdf_path = os.path.join(dir_path,'27_note_pass.obj')

cow = pyvista.PolyData(sdf_path)
clus = pyacvd.Clustering(cow)

clus.subdivide(3)
clus.cluster(3900)

print(dir_path_o)
# remesh
remesh = clus.create_mesh()

remesh.save(dir_path_o)
