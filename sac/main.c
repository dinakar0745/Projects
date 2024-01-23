#include <stdio.h>

int main() {
    int n, i, cl, s;
    scanf("%d", &n);
    int a[n];
    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    cl = 1;
    s = 1;
    for (i = 1; i < n; i++) {
        if (a[i] > a[i - 1]) {
            cl++;
        } else {
            if (cl > s) {
                s = cl;
            }
            cl = 1;
        }
    }
    if (cl > s) {
        s = cl;
    }
    printf("Length of the longest increasing subarray: %d", s);

    return 0;
}
