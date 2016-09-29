#include <stdlib.h> // malloc
#include <stdio.h>  // printf

int* performOps(int *A, int len, int *blen) {
    int i;
    *blen = len * 2;
    int a= *blen * sizeof(int);
    int *B = (int *)malloc((*blen) * sizeof(int));
    for (i = 0; i < len; i++) {
        B[i] = A[i];
        B[i + len] = A[(len - i) % len];
    }
    return B;
}

int main() {
  int a;
  int blen;
  int len= 4;
  int A[4]= {5, 10, 2, 1};
  int *B = performOps(A, len, &blen);
  int i;
  for (i = 0; i < blen; i++) {
    printf("%d ", B[i]);
  }
}