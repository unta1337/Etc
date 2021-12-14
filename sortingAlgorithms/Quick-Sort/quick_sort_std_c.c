#include "../_Include/include_c.h"

int comp(const void* p, const void* q)
{
	int i = *(int*)p;
	int j = *(int*)q;

	return (i > j) - (i < j);
}

void quick_sort(int arr[], int size)
{
	qsort(arr, size, sizeof(int), &comp);
}

int main(int argc, char* const argv[])
{
	sorting_test(argc, argv, &quick_sort, "Quick Sort (std)");

	return 0;
}
