#include <stdlib.h>
#include <stdio.h>

void ordenarnumeros(int arreglo[], int lon){
    int Temp;
    for(int i = 0; i < lon; i++){
        for(int j = 0; j < lon - 1; j++){if(arreglo[j] < arreglo[j + 1]){// cambia "<" a ">" para cambiar la manera de ordenar
                Temp = arreglo[j];
                arreglo[j] = arreglo[j + 1];
                arreglo[j + 1] = Temp;
            }
        }
    }

    for(int i = 0; i < lon; i++){
        printf("%d \n", arreglo[i]);
    }
        
}

main(){
    int lon, n;
    printf("Ingresa el numero de numeros a capturar: ");
    scanf("%d", &lon);
    int arr[lon];
    for(int i = 0; i < lon; i++){
    	printf("Ingresa el numero %d: ", i+1);
    	scanf("%d", &n);
        arr[i] = n;
    }
    printf("\nNumeros ordenados: \n");
    ordenarnumeros(arr, lon);
    system("pause");
}
