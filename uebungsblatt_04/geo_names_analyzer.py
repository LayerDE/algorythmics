#!/usr/bin/python3
import time


def read_info_from_file(path):
    tmp = []
    with open(path, 'r') as big_list:
        line = big_list.readline()
        while line:
            tmp2 = line.split('\t')
            if(int(tmp2[14]) > 0 and tmp2[6] == "P"):
                tmp.append(tmp2)
            line = big_list.readline()
    return tmp


def read_info_from_file_3(path):
    tmp = []
    with open(path, 'r') as big_list:
        line = big_list.readline()
        while line:
            tmp2 = line.split('\t')
            if(int(tmp2[14]) > 0 and tmp2[6] == "P" and tmp2[8] == "DE"):
                tmp.append(tmp2)
            line = big_list.readline()
    return tmp


def compute_names_by_sorting(tmp):
    name_listing = [[]]
    found = False
    for x in tmp:
        for y in range(len(name_listing)):
            for z in name_listing[y]:
                if(x[1] == z):
                    if(y >= len(name_listing)):
                        name_listing.append([[x[1], y+1]])
                    else:
                        name_listing[y+1].append([x[1], y+1])
                    name_listing[y].remove([x[1], y])
                    found = True
            if(found):
                break
        if(not found):
            name_listing[0].append([[x[1], 0]])
        found = False
    tmp = []
    for y in name_listing:
        tmp.extend(y)
    return tmp


def compute_names_by_map(list):
    max_index = 0
    locality = {}
    for element in list:
        if element[1] in locality:
            locality[element[1]] = (locality[element[1]] + 1)
            if(locality[element[1]] >= max_index):
                max_index = locality[element[1]]
        else:
            locality[element[1]] = 1
    return locality


def compare_runtimes(array):
    t0 = time.clock()
    compute_names_by_sorting(array)
    t1 = time.clock()
    compute_names_by_map(array)
    t2 = time.clock()
    # Zeit von read_info_from_file
    timebysort = (t1 - t0)
    # Zeit von compute_names_by_map
    timebymap = (t2 - t1)
    print(timebysort)
    print(timebymap)


def compare_results(array):
    """ Test

    >>> compare_results(read_info_from_file("Textfiles/AT.txt"))

    """
    res_list = compute_names_by_sorting(array)
    res_map = compute_names_by_map(array)
    for x in res_list:
        print(x)
        if not res_map[x[0]] == x[1]:
            print("Error")


if __name__ == "__main__":
    compare_results(read_info_from_file("Textfiles/allCountries.txt"))
    compare_runtimes(read_info_from_file("Textfiles/allCountries.txt"))
    compare_runtimes(read_info_from_file_3("Textfiles/allCountries.txt"))
