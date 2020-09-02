from Algorithms.Sorting.bubble_sort import bubble_sort
from Algorithms.Sorting.common import primitive_compare

myList = ['Joe', 'Karl', 'Holly', 'Steve']

myListSorted = bubble_sort(myList, primitive_compare)

print('Demo for Repl.it')
print(myListSorted)