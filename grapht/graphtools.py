# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_graphtools.ipynb (unless otherwise specified).

__all__ = ['non_pendant_edges', 'is_pendant', 'has_isolated_nodes', 'edges_removed', 'laplacian', 'sparse_is_symmetric']

# Cell
from nbdev.showdoc import *
import networkx as nx
import warnings
import scipy.sparse as sp

# Cell
def non_pendant_edges(G):
    """Returns a list of non-pendant edges of a graph `G`."""
    edges = list(G.edges())
    edges = [edge for edge in edges if not is_pendant(G, edge)]
    return edges

def is_pendant(G, edge):
    """Returns if `edge` is pendant in the graph `G`."""
    if G.degree(edge[0]) == 1 or G.degree(edge[1]) == 1:
        return True
    else:
        return False

def has_isolated_nodes(G):
    """Returns if the graph `G` has isolated nodes."""
    if len(list(nx.isolates(G))) > 0:
        return True
    else:
        return False

def edges_removed(G, Gp):
    """Returns a list of edges which are the edges of G set minus the edges of Gp."""
    return list(set(G.edges()) - set(Gp.edges()))

# Cell
def laplacian(G, setdiag=False):
    """Returns the normalised Laplacian matrix of the graph `G`.

    If `setdiag` is `False` this is the same as `nx.normalized_laplacian_matrix(G)`

    If `setdiag` is `True` the diagonal of the Laplacian matrix will always contain `1` (even if nodes are isolated)
    """
    L = nx.normalized_laplacian_matrix(G)
    if setdiag:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            L.setdiag(1)
    return L

# Cell
def sparse_is_symmetric(A):
    """Returns is a sparse matrix is `A`.

    solution taken from https://stackoverflow.com/a/30685839/2453167
    """
    if (A!=A.T).nnz == 0:
        return True
    else:
        return False