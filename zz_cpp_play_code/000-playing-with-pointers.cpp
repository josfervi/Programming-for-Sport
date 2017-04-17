// pointers
//   variables that store the
//   address of another var

// int * p // read as 'int pointer p'
// p = & a // read as 'set p equal to the address of a'

int main() {
  
  // 1 byte
  char c;
  
  // 4 bytes
  float f;
  
  // 4 bytes
  // address 204
  int a;
  a = 5;
  a++; // a = 6
  
  // address 208 
  int b = 10;
  
  // address 64
  // read as 'int pointer p'
  // a pointer var that pts to an int
  // can store the address of an int
  int* p;
  
  // read as 'set p equal to the address of a'
  p = &a; // p = 204
  
  // print the value of p
  printf("%d\n", p); // 204
  
  // print the value of &a, i.e. the address of a
  printf("%d", &a); // 204
  
  // print the value of &p, i.e. the address of p
  printf("%d", &p); // 64
  
  // dereferencing *p
  // print the value of *p, i.e. the value at address p 
  printf("%d", *p); // 6
  
  // read as 'set the value at address p equal to 8'
  // i.e.
  // read as 'set the value at address 204 equal to 8'
  *p = 8
  
  // print the value of *p, i.e. the value at address p
  printf("%d", *p); // 8
  // print the value of a
  printf("%d", a); // 8
  
  return 0;
}