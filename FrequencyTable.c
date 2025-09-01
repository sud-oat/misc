#include <stdio.h>
#include <stdlib.h>

int main(){

    int n = 27;
    int *A;
    int i;
    int v;


    A = (int*) malloc(n*sizeof(int));
    for (i = 0; i<n; i++){
        A[i] = 0;
    }

    FILE *ptr;
    ptr = fopen("sampletext.txt", "r");
    if (ptr == NULL){
        return 1;
    }
    char c;
    while ((c = fgetc(ptr)) != EOF){
        v = c - 'a';
        //printf(%'a') Can also work to return the ASCII/Unicode value of a;
        if (v>=0 && v<26){
            A[v]++;
        } else{
            A[26]++;
        }
    }
    fclose(ptr);

    ptr = fopen("output.txt", "w");
    if (ptr == NULL){
        return 1;
    }
    for (i = 0; i<n; i++){
        fprintf(ptr, "%d\n", A[i]);
    }
    fclose(ptr);
    free(A);
    return 0;
}
