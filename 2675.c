#include <stdio.h>

int main()
{
	int N, P, i, j, k;
	char a[30];
	for (i = 0;i < 30;i++)
	{
		a[i] = 'a';
	}
	scanf("%d", &N);
	for (i = 0;i < N;i++)
	{
		scanf("%d %s", &P, a);
		j=0;
		while (a[j] != 'a' && a[j]!='\0')
		{
			for (k = 0;k < P;k++)
			{
				printf("%c", a[j]);
			}
			j++;
		}
		if(i!=(N-1))
			printf("\n");
	}
}	
