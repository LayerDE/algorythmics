#!/usr/bin/python3
# import ctypes
# import math


class PriorityQueueItem:
    """ Provides a handle for a queue item.
    A simple class implementing a key-value pair,
    where the key is an integer, and the value can
    be an arbitrary object. Index is the heap array
    index of the item.
    """
    def __init__(self, key, value, index):
        self._key = key
        self._value = value
        self._index = index

    def __lt__(self, other):
        """ Enables us to compare two items with a < b.
        The __lt__ method defines the behavior of the
        < (less than) operator when applied to two
        objects of this class. When using the code a < b,
        a.__lt__(b) gets evaluated.
        There are many other such special methods in Python.
        See "python operator overloading" for more details.
        """
        return self._key < other._key

    def get_heap_index(self):
        """ Return heap index of item."""
        return self._index

    def set_heap_index(self, index):
        """ Update heap index of item."""
        self._index = index


class PriorityQueueMinHeap:
    """Priority queue implemented as min heap."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._list = []

    """
    TO DO:
    Create methods:
    insert(self, key, value) -> return inserted item object
    get_min(self) -> return item._key and item._value
    delete_min(self) -> return item._key an item._value
    change_key(self, item, new_key), no return value
    size(self) -> return current heap size

    Plus your choice of additional helper (private) methods
    Helpful would be e.g.
    _repair_heap_up(), _repair_heap_down(), _swap_items() ...

    Use private methods (_method_name) if they only
    get accessed within the class.
    Private methods have a leading underscore:
    def _swap_items(self, i, j):
        # Swap items with indices i,j (also swap their indices!)
        ...

    """
    def insert(self, key, value):  # todo heapify
        tmp2 = len(self._list)
        tmp = PriorityQueueItem(key, value, tmp2)
        self._list.append(tmp)
        self._heapify_rekrusiv_up(tmp2)
        return tmp

    def get_min(self):
        item = self._list[0]
        return [item._key, item._value]

    def delete_min(self):
        self._switch_elements(0, len(self._list) - 1)
        item = self._list.pop()
        self._heapify_rekrusiv_down(0)
        return [item._key, item._value]

    def change_key(self, item, new_key):
        item._key = new_key
        self._heapify(item.get_heap_index())

    def size(self):
        return len(self._list).bit_length()

    def _heapify(self, start_index):
        if(self._list[start_index]._key < self._list[_calc_index_up(start_index)]._key and start_index != 0):
            self._switch_elements(start_index, _calc_index_up(start_index))
            self._heapify_rekrusiv_up(_calc_index_up(start_index))
        else:
            self._heapify_rekrusiv_down(start_index)

    def _heapify_rekrusiv_up(self, start_index: int):
        if(start_index != 0):
            if(self._list[start_index]._key < self._list[_calc_index_up(start_index)]._key):
                self._switch_elements(start_index, _calc_index_up(start_index))
                self._heapify_rekrusiv_up(_calc_index_up(start_index))

    def _heapify_rekrusiv_down(self, start_index: int):
        if(_calc_index_down(start_index, 1) < len(self._list)):
            if((self._list[start_index]._key > self._list[_calc_index_down(start_index, 0)]._key) or(self._list[start_index]._key > self._list[_calc_index_down(start_index, 1)]._key)):
                if(self._list[_calc_index_down(start_index, 0)]._key < self._list[_calc_index_down(start_index, 1)]._key):
                    self._switch_elements(_calc_index_down(start_index, 0), start_index)
                    self._heapify_rekrusiv_down(_calc_index_down(start_index, 0))
                else:
                    self._switch_elements(_calc_index_down(start_index, 1), start_index)
                    self._heapify_rekrusiv_down(_calc_index_down(start_index, 1))
        elif(_calc_index_down(start_index, 1) < len(self._list)):
            if(self._list[start_index]._key > self._list[_calc_index_down(start_index, 0)]._key):
                self._switch_elements(_calc_index_down(start_index, 0), start_index)

    def _switch_elements(self, indexA: int, indexB: int):
        tmp = self._list[indexA]
        self._list[indexA] = self._list[indexB]
        self._list[indexB] = tmp
        self._list[indexA].set_heap_index(indexA)
        self._list[indexB].set_heap_index(indexB)


def _calc_index_up(x):
    return ((x + 1) >> 1) - 1


def _calc_index_down(x, element):
    return (((x + 1) << 1) + element) - 1


if __name__ == "__main__":
    # Create priority queue object.
    pq1 = PriorityQueueMinHeap()
    pq1_list = []
    # Insert some flights into queue.
    for x in range(500):
        pq1_list.append(pq1.insert(x, str(x)))

    pq1.delete_min()
    print(pq1.get_min()[1])
    pq1.delete_min()
    print(pq1.get_min()[1])
    for x in range(200):
        pq1.delete_min()
    print(pq1.get_min()[1])
    pq1.change_key(pq1_list[300], 20)
    print(pq1.get_min()[1])
