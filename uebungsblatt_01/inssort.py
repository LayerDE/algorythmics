#!/usr/bin/python3


def inssort(lst):
	""" Sort list using the inssort algorithm.

	>>> inssort([24, 6, 12, 32, 18])
	[6, 12, 18, 24, 32]

	>>> inssort([])
	[]

	>>> inssort("hallo")
	Traceback (most recent call last):
		...
	TypeError: lst must be a list

    """
    # Check given parameter data type.
	if not type(lst) == list:
		raise TypeError('lst must be a list')

	# Get length of the list.
	i = 1
	while i < len(lst):
		x = lst[i]
		j = i - 1
		while j >= 0 and lst[j] > x:
			lst[j+1] = lst[j]
			j = j - 1
		lst[j+1] = x
		i = i + 1
        return lst


if __name__ == "__main__":
	# Create an unsorted list of integers.
	numbers = [10, 4, 1, 5, 2, 3, 11, 3, 9]
	# Sort the list.
	print(inssort(numbers))
