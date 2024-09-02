#include <stdio.h>

int checknum(int a)
{
	int i, cnt=0;
	for (i = 1;i <= a;i++)
	{
		if (i < 100)
		{
			cnt++;
		}
		else
		{
			if ((i - i % 100) / 100 - (i % 100 - i % 10) / 10 == (i % 100 - i % 10) / 10 - i % 10)
				cnt++;
		}
	}
	return cnt;
}

int main()
{
	int N;
	scanf("%d", &N);
	printf("%d", checknum(N));
}
	