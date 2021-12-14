#include "../_Include/include_c.h"

void merge(int arr[], int left, int middle, int right)
{
	int* sorted = (int*)malloc((right - left + 1) * sizeof(int));

	int l = left;
	int r = middle + 1;
	int index = 0;

	while (l <= middle && r <= right)
		sorted[index++] = arr[l] < arr[r] ? arr[l++] : arr[r++];

	if (l > middle)
	{
		while (r <= right)
			sorted[index++] = arr[r++];
	}
	else
	{
		while (l <= middle)
			sorted[index++] = arr[l++];
	}

	index = 0;
	for (int i = left; i <= right; i++)
		arr[i] = sorted[index++];

	free(sorted);
}

void divide(int arr[], int left, int right)
{
	while (left < right)
	{
		int middle = (left + right) / 2;
		divide(arr, left, middle);
		divide(arr, middle + 1, right);
		return merge(arr, left, middle, right);
	}
}

void merge_sort(int arr[], int size)
{
	divide(arr, 0, size - 1);
}

int main(int argc, char* const argv[])
{
	sorting_test(argc, argv, &merge_sort, "Merge Sort");

	return 0;
}
