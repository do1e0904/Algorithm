#include <stdio.h>

int main()
{
    unsigned int N, x, y, d, i, j, sum = 0 ;

    scanf("%d", &N);
    for (i = 0;i < N;i++)
    {
        scanf("%d %d", &x, &y);

        d = y - x;
        sum = 0;
        for (j = 1;2 * sum < d;j++)
        {
            sum += j;
        }
        j--;
        if (d <= (j * j))
            printf("%d\n", 2 * j - 1);
        else
            printf("%d\n", 2 * j);
    }
}