# modularizing/parent.py
local_val = "magical unicorns"

def square(x):
    return x * x

class User:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return "hello"

if __name__ == "__main__":
    print(square(5))  # Example function call
    user = User("Anna")  # Example instantiation of the User class
    print(user.name)  # Accessing attribute
    print(user.say_hello())  # Method call
    print(__name__)  # This will print '__main__' when executed directly
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
