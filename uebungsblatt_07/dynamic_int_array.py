#!/usr/bin/python3

# import argparse
import numpy as np
import time


class DynamicIntArray:
    """Dynamic integer array class implemented with fixed-size numpy array."""

    def __init__(self):
        """Create empty array with length 0 and capacity 1."""
        self._n = 0  # Number of elements in array
        self._c = 1  # Capacity
        self._a = self._create_array(self._c)
        self._switch = True  # for test 3 and 4

    def __len__(self):
        """Return number of elements in the array."""
        return self._n

    def __getitem__(self, i):
        """Return element at index i."""
        # Check for index out of bounds error.
        if not 0 <= i < self._n:
            raise IndexError('index out of bounds')
        return self._a[i]

    def append(self, value):
        """Add integer value to end of array."""
        # Check if given value is of integer type.
        if not isinstance(value, int):
            raise TypeError('value is not integer')
        if self._n == self._c:  # time to resize
            self._resize(2 * self._c)
        self._a[self._n] = value
        self._n += 1

    def remove(self):
        """Add integer value to end of array."""
        # Check if given value is of integer type.
        if self._n > 0:
            if self._n <= self._c/2:  # time to resize
                # self._resize(int(np.ceil(0.75 * self._c)))  # round up
                self._resize(int(0.75 * self._c))  # rund down
            self._n -= 1

    def append_switch(self, value):
        """Add integer value to end of array."""
        # Check if given value is of integer type.
        if not isinstance(value, int):
            raise TypeError('value is not integer')
        if self._n == self._c:  # time to resize
            self._resize(2 * self._c)
            self._switch = not self._switch
        self._a[self._n] = value
        self._n += 1

    def remove_switch(self):
        """Add integer value to end of array."""
        # Check if given value is of integer type.
        if self._n > 0:
            if self._n <= self._c/2:  # time to resize
                # self._resize(int(np.ceil(0.75 * self._c)))  # round up
                self._resize(int(0.75 * self._c))  # rund down
                self._switch = not self._switch
            self._n -= 1

    def _resize(self, new_c):
        """Resize array to capacity new_c."""
        b = self._create_array(new_c)
        for i in range(self._n):
            b[i] = self._a[i]
        # Assign old array reference to new array.
        self._a = b
        self._c = new_c

    def _create_array(self, new_c):
        """Return new array with capacity new_c."""
        return np.empty(new_c, dtype=int)  # data type = integer


if __name__ == "__main__":
    size = 10000000
    r_a = np.empty(size, dtype=float)  # runtime append
    r_r = np.empty(size, dtype=float)  # runtime remove
    a1 = DynamicIntArray()
    r_a_s = time.time()  # runtime append start
    for x in range(size):
        a1.append(x)
        r_a[x] = time.time()
    r_r_s = time.time()  # runtime remove start
    for x in range(size):
        a1.remove()
        r_r[x] = time.time()
    with open('runtime_append.txt', 'a') as fptr:
        for x in range(size):
            fptr.write(str(x + 1) + '\t' + str(r_a[x] - r_a_s) + '\n')
    with open('runtime_remove.txt', 'a') as fptr:
        for x in range(size):
            fptr.write(str(x + 1) + '\t' + str(r_r[x] - r_r_s) + '\n')
    a2 = DynamicIntArray()
    for x in range(1000000):
        a2.append(x)
    r_a_s = time.time()
    for x in range(size):
        if(a2._switch):
            a2.append_switch(x)
        else:
            a2.remove_switch()
        r_a[x] = time.time()
    a2 = DynamicIntArray()
    for x in range(1000000):
        a2.append(x)
    r_r_s = time.time()
    for x in range(size):
        if(not a2._switch):
            a2.append_switch(x)
        else:
            a2.remove_switch()
        r_r[x] = time.time()
    with open('runtime_append_switch.txt', 'a') as fptr:
        for x in range(size):
            fptr.write(str(x + 1) + '\t' + str(r_a[x] - r_a_s) + '\n')
    with open('runtime_remove_switch.txt', 'a') as fptr:
        for x in range(size):
            fptr.write(str(x + 1) + '\t' + str(r_r[x] - r_r_s) + '\n')
    print("end")
