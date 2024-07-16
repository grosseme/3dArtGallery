import numpy as np

def skeleton_points_uniform_sampling(V, E, points_per_edge = 9):
    P = []

    for edge in E:
        for i in range(1, points_per_edge + 1):
            P.append((V[edge[0]] * i + V[edge[1]] * (points_per_edge + 1 - i)) / (points_per_edge + 1))

    return np.concatenate((np.array(P), V), axis=0)

def skeleton_points_fixed_length_sampling(V, E, target_length):
    P = []

    for edge in E:
        u, v = V[edge[0]], V[edge[1]]
        edge_length = np.linalg.norm(u - v)
        points_per_edge = int(np.round(edge_length / target_length) - 1)

        for i in range(1, points_per_edge + 1):
            P.append((V[edge[0]] * i + V[edge[1]] * (points_per_edge + 1 - i)) / (points_per_edge + 1))

    if len(P) == 0:
        return V
    
    return np.concatenate((np.array(P), V), axis=0)