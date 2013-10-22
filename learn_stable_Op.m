function [w,b,loss] = learn_stable_Op(Xtrain,Ytrain)

num_actions = size(Ytrain,1) / size(Xtrain,1);
d = size(Xtrain,2);

G = [];
h = [];

weights = zeros(num_actions*d, d);
for k=1:num_actions
    Xcat = [];
    Ycat = [];
    for i=1:size(Xtrain,1)
        Xcat = cat(1,Xcat,Xtrain(i,:));
        Ycat = cat(1,Ycat,Ytrain((i-1)*num_actions + k,:));
    end
    weights((k-1)*d + 1 : k*d, :) = Ycat'*pinv(Xcat');
    [u,s,v] = svds(weights((k-1)*d + 1 : k*d, :),1);
    fprintf('top singular value = %f\n',s);
    tmp = u*v';
    ebar = tmp(:);
    G = [G;ebar'];
    h = [h;1];
end

for i=1:15
    cvx_begin quiet
    variable w(num_actions*d, d);
    variable b(num_actions,d);
    loss = L2Loss(Xtrain,Ytrain,w,b);
    minimize (loss)
    subject to 
    for k=1:num_actions
       wvec = w((k-1)*d + 1 : k*d, :);
       -G*wvec(:) + h >= 0
    end
    cvx_end
    fprintf('Training loss = %f\n',loss);
    for k=1:num_actions
        [u,s,v] = svds(w((k-1)*d + 1 : k*d, :),1);
        fprintf('top singular value for action %d = %f\n',k,s);
        tmp = u*v';
        ebar = tmp(:);
        G = [G ; ebar'];
        h = [h ; 1];
    end
end

end

function loss = L2Loss(X,Y,w,b)
d = size(X,2);
actions = size(Y,1) / size(X,1);
% X_t * w = X_{t+1}
loss = 0;
for i=1:size(X,1)
    for k=1:actions
        cur_loss = norm(X(i,:) * w((k-1)*d + 1 : k*d, :) + b(k,:) - Y((i-1)*actions + k,:));
        loss = loss + cur_loss;
    end
end
loss = loss / size(X,1);
end