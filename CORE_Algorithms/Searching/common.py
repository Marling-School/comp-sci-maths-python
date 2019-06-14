from typing import List, Callable, TypeVar, Optional
from CORE_Algorithms.Sorting.common import CompareFunction

Criteria = TypeVar('Criteria')
Searchable = TypeVar('Searchable')

# A match function compares a searchable item to a criteria
MatchFunction = Callable[[Criteria, Searchable], bool]

"""
A search function requires
* the input list
* the criteria
* a function to check the criteria against a searchable item
* a function for comparing two searchable items (required for sorting) 
"""
SearchFunction = Callable[[List[Searchable],
                           Criteria,
                           MatchFunction,
                           CompareFunction], Optional[Searchable]]

