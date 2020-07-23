import unittest

from src.fizz_buzz import fizz_buzz
class TestFizz_buzz(unittest.TestCase):

    def test_is_number_divisible_by_three(self):
        # fizz_buzz=FizzBuzz()
        self.assertEqual("Fizz", fizz_buzz(3))

    def test_is_number_divisible_by_five(self):
        self.assertEqual("Buzz", fizz_buzz(5))

    def test_is_number_divisible_by_three_and_five(self):
        self.assertEqual("FizzBuzz", fizz_buzz(15))

    def test_is_number_not_divisible_by_three_and_five(self):
        self.assertEqual("7", fizz_buzz(7))