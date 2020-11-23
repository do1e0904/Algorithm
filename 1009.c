#include <stdio.h>

int main()
{
    int n, a, b, c, i, j;
    scanf("%d", &n);
    for (i = 0;i < n;i++)
    {
        c = 1;
        scanf("%d %d", &a, &b);
        for (j = 0;j < b;j++)
        {
            c *= a;
            c %= 10;
        }
        if (c != 0)
            printf("%d\n", c);
        else
            printf("10\n");
    }
}
