#include <stdio.h>

int main()
{
    int a;
    scanf("%d", &a);

    if (a >= 90)
        printf("A");
    else if (80 <= a)
        printf("B");
    else if (70 <= a)
        printf("C");
    else if (60 <= a)
        printf("D");
    else
        printf("F");
}
