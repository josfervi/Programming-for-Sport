// not verified

#include <stdio.h>

#define ARRAY_SIZE 128

__global__ void kernel()
{
	int idx = threadIdx.x;
	
	// declare a shared variable
	// shared by all the threads
	// in this thread block
	// Q: does each thread have to do this?
	__shared__ int array[ARRAY_SIZE];
	
	array[idx] = idx; // write op
	
	// all writes should complete before we allow any reads
	__syncthreads();
	
	if (idx < ARRAY_SIZE-1)
	{
	    int temp = array[idx + 1]; // read op
	    
	    // all reads should complete before we allow any writes
	    __syncthreads();
	    
	    array[idx] = temp;
	    
	    // to be safe
	    // all writes should complete before we move on
	    __syncthreads();
	}
}

int main(int argc, char **argv) {
    
    // launch the kernel
    kernel<<<1, ARRAY_SIZE>>>();
    
    return 0;
}