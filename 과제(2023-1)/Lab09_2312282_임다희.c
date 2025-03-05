#include <stdio.h>
#include <ctype.h>
#define SIZE 100

main()
{
    int array[SIZE], n;
    int gethex(int*);
    int i, sum;

    for (n = 0; n < SIZE && gethex(&array[n]) != EOF; n++)
        ;
    sum = 0;
    for (i = 0; i < n; i++)
        sum += array[i];
    printf("The sum is %d\n", sum);
}

int gethex(int* pn)
{
    int c, sign;

    while (isspace(c = getchar())) 
        ;
    if (!(isdigit(c)||isalpha(c)) && c != EOF && c != '+' && c != '-') {
        ungetc(c, stdin); 
        return 0;
    }
    sign = (c == '-') ? -1 : 1;
    if (c == '+' || c == '-')
        c = getchar();
    for (*pn = 0; isdigit(c)||isalpha(c); c = getchar())
        if (c >= '0' && c <= '9')
            *pn = 16 * *pn + (c - '0');
        else if (c >= 'A' && c <= 'F')
            *pn = 16 * *pn + (c - '7');
        else if (c >= 'a' && c <= 'f')
            *pn = 16 * *pn + (c - 'W');
    *pn *= sign;
    if (c != EOF)
        ungetc(c, stdin);
    return c;
}