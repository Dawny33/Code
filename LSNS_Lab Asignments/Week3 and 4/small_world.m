function A = small_world(n, k, beta);

kHalf = k/2;
rows = reshape(repmat([1:n]', 1, k), n*k, 1);
columns = rows+reshape(repmat([[1:kHalf] [n-kHalf:n-1]], n, 1), n*k, 1);
columns = mod(columns-1, n) + 1;
B = sparse(rows, columns, ones(n*k, 1));
A = sparse([], [], [], n, n);

for i = [1:n]
    col= [full(A(i, 1:i-1))'; full(B(i:end, i))];
    for j = i+find(col(i+1:end))'
        if (rand()<beta)
            col(j)=0;
            k = randi(n);
            while k==i || col(k)==1
                k = randi(n);
            end
            col(k) = 1;
        end
    end
    A(:,i) = col;
end

T = triu(A);
A = T+T';
C = full(A);


end