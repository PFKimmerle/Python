# Python Module and Namespace Project

## Overview
This project is designed to demonstrate and educate on basic Python concepts such as modules, the `__name__` variable, and how Python manages namespaces and imports. It provides a practical example of the differences in execution context when a Python script is run directly versus being imported as a module.

## Detailed Descriptions
### parent.py
**Functionality**: Contains variable, function, and class definitions. It includes conditional execution blocks to showcase how Python differentiates between direct execution and being imported as a module.
- **Components**:
  - `greeting`: A function that prints a greeting message.
  - `DataClass`: A class that encapsulates a simple data model.
  - Execution Block: Checks if the script is the main execution context to decide whether to execute certain code blocks.

### child.py
**Functionality**: Demonstrates the effects of importing one Python file into another. It imports `parent.py` and executes its contents as a module.
- **Behavior**: On import, `parent.py`'s non-protected statements are executed, illustrating how imported modules behave.

## Usage Instructions
To get started with this project, follow these steps:

1. **Run parent.py directly**:
   - Navigate to the project directory.
   - Execute `python parent.py` in the terminal.
   - This will run the script in the `__main__` context and display outputs from the defined functions and classes.

2. **Run child.py to see import effects**:
   - Run `python child.py` in the terminal.
   - This executes `parent.py` as an imported module, showing how the script behaves differently when imported.

## Installation Guide
Follow these steps to install and run the project:

1. **Pre-requisites**:
   - Ensure Python 3.x is installed on your system.

2. **Clone the Repository**:
   - Clone this repository to your local machine using.

3. **Navigate to the Project Directory**:
   - Change directory to the cloned repository.

## Resources
- [Python Official Documentation](https://www.python.org/doc/)
- [Python Modules and Packages](https://docs.python.org/3/tutorial/modules.html)
- [Understanding the `__name__` Variable in Python](https://realpython.com/python-main-function/)

## License Information
This project is open-sourced under the MIT License. The details of this license can be found in the LICENSE file in the repository.
