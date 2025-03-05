#include <stdio.h>

void switch_arrays(int* a, int* b) {
	int* temp;
	temp = *a;
	*a = *b;
	*b = temp;
}
void main() {
	int a1[] = { 1,2,3 };
	int a2[] = { 4,5,6,7,8,9 };
	int i;
	switch_arrays(a1, a2);
	for (i = 0; i < 3; i++)
		printf("%d ", a1[i]);
	printf("\n");
}