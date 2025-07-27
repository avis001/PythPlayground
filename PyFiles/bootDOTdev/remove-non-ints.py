def remove_nonints(nums):
    result = []

    for each in nums:
        match each:
            case bool():
                continue
            case int():
                result.append(each)
            case _:
                continue

    return result


def main():
    print(remove_nonints([1, "3", 2, "asadsad", True]))


main()
