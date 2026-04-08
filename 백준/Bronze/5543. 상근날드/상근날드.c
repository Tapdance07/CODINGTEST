#include <stdio.h>

int main(void) {

	int i;
	int enter[5];
	int burger = 2000;
	int renum = 0;
	int soda = 2000;
	int set = 0;
	for (i = 0; i < 5; i++)
	{
		scanf("%d", &enter[i]);
		if (enter[i] < 100 || enter[i]>2000) {
			printf("100원 이상, 2000원이하의 가격을 입력해주세요\n");
			scanf("%d", &renum);
			enter[i] = renum;
		}
	}
	for (i = 0; i < 3; i++)
	{
		if (burger > enter[i])
			burger = enter[i];
	}
	for (i = 3; i < 5; i++)
	{
		if (soda > enter[i])
			soda = enter[i];
	}
	set = burger + soda - 50;
	printf("%d", set);
	return 0;
}