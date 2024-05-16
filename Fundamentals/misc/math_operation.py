import unittest

class MathOperations:
    def __init__(self):
        self.result = 0
    
    def add(self, *args):
        self.result += sum(args)
        return self
    
    def subtract(self, *args):
        self.result -= sum(args)
        return self
    
    def reset(self):
        self.result = 0
        return self

class TestMathOperations(unittest.TestCase):
    def setUp(self):
        # Setup runs before each test method
        self.mo = MathOperations()

    def test_add(self):
        # Test that adding single values works
        self.assertEqual(self.mo.add(1).result, 1)
        # Reset and test adding multiple values
        self.mo.reset()
        self.assertEqual(self.mo.add(1, 2, 3).result, 6)

    def test_subtract(self):
        # Test that subtracting single values works
        self.assertEqual(self.mo.add(10).subtract(1).result, 9)
        # Reset and test subtracting multiple values
        self.mo.reset()
        self.assertEqual(self.mo.add(10).subtract(1, 2, 3).result, 4)

    def test_chaining(self):
        # Test chaining of add and subtract methods
        self.assertEqual(self.mo.add(1, 2).add(3, 4).subtract(2).add(1).subtract(1, 1).result, 7)
        
    def test_reset(self):
        # Test the reset functionality
        self.mo.add(5).subtract(3)
        self.assertNotEqual(self.mo.result, 0)
        self.mo.reset()
        self.assertEqual(self.mo.result, 0)

if __name__ == '__main__':
    unittest.main()
