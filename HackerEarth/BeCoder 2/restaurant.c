#include <stdio.h>
 
typedef unsigned int int_t;
typedef unsigned long long llint_t;
 
#define MOD 1000000007
 
llint_t STIRLING2ESP[1001][1001];
 
llint_t s(llint_t n, llint_t k)
{
return STIRLING2ESP[n][k];
}
 
llint_t a(llint_t n, llint_t k, llint_t v)
{
STIRLING2ESP[n][k] = v % MOD;
}
 
void init()
{
llint_t n, k;
a(0,0,0);
for (n = 1; n < 1001; n++)
{
a(n,1,1);
a(n,n,1);
for (k = 2; k < n; k++)
{
a(n,k, s(n-1,k-1) + k * s(n-1,k) );
}
}
}
 
llint_t modexp(llint_t base, llint_t exposant, llint_t modulo)
{
llint_t result = 1;
 
while (exposant)
{
if (exposant & 1)
result = (result * base) % modulo;
base = (base * base) % modulo;
exposant >>= 1;
}
 
return result;
}
 
llint_t process(int_t N, int_t M, int_t K)
{
llint_t S, P, k;
if (K >= N) return modexp(M,N,MOD);
S = 0;
P = M % MOD;
for (k = 1; k < K+1; k++)
{
S = (S + s(N,k) * P) % MOD;
P = (P * (M - k)) % MOD;
}
return S;
}
 
int main()
{
int_t T, t, N, M, K;
 
init();
 
scanf("%u", &T);
for (t = 0; t != T; t++)
{
scanf("%u %u %u", &N, &M, &K);
printf("%llu\n", process(N, M, K));
}
 
return 0;
}