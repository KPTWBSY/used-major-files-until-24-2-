#include <stdio.h>

/*print Fahrenheit-Celsius table
for fahr=300,280,260,...,0,
floating-point version */

main()
{
	float fahr;

	printf("  F      C\n\n");
	for (fahr = 300; fahr >= 0; fahr = fahr - 20)
		printf("%3.0f  %6.1f\n", fahr, (5.0 / 9.0) * (fahr - 32));

}