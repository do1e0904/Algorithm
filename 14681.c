#include <stdio.h>

int main()
{
    int x, y;
    
    scanf("%d", &x);
    scanf("%d", &y);
    
    if(0<x && 0<y)
        printf("1");
    if(x<0 && 0<y)
        printf("2");
    if(x<0 && y<0)
        printf("3");
    if(0<x && y<0)
        printf("4");
    
}
