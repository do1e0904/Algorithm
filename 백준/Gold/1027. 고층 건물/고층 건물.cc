#include <stdio.h>
#include <math.h>

int main()
{
	int N, i, j, MAX = 0;
	double delta, delta_tmp;
	int height[51];
	int cnt[51];

	scanf("%d", &N);

	for (i = 0; i < N; i++)
	{
		scanf("%d", &height[i]);
		cnt[i] = 0;
	}

	while (i < 51)
	{
		height[i] = 0;
		cnt[i] = 0;
		i++;
	}

	i = 0;
	while (i < (N - 1))
	{
		delta = (double)(height[i + 1] - height[i]);    
		cnt[i]++;
		cnt[i + 1]++;

		for (j = (i + 1);j < N;j++)
		{
			delta_tmp = ((double)(height[j] - height[i]) / (j - i));
			if (delta < 0 && delta_tmp>=0)
			{
				delta = delta_tmp;
				cnt[i]++;
				cnt[j]++;
			}
			else if (delta < delta_tmp)
			{
				delta = delta_tmp;
				cnt[i]++;
				cnt[j]++;
			}
		}
		i++;

	}
	
	for (i = 0;i < N;i++)
	{
		if (MAX < cnt[i])
			MAX = cnt[i];
	}
	printf("%d", MAX);
}