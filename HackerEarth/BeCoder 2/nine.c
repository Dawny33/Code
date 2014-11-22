# include <stdio.h>
# include <string.h>
long long comb(long long n, long long r)
{
long long y;
if(r == 0){
return 1;
} else if( r > n){
return 0;
} else {
if(r == 2){
y = (n * (n-1))/2;
}else if( r == 3){
y = (n * (n-1) * (n-2))/6;
}else if(r ==4){
y = (n*(n-1)*(n-2)*(n-3))/24;
}
return y;
}
}
int main()
{
int t;
scanf("%d",&t);
int i;
getchar();
for(i = 0; i < t; i++){
char b[10005];
gets(b);
long long l;
long long c = 0;
l = strlen(b);
int j,k,p,s;
long long a[10]={0};
for(j = 0; j < l;j++){
a[b[j] -48]++;
}
c = c + a[9];
for(j = 0; j < 10;j++){
for(k = j; k < 10;k++){
if((j + k )% 9 == 0 && (j != 0 || k != 0)){
if(j == k){
c = c + comb(a[j],2);
}else{
c = c + (a[j]*a[k]);
}
}
for(p = k; p < 10 ;p++){
if((j+k+p)%9 == 0 && (j != 0 || k != 0 || p != 0)){
if(j == k && k == p){
c =c + comb(a[j],3);
}else if(j == k){
c = c + (comb(a[j],2) * a[p]);
} else if(k == p) {
c = c + (comb(a[k],2) * a[j]);
} else{
c = c + (a[j]*a[k]*a[p]);
}
}
for(s = p; s < 10;s++){
if((j+k+p+s)%9 == 0 && (j != 0 || k != 0 || p != 0 || s != 0)){
if(j ==k && k == p && p == s){
c = c + comb(a[j],4);
}else if(j == k && k == p){
c = c + (comb(a[j],3) * a[s]);
}else if(k == p && p == s){
c = c + (comb(a[k],3)*a[j]);
}else if( j == k && p == s)
c = c +(comb(a[j],2) * comb(a[p],2));
else if( j == k){
c = c + (comb(a[j],2) * a[p]*a[s]);
} else if(k == p){
c = c + (comb(a[k],2) * a[j]*a[s]);
} else if(p == s){
c =c + (comb(a[p],2) * a[j]*a[k]);
} else {
c = c + (a[j] * a[k] * a[p] * a[s]);
}
}
}
}
}
}
int co;
co = c%1000000007;
printf("%d\n",co);
}
return 0;
}