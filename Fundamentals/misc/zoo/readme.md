# Zoo Management System

This project implements a Zoo Management System in Python, demonstrating principles of object-oriented programming including inheritance, polymorphism, and encapsulation. The system allows for managing a zoo with various types of animals, showing how different animal behaviors can be modeled using classes.

## Features

- **Animal Classes**: Different animal types are represented using a class hierarchy where all animal types inherit from a base `Animal` class.
- **Zoo Class**: Manages collections of animals.
- **Interactive Management**: Add animals to the zoo, feed them, and display their information (runs automatically).

## Structure

- `animal.py`: Contains the base class `Animal` and derived classes such as `Lion`, `Tiger`, and `Bear`.
- `zoo.py`: Contains the `Zoo` class which manages instances of `Animal` classes.

## Usage

To run the Zoo Management System:
1. Navigate to the directory containing `zoo.py` and `animal.py`.
2. Run the script using Python by entering the following command:'python zoo.py'
This command initializes the zoo, adds various animals, and displays information about each animal.

# License

This project is released under the MIT License.
