#include <stdio.h>

int main()
{
    int A, B;
    do
    {
        scanf("%d %d", &A, &B);
    }while(A>10||B>10);
    
    printf("%d", A-B);
    
    return 0;
}
