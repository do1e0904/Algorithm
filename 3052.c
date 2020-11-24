#include <stdio.h>

int main()
{
	int N, i, cnt=0;
	int a[42];
	for (i = 0;i < 42;i++)
	{
		a[i] = 0;
	}
	for (i = 0;i < 10;i++)
	{
		scanf("%d", &N);
		N %= 42;
		if (a[N] == 0)
		{
			cnt++;
			a[N]++;
		}
	}
	printf("%d", cnt);
}
