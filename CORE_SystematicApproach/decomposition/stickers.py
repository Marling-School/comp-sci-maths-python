from typing import Tuple, List, Set


def harvest_duplicates(collection: List[str]) -> Tuple[List[str], List[str]]:
    """
    Given a collection of stickers, it splits the collection into
    those stickers which are unique, and those which are duplicates
    :param collection: The input collection
    :return: A tuple containing the collection with duplicates removed, and the duplicates
    """
    dedup_collection: List[str] = []
    swaps: List[str] = []

    for sticker in collection:
        if sticker not in dedup_collection:
            dedup_collection.append(sticker)
        else:
            swaps.append(sticker)

    return dedup_collection, swaps
