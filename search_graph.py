import random
import numpy
from numpy import matrix as MA
from knnsearch import knnsearch
def  search_graph(query, nodes, DS, K):
    random.seed(100)
    k = nodes.shape[1]
    depth = 0
    flag  = 0
    parent_id = randd(1, size(nodes,1), 1); # Check this
    visited = 1;
    
    while 1:

        parent_vec = double(DS(parent_id,:))  # parent node
        parent_dist = sqrt((query-parent_vec)*numpy.tranpose(query-parent_vec)) # query to parent distance
        child_ids = nodes(parent_id,:);
        (nn1_ind, nn1_dist) = knnsearch(query, double(DS(child_ids,:)), K)
        visited = visited + k
        if (parent_dist <= nn1_dist):
            flag=1
            break
        parent_id = child_ids(nn1_ind)
        depth = depth+1

return nn_id, nn_dist, visited

