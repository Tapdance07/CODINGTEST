#include <stdio.h>


int main()
{
	int n, a, b;
	scanf("%d", &n);

	int ans = -1;
	for (a = 0; a * 5 <= n; a++)
		for (b = 0; a * 5 + b * 3 <= n; b++)
			if (a * 5 + b * 3 == n)
				ans = a + b;

	printf("%d", ans);
}