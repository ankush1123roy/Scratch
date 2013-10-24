import numpy 
from copy import deepcopy
from numpy import matrix as MA
def knnsearch(varargin):
    # Check inputs
    (Q,R,K,fident) = parseinputs(varargin{:})
    # Check outputs
    error(nargoutchk(0,2,nargout))
    [N,M] = size(Q)
    L=size(R,1)
    if M !=R.shape[1]:  # added by kiana
        print ('Index exceeds matrix Dimensions .. ')
        return
    idx = numpy.zeros((N,K),dt4)
    D = idx
    if K==1:
        % Loop for each query point

        for k in range(1,N+1):
            d=numpy.zeros((L,1),dt4)
            
            for t in range(1,M+1):
                d=d+(R(:,t)-Q(k,t)).^2 # This loop ends here
            if fident:
                d[k]=inf

            [D(k),idx(k)]=min(d)



    else:
        for k in range(1,N+1):
            d=numpy.zeros((L,1),dt4)
            for t in range(1:M+1):
                d=d+(R(:,t)-Q(k,t)).^2

            if fident:
                d(k)=inf
            s = deepcopy(d)
            t  = sorted(range(len(s)),key=lambda x:s[x])
            s.sort()

        idx[k,:]=t[1:K]
        D[k,:]=s[1:K]

    if nargout>1:
        D=numpy.sqrt(D)



def parseinputs(varargin):

    #Check input and output
    error(nargchk(1,3,nargin));
    Q=varargin{1};
    if nargin<2:
        R=Q
        fident = true
    else:
        fident = false
        R=varargin{2}
    
    if isempty(R):
        fident = true
        R=Q
        
    if not fident:
        fident = isequal(Q,R)

    if nargin < 3:
        K=1
    else:
        K=varargin{3}

return Q,R,K,fident

if __name__ = '__main_':
    
# Check the return of KNN
