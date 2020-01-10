# AUTOGENERATED! DO NOT EDIT! File to edit: 02_metrics.ipynb (unless otherwise specified).

__all__ = ['sparse_norm', 'sparse_2norm', 'sparse_maxnorm', 'laplacian_distance', 'LineDistances', 'average_gmdegree',
           'edge_degree_gm']

# Cell
from nbdev.showdoc import *
from .graphtools import laplacian
from functools import lru_cache
import networkx as nx
import numpy as np
import scipy.sparse as sp

# Cell
def sparse_norm(A, ord=2):
    "Like scipy.sparse.lingalg.norm but with 2 and max norm implemented"
    if ord == 2:
        return sparse_2norm(A)
    elif ord == 'max':
        return sparse_maxnorm(A)
    else:
        return sp.linalg.norm(A, ord=ord)

def sparse_2norm(A):
    "Returns the matrix 2-norm of a sparse matrix `A`"
    return np.abs(sp.linalg.eigsh(A, k=1, which='LM', return_eigenvectors=False))[0]

def sparse_maxnorm(A):
    "Returns the max |A_ij| for a sparse matrix `A`"
    return max(-A.min(), A.max())

# Cell
def laplacian_distance(G, Gp, setdiag=False):
    "Calculates $|| \mathcal{L} -  \mathcal{L}_p ||$ using the matrix 2-norm"
    L = laplacian(G, setdiag)
    Lp = laplacian(Gp, setdiag)
    E = Lp - L
    return sparse_2norm(E)

# Cell
class LineDistances():

    def __init__(self, G):
        self.G = G
        self.line_graph = nx.line_graph(G)

    @lru_cache(maxsize=None)
    def __call__(self, edge1, edge2):
        "Calculating the linegraph distance between `edge1` and `edge2`"
        return nx.shortest_path_length(self.line_graph, edge1, edge2)

    def average_distance(self, edges):
        "Calculates the average linegraph distance between all pairs of edges in `edges`"
        distances = []
        for i in range(len(edges)):
            for j in range(i+1, len(edges)):
                distances.append(self(edges[i], edges[j]))
        return np.mean(distances)

# Cell
def average_gmdegree(G, edges):
    "The average edge degree geometric mean over all edges in `edges`"
    return np.mean([edge_degree_gm(G, edge) for edge in edges])

def edge_degree_gm(G, edge):
    "For an edge (u, v) with degree du, dv this function returns the geometric mean of du and dv"
    return np.sqrt(G.degree(edge[0]) * G.degree(edge[1]))