"""
Divide and conqure

- Choose a pivot
- Apply Split On Both sides.
- Then apply sort on the results.
- The split step is iterative so we will move on to the sort only after we reach the leaves of the tree.
- exit condition is endI < startI

- Merge arrays (Sort) Logic.
- the arrays are already sorted.
- So we can in parallel compare the elements at the same index and move the smallest to the sorted array. Then increament the index of the array that we took the element out off.
- Any remaing items should be appeneded to the resultant.
"""


def mergeSort(list, startI, endI):
    if endI < startI:
        return []
    if endI == startI:
        return [list[startI]]

    offset = endI - startI
    pivot = startI + offset // 2

    print(f"BF sI - {startI} eI - {endI} pi - {pivot}")

    left = mergeSort(list, startI, pivot)
    right = mergeSort(list, pivot + 1, endI)

    print(f"sI - {startI} eI - {endI} pi - {pivot} left - {left} right - {right}")

    leftI = rightI = 0
    sortedList = []

    while leftI < len(left) and rightI < len(right):
        if left[leftI] < right[rightI]:
            sortedList.append(left[leftI])
            leftI += 1
        else:
            sortedList.append(right[rightI])
            rightI += 1

    if leftI < len(left):
        while leftI < len(left):
            sortedList.append(left[leftI])
            leftI += 1

    if rightI < len(right):
        while rightI < len(right):
            sortedList.append(right[rightI])
            rightI += 1

    print(f"sortedL left - {left} right - {right}")
    return sortedList


def sort(list):
    return mergeSort(list, 0, len(list) - 1)
