#include<stdio.h>

int main() {
    double first, second, temp;
    
    //Intercambio de dos numeros
    first = 20;
    second = 30;
    printf("Intercambio de dos numeros \n");
    printf("Datos \n");
    printf("Primer numero = %.2lf \n", first);
    printf("Segundo numero = %.2lf \n", second);
    //Value of first is assigned to temp
    temp = first;

    //Value of second is assigned to first
    first = second;

    //Value of temp (initial value of first) is assigned to second
    second = temp;

    printf("\nResultados el intercambio \n");
    printf("Primer numero = %.2lf \n", first);
    printf("Segundo numero = %.2lf \n", second);
    return 0;
}
