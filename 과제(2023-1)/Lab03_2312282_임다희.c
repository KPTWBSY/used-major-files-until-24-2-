#include <stdio.h> 
main() {
	int prime[1000];
	int p,a,i;
	prime[0] = prime[1] = 0;
	for (p = 2; p < 1000; p++) {
		prime[p] = 1;
	}
	for (p = 2; p*p<1000; p++) {
		if (prime[p] == 1) {
			for (a=2; a*p< 1000; a++) {
				prime[a*p] = 0;
			}
		}
	}
	i = 0;
	for (p =0; p < 1000; p++) {
		if (prime[p] == 1) {
			printf("%3d ", p);
			i++;
			if (i % 15 == 0) {
				printf("\n");
			}
		}
	}
}