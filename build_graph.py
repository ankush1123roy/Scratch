""" Original Matlab Code by Kiana Hajebi 
Changed to Python by Ankush Roy. This works for K = 1"""
from knnsearch import knnsearch
import numpy
from numpy import matrix as MA
def  build_graph(X, k):
    dt = numpy.dtype('f8')
    f=[]
    nodes = single(numpy.zeros((X.shape[1],k),dt));
    for i in range(1,X.shape[0]):
        print i
        query = X[i:]
        (nns_inds, nns_dists) = knnsearch(double[query], double[X], k+1)
        f = find(nns_inds==i);

        if not isempty(f):
            nns[f:] = [];
            nns_inds[f] = [];
    
        for j in range(1,length(nns_inds)):
            nodes[i:] = nns_inds

    return nodes

if __name__ == '__main__':
    X = [i in range(10)]
    for i in range(10):
        Vect = [random.randint(0,100) for r in range(10)]
        X = numpy.vstack([X,Vect])
    X = numpy.delete(X,(0),axis = 0)
    print X
    K = 1
    build_graph(X,K)
