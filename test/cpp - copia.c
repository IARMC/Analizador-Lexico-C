#include<stdio.h>
int main() {
    double first, second, temp;
    //Intercambio de dos números
    first = 20;
    second = 30;
    
    //Value of first is assigned to temp
    temp = first;

    //Value of second is assigned to first
    first = second;

    //Value of temp (initial value of first) is assigned to second
    second = temp;

    printf("Resultados el intercambio");
    printf("Primer número = %.2lf", first);
    printf("Segundo número = %.2lf", second);
    return 0;
}