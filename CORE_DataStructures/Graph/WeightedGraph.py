from typing import Set, Dict, List, Callable, Tuple, TypeVar, Generic
from functools import reduce

T = TypeVar('T', str, int)


class WeightedGraph(Generic[T]):

    __data: Dict[T, Set[Tuple[T, int]]]

    def __init__(self):
        self.__data = {}

    def __repr__(self):
        return "{}".format(self.__data)

    def __ensure_key_exists(self, vertex: T):
        if vertex not in self.__data:
            self.__data[vertex] = set()

    def add_relationship(self, from_v: T, to_v: T, weight: int):
        self.__ensure_key_exists(from_v)
        self.__ensure_key_exists(to_v)

        self.__data[from_v].add((to_v, weight))

    def get_relationships(self, from_v: T):
        if from_v not in self.__data:
            raise Exception("Graph Does Not Contain {}".format(from_v))

        return self.__data[from_v]

    def generate_adjacency_matrix(self, to_index: Callable[[T], int]) -> List[List[T]]:

        pass
        return [[]]

    def print_adj_list(self):
        print("Adjacency List")
        print("Key\tRelationships")
        for key, relationships in self.__data.items():
            print("{}\t{}".format(key, relationships))
        print("-----")
