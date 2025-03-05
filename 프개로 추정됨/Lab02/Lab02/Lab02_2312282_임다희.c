#include <stdio.h>

void strmul(char*s, char *t, int n);
void strsum(char to[], char from1[], char from2[]); 

main() {
    char s[100], t[100], u[100];
    strmul(t, "abc", 2);
    strmul(u, "DE", 3);
    strsum(s, t, u);
    printf("Ãâ·Â:%s\n", s);
}

void strmul(char *s, char *t, int n) {
    int i, j, k;
    i = j = 0;
    for (k = 0; k < n; k++){
        while ((s[i] = t[j]) != '\0') {
            i++;
            j++;
        }
        j = 0;
    }
    printf("\"%s\"\n", s);
}
void strsum(char to[], char from1[], char from2[]) {
    int i, j;
    i = 0;
    while ((to[i] = from1[i]) != '\0') {
        ++i;
    }
    j = 0;
    while ((to[i] = from2[j]) != '\0') {
        i++;
        j++;
    }
    printf("s:\"%s\"\n", to);

}