import unittest
from CORE_DataStructures.LinkedList.LinkedList import LinkedList


class TestStringMethods(unittest.TestCase):

    def test_linked_list(self):
        my_list = LinkedList[str]()
        my_list.insert_at_start('Joe')  # Joe
        my_list.insert_after_match('Kate', lambda x: x == 'Joe')  # Joe, Kate
        my_list.insert_after_match('Indigo', lambda x: x == 'Joe')  # Joe, Indigo, Kate
        my_list.insert_before_match('Tom', lambda x: x == 'Indigo')  # Joe, Tom, Indigo, Kate
        my_list.insert_at_end('Kirsten')  # Joe, Tom, Indigo, Kate, Kirsten

        at0: str = my_list.get_at_index(0)
        at1: str = my_list.get_at_index(1)
        at2: str = my_list.get_at_index(2)
        at3: str = my_list.get_at_index(3)
        at4: str = my_list.get_at_index(4)
        self.assertEqual(at0, 'Joe')
        self.assertEqual(at1, 'Tom')
        self.assertEqual(at2, 'Indigo')
        self.assertEqual(at3, 'Kate')
        self.assertEqual(at4, 'Kirsten')
        print("Tested Linked List {}".format(my_list))

        print("Iterating Items")
        for x in my_list.items():
            print(x)


if __name__ == '__main__':
    unittest.main()
