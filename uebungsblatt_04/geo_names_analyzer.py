#!/usr/bin/python3

def read_info_from_file(path)
    tmp=[]
    tmp2
    with open(path, 'r') as big_list
        line = big_list.readline()
        while line:
            tmp2=line.split('\t')
            if(tmp2[14]>0&&tmp2[8]=="P")
                tmp.append(tmp2)
            line = big_list.readline()
    return tmp

def compute_names_by_sorting(path)
    tmp=read_info_from_file(path)
    name_listing=[]
    found=False
    max_count=0
    for x in tmp:
        for y in range(len(name_listing)):
            for z in y:
                if(x[1]==z)
                    if(y>=len(name_listing))
                        name_listing.append([x])
                    else:
                        name_listing[y+1].append(x)
                    name_listing[y].remove(x)
                    found=True
            if(found)
                break
        found=False
    tmp=[]
    for y in name_listing:
        tmp.extend(y)
    return tmp


def compute_names_by_map(path)
    