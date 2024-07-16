import numpy as np
import polyscope as ps
from src.read_mesh import read_mesh
from src.read_skeleton import read_skeleton
from src.display_mesh import display_mesh

V, F = read_mesh('spot')
S_V, S_E = read_skeleton('spot')

display_mesh(V, F, S_V = S_V, S_E = S_E)