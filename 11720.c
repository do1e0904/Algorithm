#include <stdio.h>

int main()
{
	int N, i, sum = 0;
	char a[110];
	scanf("%d", &N);
	scanf("%s", a);
	for (i = 0;i < N;i++)
	{
		sum += (a[i] - 48);
	}
	printf("%d", sum);
}
	
