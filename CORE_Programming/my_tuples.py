from typing import List
from collections import namedtuple

nameAndScore = namedtuple("nameAndScore", "name score")


def getNameAndScore(rawCsv: str) -> nameAndScore:
    parts: List[str] = rawCsv.split(",")
    name: str = parts[0]
    score: int = int(parts[1])
    return nameAndScore(name, score)


answer = getNameAndScore("Lucy,50")
print("The Name is {} with a score of {}".format(answer.name, answer.score))


# Parses a CSV such as 'Fred,10' into a tuple containing the name and the score
def getNameAndScoreAgain(rawCsv: str) -> (str, int):
    parts: List[str] = rawCsv.split(",")
    name: str = parts[0]
    score: int = int(parts[1])
    return name, score


name1, score1 = getNameAndScoreAgain("Fred,45")
print("1 - Name is {} and Score is {}".format(name1, score1))

nameScore2 = getNameAndScoreAgain("Sally,104")
print("2 - Name is {} and Score is {}".format(nameScore2[0], nameScore2[1]))


def getFloorAndMod(a: int, b: int) -> (int, int):
    return a // b, a % b


print(getFloorAndMod(77, 13))