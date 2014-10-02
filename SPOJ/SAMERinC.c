#include <stdio.h>

int main()
{
	int s,n;
	scanf("%d",&s);
	
	while(s>0)
	{
		n = s*(s+1)*((2*s)+1)/6;
		printf("%d",n);
		scanf("%d",&s);
	}
	return 0;
}