import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from _Include.include_py import *

def main():
    sorting_test(sys.argv, bubble_sort, 'Bubble Sort')

def bubble_sort(lst: list) -> None:
    size: int = len(lst)

    for i in range(size - 1):
        for j in range(size - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

if __name__ == '__main__':
    main()
