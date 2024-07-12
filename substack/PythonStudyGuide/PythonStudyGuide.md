# Python Study Guide

### Variable Declaration
- **Definition:** Assigning a value to a variable.
- **Example:**
    ```python
    x = 5
    name = "Alice"
    ```

### Log Statement
- **Definition:** Printing information to the console.
- **Example:**
    ```python
    print("Hello, World!")
    ```

### Type Check
- **Definition:** Checking the data type of a variable.
- **Example:**
    ```python
    isinstance(x, int)
    ```

### Length Check
- **Definition:** Finding the number of items in a collection.
- **Example:**
    ```python
    len(name)
    ```

### Single Line Comment
- **Definition:** Begins with a `#`.
- **Example:**
    ```python
    # This is a single-line comment
    ```

### Multiline Comment
- **Definition:** Enclosed within triple quotes.
- **Example:**
    ```python
    """
    This is a
    multiline comment
    """
    ```

### Boolean
- **Definition:** Represents `True` or `False`.
- **Example:**
    ```python
    is_active = True
    ```

### Numbers
- **Definition:** Integer or floating-point numbers.
- **Example:**
    ```python
    age = 30
    pi = 3.14
    ```

### Strings
- **Definition:** Sequence of characters.
- **Example:**
    ```python
    greeting = "Hello, World!"
    ```

### List - Initialize
- **Definition:** Ordered collection of items.
- **Example:**
    ```python
    fruits = ["apple", "banana", "cherry"]
    ```

### List - Access Value
- **Definition:** Accessing an item in a list.
- **Example:**
    ```python
    print(fruits[0])
    ```

### List - Change Value
- **Definition:** Changing an item in a list.
- **Example:**
    ```python
    fruits[1] = "blueberry"
    ```

### List - Add Value
- **Definition:** Adding an item to a list.
- **Example:**
    ```python
    fruits.append("orange")
    ```

### List - Delete Value
- **Definition:** Deleting an item from a list.
- **Example:**
    ```python
    del fruits[2]
    ```

### Tuple - Initialize
- **Definition:** Ordered, immutable collection of items.
- **Example:**
    ```python
    coordinates = (10, 20)
    ```

### Tuple - Access Value
- **Definition:** Accessing an item in a tuple.
- **Example:**
    ```python
    print(coordinates[0])
    ```

### Tuple - Change Value
- **Definition:** Not allowed in tuples.
- **Example:**
    ```python
    coordinates[0] = 15  # This will raise an error
    ```

### Tuple - Add Value
- **Definition:** Not allowed in tuples.
- **Example:**
    ```python
    coordinates.append(30)  # This will raise an error
    ```

### Tuple - Delete Value
- **Definition:** Not allowed in tuples.
- **Example:**
    ```python
    del coordinates[0]  # This will raise an error
    ```

### Dictionary - Initialize
- **Definition:** Collection of key-value pairs.
- **Example:**
    ```python
    student = {"name": "Alice", "age": 20}
    ```

### Dictionary - Access Value
- **Definition:** Accessing a value in a dictionary.
- **Example:**
    ```python
    print(student["name"])
    ```

### Dictionary - Change Value
- **Definition:** Changing a value in a dictionary.
- **Example:**
    ```python
    student["age"] = 21
    ```

### Dictionary - Add Value
- **Definition:** Adding a value to a dictionary.
- **Example:**
    ```python
    student["major"] = "CS"
    ```

### Dictionary - Delete Value
- **Definition:** Deleting a value from a dictionary.
- **Example:**
    ```python
    del student["age"]
    ```

### If Conditional
- **Definition:** If condition is met.
- **Example:**
    ```python
    if age > 18:
        print("Adult")
    ```

### Else If Conditional
- **Definition:** Else if condition is met.
- **Example:**
    ```python
    elif age == 18:
        print("Just became an adult")
    ```

### Else Conditional
- **Definition:** Else condition if no prior conditions met.
- **Example:**
    ```python
    else:
        print("Minor")
    ```

### For Loop - Start, Stop, Increment
- **Definition:** Loop with start, stop, and increment.
- **Example:**
    ```python
    for i in range(0, 5, 1):
        print(i)
    ```

### For Loop - Break
- **Definition:** Breaking out of a loop.
- **Example:**
    ```python
    for i in range(10):
        if i == 5:
            break
        print(i)
    ```

### For Loop - Continue
- **Definition:** Skipping to the next iteration in a loop.
- **Example:**
    ```python
    for i in range(10):
        if i == 5:
            continue
        print(i)
    ```

### For Loop - Sequence
- **Definition:** Looping through a sequence.
- **Example:**
    ```python
    for fruit in fruits:
        print(fruit)
    ```

### While Loop - Start, Stop, Increment
- **Definition:** Loop with start, stop, and increment.
- **Example:**
    ```python
    count = 0
    while count < 5:
        print(count)
        count += 1
    ```

### Function - Parameter
- **Definition:** Function parameter.
- **Example:**
    ```python
    def greet(name):
        print("Hello, " + name)
    ```

### Function - Argument
- **Definition:** Function argument.
- **Example:**
    ```python
    greet("Alice")
    ```

### Function - Return
- **Definition:** Returning a value from a function.
- **Example:**
    ```python
    def add(a, b):
        return a + b
    ```

### NameError
- **Definition:** Variable not defined.
- **Example:**
    ```python
    print(x)
    ```

### TypeError
- **Definition:** 'tuple' object does not support item assignment.
- **Example:**
    ```python
    coordinates[0] = 15
    ```

### KeyError
- **Definition:** Dictionary key not found.
- **Example:**
    ```python
    print(student["favorite_team"])
    ```

### IndexError
- **Definition:** List index out of range.
- **Example:**
    ```python
    print(fruits[5])
    ```

### IndentationError
- **Definition:** Unexpected indent.
- **Example:**
    ```python
    print("Hello")
        print("World")
    ```

### AttributeError: 'tuple' object has no attribute 'pop'
- **Definition:** 'tuple' object has no attribute 'pop'
- **Example:**
    ```python
    coordinates.pop()
    ```

### AttributeError: 'tuple' object has no attribute 'append'
- **Definition:** 'tuple' object has no attribute 'append'
- **Example:**
    ```python
    coordinates.append(30)
    ```

### Tuples - Change Value
- **Definition:** Not allowed in tuples.
- **Example:**
    Not allowed in tuples.
    ```python
    coordinates = (10, 20)
    coordinates[0] = 15  # This will raise a TypeError
    ```

### Tuples - Add Value
- **Definition:** Not allowed in tuples.
- **Example:**
    Not allowed in tuples.
    ```python
    coordinates = (10, 20)
    coordinates.append(30)  # This will raise an AttributeError
    ```

### Tuples - Delete Value
- **Definition:** Not allowed in tuples.
- **Example:**
    Not allowed in tuples.
    ```python
    coordinates = (10, 20)
    del coordinates[0]  # This will raise a TypeError
    ```