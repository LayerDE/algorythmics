#!/usr/bin/python3


def heapsort(lst):
    """ Sort list using the MinSort algorithm.

    >>> heapsort([24, 6, 12, 32, 18])
    [6, 12, 18, 24, 32]

    >>> heapsort([])
    []

    >>> heapsort("hallo")
    Traceback (most recent call last):
        ...
    TypeError: lst must be a list

    """
    # Check given parameter data type.
    if not type(lst) == list:
        raise TypeError('lst must be a list')

    length = len(lst) - 1
    leastParent = int(length / 2)
    for i in range(leastParent, -1, -1):
        heapify(lst, i, length)

    for i in range(length, 0, -1):
        if lst[0] > lst[i]:
            swap(lst, 0, i)
            heapify(lst, 0, i - 1)
    return lst


def heapify(lst, first, last):
    largest = 2 * first + 1
    while largest <= last:
        if (largest < last) and (lst[largest] < lst[largest + 1]):
            largest += 1

        if lst[largest] > lst[first]:
            swap(lst, largest, first)
            first = largest
            largest = 2 * first + 1
        else:
            return


def swap(lst, x, y):
    tmp = lst[x]
    lst[x] = lst[y]
    lst[y] = tmp


if __name__ == "__main__":
    # Create an unsorted list of integers.
    numbers = [10, 4, 1, 5, 2, 3, 11, 3, 9]
    # Sort the list.
    print(heapsort(numbers))
