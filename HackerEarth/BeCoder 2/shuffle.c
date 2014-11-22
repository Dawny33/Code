     #include<stdio.h>
    unsigned long long int fac(unsigned long long int);
    int main()
    {
    int i,n,num;
    unsigned long long int result,temp,sum;
    scanf("%d",&n);
    while(n--)
    {
    sum=0;
    scanf("%d",&num);
    temp=fac(num);
    for(i=0;i<=num;i++)
    {
    if(i%2)sum=sum-(temp/fac(i));
    else
    sum=sum+(temp/fac(i));
    }
    printf("%llu\n",sum);
    }
    return 0;
    }
    unsigned long long int fac(unsigned long long int n)
    {
    if(n==1||n==0)return 1;
    return n*fac(n-1);
    } 