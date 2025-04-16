import unittest
import KmpPatterMatching


class Test(unittest.TestCase):
    def testPrefixLength(self):
        testCases = [
            # Basic patterns
            ("aaaa", [0, 1, 2, 3]),
            ("abab", [0, 0, 1, 2]),
            ("abcabc", [0, 0, 0, 1, 2, 3]),
            ("aaabaaa", [0, 1, 2, 0, 1, 2, 3]),
            ("ababaca", [0, 0, 1, 2, 3, 0, 1]),
            ("aabaabaaa", [0, 1, 0, 1, 2, 3, 4, 5, 2]),
            ("aabaabaaaa", [0, 1, 0, 1, 2, 3, 4, 5, 2, 2]),
            ("abcabcabc", [0, 0, 0, 1, 2, 3, 4, 5, 6]),
            ("aabaabaabbaa", [0, 1, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2]),
            ("ababababc", [0, 0, 1, 2, 3, 4, 5, 6, 0]),
            # More complex patterns
            ("aabaaab", [0, 1, 0, 1, 2, 2, 3]),
            ("aaacaaaaac", [0, 1, 2, 0, 1, 2, 3, 3, 3, 4]),
            ("abracadabra", [0, 0, 0, 1, 0, 1, 0, 1, 2, 3, 4]),
            ("aaaaabaacd", [0, 1, 2, 3, 4, 0, 1, 2, 0, 0]),
            ("aaaabaaaa", [0, 1, 2, 3, 0, 1, 2, 3, 4]),
            ("aabaabaaab", [0, 1, 0, 1, 2, 3, 4, 5, 2, 3]),
            # Palindromes and near-palindromes
            ("radar", [0, 0, 0, 0, 1]),
            ("racecar", [0, 0, 0, 0, 0, 0, 1]),
            ("aaaabaaabaaa", [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]),
            ("abacababc", [0, 0, 1, 0, 1, 2, 3, 2, 0]),
            ("aabbaabb", [0, 1, 0, 0, 1, 2, 3, 4]),
            # Edge cases
            ("a", [0]),
            ("z", [0]),
            ("", []),
            ("abcdef", [0, 0, 0, 0, 0, 0]),
            ("xyzabc", [0, 0, 0, 0, 0, 0]),
            ("abcdabca", [0, 0, 0, 0, 1, 2, 3, 1]),
            # Repetitive patterns
            ("aaaaaa", [0, 1, 2, 3, 4, 5]),
            ("aaaaaaaaaa", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
            ("abababab", [0, 0, 1, 2, 3, 4, 5, 6]),
            ("abcabcabcabc", [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
            # Special characters and case sensitivity
            ("a$b$a$b", [0, 0, 0, 0, 1, 2, 3]),
            ("AaAaAaAa", [0, 0, 1, 2, 3, 4, 5, 6]),
            # Long patterns
            ("a" * 1000, [i for i in range(1000)]),
            ("ab" * 500, [0] + [i for i in range(999)]),
        ]

        for testCase in testCases:
            print(f"Pattern -- {testCase[0]}")
            print(f"Expected -- {testCase[1]}")
            prefixLength = KmpPatterMatching.prefixLength(testCase[0])
            self.assertEqual(prefixLength, testCase[1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
