from pyvista import examples
import os
import pyacvd
import pyvista

dir_path = '/home/minjay/gSDF/outputs/hsdf_osdf_1net/dexycbs0_29k_resnet18_h1_o1_sdf5_cls0_mano1_d0_ot1_or0_hand_kine_6_obj_kine_6_np2000_e1600_ae1201_pe0_scale6.2_b128_hsw0.5_osw0.5_hcw0.0_mjw0.5_msw5e-07_mpw5e-05_vw0.5_ocrw0.0/result_dexycb_gt_0/'

dir_path_o = os.path.join(dir_path,'1000_obj')

os.makedirs(dir_path_o, exist_ok=True)

sdf_path = os.path.join(dir_path,'sdf_mesh')

file_list = os.listdir(sdf_path)

obj_path = []

for file_name in file_list :
    if 'obj' in file_name :
        obj_path.append(file_name)

print(obj_path)

for file_name in obj_path :
    
    cow = pyvista.PolyData(os.path.join(sdf_path,file_name))
    clus = pyacvd.Clustering(cow)

    clus.subdivide(2)
    clus.cluster(1000)

    # remesh
    remesh = clus.create_mesh()
    
    remesh.save(os.path.join(dir_path_o,file_name))
