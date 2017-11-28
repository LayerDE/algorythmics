#!/usr/bin/python3
from random import randint
from random import sample
# xz_x ist ersatz für zu lange namen


class HashFunction(object):

    # def __init__(self, hm):
    #     self.a = 0
    #     self.b = 0
    #     self.u = 0
    #     self.m = hm
    #     if self.u > self.m:
    #         self.p = next_prime(self.u)
    #     else:
    #         self.p = next_prime(self.m+1)
    #     self.set_random_parameters()

    def __init__(self, hp, hu, hm):  # no overloding
        self.a = 0
        self.b = 0
        self.m = hm
        self.p = hp
        self.u = hu
        self.set_random_parameters()

    def set_random_parameters(self):
        self.a = randint(1, self.p-1)
        self.b = randint(0, self.p-1)

    def h_ab(self, x):  # univeral
        return (self.a * x + self.b) % self.p % self.m

    def g_ab(self, x):  # non universal
        return x % self.p


def next_prime(x):  # old code
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                return next_prime(x+1)
        return x
    else:
        return 1


# gen_hast_table
def xz3(key_list: list, hash_ptr: object, universal: bool):
    table = []
    for x in range(hash_ptr.m):
        table.append([])
    for key in key_list:
        if(universal):
            table[hash_ptr.h_ab(key)].append(key)
        else:
            table[hash_ptr.g_ab(key)].append(key)
    return table


# mean_bucket_size
def xz2(table: list, list_size: int):
    count = 0
    for bucket in table:
        if bucket:
            count = count + 1
    return list_size / count


# estimate_c_for_single_set
def xz1(key_list: list, hash_ptr: object, universal: bool):
    tmp = 0
    for n in range(1000):
        tmp = tmp + xz2(xz3(key_list, hash_ptr, universal), len(key_list))
        # print(key_list)
        hash_ptr.set_random_parameters()

    mean = tmp / 1000

    return ((mean - 1) * hash_ptr.m) / len(key_list)


# estimate_c_for_multiple_sets
def xz4(n: int, k: int, hash_ptr: object, universal: bool):

    minimum = float("inf")
    maximum = float("-inf")
    all_c = 0

    for i in range(n):
        random_keys = sample(range(1, (2 ** k) + 1), hash_ptr.u)
        c = xz1(random_keys, hash_ptr, universal)

        all_c = all_c + c
        if c < minimum:
            minimum = c
        if c > maximum:
            maximum = c

    return [all_c / n, minimum, maximum]


if __name__ == "__main__":
    tmp1 = HashFunction(101, 100, 10)
    print(xz4(1000, 20, tmp1, True))
    tmp2 = HashFunction(10, 100, 0)
    print(xz4(1, 20, tmp2, False)[0])
