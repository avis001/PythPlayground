def search(list, target):
    startIndex = 0
    endIndex = len(list) - 1

    return binarySearch(list, target, startIndex, endIndex)


def binarySearch(list, target, startIndex, endIndex):
    if endIndex == startIndex:
        return startIndex if list[startIndex] == target else -1

    if endIndex < startIndex:
        return -1

    len = endIndex - startIndex
    pivot = startIndex + len // 2

    if list[pivot] == target:
        return pivot

    if target > list[pivot]:
        return binarySearch(list, target, pivot + 1, endIndex)
    else:
        return binarySearch(list, target, startIndex, pivot - 1)
