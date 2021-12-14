#include <stdio.h>
#include <stdlib.h>

#define SIZE 10			// size of your array. (outermost dimension)
#define N 4				// size of your nested dimension array.
#define KEY 3			// index you want to make them a key.

int comp(const void* p, const void* q)
{
	int i = ((int*)p)[KEY];
	int j = ((int*)q)[KEY];

	return (i > j) - (i < j);
}

int main()
{
	int arr[SIZE][N];
	for (int i = 0; i < SIZE; i++)
	{
		arr[i][0] = i;
		for (int j = 1; j < N - 1; j++)
			arr[i][j] = 0;
		arr[i][N - 1] = SIZE - i;
	}

	printf("Initial Array:\n");
	for (int i = 0; i < SIZE; i++)
	{
		printf("{ ");
		for (int j = 0; j < N; j++)
			printf("%2d ", arr[i][j]);
		printf("}\n");
	}
	printf("\n");

	qsort(arr, SIZE, N * sizeof(int), comp);

	printf("Sorted Array:\n");
	for (int i = 0; i < SIZE; i++)
	{
		printf("{ ");
		for (int j = 0; j < N; j++)
			printf("%2d ", arr[i][j]);
		printf("}\n");
	}
	printf("\n");

	return 0;
}
