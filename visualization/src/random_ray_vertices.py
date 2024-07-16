import os
import numpy as np
import polyscope as ps
from src.read_skeleton import read_skeleton

def rand_ray(filename):
  S_V = read_skeleton(filename)
  
  num_vert = len(S_V)
  vecs= np.random.rand(num_vert, 3)
  
return vecs
  



