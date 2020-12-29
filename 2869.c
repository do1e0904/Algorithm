#include <stdio.h>

int main()
{
	int up, down, goal, cnt = 0;

	scanf("%d %d %d", &up, &down, &goal);

	goal -= up;
	cnt = goal / (up - down);
	if ((goal % (up - down) )!= 0)
		cnt++;
	cnt++;
	printf("%d", cnt);
}	
