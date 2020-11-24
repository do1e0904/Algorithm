#include <stdio.h>
#include <string.h>

int main()
{
	int i;
	char a[110];
	char alphabet[26];
	
	for (i = 0;i < 110;i++)
	{
		a[i] = 0;
	}
	scanf("%s", a);
	for (i = 0;i < 26;i++)
	{
		alphabet[i] = -1;
	}
	
	for (i = 0;i < 110;i++)
	{
		if (alphabet[(int)(a[i]) - 97] == -1)
			alphabet[(int)(a[i]) - 97] = i;
	}
	for (i = 0;i < 26;i++)
		printf("%d ", alphabet[i]);
}
	
