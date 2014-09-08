function A = ER_prob(n,e)
p = e/nchoosek(n,2);
A = zeros(n,n);
for i = 1:e
     r1 = randi(n);
     r2 = randi(n);
     while (r1==r2||A(r1,r2)==1||A(r2,r1)==1)
         r1 = randi(n);
         r2 = randi(n);
     end
     if(rand(1)<p)
        A(r1,r2) = 1;
        A(r2,r1) = 1;
     else
         i=i-1;
     end
end
[r,c] = find(triu(A));
edges = [r,c];

xlswrite('File_prob.xls',edges);
