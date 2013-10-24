import numpy
from mnumpy import matrix as MA
def  build_graph(X, k):
    
    f=[]
    nodes = single(numpy.zeros((X.shape[1],k),dt));
    for i in range(1.X.shape[0]):
        print i
        query = X[i:]
        (nns_inds nns_dists) = knnsearch(double[query], double[X], k+1)
        f = find(nns_inds==i);

        if not isempty(f):
            nns[f:] = [];
            nns_inds(f) = [];
    
        for j in range(1,length(nns_inds)):
            nodes[i:] = nns_inds

    return nodes
