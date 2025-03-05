#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct names {
    char first[20];
    char last[20];
};

struct date {
    char month[12];
    int day, year;
};

struct person {
    struct names name;
    struct date birthday;
};

/* Converts "January", "February", ..., "December"
   into corresponding numbers 1, 2, ..., 12 */
int convert(char* mon) {
    static const char* months[] = { "January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December" };

    for (int i = 0; i < 12; ++i) {
        int j;
        for (j = 0; mon[j] != '\0' && months[i][j] != '\0' && mon[j] == months[i][j]; ++j) {

        }

        if (mon[j] == '\0' && months[i][j] == '\0') {
            return i + 1;
        }
    }

    return -1;
}

/* argv[1] contains the filename: cast.txt */
int main(int argc, char* argv[]) {
    struct person cast[20];
    int ncast = 0;
    FILE* f;
    int i;

    if (argc < 2) {
        fprintf(stderr, "usage:  %s  filename\n", argv[0]);
        exit(1);
    }

    if ((f = fopen(argv[1], "r")) == NULL) {
        fprintf(stderr, "%s: can't open %s\n", argv[0], argv[1]);
        exit(1);
    }

    while (fscanf(f, "%s %s %s %d, %d",
        cast[ncast].name.first, cast[ncast].name.last,
        cast[ncast].birthday.month, &cast[ncast].birthday.day,
        &cast[ncast].birthday.year) == 5) {

        ncast++;
        if (ncast >= 20) {
            break;
        }
    }

    fclose(f);

    printf("Cast of Captain America: Civil War\n");
    printf("==================================\n\n");
    printf("Name   (Birthday)\n\n");
    for (i = 0; i < ncast; i++)
        printf("%s, %s  <%02d/%02d/%02d>\n",
            cast[i].name.last, cast[i].name.first,
            convert(cast[i].birthday.month),
            cast[i].birthday.day,
            cast[i].birthday.year % 100);
}