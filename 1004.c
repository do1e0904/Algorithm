#include <stdio.h>
#include <math.h>

int main()
{
	int count, n, x1, y1, x2, y2, cx, cy, r, i, j, min;
	float delta1, delta2;
	
	scanf("%d", &count);
	for (i = 0;i < count;i++)
	{
		min = 0;
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		scanf("%d", &n);
		for (j = 0;j < n;j++)
		{
			scanf("%d %d %d", &cx, &cy, &r);
			delta1 = sqrt((x1 - cx) * (x1 - cx) + (y1 - cy) * (y1 - cy));
			delta2 = sqrt((x2 - cx) * (x2 - cx) + (y2 - cy) * (y2 - cy));

			if ((delta1 < r || delta2 < r) && !(delta1 < r && delta2 < r))
				min++;
		}
		printf("%d\n", min);
	}
}
