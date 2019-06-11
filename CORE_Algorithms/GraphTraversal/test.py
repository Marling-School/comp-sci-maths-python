import unittest
from typing import Set
from CORE_Algorithms.GraphTraversal.Graph import Graph
from CORE_Algorithms.GraphTraversal.GraphImpl import GraphImpl


class TestStringMethods(unittest.TestCase):
    my_graph: Graph[str]

    def setUp(self) -> None:
        self.my_graph: Graph[str] = GraphImpl()
        self.my_graph.add_edge('S', 'A')
        self.my_graph.add_edge('S', 'B')
        self.my_graph.add_edge('S', 'C')
        self.my_graph.add_edge('A', 'D')
        self.my_graph.add_edge('D', 'G')
        self.my_graph.add_edge('B', 'E')
        self.my_graph.add_edge('E', 'G')
        self.my_graph.add_edge('C', 'F')
        self.my_graph.add_edge('F', 'G')

    def test_graph(self):
        print("My Graph: {}".format(self.my_graph))
        s_edges: Set[str] = self.my_graph.get_related('S')
        self.assertTrue('A' in s_edges)
        self.assertTrue('B' in s_edges)
        self.assertFalse('D' in s_edges)

        g_edges: Set[str] = self.my_graph.get_related('G')
        self.assertTrue('D' in g_edges)
        self.assertTrue('F' in g_edges)
        self.assertFalse('B' in g_edges)

    def test_dfs(self):
        print("Depth First Search on {}".format(self.my_graph))
        for v in self.my_graph.depth_first_search('S'):
            print(v, end=", ")
        print("")

    def test_bfs(self):
        print("Breadth First Search on {}".format(self.my_graph))
        for v in self.my_graph.breadth_first_search('S'):
            print(v, end=", ")
        print("")
