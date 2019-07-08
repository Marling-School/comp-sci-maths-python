from typing import List, Tuple

# This code is more declarative
PersonWithAge = Tuple[str, int]
people: List[PersonWithAge] = [('joe', 36),
                               ('kate', 36),
                               ('tom', 5),
                               ('indigo', 1),
                               ('paul', 50),
                               ('vicki', 25),
                               ('nina', 43)]
min_age: int = 30

results: List[PersonWithAge] = []
for p in people:
    if p[1] > min_age:
        results.append(p)

print("People found over age {}: {}".format(min_age, results))

