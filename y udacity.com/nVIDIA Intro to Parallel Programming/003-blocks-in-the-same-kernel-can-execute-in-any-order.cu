#include <stdio.h>

#define NUM_BLOCKS 16
#define BLOCK_WIDTH 1

__global__ void hello()
{
    printf("Hello world! I'm a thread in block %d\n", blockIdx.x);
}


int main(int argc,char **argv)
{
    // launch the kernel
    hello<<<NUM_BLOCKS, BLOCK_WIDTH>>>();

    // force the printf()s to flush
    cudaDeviceSynchronize();

    printf("That's all!\n");

    return 0;
}

// Quiz:
//   how many different outputs
//   can different runs of this
//   program produce?
//
// Answer:
//   16! ~ 21 trillion
//   for the reasons given:
//     CUDA does makes few guarantees
//     about when and where thread
//     blocks will run.