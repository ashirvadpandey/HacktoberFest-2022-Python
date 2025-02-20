import unittest
import utility
from solution import solution

class Test(unittest.TestCase):
    """Calculator Tests"""
    def test_calculator_test_a(self):
        """Normal Test 1"""
        self.assertEqual(solution(1, 1, "+"), 2, "Test 1 Failed")

    def test_calculator_test_b(self):
        """Normal Test 2"""
        self.assertEqual(solution(1, 1, "-"), 0, "Test 2 Failed")

    def test_calculator_test_c(self):
        """Normal Test 3"""
        self.assertEqual(solution(1, 1, "*"), 1, "Test 3 Failed")

    def test_calculator_test_d(self):
        """Normal Test 4"""
        self.assertEqual(solution(1, 1, "/"), 1.0, "Test 4 Failed")

    def test_calculator_test_e(self):
        """Exception Test 1"""
        self.assertEqual(solution(1, 0, "/"), -1, "Test 5 Failed")

    def test_calculator_test_f(self):
        """Exception Test 2"""
        self.assertEqual(solution("a", "b", "+"), -1, "Test 6 Failed")

    def test_calculator_test_g(self):
        """Exception Test 3"""
        self.assertEqual(solution(1, 1, "a"), -1, "Test 7 Failed")

    def test_calculator_test_h(self):
        """Exception Test 4"""
        self.assertEqual(solution(1, 1), -1, "Test 8 Failed")

if __name__ == "__main__":
    utility.main()
