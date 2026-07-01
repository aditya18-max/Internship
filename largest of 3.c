#include <stdio.h>

int main() {
    int a, b, c;
    
    printf("Enter 3 numbers: ");
    scanf("%d %d %d", &a, &b, &c);
    
    if (a > b && a > c) {
        printf("A is greater\n");
    } 
    else if (b > c) {
        printf("B is greater\n");
    } 
    else {
        printf("C is greater\n");
    }
    
    return 0;
}