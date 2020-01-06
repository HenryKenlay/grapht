# AUTOGENERATED! DO NOT EDIT! File to edit: 02_spectral.ipynb (unless otherwise specified).

__all__ = ['laplacian_distance', 'laplacian', 'sparse_2norm']

# Cell

def laplacian_distance(G, Gp, setdiag=False):
    "Calculates || L - Lp || using the matrix 2-norm"
    L = laplacian(G, setdiag)
    Lp = laplacian(Gp, setdiag)
    E = Lp - L
    return sparse_2norm(E)

def laplacian(G, setdiag=False):
    "Laplacian matrix of the graph `G`"
    L = nx.normalized_laplacian_matrix(G)
    if setdiag:
        L.setdiag(1)
    return L

def sparse_2norm(A):
    "Returns the matrix 2-norm of a sparse matrix `A`"
    return np.abs(sp.linalg.eigsh(A, k=1, which='LM', return_eigenvectors=False))[0]