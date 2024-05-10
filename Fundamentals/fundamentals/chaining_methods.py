# Python script defining and using a User class with method chaining enabled.

## User Class Definition with Method Chaining
class User:
    # Initialization of the User object with attributes
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    # Method to display user information, returns self to allow method chaining
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        return self

    # Method to enroll the user as a rewards member, returns self to allow method chaining
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return self
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    # Method to spend points if the user has enough, returns self to allow method chaining
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print("Not enough points to spend.")
        return self

## Using Chained Methods with User Instances

# Create user instances
user1 = User("John", "Doe", "johndoe@example.com", 30)
user2 = User("Jane", "Smith", "janesmith@example.com", 25)

# Chained method calls
user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()

## Notes on Method Chaining
# Method chaining works by returning the instance (self) in each method that does not inherently need to return another specific value.
# This pattern is common in many OOP languages where 'this' (similar to 'self' in Python) is used.

