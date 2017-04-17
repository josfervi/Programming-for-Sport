int main() {
    
    // @ 300
    int x = 5;
    
    int * p = &x;
    
    // print p would print '300'
    
    // print *p would print '5'
    
    // since p is an int pointer
    // p = p + 1
    // increments p by 4,
    // the number of bytes in an int
    p = p + 1; // p = 304
    
    // print *p will print the value at address 304
    
    
    // 
    int A[5];
    
    // int takes up 4 bytes
    
    // @ 200
    A[0] = 1;
    
    // @ 204
    A[1] = 2;
    
    // @ 208
    A[2] = 3;
    
    // @ 212
    A[3] = 4;
    
    // @ 216
    A[4] = 5;
    
    int * ptr;
    p = &A[0];
    
    // pointer arithmetic
    
    // print p would print '200'
    // print *p would print '1'
    
    // print p+1 would print '204'
    // print *(p+1) would print '2'
    
    // print p+2 would print '208'
    // print *(p+2) would print '3'
    
    int * pointer;
    pointer = A;
    
    // A is already an int pointer
    // and it points to A[0]
    // i.e. A == &A[0] == the base address of array A
    
    // print pointer would print '200'
    // print A would print '200'
    // print *A would print '1'
    // print A+1 would print '204'
    // print *(A+1) would print '2'
    
    // A++; // gives an error, but
    // pointer++; // doesn't give an error
    
    // for 0 <= i < size of A
    //
    //   &A[i] == A+i == the address of A[i]
    //
    //   A[i] == *(A+i)
}