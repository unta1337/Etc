#include "../_Include/include_c.h"

void bubble_sort(int arr[], int size)
{
    for (int i = 0; i < size - 1; i++)
    {
        for (int j = 0; j < size - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
                swap(&arr[j], &arr[j + 1]);
        }
    }
}

int main(int argc, char* const argv[])
{
    sorting_test(argc, argv, &bubble_sort, "Bubble Sort");

    return 0;
}
