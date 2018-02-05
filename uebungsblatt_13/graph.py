#!/usr/bin/python3

import re
from math import inf
import sys

class Graph:

    def __init__(self):
        self._num_nodes = 0
        self._num_arcs = 0
        # List for storing node objects.
        self._nodes = []
        # List of lists for storing edge objects for each node.
        # self._adjacency_lists = []
        self._arcs = []

    def read_graph_from_file(self, file_name, directed):
        """ Read in graph from .graph file.

        Specification of .graph file format:
            First line: number of nodes
            Second line: number of arcs
            3-column lines with node information:
                node_id latitude longitude
            4-column lines with edge information:
                tail_node_id head_node_id distance(m) max_speed(km/h)
        Comment lines (^#) are ignored

        >>> graph = Graph()
        >>> graph.read_graph_from_file('test.graph', True)
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        """
        c_lines = 0
        with open(file_name, 'rt') as f:
            for line in f:
                cols = line.strip().split(' ')
                # Skip comment lines.
                if re.search('^#', cols[0]):
                    continue
                c_lines += 1
                if c_lines == 1:
                    if self._num_nodes != 0:
                        raise Exception('Graph already read in')
                    self._num_nodes = int(cols[0])
                elif c_lines == 2:
                    self._num_arcs = int(cols[0])
                elif c_lines <= self._num_nodes + 2:  # all node info lines.
                    if not len(cols) == 3:
                        raise Exception('Node info line with != 3 cols')
                    node = Node(int(cols[0]), float(cols[1]), float(cols[2]))
                    # Append node to list.
                    self._nodes.append(node)
                    # Append empty adjacency list for node.
                    # self._adjacency_lists.append([])
                else:  # all arc info lines.
                    if not len(cols) == 4:
                        raise Exception('Arc info line with != 4 cols')
                    tail_node_id = int(cols[0])
                    head_node_id = int(cols[1])
                    arc = Arc(tail_node_id, head_node_id, float(cols[2]),
                              int(cols[3]))

                    if int(cols[3]) == 0:
                        print(tail_node_id)

                    self._arcs.append(arc)

                    # Append arc to tail node's adjacency list.
                    self._nodes[tail_node_id].arc_ids.append(len(self._arcs)-1)

                    if not directed:  # Create undirected graph
                        a_arc = Arc(head_node_id,
                                    tail_node_id, float(cols[2]), int(cols[3]))
                        self._arcs.append(a_arc)
                        self._nodes[head_node_id].arc_ids.\
                            append(len(self._arcs)-1)
        f.closed

    def get_num_nodes(self):
        """Return number of nodes in graph."""
        return self._num_nodes

    def get_num_arcs(self):
        """Return number of arcs in graph."""
        return self._num_arcs

    def set_arc_costs_to_travel_time(self, max_vehicle_speed):
        """Set arc costs to travel time in whole seconds.

        >>> graph = Graph()
        >>> graph.read_graph_from_file('test.graph', True)
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        >>> graph.set_arc_costs_to_travel_time(100)
        >>> graph
        [0->1(4), 0->2(8), 1->2(2), 2->3(6), 3->1(5), 4->3(2)]
        """
        for arc in self._arcs:
            # Compute max possible speed for this arc.
            max_speed = min(arc.max_speed, int(max_vehicle_speed))
            if(max_speed == 0):
                max_speed = 1
                print("map error")
            # Compute travel time in whole seconds.
            travel_time_sec = '%.0f' % (arc.distance / (max_speed / 3.6))
            # Set costs to travel time in whole seconds.
            arc.costs = int(travel_time_sec)

    def set_arc_costs_to_distance(self):
        """Set arc costs to distance.

        >>> graph = Graph()
        >>> graph.read_graph_from_file('test.graph', True)
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        >>> graph.set_arc_costs_to_travel_time(100)
        >>> graph.set_arc_costs_to_distance()
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        """
        for arc in self._arcs:
            arc.costs = arc.distance

    def compute_lcc(self):
        """Mark all nodes in the largest connected component.
        """
        tmp = self._nodes[:]
        cc_list = []
        cc_cnt = []
        for x in range(len(tmp)):
            if(tmp[x] is not None):
                tmp2 = [tmp[x]]
                cc_list.append([tmp[x]])
                cc_cnt.append(1)
                tmp[x] = None
                while(len(tmp2)>0):  # endlosschleife bis es keine anhängenden knoten mehr gibt
                    tmp3 = []
                    for tmp2_node in tmp2:
                        for tmp4 in tmp2_node.arc_ids:
                            tmp_node_id = self._arcs[tmp4].head_node_id
                            if(tmp[tmp_node_id] is not None):
                                tmp3.append(tmp[tmp_node_id])
                                cc_list[len(cc_list)-1].append(tmp[tmp_node_id])
                                cc_cnt[len(cc_list)-1] += 1
                                tmp[tmp_node_id] = None
                    tmp2 = tmp3
        tmp_cc_max_cnt = 0
        tmp_cc_max_cnt_index = 0
        for x in range(len(cc_cnt)):
            if(tmp_cc_max_cnt < cc_cnt[x]):
                tmp_cc_max_cnt_index = x
        for x in cc_list[tmp_cc_max_cnt_index]:
            x.set_lcc()

    def compute_shortest_paths(self, start_node_id):
        """Compute the shortest paths for a given start node.

        Compute the shortest paths from the given start node
        using Dijkstra's algorithm.
        """
        active_nodes = [start_node_id]
        self._nodes[start_node_id]._costs = 0
        costs = 0
        while(costs != inf):
            tmp_costs = inf
            for tmp0 in range(len(active_nodes)):
                if(tmp_costs > self._nodes[active_nodes[tmp0]]._costs):
                    tmp_costs = self._nodes[active_nodes[tmp0]]._costs
                    tmp_nxnode = tmp0
            costs = tmp_costs
            if(tmp_costs == inf):
                break
            else:
                tmp_nxnode = active_nodes.pop(tmp_nxnode)
            for tmp1 in self._nodes[tmp_nxnode].arc_ids:
                tmp2 = self._arcs[tmp1].head_node_id
                if(self._nodes[tmp2]._costs == inf):
                    active_nodes.append(tmp2)
                    tmp_costs = costs + self._arcs[tmp1].costs
                    self._nodes[tmp2].set_prenode(tmp_nxnode, tmp_costs)
                else:
                    for tmp3 in active_nodes:
                        if(tmp3 == tmp2):
                            if(self._nodes[tmp_nxnode]._costs +
                                    self._arcs[tmp1].costs <
                                    self._nodes[tmp2]._costs):
                                self._nodes[tmp2].set_prenode(
                                    start_node_id, self._arcs[tmp1].costs)
                            break

    def export_map_route(self, end_node_id, color, label):
        prenode_id = end_node_id
        tmp_str = "(" + color + "|" + label + ")"
        while(prenode_id is not None):
            tmp_str = self._nodes[prenode_id].str_map() + " " + tmp_str
            prenode_id = self._nodes[prenode_id]._prenode
        return tmp_str

    def export_routes(self, routes):
        tmp_str = "[map]\n"
        for route in routes:
            tmp_str += "\t" + route + "\n"
        return tmp_str + "\n[/map]"

    def __repr__(self):
        """ Define object's string representation.

        >>> graph = Graph()
        >>> graph.read_graph_from_file('test.graph', True)
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        """
        obj_str_repr = ''
        for arc in self._arcs:
            obj_str_repr += repr(arc) + ', '
        if obj_str_repr:
            return '[' + obj_str_repr[:-2] + ']'
        else:
            return '[]'


class Node:

    def __init__(self, node_id, latitude, longitude):
        self._id = node_id
        self._latitude = latitude
        self._longitude = longitude
        self.arc_ids = []
        self._prenode = None
        self._costs = inf
        self._lcc = False

    def __repr__(self):
        """Define object's string representation."""
        return '%i' % (self._id)

    def set_lcc(self):
        self._lcc = True

    def set_prenode(self, prenode, costs):
        self._prenode = prenode
        self._costs = costs

    def str_map(self):
        return str(self._latitude)+","+str(self._latitude)


class Arc:
    def __init__(self, tail_id, head_id, distance, max_speed):
        self.tail_node_id = tail_id  # ID of tail node.
        self.head_node_id = head_id  # ID of head node.
        self.distance = distance  # Distance in meter.
        self.max_speed = max_speed  # Maximum speed.
        self.costs = distance  # Set default costs to distance.

    def __repr__(self):
        """ Define object's string representation."""
        return '%i->%i(%i)' % (self.tail_node_id, self.head_node_id,
                               self.costs)

def main(argv):
    ugraph = Graph()
    ugraph.read_graph_from_file('test3.graph', False)
    print(ugraph)
    ugraph.compute_lcc()
    x = 0
    str_wege = []
    for node in ugraph._nodes:
        if(node._lcc):
            x += 1
    print(x)  # lcc göße zeigen!
    test_way = Graph()
    test_way.read_graph_from_file("test3.graph",True)
    print("freiburg eingelesen")
    test_way.set_arc_costs_to_distance()
    print("strecken berechnet")
    test_way.compute_shortest_paths(1)
    print("wege berechnet")
    str_wege.append(test_way.export_map_route(2, "green", "Kurz"))
    print("export #kurz")
    print(test_way.export_routes(str_wege))
    freiburg = Graph()
    freiburg.read_graph_from_file("freiburg.graph",True)
    print("freiburg eingelesen")
    freiburg.set_arc_costs_to_distance()
    print("strecken berechnet")
    freiburg.compute_shortest_paths(95466)
    print("wege berechnet")
    str_wege.append(freiburg.export_map_route(136096, "green", "Kurz"))
    print("export #kurz")
    for x in [[300, "black"], [130, "blue"], [50, "red"]]:
        freiburg.set_arc_costs_to_travel_time(x[0])
        print("strecken berechnet")
        freiburg.compute_shortest_paths(95466)
        print("wege berechnet")
        str_wege.append(freiburg.export_map_route(136096, x[1], str(x[0])))
        print("export #"+str(x[0]))
    print(freiburg.export_routes(str_wege))


if __name__ == "__main__":
    main(sys.argv)
