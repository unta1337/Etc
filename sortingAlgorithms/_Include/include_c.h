#ifndef _INCLUCE_C_H
#define _INCLUCE_C_H

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int isSorted(int arr[], int size)
{
	for (int i = 0; i < size - 1; i++)
	{
		if (arr[i] > arr[i + 1])
			return 0;
	}

	return 1;
}

void swap(int* p, int* q)
{
    int temp = *p;
    *p = *q;
    *q = temp;
}

void sorting_test(int argc, char* const argv[], void (*sorting_algorithm)(int arr[], int size), const char* name)
{
	srand((unsigned int)time(NULL));

    int showArray = argc < 3 ? 0 : (int)strtol(argv[2], NULL, 10);

	int size = argc < 2 ? 10 : (int)strtol(argv[1], NULL, 10);
	int* arr = (int*)malloc(size * sizeof(int));

	for (int i = 0; i < size; i++)
		arr[i] = rand() % 1000;

	printf("%s\n\n", name);

	printf("Size of array: %d\n\n", size);

    if (showArray == 0 || showArray == 1)
    {
        printf("Initial array:\t");
        for (int i = 0; i < size; i++)
            printf("%d ", arr[i]);
        printf("\n\n");
    }

	sorting_algorithm(arr, size);

    if (showArray == 0 || showArray == 2)
    {
        printf("Sorted array:\t");
        for (int i = 0; i < size; i++)
            printf("%d ", arr[i]);
        printf("\n\n");
    }

	printf("Is Sorted: %c\n\n", isSorted(arr, size) ? 'T' : 'F');

	int start = size / 3;
	int show_range = size / 3 * 2 / 5;
	int end = start + show_range;
	if (end - start > 50)
		end = start + 50;

	printf("Partial array (from %d to %d):\t", start, end );
	for (int i = start; i <= end; i++)
		printf("%d ", arr[i]);
	printf("\n");
}

#endif
