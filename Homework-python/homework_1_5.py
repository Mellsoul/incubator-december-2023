import unittest

def concatenate_strings(str1, str2):
    return str1 + str2

class TestStringConcatenationIntegration(unittest.TestCase):
    def test_concatenate_strings(self):
        # Input strings
        str1 = "Hello, "
        str2 = "World!"

        # Expected result after concatenation
        expected_result = "Hello, World!"

        # Calling the concatenate_strings function
        actual_result = concatenate_strings(str1, str2)

        # Asserting that the actual result matches the expected result
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()