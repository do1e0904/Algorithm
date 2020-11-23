#include <stdio.h>

int main()
{
	int  count, n, i;
	int fib[50];

	fib[0] = 0;
	fib[1] = 1;
	
	for (i = 2;i < 50;i++)
	{
		fib[i] = fib[i - 2] + fib[i - 1];
	}

	scanf("%d", &count);

	for (i = 0;i < count;i++)
	{
		scanf("%d", &n);
		if (n == 0)
			printf("1 0\n");
		else
			printf("%d %d\n", fib[n-1], fib[n]);
	}
}
