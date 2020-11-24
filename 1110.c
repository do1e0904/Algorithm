#include <stdio.h>

int main()
{
	int N, a, b, cnt=0, tmp;
	scanf("%d", &N);

	tmp = N;

	do
	{
		b = tmp % 10;
		a = (tmp - b) / 10;

		tmp = 10 * b + (a + b) %10;
		cnt++;

	} while (tmp != N);

	printf("%d", cnt);
}
