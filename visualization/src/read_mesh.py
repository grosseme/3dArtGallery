import os
import gpytoolbox as gpy
import polyscope as ps

def read_mesh(filename):
    PATH = os.getcwd()
    READ_PATH = PATH + '\\meshes\\' + filename + '.obj'

    V, F = gpy.read_mesh(READ_PATH)
    return V, F