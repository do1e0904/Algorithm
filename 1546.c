#include <stdio.h>

int main()
{
	int N, MAX, i;
	int score[1000];
	float ave = 0;

	scanf("%d", &N);
	
	MAX = 0;
	for (i = 0;i < N;i++)
	{
		scanf("%d", &score[i]);
		if (score[i] > MAX)
			MAX = score[i];
	}
	
	for (i = 0;i < N;i++)
	{
		ave += ((float)score[i] / MAX);
	}
	ave /= N;
	
	printf("%f", ave*100);
}
