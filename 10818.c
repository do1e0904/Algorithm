#include <stdio.h>

int main()
{
    int N, MAX, min, a, i;
    scanf("%d", &N);
    scanf("%d", &a);
    MAX=a;
    min=a;
    for(i=0;i<N;i++)
    {
        scanf("%d", &a);
        if(a>MAX)
            MAX=a;
        else if(a<min)
            min=a;
    }
    printf("%d %d", min, MAX);
}
