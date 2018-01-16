import random
import sys
import time


class BinarySearchTree:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if(self.head is None):
            self.head = node
        else:
            cur = self.head
            while(cur is not None):
                if(node.key_int == cur.key_int):
                    cur.set_val(node.val_str)
                    break
                elif(node.key_int < cur.key_int):
                    if(cur.next_node[0] is not None):
                        cur = cur.next_node[0]
                    else:
                        cur.set_nx_node(node, 0)
                else:
                    if(cur.next_node[1] is not None):
                        cur = cur.next_node[1]
                    else:
                        cur.set_nx_node(node, 1)

    def lookup(self, key):
        cur = self.head
        while(cur is not None):
            if(key == cur.key_int):
                return cur
            elif(key < cur.key_int):
                cur = cur.next_node[0]
            else:
                cur = cur.next_node[1]
        return None

    def to_string(self, str_lenght):
        tmp = ""
        tmp_len = self.get_lenght()
        lenght = tmp_len[0]
        max_key = tmp_len[1]+3
        if(max_key < str_lenght):
            max_key = str_lenght
        size = 1
        nodes = [self.head]
        filler = ""
        for _ in range(max_key):
            filler = filler + " "
        for _ in range(lenght-1):
            size = size * 2 + 1
        # print(filler + str(size) + filler +str(lenght)) #DEBUG
        for _ in range(lenght):
            second = False
            # print("master")
            nx_nodes = []
            size1_2 = int(size/2)
            for _ in range(size1_2):
                    tmp = tmp + filler
            for node in nodes:
                if(second):
                    for _ in range(size):
                        tmp = tmp + filler
                # print("in here")
                if(node is not None):
                    # print("a")
                    tmp = tmp + node.to_string(max_key)
                    nx_nodes.extend(node.next_node)
                else:
                    # print("b")
                    tmp = tmp + filler
                    nx_nodes.extend([None, None])
                # for _ in range(size):
                #    tmp = tmp + filler
                second = True
            tmp = tmp + "\n"
            nodes = nx_nodes
            size = size1_2
        return tmp

    def get_lenght(self):
        nodes = []
        if(self.head is not None):
            nodes.append(self.head)
            max_key_lenght = len(str(self.head.key_int))
        else:
            max_key_lenght = 0
        length = 0
        while(len(nodes) > 0):
            tmp = []
            length += 1
            for node in nodes:
                if(node is not None):
                    for nx_node in node.next_node:
                        if(nx_node is not None):
                            if(len(str(nx_node.key_int)) > max_key_lenght):
                                max_key_lenght = len(str(nx_node.key_int))
                            tmp.append(nx_node)
            nodes = tmp
        return [length, max_key_lenght]


class Node:
    def __init__(self, key, value):
        self.key_int = key
        self.val_str = value
        self.head = None
        self.next_node = [None, None]

    def set_val(self, value):
        self.val_str = value

    def set_nx_node(self, node, index):
        self.next_node[index] = node
        self.next_node[index].set_head(self)

    def set_head(self, head):
        self.head = head

    def to_string(self, str_lenght):
        tmp_key = str(self.key_int)
        ksize = len(tmp_key)
        tmp = "(" + tmp_key + ":"\
            + self.val_str[0:str_lenght - ksize - 3]
        while(len(tmp) + 1 < str_lenght):
            tmp = tmp + " "
        return tmp + ")"


def test_sorted(n):
    x = BinarySearchTree()
    for y in range(n):
        x.insert(Node(y, str(y)+" node"))


def test_random(n):
    x = BinarySearchTree()
    for y in range(n):
        x.insert(Node(random.randint(0, n << 4), str(y) + " node"))


def test_to_string_and_insert():
    x = BinarySearchTree()
    for y in range(4):
        z = Node(random.randint(0, 10 << 4), str(y) + " node")
        x.insert(z)
        # print(z.to_string(8))
    # print(Node(random.randint(0,10<<4),str(0)+" node").to_string(10))
    print(x.to_string(8))
    # test_sorted(1<<31)


def get_runtime(m):
    print("get runtime")
    for n in range(m):
        x = BinarySearchTree()
        start = time.time()
        for y in range(1 << n):
            x.insert(Node(random.randint(0, n << 4), str(y) + " node"))
        end = time.time() - start
        tiefe = x.get_lenght()[0]
        x2 = BinarySearchTree()
        start2 = time.time()
        for y in range(1 << n):
            x2.insert(Node(y, str(y)+" node"))
        end2 = time.time() - start2
        tiefe2 = x2.get_lenght()[0]
        print(str(1 << n) + "| Random: " + str(tiefe) + " ; " + str(end) +
              " |Sorted: " + str(tiefe2) + " ; " + str(end2))


def test_lookup(n, m):
    print("Lookup test finding")
    x = BinarySearchTree()
    for y in range(n):
        tmp = Node(random.randint(0, n << 4), str(y) + " node")
        if(y == m):
            print(tmp.to_string(20))
            skey = tmp.key_int
        x.insert(tmp)
    print(x.lookup(skey).to_string(20))


def test_lookup2(n):
    print("Lookup test random")
    x = BinarySearchTree()
    skey = random.randint(0, n << 4)
    for y in range(n):
        tmp = Node(random.randint(0, n << 4), str(y) + " node")
        if(tmp.key_int == skey):
            print(tmp.to_string(20) + "True!")
            skey = tmp.key_int
        x.insert(tmp)
    tmp2 = x.lookup(skey)
    if(tmp2 is not None):
        print(tmp2.to_string(20))
    else:
        print("False")


def main(argv):
    test_to_string_and_insert()
    test_lookup(1 << 12, random.randint(0, 1 << 12))
    test_lookup2(1 << 12)
    get_runtime(20)


if __name__ == "__main__":
    main(sys.argv)
