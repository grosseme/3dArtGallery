import numpy as np
import polyscope as ps
from src.read_mesh import read_mesh
from src.read_skeleton import read_skeleton
from src.display_mesh import display_mesh
from src.skeleton_points_sampling import skeleton_points_fixed_length_sampling
from src.random_ray_vertices import rand_ray

V, F = read_mesh('spot')
S_V, S_E = read_skeleton('spot')
S_P = skeleton_points_fixed_length_sampling(S_V, S_E, 5e-3)
vecs = rand_ray(S_V)

display_mesh(V, F, S_V = S_V, S_E = S_E, S_P = S_P, vecs = vecs)