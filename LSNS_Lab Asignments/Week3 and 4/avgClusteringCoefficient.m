%Module for calculating the avg. clustering coefficient.

function [acc, c] = avgClusteringCoefficient(graph)

%Determine node degrees
deg = sum(graph, 2); 

%Number of triangles for each node
cn = diag(graph*triu(graph)*graph); 

%The local clustering coefficient of each node
c = zeros(size(deg));
c(deg > 1) = 2 * cn(deg > 1) ./ (deg(deg > 1).*(deg(deg > 1) - 1)); 

%Average clustering coefficient of the graph
acc = mean(c(deg > 1));
end