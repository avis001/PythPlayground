def number_sum(n):
    sum = 0

    while n > 0:
        sum += n
        n -= 1

    return sum


def main():
    print(number_sum(5))


main()
