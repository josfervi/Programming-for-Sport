#include <stdio.h>

int main() {
  
  int a = 1;
  
  int * p;
  p = &a;
  
  printf("%u\n", p);
  
  printf("%u\n", *p);
  printf("%u\n", p[0]);
  
  printf("%u\n", p+1);
  
  printf("%u\n", *(p+1));
  printf("%u\n", p[1]);
  
  return 0;
}