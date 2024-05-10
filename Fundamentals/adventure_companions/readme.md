# Adventure Companions

## Overview
"Adventure Companions" is a Python project designed to practice Object-Oriented Programming (OOP) and class associations. This project simulates the interactions between adventurers and their animal companions as they embark on various journeys.

## Project Structure
The project consists of three main Python scripts organized into a single folder:
- **companion.py**: Defines the `Companion` class representing animal companions with attributes and methods that manage their behaviors and states.
- **adventurer.py**: Defines the `Adventurer` class representing the human characters that adventure with their animal companions.
- **main.py**: Uses the `Adventurer` and `Companion` classes to create instances and demonstrate their interactions.

### Detailed Descriptions
#### Companion Class (`companion.py`)
The `Companion` class encapsulates details about the adventurous animals, including their name, species, skills, health, and energy. Key methods include:
- `rest()`: Increases the companion's energy.
- `snack()`: Boosts health and energy through snacking.
- `adventure()`: Simulates an adventurous activity, enhancing health.
- `sound()`: Outputs a sound representing the companion's current state.

#### Adventurer Class (`adventurer.py`)
The `Adventurer` class represents individuals who explore with their companions. It includes:
- Attributes for the adventurer's name, snacks, food, and their companion.
- `go_on_adventure()`: Depicts an adventure activity with the companion.
- `feed_companion()`: Feeds the companion, improving their stats.
- `bathe_companion()`: Invokes the companion's sound as part of their care.


## Usage Instructions

To use the Adventure Companions application, perform the following steps:

1. **Installation**:
    Ensure Python 3.8 or higher is installed on your computer.
    
2. **Repository Setup**:
    Clone the repository to your local machine.

3. **Navigate to the Project**:
    Change to the project directory.

4. **Run the Application**:
    Execute the main script to start the program: 'python main.py'

## Installation Guide

No additional installation steps are required apart from setting up Python and cloning the repository as mentioned in the usage instructions.

## Resources

- [Python Official Documentation](https://www.python.org/doc/)
- [Learn Python](https://www.learnpython.org/)
- [Real Python Tutorials](https://realpython.com/)

## License Information

Adventure Companions is open-sourced under the MIT License. 

