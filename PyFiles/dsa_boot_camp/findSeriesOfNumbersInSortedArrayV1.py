def findLeftMost(list, target, startI, endI, targetI=-1):
    if startI > endI:
        return targetI

    if startI == endI:
        return startI if list[startI] == target else targetI

    offset = endI - startI
    pivot = startI + offset // 2

    if list[pivot] == target:
        targetI = pivot
        return findLeftMost(list, target, startI, pivot - 1, targetI)

    if list[pivot] > target:
        return findLeftMost(list, target, startI, pivot - 1, targetI)
    else:
        return findLeftMost(list, target, pivot + 1, endI, targetI)


def findRightMost(list, target, startI, endI, targetI=-1):
    if startI > endI:
        return targetI

    if startI == endI:
        return startI if list[startI] == target else targetI

    offset = endI - startI
    pivot = startI + offset // 2

    if list[pivot] == target:
        targetI = pivot
        return findRightMost(list, target, pivot + 1, endI, targetI)

    if list[pivot] > target:
        return findRightMost(list, target, startI, pivot - 1, targetI)
    else:
        return findRightMost(list, target, pivot + 1, endI, targetI)


def findSeries(list, target):
    leftI = findLeftMost(list, target, 0, len(list) - 1)
    rightI = findRightMost(list, target, 0, len(list) - 1)

    return [leftI, rightI]
