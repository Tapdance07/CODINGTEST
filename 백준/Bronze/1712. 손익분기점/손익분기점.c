#include <stdio.h>

int main() {

	int A;
	int B;
	int C;
	int total = 0;
	scanf("%d %d %d", &A ,&B , &C);
	while (1)
	{
		
		total = A/(C - B) + 1;
		if (B >= C)
		{
			printf("-1");
			break;
		}
		else
		{
			
			printf("%d", total);
			break;
		}
	}

}