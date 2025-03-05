#include <stdio.h>
int binsearch(int x, int v[], int n) {

	int low, high, mid;
	low = 0, high = n - 1;
	while (low <= high) {
		mid = (low + high) / 2;
		if (x < v[mid])
			high = mid - 1;
		else if (x > v[mid]) {
			low = mid + 1;
		}
		else
			return mid;
	}
	return -1;
}

main() {
	int a[] = { 2,5,7,9,13,17,20,22,28,33,40,40,51,57,70 };

	printf("%d\n", binsearch(40, a, 14));
}