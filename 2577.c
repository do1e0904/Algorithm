#include <stdio.h>

int main()
{
	int a, b, c, tmp, i;
	int freq[10] = { 0,0,0,0,0,0,0,0,0,0 };

	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);

	tmp = a * b * c;

	while (tmp > 0)
	{
		freq[tmp % 10]++;
		tmp /= 10;
	}

	for (i = 0;i < 10;i++)
	{
		printf("%d\n", freq[i]);
	}
}
