# AUTOGENERATED! DO NOT EDIT! File to edit: 02_spectral.ipynb (unless otherwise specified).

__all__ = ['laplacian', 'laplacian_distance', 'sparse_2norm']

# Cell
from nbdev.showdoc import *
import networkx as nx
import numpy as np
import scipy.sparse as sp

# Cell
def laplacian(G, setdiag=False):
    "Laplacian matrix of the graph `G`"
    L = nx.normalized_laplacian_matrix(G)
    if setdiag:
        L.setdiag(1)
    return L

# Cell
def laplacian_distance(G, Gp, setdiag=False):
    "Calculates $|| \mathcal{L} -  \mathcal{L}_p ||$ using the matrix 2-norm"
    L = laplacian(G, setdiag)
    Lp = laplacian(Gp, setdiag)
    E = Lp - L
    return sparse_2norm(E)

# Cell
def sparse_2norm(A):
    "Returns the matrix 2-norm of a sparse matrix `A`"
    return np.abs(sp.linalg.eigsh(A, k=1, which='LM', return_eigenvectors=False))[0]