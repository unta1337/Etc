#include "../_Include/include_c.h"

#include <math.h>

//#include "queue.h"				// 두 개의 스택을 이용한 큐.
#include "improved_queue.h"			// 원형 큐.

int get_max_length(int arr[], int size)
{
	int max = arr[0];

	for (int i = 0; i < size; i++)
	{
		if (max < arr[i])
			max = arr[i];
	}

	int length = 0;
	while (max != 0)
	{
		length++;
		max /= 10;
	}

	return length;
}

int get_digit(int value, int digit_index)
{
	if (digit_index <= 0)
		return 0;

	int division_value = (int)pow(10, digit_index - 1);

	return value / division_value % 10;
}

void radix_sort(int arr[], int size)
{
	int max_length = get_max_length(arr, size);

	Queue** bucket = (Queue**)malloc(10 * sizeof(Queue*));
	for (int i = 0; i < 10; i++)
		bucket[i] = create_queue(size);

	for (int i = 1; i <= max_length; i++)
	{
		for (int j = 0; j < size; j++)
		{
			int index = get_digit(arr[j], i);
			bucket[index]->enqueue(bucket[index], arr[j]);
		}

		int arr_index = 0;
		for (int k = 0; k < 10; k++)
		{
			while(!bucket[k]->is_empty(bucket[k]))
				arr[arr_index++] = bucket[k]->dequeue(bucket[k]);
		}
	}

	for (int i = 0; i < 10; i++)
		delete_queue(bucket[i]);
	free(bucket);
}


int main(int argc, char* const argv[])
{
	sorting_test(argc, argv, &radix_sort, "Radix Sort");

	return 0;
}
