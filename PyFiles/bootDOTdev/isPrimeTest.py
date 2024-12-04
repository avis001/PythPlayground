import unittest
import isPrime


class Test(unittest.TestCase):
    def testIsPrimeForPrimeNumbers(self):
        self.assertTrue(isPrime.is_prime(2))
        self.assertTrue(isPrime.is_prime(3))
        self.assertTrue(isPrime.is_prime(5))
        self.assertTrue(isPrime.is_prime(7))
        self.assertTrue(isPrime.is_prime(6113))

    def testIsPrimeForNonPrimeNumbers(self):
        self.assertFalse(isPrime.is_prime(0))
        self.assertFalse(isPrime.is_prime(1))
        self.assertFalse(isPrime.is_prime(4))
        self.assertFalse(isPrime.is_prime(12))
        self.assertFalse(isPrime.is_prime(6112))
        self.assertFalse(isPrime.is_prime(-55))


if __name__ == "__main__":
    unittest.main(verbosity=2)
