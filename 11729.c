#include <stdio.h>
#include <math.h>

void hanoi_tower(int n, int from, int tmp, int to)
{
	if (n == 1) printf("%d %d\n", from, to);
	else {
		hanoi_tower(n - 1, from, to, tmp);
		printf("%d %d\n",from, to);
		hanoi_tower(n - 1, tmp, from, to);
	}
}

int main(void)
{
	int N;
	scanf("%d", &N);

	printf("%d\n", (int)pow(2, N) - 1);
	hanoi_tower(N, 1, 2, 3);
	return 0;
}
