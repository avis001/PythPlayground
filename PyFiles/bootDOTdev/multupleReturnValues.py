def become_warrior(first_name, last_name, power):
    return f"{first_name} {last_name} the warrior", power


# Don't edit below this line


def main():
    test("Frodo", "Baggins", 5)
    test("Bilbo", "Baggins", 10)
    test("Gandalf", "The Grey", 9000)


def test(input1, input2, input3):
    result1, result2 = become_warrior(input1, input2, input3)
    print(result1, "has a power level of:", result2)


main()
