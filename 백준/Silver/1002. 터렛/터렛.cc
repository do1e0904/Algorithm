#include <stdio.h>
#include <math.h>

int main()
{
	int N, x1, y1, r1, x2, y2, r2, i, result;
	double delta;
	scanf("%d", &N);
	for (i = 0;i < N;i++)
	{
		
		scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
;
		delta = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
		if (x1 == x2 && y1 == y2 && r1 == r2)
		{
			printf("-1\n");
		}
		else if ((float)(r1 + r2) > delta && ((float)(delta + r1) > r2 && ((float)(delta + r2) > r1)))
		{
			printf("2\n");
		}
		else if ((float)(r1 + r2) == delta || (float)abs(r1 - r2) == delta)
		{
			printf("1\n");
		}
		else
			printf("0\n");
				
	}
	return 0;
}