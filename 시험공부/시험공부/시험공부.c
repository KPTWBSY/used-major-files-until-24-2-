#include <stdio.h>
main()
{
	double dx;
	float fx;
	int i, ix;

	dx = fx = ix = 3;
	for (i = 0; i < 20; i++) {
		printf("i=%d,ix=%d,fx=%.0f,dx=%.0f\n", i, ix, fx, dx);
		ix = 3 * ix, fx = 3 * fx, dx = 3 * dx;
	}
	printf("\n");
}