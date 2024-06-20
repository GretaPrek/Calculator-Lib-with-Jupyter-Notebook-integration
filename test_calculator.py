import unittest
import math
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_initial_memory(self):
        """
        Tests that the memory_reset method sets the memory to 0.
        """
        self.assertEqual(self.calc.memory, 0)

    def test_add_positive(self):
        """
        Tests that add method can add positive number.
        """
        initial_memory = 5
        number_to_add = 3
        expected_result = initial_memory + number_to_add

        self.calc.memory = initial_memory
        self.calc.add(number_to_add)
        result = self.calc.memory
        self.assertEqual(result, expected_result)

    def test_add_zero(self):
        """
        Tests that add method can add zero.
        """
        initial_memory = 5
        number_to_add = 0
        expected_result = initial_memory + number_to_add

        self.calc.memory = initial_memory
        self.calc.add(number_to_add)
        result = self.calc.memory
        self.assertEqual(result, expected_result)

    def test_add_negative(self):
        """
        Tests that add method can add negative number.
        """
        initial_memory = 0
        number_to_add = -5
        expected_result = initial_memory + number_to_add

        self.calc.memory = initial_memory
        self.calc.add(number_to_add)
        result = self.calc.memory
        self.assertEqual(result, expected_result)

    def test_substract_positive(self):
        """
        Tests that substract method can substract positive number.
        """
        initial_memory = 10
        number_to_test = 3
        expected_result = initial_memory - number_to_test

        self.calc.memory = initial_memory
        self.calc.substract(number_to_test)
        result = self.calc.memory
        self.assertEqual(result, expected_result)

    def test_substract_from_zero(self):
        """
        Tests that substract method can substract positive number from zero.
        """
        number_to_test = 10
        expected_result = - number_to_test

        self.calc.substract(number_to_test)
        result = self.calc.memory
        self.assertEqual(result, expected_result)

    def test_substract_negative_from_zero(self):
        """
        Tests that substract method can substract negative number from zero.
        """
        number_to_test = -7
        expected_result = - number_to_test

        self.calc.substract(number_to_test)
        result = self.calc.memory
        self.assertEqual(result, expected_result)

    def test_multiply_by_zero(self):
        """
        Tests that multiply method can multiply positive number from zero.
        """
        initial_memory = 2
        number_to_test = 0
        expected_result = initial_memory * number_to_test

        self.calc.multiply(number_to_test)
        result = self.calc.memory
        self.assertEqual(result, expected_result)
    def test_multiply_by_one(self):
        """
        Tests that multiply method can multiply positive number from one.
        """
        initial_memory = 2
        number_to_test = 1
        expected_result = initial_memory * number_to_test

        self.calc.memory = initial_memory
        self.calc.multiply(number_to_test)
        result = self.calc.memory
        self.assertEqual(result, expected_result)
    def test_multiply_by_negative_number(self):
        """
        Tests that multiply method can multiply positive number and negative number.
        """
        initial_memory = 2
        number_to_test = -3
        expected_result = initial_memory * number_to_test

        self.calc.memory = initial_memory
        self.calc.multiply(number_to_test)
        result = self.calc.memory
        self.assertEqual(result, expected_result)


    def test_divide_by_zero(self):
        """
        Tests that divide method can catch and ZeroDivisionError if dividing positive number from zero.
        """
        initial_memory = 16
        number_to_test = 0

        self.calc.memory = initial_memory

        # Catch the expected exception
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(number_to_test)


    def test_divide_by_one(self):
        """
        Tests that divide method can divide positive number from one.
        """
        initial_memory = 2
        number_to_test = 1
        expected_result = initial_memory / number_to_test

        self.calc.memory = initial_memory

        self.calc.divide(number_to_test)
        result = self.calc.memory
        self.assertEqual(result, expected_result)

    def test_take_n_root_by_square(self):
        """
        Tests that take (n) root method can take root with postive n(root).
        """
        initial_memory = 3
        number_to_test = 2
        expected_result = math.pow(initial_memory, 1 / number_to_test)

        self.calc.memory = initial_memory

        self.calc.take_n_root(number_to_test)
        result = self.calc.memory
        self.assertEqual(result, expected_result)
    def test_take_n_root_negative_base_even_root(self):
        """
        Tests that take (n) root method can catch ValueError for negative base.
        """
        initial_memory = -2
        number_to_test = 2

        self.calc.memory = initial_memory
        # Catch the ValueError exception and pass or give a message
        try:
            self.calc.take_n_root(number_to_test)
        except ValueError:
            pass
        else:
            self.fail("Negative base and even root did not raise expected ValueError")



    def test_memory_reset(self):
        """
        Tests that the memory_reset method sets the memory to 0.
        """

        initial_memory = 10
        self.calc.memory = initial_memory

        self.calc.memory_reset()

        self.assertEqual(self.calc.memory, 0)



    def tearDown(self):
        pass  # Optional cleanup if needed

if __name__ == "__main__":
    unittest.main()
