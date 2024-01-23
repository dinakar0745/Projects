#include <stdio.h>
#include <string.h>

int main(void) {
    char t[1000];
    scanf("%s", t);
    char s[2];
    char x[2];
    s[0] = t[strlen(t) - 2];
    s[1] = '\0';
    x[0] = t[strlen(t) - 1];
    x[1] = '\0';
    printf("K%s%s", s, x);
    return 0;
}
