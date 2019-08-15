from unittest import TestCase
from CORE_SystematicApproach.decomposition.stickers import harvest_duplicates


class MyTest(TestCase):

    def test_harvest_duplicates(self):
        my_collection = ['red', 'green', 'red', 'red', 'blue', 'violet', 'blue']
        deduped, swaps = harvest_duplicates(my_collection)
        dedup_set = set(deduped)
        print(f'Deduped {deduped}, Swaps: {swaps}')
        self.assertEqual({'red', 'green', 'blue', 'violet'}, dedup_set)
        self.assertEqual(2, swaps.count('red'))
        self.assertEqual(1, swaps.count('blue'))

    def test_harvest_needs(self):
        pass

    def test_assign_duplicates(self):
        pass

    def test_distribute(self):
        pass

    def test_swap(self):
        pass