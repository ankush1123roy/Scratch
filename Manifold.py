# Author: ankush2@ualberta.ca

import numpy
from numpy import matrix as MA
from numpy import linalg
                                                                                                                                                                                                                                                                                            
def learn_stable_Op(Xtrain,Ytrain):
	dt = numpy.dt('f8')
	num_actions = Ytrain.shape[0] / Xtrain.shape[1]
	d = Xtrain.shape[1]
	G = []
	h = []
	weights = numpy.zeros((num_actions*d, d),dt)
	for k in range(num_actions):
    		Xcat = []
    		Ycat = []
    		for i in range(Xtrain.shape[0]):
        		Xcat = cat(1,Xcat,Xtrain(i,:))
        		Ycat = cat(1,Ycat,Ytrain((i-1)*num_actions + k,:))

    		weights((k-1)*d + 1 : k*d, :) = Ycat'*pinv(Xcat')
    		(u,s,v) = numpy.linalg.svd(weights((k-1)*d + 1 : k*d, :),1,full_matrices = True)
    		print('top singular value = %f\n',s)                                                                                                                                        
    		tmp = u*v'
    		ebar = tmp.flattent(:).T
    		G = [G;ebar']
    		h = [h;1]
	
	for i in range(15):
    		cvx_begin quiet
    		variable w(num_actions*d, d);
    		variable b(num_actions,d);
    		loss = L2Loss(Xtrain,Ytrain,w,b);
    		minimize (loss)
    		subject to
    		for k in range(num_actions):
		       wvec = w((k-1)*d + 1 : k*d, :) 
			 -G*wvec(:) + h >= 0
       		fprintf('Training loss = %f\n',loss);                                                                                                                                                 
    		for k in range(num_actions):
        		[u,s,v] = svds(w((k-1)*d + 1 : k*d, :),1)
        		fprintf('top singular value for action %d = %f\n',k,s);                                                                                                                           
        		tmp = u*v';
        		ebar = tmp(:);
        		G = [G ; ebar'];
        		h = [h ; 1];
    		                                                                                                                                     
	return w,b,loss

def L2Loss(X,Y,w,b):
	d = size(X,2);
	actions = size(Y,1) / size(X,1);
	loss = 0;
	for i in range(size(X,1)):
	    for k in range(actions):
	        cur_loss = norm(X(i,:) * w((k-1)*d + 1 : k*d, :) + b(k,:) - Y((i-1)*actions + k,:))
	        loss = loss + cur_loss;
    

	loss = loss / size(X,1);
	return loss

if __init__ == '__main__':
(w,b,loss) = learn_stable_Op(Xtrain,Ytrain)

