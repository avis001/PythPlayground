import unittest
import mountRental


class Test(unittest.TestCase):
    def testRentalOverdue(self):
        self.assertTrue(mountRental.check_mount_rental(5, 4), "overtime charged")

    def testRentalReturnedOnTime(self):
        self.assertTrue(mountRental.check_mount_rental(5, 9), "no charges yet")

    def testRentalOnTime(self):
        self.assertTrue(mountRental.check_mount_rental(5, 5), "overtime charged")


if __name__ == "__main__":
    unittest.main(verbosity=2)
