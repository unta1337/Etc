import random

def is_sorted(lst: list) -> bool:
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False

    return True

def sorting_test(argv: list, sorting_algorithm , name: str) -> None:
    showArray: int = int(argv[2]) if len(argv) > 2 else 0

    size: int = int(argv[1]) if len(argv) > 1 else 10
    lst: list = []
    for _ in range(size):
        lst.append(random.randrange(size))

    print(name, end = '\n\n')

    print(f'Size of list: {size}', end = '\n\n')

    if showArray == 0 or showArray == 1:
        print('Initial List:', end = '\t')
        for e in lst:
            print(e, end = ' ')
        print(end = '\n\n')

    sorting_algorithm(lst)

    if showArray == 0 or showArray == 2:
        print('Sorted List:', end = '\t')
        for e in lst:
            print(e, end = ' ')
        print(end = '\n\n')

    print(f'Is Sorted: {is_sorted(lst)}')