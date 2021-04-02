#include <stdio.h>
#include <string.H>
#define MAX 10

int main(){
    int numero[10], arreglos[MAX];
    int i, val, suma = 0;

    for(i = 0; i < 10; i++){
        val = i * 10;
        numero[i] = val;
        printf("Numero %d: %d \n", i, numero[i]);
        suma = suma + val;
    }
    printf("Suma : %d",suma);
    return 0;
}
