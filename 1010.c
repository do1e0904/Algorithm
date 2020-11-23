#include <stdio.h>

int main()
{
    int n, a, b, c, d, i, j, k;
    scanf("%d", &n);
    for (i = 0;i < n;i++)
    {
        c = 1;
        d = 1;
        k = 1;
        scanf("%d %d", &a, &b);
        for (j=0;j < a;j++)
        {
            c *= (b - j);
            c /= k;
            k++;
        }
        printf("%d\n", c);
    }
}
