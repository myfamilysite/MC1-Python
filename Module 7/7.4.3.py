import unittest


def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty.")

    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("The list must contain only numeric values.")

    total = sum(numbers)
    count = len(numbers)

    return total / count


class TestCalculateAverage(unittest.TestCase):

    def test_average_positive_numbers(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)

    def test_average_with_zero(self):
        self.assertEqual(calculate_average([0, 10, 20]), 10)

    def test_average_negative_numbers(self):
        self.assertEqual(calculate_average([-2, -4, -6]), -4)

    def test_average_float_numbers(self):
        self.assertEqual(calculate_average([1.5, 2.5, 3.5]), 2.5)

    def test_empty_list_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_non_numeric_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            calculate_average([1, 2, "three", 4])

    def test_non_numeric_none_raises_type_error(self):
        with self.assertRaises(TypeError):
            calculate_average([1, None, 3])


if __name__ == "__main__":
    unittest.main()