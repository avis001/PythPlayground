"""
- create a seen list which will hold the list of elements alread seen. Store it in a Dict { value: Key }.
- loop over the list.
- diff = sum - currentElement
- check if diff is in the seen dict.
- if yes return current index and the index from seen dict
- if no add the element to the dict and move on.
- exit condition while i < len(list)
"""


def two_sum(list, sum):
    seen = {}

    for index, element in enumerate(list):
        diff = sum - element

        if diff in seen:
            return (seen[diff], index)
        else:
            seen[element] = index

    return [-1, -1]
