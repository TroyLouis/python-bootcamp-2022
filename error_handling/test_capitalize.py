import unittest
import capitalize

class TestCapitalize(unittest.TestCase):

    def test_one_word(self):
        text = "python"
        result = capitalize.capitalize_text(text)
        self.assertEqual(result,'Python')

    def test_sentence(self):
        text = "hello would you like to go to the park?"
        result = capitalize.capitalize_text(text)
        self.assertEqual(result,'Hello would you like to go to the park?')

if __name__ == "__main__":
    unittest.main()
