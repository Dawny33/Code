function ac = Graph_CPL(n,k)
i = 1;
ag = zeros;
for beta = 0:.0001:1
    for j = 1:100
        C = small_world(n,k,beta);
        [ag1(j), bg] = charpathlength(full(C));
        j=j+1;
    end
    ag(i)=mean(ag1);
    i=i+1;
end
ag = ag/ag(1);
plot((0:.0001:1),smooth(ag))