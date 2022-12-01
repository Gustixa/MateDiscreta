% % cu
/**
 * --------------------------------------------------------
 * Universidad del Valle de Guatemala
 * CC3056 - Programación de Microprocesadores
 * --------------------------------------------------------
 * Streams.cu
 * --------------------------------------------------------
 * Suma de dos vectores en CUDA
 * Demuestra la forma de usar CUDA 7 Streams para
 * concurrencia simplificada
 * --------------------------------------------------------
 * AUTH.	Mark Harris
 * MOD.   Kimberly B.
 * DATE		2022-10-7
 * --------------------------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include <cuda_runtime.h>

#define SIZE 10
		// GLOBAL1: funcion llamada desde el host y ejecutada en el device (kernel)
		__global__ void
		Kernel1(int *a, int *b, int *c)
{
	int myID = threadIdx.x + blockDim.x * blockIdx.x;
	// Solo trabajan N hilos
	if (myID < SIZE)
	{
		c[myID] = a[myID] + b[myID];
	}
}

// GLOBAL2: funcion llamada desde el host y ejecutada en el device (kernel)
__global__ void Kernel2(int *d, int *e, int *f)
{
	int myID = threadIdx.x + blockDim.x * blockIdx.x;
	// Solo trabajan N hilos
	if (myID < SIZE)
	{
		f[myID] = d[myID] * e[myID];
	}
}

__global__ void kernel3(int *g, int *h, int *i)
{
	int myId = threadIdx.x + blockDim.x * blockIdx.x;
	if (myId < SIZE)
	{
		i[myId] = (g[myId] - h[myId]) * 5;
	}
}

int main(void)
{
	cudaStream_t stream1, stream2, stream3;
	cudaStreamCreate(&stream1);
	cudaStreamCreate(&stream2);
	cudaStreamCreate(&stream3);

	int *a1, *b1, *c1; // host vars to use in stream 1 mem ptrs
	int *a2, *b2, *c2; // host vars to use in stream 2 mem ptrs
	int *a3, *b3, *c3;

	int *dev_a1, *dev_b1, *dev_c1; // stream 1 mem ptrs
	int *dev_a2, *dev_b2, *dev_c2; // stream 2 mem ptrs
	int *dev_a3, *dev_b3, *dev_c3;

	// stream 1 - mem allocation at Global memmory for device and host, in order
	cudaMalloc((void **)&dev_a1, SIZE * sizeof(int));
	cudaMalloc((void **)&dev_b1, SIZE * sizeof(int));
	cudaMalloc((void **)&dev_c1, SIZE * sizeof(int));

	cudaHostAlloc((void **)&a1, SIZE * sizeof(int), cudaHostAllocDefault);
	cudaHostAlloc((void **)&b1, SIZE * sizeof(int), cudaHostAllocDefault);
	cudaHostAlloc((void **)&c1, SIZE * sizeof(int), cudaHostAllocDefault);

	// stream 2 - mem allocation at Global memmory for device and host, in order
	cudaMalloc((void **)&dev_a2, SIZE * sizeof(int));
	cudaMalloc((void **)&dev_b2, SIZE * sizeof(int));
	cudaMalloc((void **)&dev_c2, SIZE * sizeof(int));

	cudaHostAlloc((void **)&a2, SIZE * sizeof(int), cudaHostAllocDefault);
	cudaHostAlloc((void **)&b2, SIZE * sizeof(int), cudaHostAllocDefault);
	cudaHostAlloc((void **)&c2, SIZE * sizeof(int), cudaHostAllocDefault);

	// stream 3 - mem allocation at Global memmory for device and host, in order
	cudaMalloc((void **)&dev_a3, SIZE * sizeof(int));
	cudaMalloc((void **)&dev_b3, SIZE * sizeof(int));
	cudaMalloc((void **)&dev_c3, SIZE * sizeof(int));

	cudaHostAlloc((void **)&a3, SIZE * sizeof(int), cudaHostAllocDefault);
	cudaHostAlloc((void **)&b3, SIZE * sizeof(int), cudaHostAllocDefault);
	cudaHostAlloc((void **)&c3, SIZE * sizeof(int), cudaHostAllocDefault);
	// Generate data
	for (int i = 0; i < SIZE; i++)
	{
		a1[i] = 1 + i;
		b1[i] = 5 + i;

		a2[i] = 3 + i;
		b2[i] = 4 + i;

		a3[i] = 7 + i;
		b3[i] = 10 + i;
	}

	for (int i = 0; i < SIZE; i++)
	{
		// STREAM 1
		// HOST TO DEVICE COPY DATA (TO OPERATE)
		cudaMemcpyAsync(dev_a1, a1, SIZE * sizeof(int), cudaMemcpyHostToDevice, stream1);
		cudaMemcpyAsync(dev_b1, b1, SIZE * sizeof(int), cudaMemcpyHostToDevice, stream1);

		Kernel1<<<1, SIZE, 0, stream1>>>(dev_a1, dev_b1, dev_c1);
		cudaMemcpyAsync(c1, dev_c1, SIZE * sizeof(int), cudaMemcpyDeviceToHost, stream1);

		// STREAM 2
		// HOST TO DEVICE COPY DATA (TO OPERATE)
		cudaMemcpyAsync(dev_a2, a2, SIZE * sizeof(int), cudaMemcpyHostToDevice, stream2);
		cudaMemcpyAsync(dev_b2, b2, SIZE * sizeof(int), cudaMemcpyHostToDevice, stream2);

		Kernel2<<<1, SIZE, 1, stream2>>>(dev_a2, dev_b2, dev_c2);
		cudaMemcpyAsync(c2, dev_c2, SIZE * sizeof(int), cudaMemcpyDeviceToHost, stream2);

		// STREAM 3
		//
		cudaMemcpyAsync(dev_a3, a3, SIZE * sizeof(int), cudaMemcpyHostToDevice, stream3);
		cudaMemcpyAsync(dev_b3, b3, SIZE * sizeof(int), cudaMemcpyHostToDevice, stream3);

		Kernel3<<<1, SIZE, 1, stream2>>>(dev_a3, dev_b3, dev_c3);
		cudaMemcpyAsync(c3, dev_c3, SIZE * sizeof(int), cudaMemcpyDeviceToHost, stream3);
	}

	cudaStreamSynchronize(stream1); // wait for stream1 to finish
	cudaStreamSynchronize(stream2);
	cudaStreamSynchronize(stream3);

	printf("--- STREAM 1 ---\n");
	printf("> Vector a1:\n");
	for (int i = 0; i < SIZE; i++)
	{
		printf("%d ", a1[i]);
	}

	printf("> \n Vector b1:\n");
	for (int i = 0; i < SIZE; i++)
	{
		printf("%d ", b1[i]);
	}

	printf("> \n Vector c1:\n");
	for (int i = 0; i < SIZE; i++)
	{
		printf("%d ", c1[i]);
	}

	printf("\n\n--- STREAM 2 ---\n");

	printf("> Vector a2:\n");
	for (int i = 0; i < SIZE; i++)
	{
		printf("%d ", a2[i]);
	}

	printf("> \n Vector b2:\n");
	for (int i = 0; i < SIZE; i++)
	{
		printf("%d ", b2[i]);
	}

	printf("> \n Vector c2:\n");
	for (int i = 0; i < SIZE; i++)
	{
		printf("%d ", c2[i]);
	}
	printf("\n");

	printf("\n\n--- STREAM 3 ---\n");

	printf("> Vector a3:\n");
	for (int i = 0; i < SIZE; i++)
	{
		printf("%d ", a3[i]);
	}

	printf("> \n Vector b3:\n");
	for (int i = 0; i < SIZE; i++)
	{
		printf("%d ", b3[i]);
	}

	printf("> \n Vector c3:\n");
	for (int i = 0; i < SIZE; i++)
	{
		printf("%d ", c3[i]);
	}
	printf("\n");
	cudaStreamDestroy(stream1); // because we care
	cudaStreamDestroy(stream2);
	cudaStreamDestroy(stream3);

	return 0;
}