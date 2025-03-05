#include <stdio.h>
#include <stdlib.h>
#define ARRAYSIZE 10000

int isort(int v[], int n)
{
	int i, j, temp,count;
	count = 0;
	for (i = 1; i < n; i++) {
		for (j = i - 1; j >= 0 && v[j] > v[j + 1]; j--) {
			temp = v[j], v[j] = v[j + 1], v[j + 1] = temp;
			count++;
		}
	}
	return count;
}
void copyarray(int a[], int b[], int n) {
	int w;
	for (w = 0; w < n; w++) {
		a[w] = b[w];
	}
}

void printarray(int a[], int n) {
	int x;
	for (x = 0; x < n; x++)
		printf("%d ", a[x]);
	printf("\n");
}
main() {
	int numbers[ARRAYSIZE], data[ARRAYSIZE];
	int i, n, count;

	for (i = 0; i < ARRAYSIZE; i++) {
		numbers[i] = rand();
	}
	printf("Before sort(the first 8 numbers): ");
	printarray(numbers, 8);
	printf("\n");
	for (n = 10; n <= ARRAYSIZE; n *= 10) {
		copyarray(data, numbers, n);
		count = isort(data, n);
		printf("After insertion sort (the first 5 numbers):");
		printarray(data,5);
		printf("The number of swaps in insertion sort : %d\n\n", count);
	}
}