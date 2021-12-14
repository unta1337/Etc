#include <stdio.h>
#include <stdlib.h>

#define SIZE 10

int comp(const void* p, const void* q)
{
	int i = ((int*)p)[1];
	int j = ((int*)q)[1];

	return (i > j) - (i < j);
}

int main()
{
	int arr[SIZE][2];
	for (int i = 0; i < SIZE; i++)
	{
		arr[i][0] = i;
		arr[i][1] = SIZE - i;
	}

	printf("Initial Array:\n");
	for (int i = 0; i < SIZE; i++)
		printf("{ %2d, %2d }\n", arr[i][0], arr[i][1]);
	printf("\n");

	qsort(arr, SIZE, 2 * sizeof(int), comp);

	printf("Sorted Array:\n");
	for (int i = 0; i < SIZE; i++)
		printf("{ %2d, %2d }\n", arr[i][0], arr[i][1]);
	printf("\n");

	return 0;
}
