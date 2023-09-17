#include <stdio.h>

char* ts(int a1, int a2, int b1, int b2) {
    int nea = a1 - a2;
    int neb = b1 - b2;
    if (nea == 0) {
        return "YES";
    } else {
        return "NO";
    }
}

int main() {
    int t;
    scanf("%d", &t);
    while(t--){
        int a1, a2, b1, b2;
        scanf("%d %d %d %d", &a1, &a2, &b1, &b2); 
        char* result = ts(a1, a2, b1, b2);
        printf("%s\n", result);
    }
    
    return 0;
}
