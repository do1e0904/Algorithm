#include <stdio.h>
#include <string.h>

int main()
{
	int N, i, j, plus, score;
	char test[100];

	scanf("%d", &N);
	for (i = 0;i < N;i++)
	{
		scanf("%s", &test);
		score = 0;
		plus = 0;

		for (j = 0;j < strlen(test);j++)
		{
			if (test[j] == 'O')
				plus++;
			else
				plus = 0;
			score += plus;
		}
		printf("%d\n", score);
	}
    return 0;
}
