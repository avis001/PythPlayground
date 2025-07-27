def find_min(nums):
    min = float("inf")

    for each in nums:
        if each < min:
            min = each

    return min


def main():
    print(find_min([1, 11, 111, -1, -11, -111]))


main()
