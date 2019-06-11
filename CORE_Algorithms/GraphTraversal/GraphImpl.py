from typing import TypeVar, Dict, Set, List

from CORE_Algorithms.GraphTraversal.Graph import Graph
from CORE_Algorithms.Queue.Queue import Queue
from CORE_Algorithms.Queue.QueueImpl import QueueImpl
from CORE_Algorithms.Stack.Stack import Stack
from CORE_Algorithms.Stack.StackImpl import StackImpl

T = TypeVar('T', str, int, float)


class GraphImpl(Graph[T]):
    __data: Dict[T, Set[T]]

    def __init__(self):
        self.__data = {}

    def __repr__(self):
        return "{}".format(self.__data)

    def __ensure_key_exists(self, vertex: T):
        if vertex not in self.__data:
            self.__data[vertex] = set()

    def add_edge(self, from_v: T, to_v: T) -> None:
        self.__ensure_key_exists(from_v)
        self.__ensure_key_exists(to_v)

        from_links: Set[T] = self.__data[from_v]
        from_links.add(to_v)

        to_links: Set[T] = self.__data[to_v]
        to_links.add(from_v)

    def get_related(self, from_v: T) -> Set[T]:
        return self.__data[from_v]

    def breadth_first_search(self, start_vertex: T) -> List[T]:
        pending_queue: Queue[T] = QueueImpl()
        unvisited: Set[T] = set(self.__data.keys())

        items: List[T] = []

        # Visit the starting vertex
        unvisited.remove(start_vertex)
        items.append(start_vertex)
        pending_queue.enqueue(start_vertex)

        vertex: T = start_vertex
        while True:
            # Get the related edges which are also in the unvisited set
            related: Set[T] = self.get_related(vertex).intersection(unvisited)

            # If we have related edges, add them all to the items,
            # remove them from unvisited and push them to the queue
            if len(related) > 0:
                for other in related:
                    unvisited.remove(other)
                    items.append(other)
                    pending_queue.enqueue(other)
            else:
                vertex = pending_queue.dequeue()

            if pending_queue.is_empty():
                break

        return items

    def depth_first_search(self, start_vertex: T) -> List[T]:
        pending_stack: Stack[T] = StackImpl()
        unvisited: Set[T] = set(self.__data.keys())

        items: List[T] = []

        vertex: T = start_vertex
        while True:
            # Get the related edges which are also in the unvisited set
            related: Set[T] = self.get_related(vertex)

            if vertex in unvisited:
                unvisited.remove(vertex)
                items.append(vertex)
                pending_stack.push(vertex)

            # Filter out the unvisited ones
            related = related.intersection(unvisited)

            # If we have related edges, visit one of them
            if len(related) > 0:
                vertex: T = related.pop()
            else:
                vertex = pending_stack.pop()

            if pending_stack.is_empty():
                break

        return items
