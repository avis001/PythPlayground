def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u"}
    vowelsCount = 0
    vowelsPresent = set()
    for char in text:
        if char.casefold() in vowels:
            vowelsCount += 1
            vowelsPresent.add(char)

    return vowelsCount, vowelsPresent


def main():
    i = "Am a little Star. You are my only star."
    a, b = count_vowels(i)
    print(i)
    print(a)
    print(b)


main()
