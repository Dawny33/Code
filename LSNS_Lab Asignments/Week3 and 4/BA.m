function [C, L, degree] = BA(n,m0,m)

%adjacency matrix
C = scalefree(n, m0, m);

% characteristic path length
L = pathlength(n, C)

% avg. Clustering coefficient
[acc , bg] = avgClusteringCoefficient(C); 
acc
degree = sum(C);

%distribution
table = tabulate(degree);
table(:,[2])=table(:,[2])/n;
plot(table(:,[1]),table(:,[2]))

