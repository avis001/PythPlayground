def factorial(num):
    factorial = 1

    while num > 0:
        factorial *= num
        num -= 1

    return factorial


def main():
    print(factorial(5))


main()
