import unittest

def reverseList(lst):
    # Initialize two pointers, one at the start and one at the end of the list
    left, right = 0, len(lst) - 1
    # Continue swapping elements until the two pointers meet in the middle
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left, right = left + 1, right - 1
    return lst

def isPalindrome(word):
    # Check if the word reads the same forwards and backwards
    return word == word[::-1]

def coins(cents):
    # Define coin values in descending order
    coin_values = [25, 10, 5, 1]
    change = []
    # Calculate the number of each coin type needed starting from the highest value
    for value in coin_values:
        num_coins, cents = divmod(cents, value)
        change.append(num_coins)
    return change

def factorial(n):
    # Base case: the factorial of 0 is 1
    if n == 0:
        return 1
    else:
        # Recursive case: multiply the number by the factorial of the number minus one
        return n * factorial(n - 1)

def fibonacci(n):
    # Base cases: fib(0) is 0 and fib(1) is 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: fib(n) is the sum of the previous two Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

class TestAlgorithms(unittest.TestCase):
    # Tests for reverseList
    def test_reverseList(self):
        self.assertEqual(reverseList([1, 3, 5]), [5, 3, 1])
        self.assertEqual(reverseList([]), [])
        self.assertEqual(reverseList([7]), [7])

    # Tests for isPalindrome
    def test_isPalindrome(self):
        self.assertTrue(isPalindrome("racecar"))
        self.assertFalse(isPalindrome("hello"))
        self.assertTrue(isPalindrome("radar"))
        self.assertFalse(isPalindrome("python"))
        self.assertTrue(isPalindrome(""))

    # Tests for coins
    def test_coins(self):
        self.assertEqual(coins(87), [3, 1, 0, 2])
        self.assertEqual(coins(99), [3, 2, 0, 4])
        self.assertEqual(coins(25), [1, 0, 0, 0])
        self.assertEqual(coins(56), [2, 0, 1, 1])
        self.assertEqual(coins(7), [0, 0, 1, 2])

    # Tests for factorial
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(3), 6)

    # Tests for fibonacci
    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(0), 0)

if __name__ == '__main__':
    unittest.main()
