# include <stdio.h>

// The KERNEL itself: THE GPU CODE.
// 
// looks like a serial program that will run on one thread
// the CPU is responsible for launching the program on many parallel threads
__global__ void square(float *d_out, float *d_in) {
    int idx = threadIdx.x;
    float f = d_in[idx]; // do you need this intermediate var?
    d_out[idx] = f * f;
}


// another Kernel
__global__ void cube(float * d_out, float * d_in){
	int idx = threadIdx.x;
	float f = d_in[idx];
	d_out[idx] = f * f * f;
}

// What lies below is THE CPU CODE.
int main(int argc, char **argv) {
    const int ARRAY_SIZE = 64;
    const int ARRAY_NUM_BYTES = ARRAY_SIZE * sizeof(float);
    
    // generate the input array on the host/CPU
    float h_in[ARRAY_SIZE];
    for (int i = 0; i < ARRAY_SIZE; i++) {
        h_in[i] = float(i);
    }
    float h_out[ARRAY_SIZE];
    
    // declare GPU memory pointers
    float * d_in;
    float * d_out;
    
    // allocate GPU memory
    cudaMalloc((void **) &d_in, ARRAY_NUM_BYTES);
    cudaMalloc((void **) &d_out, ARRAY_NUM_BYTES);
    
    // transfer the data from the CPU to the GPU
    cudaMemcpy(d_in, h_in, ARRAY_NUM_BYTES, cudaMemcpyHostToDevice);
    
    // launch the kernel
    square<<<1, ARRAY_SIZE>>>(d_out, d_in);
    // cube<<<1, ARRAY_SIZE>>>(d_out, d_in);
    
    // copy back the result data from the GPU to the CPU
    cudaMemcpy(h_out, d_out, ARRAY_NUM_BYTES, cudaMemcpyDeviceToHost);
    
    // print out the resulting array
    for (int i = 0; i < ARRAY_SIZE; i++) {
        printf("%f", h_out[i]);
        printf( ((i % 4) == 3) ? "\n" : "\t" );
    }
    
    // free GPU memory allocation
    cudaFree(d_in);
    cudaFree(d_out);
    
    return 0;
}