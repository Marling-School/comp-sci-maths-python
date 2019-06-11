from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Set, List

T = TypeVar('T', str, int, float)


class Graph(Generic[T], ABC):
    """
    Interface for a graph, edges can be added, and then the set of related vertices can be queried
    """
    @abstractmethod
    def add_edge(self, from_v: T, to_v: T) -> None:
        pass

    @abstractmethod
    def get_related(self, from_v: T) -> Set[T] or None:
        pass

    @abstractmethod
    def breadth_first_search(self, start_vertex: T) -> List[T]:
        pass

    @abstractmethod
    def depth_first_search(self, start_vertex: T) -> List[T]:
        pass
