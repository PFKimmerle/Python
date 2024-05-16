class Underscore:
    def map(self, iterable, callback):
        # Applies callback to every item of iterable and returns a list of results
        return [callback(item) for item in iterable]

    def find(self, iterable, callback):
        # Returns the first item in iterable for which callback returns True
        for item in iterable:
            if callback(item):
                return item
        return None  # Return None if no element matching the condition is found

    def filter(self, iterable, callback):
        # Returns a list of items for which callback returns True
        return [item for item in iterable if callback(item)]

    def reject(self, iterable, callback):
        # Returns a list of items for which callback returns False
        return [item for item in iterable if not callback(item)]

# Create an instance of our class
_ = Underscore()

# Example usage
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print("Evens:", evens)  # Output: Evens: [2, 4, 6]

# More examples
mapped = _.map([1, 2, 3], lambda x: x * 2)
print("Mapped:", mapped)  # Output: Mapped: [2, 4, 6]

first_greater_than_four = _.find([1, 2, 3, 4, 5, 6], lambda x: x > 4)
print("First greater than 4:", first_greater_than_four)  # Output: First greater than 4: 5

rejected_evens = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print("Rejected evens:", rejected_evens)  # Output: Rejected evens: [1, 3, 5]
