def is_prime(number):
    if number < 2:
        return False

    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False

    return isPrime
