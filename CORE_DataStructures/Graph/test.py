import unittest
from CORE_DataStructures.Graph.WeightedGraph import WeightedGraph


class TestStringMethods(unittest.TestCase):

    def test_adj_list_graph(self):
        my_graph: WeightedGraph[str] = WeightedGraph()
        my_graph.add_relationship('J', 'K', 5)
        my_graph.add_relationship('J', 'T', 3)
        my_graph.add_relationship('T', 'I', 7)
        print("My Graph:{}".format(my_graph))
        my_graph.print_adj_list()
        my_adj_matrix = my_graph.generate_adjacency_matrix(ord)
        print("Adjacency Matrix", my_adj_matrix)
