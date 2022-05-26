import unittest
import capitalize

class TestCapitalize(unittest.TestCase):

    def test_one_word(self):
        text = "python"
        result = capitalize.capitalize_text(text)
        self.assertEqual(result,'Python')

if __name__ == "__main__":
    unittest.main()
