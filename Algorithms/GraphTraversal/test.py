import unittest
import logging
from typing import Set, List
from Algorithms.GraphTraversal.Graph import Graph
from Algorithms.GraphTraversal.GraphImpl import GraphImpl


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
        logging.info("My Graph: {}".format(self.my_graph))
        s_edges: Set[str] = self.my_graph.get_related('S')
        self.assertTrue('A' in s_edges)
        self.assertTrue('B' in s_edges)
        self.assertFalse('D' in s_edges)

        g_edges: Set[str] = self.my_graph.get_related('G')
        self.assertTrue('D' in g_edges)
        self.assertTrue('F' in g_edges)
        self.assertFalse('B' in g_edges)

    def test_dfs(self):
        logging.info("Depth First Search on {}".format(self.my_graph))
        dfs: List[str] = self.my_graph.depth_first_search('S')
        for v in dfs:
            logging.info(v, end=", ")
        logging.info("")

    def test_bfs(self):
        logging.info("Breadth First Search on {}".format(self.my_graph))
        bfs: List[str] = self.my_graph.breadth_first_search('S')
        for v in bfs:
            logging.info(v, end=", ")
        logging.info("")
