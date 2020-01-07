# AUTOGENERATED! DO NOT EDIT! File to edit: 05_data.ipynb (unless otherwise specified).

__all__ = ['make_planar_graph']

# Cell
from nbdev.showdoc import *
import numpy as np
import networkx as nx
import scipy
from gnnbench.data.io import load_dataset

# Cell
def make_planar_graph(n):
    """
    Makes a planar graph with n nodes

    Code adapted from https://stackoverflow.com/questions/26681899/how-to-make-networkx-graph-from-delaunay-preserving-attributes-of-the-input-node
    """
    points = np.random.rand(n, 2)
    delTri = scipy.spatial.Delaunay(points)
    edges = set()
    for n in range(delTri.nsimplex):
        edge = sorted([delTri.vertices[n,0], delTri.vertices[n,1]])
        edges.add((edge[0], edge[1]))
        edge = sorted([delTri.vertices[n,0], delTri.vertices[n,2]])
        edges.add((edge[0], edge[1]))
        edge = sorted([delTri.vertices[n,1], delTri.vertices[n,2]])
        edges.add((edge[0], edge[1]))
    graph = nx.Graph(list(edges))
    pos = pos = dict(zip(range(len(points)), points))
    return graph, pos