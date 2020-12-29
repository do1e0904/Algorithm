#include <stdio.h>

int main()
{
	int T, a, b, i, j, k, tmp, sum_i = 0;
	int list[20][20];

	for (j = 0; j < 20;j++)
		list[0][j] = j;
	for (i = 1;i < 20;i++)
	{
		for (j = 0;j < 20;j++)
		{
			k = 0;
			tmp = 0;
			while (k <= j)
			{
				tmp += list[i - 1][k];
				k++;
			}
			list[i][j] = tmp;
		}
	}

	scanf("%d", &T);
	for (i = 0;i < T;i++)
	{
		tmp = 0;
		scanf("%d", &a);
		scanf("%d", &b);
		if (a == 1)
			printf("%d\n", list[1][b]);
		else
		{
			k = 1;
			while (k <= b)
			{
				tmp += (k * list[a - 2][b - k + 1]);
				k++;
			}
			printf("%d\n", tmp);
		}		
	}
}	
