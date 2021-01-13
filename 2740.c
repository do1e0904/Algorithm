#include <stdio.h>

int A[101][101];
int B[101][101];

int main(void)
{
	int N_A, M_A, N_B, M_B, i, j, k, tmp;

	scanf("%d %d", &N_A, &M_A);
	for (i = 0;i < N_A;i++)
		for (j = 0;j < M_A;j++)
			scanf("%d", &A[i][j]);

	scanf("%d %d", &N_B, &M_B);
	for (i = 0;i < N_B;i++)
		for (j = 0;j < M_B;j++)
			scanf("%d", &B[i][j]);

	
	for (i = 0;i < N_A;i++)
	{
		for (j = 0;j < M_B;j++)
		{
			tmp = 0;
			for (k = 0;k < M_A;k++)
			{
				tmp += (A[i][k] * B[k][j]);
			}
			printf("%d ", tmp);
		}
		printf("\n");
	}
		
	return 0;
}
