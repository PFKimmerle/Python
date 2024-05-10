# Python script defining and using a User class with methods to manage user attributes and behaviors.

## User Class Definition
class User:
    # Initialization of the User object with attributes
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    # Method to display user information
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

    # Method to enroll the user as a rewards member
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    # Method to spend points if the user has enough
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print("Not enough points to spend.")

## Creating User Instances and Testing Class Methods

# Instance creation and testing display_info method
user1 = User("John", "Doe", "johndoe@example.com", 30)
user1.display_info()

# Testing enroll method
user1.enroll()

# Creating more instances
user2 = User("Jane", "Smith", "janesmith@example.com", 25)
user3 = User("Emily", "Jones", "emilyjones@example.com", 22)

# Spending points and handling different scenarios
user1.spend_points(50)

# Enroll second user and spend points
user2.enroll()
user2.spend_points(80)

# Try to spend points without enough balance
user3.spend_points(40)

# Display user info to confirm changes
user1.display_info()
user2.display_info()
user3.display_info()

## BONUS: Attempt to re-enroll first user and check logic
user1.enroll()
