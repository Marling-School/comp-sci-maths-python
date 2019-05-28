import unittest
from CORE_DataStructures.PriorityQueue.PriorityQueue import PriorityQueue


class TestStringMethods(unittest.TestCase):

    def test_priority_queue(self):
        my_queue: PriorityQueue[str] = PriorityQueue(5)
        my_queue.enqueue('Joe', 4)
        my_queue.enqueue('Kate', 3)
        my_queue.enqueue('Indigo', 5)
        a = my_queue.dequeue()
        my_queue.enqueue('Tom', 7)
        my_queue.enqueue('Kirsten', 3)
        b = my_queue.dequeue()
        my_queue.enqueue('Nina', 2)
        c = my_queue.dequeue()
        my_queue.enqueue('Gaz', 4)
        d = my_queue.dequeue()
        my_queue.enqueue('Steve', 9)
        e = my_queue.dequeue()
        my_queue.enqueue('Louise', 2)
        my_queue.enqueue('Chris', 7)
        f = my_queue.dequeue()
        g = my_queue.dequeue()
        h = my_queue.dequeue()

        self.assertEqual(a, ('Kate', 3))
        self.assertEqual(b, ('Kirsten', 3))
        self.assertEqual(c, ('Nina', 2))
        self.assertEqual(d, ('Joe', 4))
        self.assertEqual(e, ('Gaz', 4))
        self.assertEqual(f, ('Louise', 2))
        self.assertEqual(g, ('Indigo', 5))
        self.assertEqual(h, ('Tom', 7))
        print("Tested Priority Queue {}".format(my_queue))


if __name__ == '__main__':
    unittest.main()
