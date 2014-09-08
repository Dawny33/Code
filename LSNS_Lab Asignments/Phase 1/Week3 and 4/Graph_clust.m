function ac = Graph_clust(n,k);
i=1;
bg = zeros;
ag = zeros;
for beta = 0:.0001:1
    for j = 1:200
        C = small_world(n,k,beta);
        [ag1(j), bg] = avgClusteringCoefficient(full(C));
        j=j+1;
    end
    ag(i)=mean(ag1);
    i=i+1;
end

ag = ag/ag(1);

semilogx((0:.0001:1), smooth(ag))