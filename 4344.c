#include <stdio.h>

int main()
{
	int N, student, i, j, cnt;
	float ave = 0;

	scanf("%d", &N);
	for (i = 0;i < N ;i++)
	{
		int score[1010];
		ave = 0;
		scanf("%d", &student);
		for (j = 0;j < student; j++)
		{
			scanf("%d", &score[j]);
			ave += score[j];
		}
		ave /= student;
		cnt = 0;
		for (j = 0;j < student;j++)
		{
			if (score[j] > ave) 
				cnt++;
		}
		printf("%.3f%%\n", (float)cnt/student*100);
	}
}
