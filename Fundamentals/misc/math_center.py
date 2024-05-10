class MathCenter:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num + sum(nums)
        return self

    def subtract(self, num, *nums):
        self.result -= num + sum(nums)
        return self

# create an instance:
mc = MathCenter()

# to test:
x = mc.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # should print 5

# Running each of the methods a few more times to check the result
mc.add(5).add(20, 30).subtract(10, 10)
print(mc.result)  # Extended testing of the functionality
