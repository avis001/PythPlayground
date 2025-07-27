def findLeft(list, target, startIndex, endIndex, targetIndex=-1):
    if startIndex > endIndex:
        return targetIndex

    if startIndex == endIndex:
        return startIndex if list[startIndex] == target else targetIndex

    offset = endIndex - startIndex
    pivot = startIndex + offset // 2

    print(
        f"L -- startI - {startIndex} endI - {endIndex} pivot - {pivot} targetI - {target}"
    )

    if list[pivot] == target:
        targetIndex = pivot

    if list[pivot] < target:
        return findRight(list, target, pivot + 1, endIndex, targetIndex)

    return findLeft(list, target, startIndex, pivot - 1, targetIndex)


def findRight(list, target, startIndex, endIndex, targetIndex=-1):
    if startIndex > endIndex:
        return targetIndex

    if startIndex == targetIndex:
        return startIndex if list[startIndex] else targetIndex

    offset = endIndex - startIndex
    pivot = startIndex + offset // 2

    print(
        f"R-- startI - {startIndex} endI - {endIndex} pivot - {pivot} targetI - {target}"
    )

    if list[pivot] == target:
        targetIndex = pivot

    if list[pivot] > target:
        return findRight(list, target, startIndex, pivot - 1, targetIndex)

    return findRight(list, target, pivot + 1, endIndex, targetIndex)


def binarySearch(list, target, startI, endI):
    if startI > endI:
        return -1

    if startI == endI:
        return startI if list[startI] == target else -1

    offset = endI - startI
    pivot = startI + offset // 2

    if list[pivot] == target:
        return pivot

    if list[pivot] > target:
        return binarySearch(list, target, startI, pivot - 1)
    else:
        return binarySearch(list, target, pivot + 1, endI)


def findSeries(list, target):
    firstIndex = binarySearch(list, target, 0, len(list) - 1)

    if firstIndex == -1:
        return (-1, -1)

    print(f"firstI -- {firstIndex}")

    lIndex = findLeft(list, target, 0, firstIndex - 1)

    lIndex = lIndex if lIndex > -1 else firstIndex

    rIndex = findRight(list, target, firstIndex + 1, len(list) - 1)

    rIndex = rIndex if rIndex > -1 else firstIndex

    return (lIndex, rIndex)
