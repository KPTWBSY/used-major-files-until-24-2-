#include <stdio.h>
main() {
	int x, y, z;
	x = 37;
	y = 5;
	z = 6;
	printf("%d\n", x / y);
	printf("%d\n", x / y * z);
	printf("%d\n", x % y);
	printf("%d\n", x % y * z);
	printf("%d\n", x % (y * z));

	printf("%d\n", -x / y);
	printf("%d\n", x / -y);
	printf("%d\n", -x % y);
	printf("%d\n", x % -y);
	printf("%d\n", -x % -y);
}