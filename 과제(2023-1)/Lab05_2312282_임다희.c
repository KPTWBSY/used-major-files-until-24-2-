#include <stdio.h>
#include <string.h>

unsigned setbits(unsigned x, int p, int n, unsigned y) {
	int bitsA, bitsC, bitsE;
	bitsA = x & (~0 << (p + 1));
	bitsC = x & ~(~0 << (p - n + 1));
	bitsE = (y & ~(~0 << n)) << (p - n + 1);
	return bitsA | bitsC | bitsE;
}
main() {
	printf("%x\n", setbits(0x12345678, 7, 8, 0x89ABCDEF));
	printf("%x\n", setbits(0x12345678, 15, 16, 0x89ABCDEF));
	printf("%x\n", setbits(0x12345678, 15, 8, 0x89ABCDEF));
	printf("%x\n", setbits(0x12345678, 9, 10, 0x89ABCDEF));
}