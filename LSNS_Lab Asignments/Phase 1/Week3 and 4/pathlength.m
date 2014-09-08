function L = pathlength(n,C)
pairs = zeros;
k=1;
for i = 1:n
    for j = (i+1):n
        if(i~=j)
            pairs(k,1)=i;
            pairs(k,2)=j;
            k=k+1;
        end
    end
end
D = dijkstra(C,pairs);
L = sum(D)/(n*(n-1));
