#include <stdio.h>

int main()
{
	int year;
	scanf("%d", &year);

	if (year % 4 != 0)
	{
		printf("0");
		return 0;
	}
	if (year % 100 == 0 && year % 400 != 0)
	{
		printf("0");
		return 0;
	}
	else
		printf("1");
}
