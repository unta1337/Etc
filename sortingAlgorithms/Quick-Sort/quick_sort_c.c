#include "../_Include/include_c.h"

int partition(int arr[], int left, int right)
{
	int pivotIndex = right;
	int pivot = arr[pivotIndex];

	int l = left;
	int r = right;

	while (l < r)
	{
		while ((arr[l] < pivot) && (l <= r))
			l++;
		while ((arr[r] >= pivot) && (l <= r))
			r--;

		if (l < r)
			swap(&arr[l], &arr[r]);
	}
	swap(&arr[l], &arr[pivotIndex]);

	return l;
}

void quick_sort_rec(int arr[], int left, int right)
{
	while (left < right)
	{
		int pivotIndex = partition(arr, left, right);

		quick_sort_rec(arr, left, pivotIndex - 1);
		return quick_sort_rec(arr, pivotIndex + 1, right);
	}
}

void quick_sort(int arr[], int size)
{
	quick_sort_rec(arr, 0, size - 1);
}

int main(int argc, char* const argv[])
{
	sorting_test(argc, argv, &quick_sort, "Quick Sort (Right Pivot Point)");

	return 0;
}
