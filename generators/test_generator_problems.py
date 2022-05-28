import unittest
import generator_problems

class GeneratorTest(unittest.TestCase):
    def test_positive(self):
        num = 3
        lst = []
        result = generator_problems.gensquares(num)
        for x in result:
            lst.append(x)
        self.assertEqual(lst,[0,1,4])

if __name__ == "__main__":
    unittest.main()