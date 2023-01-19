#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *create_dyn_array(unsigned int n){
    int *array = malloc(n * sizeof(int));


    for (unsigned int i = 0; i < n; i++){
        scanf("%d", &array[i]);
        
    }
    return array;

}

int *add_dyn_array(int *arr, unsigned int num, int newval){
    int *array = realloc(arr, (num + 1) * sizeof(int));

    array[num] = newval;

    return array;
}

int main()
{
    unsigned int n = 5;
    int *arr = create_dyn_array(n);
    //printf(arr);

    int newval = 4;
    int *ret = add_dyn_array(arr, n, newval);

    int i = 0;
    while (i <= 6){
        printf("%d", ret[i]);
        i += 1;
    }
}