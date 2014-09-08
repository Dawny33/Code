function C = scalefree(n, m0, m)

%Algorithm found on the internet (StackOverFlow)
B = zeros(m0, m0);
for i = 1:m0
    neighbors = randsample(m0-1, m);
    neighbors = neighbors + (neighbors>=i);
    B(i,neighbors) = 1;
    B(neighbors,i) = 1;
end


[rows, columns] = find(triu(B));
nEdges = size(rows, 1);
edges = reshape([rows';columns'], 2*nEdges, 1);
edges = [edges; zeros(2*(n-m0)*m,1)];

used = zeros(n, 1); 
for i = m0+1:n
    neighbors = zeros(1, m);
    for j=1:m
       k = edges(randi(2*nEdges));
       while used(k)
           k = edges(randi(2*nEdges));
       end
       used(k) = 1;
       neighbors(j) = k;
    end
    used(neighbors) = 0;
    edges(2*nEdges+1:2*nEdges+2*m) = reshape([repmat(i, 1, m); neighbors], 1, 2*m);
    nEdges = nEdges+m;
end

edges = edges(1:2*nEdges);
first = edges(1:2:end);
second = edges(2:2:end);
A = sparse([first;second], [second;first], ones(2*nEdges, 1), n, n);
C = full(A);

[r,c] = find(triu(C));
edges = [r,c];
%xlswrite('scalefree.xls',edges);

end 
