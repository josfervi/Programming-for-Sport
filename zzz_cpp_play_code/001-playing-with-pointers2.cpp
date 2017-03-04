#include <stdio.h>

int main() {
  
  int a = 10;
  int b = 20;
  
  int r;
  
  // error when you try to set a non int pointer to the address of an int
  // r = &a; // error: invalid conversion from 'int*' to 'int' [-fpermissive]
  
  int * p;
  
  p = &b;
  // the following 4 printf statements all print
  // the value of p == the address of b
    // the value of p
  printf("%u\n", p);
    // the addres of b
  printf("%u\n", &b);
    // the address of (the value at addres p)
    // the address of M[p]
  printf("%u\n", &*p);
    // the value at address (addres of p)
    // M[&p]
    // value of p
  printf("%u\n", *&p);
  
  // the following 2 printf statements all print
  // the value of b
  printf("%u\n", *p);
  printf("%u\n", *&b);
  
  return 0;
}