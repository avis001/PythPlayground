# Given a unsorted list that was arrived at after rotating a sorted list n number of times. Find the number of rotations needed to get back the sorted list.
# Rotation -- moving the element at last index to index 0


# If the sorted list was rotated k times then the smallest element in the list would end up at the kth index.
# Also the elements before the smallest element in the list will be greater than it.
# Get the middle (pivot) element
# Check if the element before it greater than the pivot element.
# If so then this is the smallest element so return the index of the pivot element.
# If not then apply binary search with the same logic from startIndex to the pivot - 1. [ No need to lookup the right half of the pivot,
# because if the element to the left of the pivot is less than the pivot it means that the list from pivot - 1 is already sorted.]
# [1,2,3,4,5] - [5,1,2,3,4] - [4,5,1,2,3] - [3,4,5,1,2] - [2,3,4,5,1]
# Correction -- We do need to check both the halfs of the pivot as after rotation the elements that were rotated from the last index created a sorted list at the start of the list. So we will have 2 sorted sublist.
# Correction again -- We can do checks on both halfs that would brak the binary search funda and result in O(n) worst case. What we can do is check if the element at the pivot is greater than start index,
# Exit Conditions:
# 1. If startIndex > endIndex (which means we have looked into all the elements of the list and non match our criteria so the list wasn't rotated.)
# 2. If startIndex == endIndex == 0 (reached the first element nothing to compare before this which means no rotations.)
# Choosing between left and right half:
# if element at pivot is > the endIndex element, it means the smallest is in this half the right half.
# else if element at pivot is <  than endIndex element, this half the right half is sorted already
# if the pivot element and the last element are equal then we shrink our search space by 1.


def smallestElementIndex(list, startI, endI):
    if startI > endI:
        return 0

    if startI == endI == 0:
        return 0

    offset = endI - startI
    pivot = startI + offset // 2

    # wat if pivot is 0, we might end up with list[-1] which is index outta bound error? But in python -1 would take the last element of the list. And hence would work here. But as a good practice it's better to handle pivot 0.

    if pivot > 0 and list[pivot] < list[pivot - 1]:
        return pivot

    if list[pivot] > list[endI]:
        return smallestElementIndex(list, pivot + 1, endI)
    elif list[pivot] < list[endI]:
        return smallestElementIndex(list, startI, pivot - 1)
    elif list[pivot] == list[endI]:
        return smallestElementIndex(list, startI, endI - 1)


def rotations(list):
    return smallestElementIndex(list, 0, len(list) - 1)
