#include <stdio.h>

int main()
{
	int N, MAX, MAX_i, i = 1;
	
	scanf("%d", &N);
	MAX = N;
	MAX_i = i;	
	i++;

	while (i < 10)
	{
		scanf("%d", &N);
		if (N > MAX)
		{
			MAX = N;
			MAX_i = i;
		}
		i++;
	}
	printf("%d\n%d", MAX, MAX_i);
}
