# Testing
# python's package for unit tests
import unittest

import _11_packages.my_package.utility as utility

# w/ the command 'pyhton3 -m unittest' we can run all the tests in the pwd

# main class


class TestingMain(unittest.TestCase):

    # this function will be executed before each test
    def setUp(self):
        print('anything')

    # test for utility.add function
    def test_add(self):
        ''' comment for test '''
        num1 = 1
        num2 = 4
        result = utility.add(num1, num2)
        # check the expected result
        self.assertEqual(result, 5)

    def test_add2(self):
        num1 = 1
        num2 = 'asd'
        result = utility.add(num1, num2)
        # check the expected error to be true
        self.assertIsInstance(result, ValueError)

    def test_add3(self):
        num1 = 1
        num2 = None
        result = utility.add(num1, num2)
        # check the expected error to be true
        self.assertEqual(result, 'please enter number')


# run the tests only if this file is being run
if __name__ == '__main__':
    unittest.main()
