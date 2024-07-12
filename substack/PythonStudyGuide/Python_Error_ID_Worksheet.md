# Python Error Identification Worksheet

### Instructions
Identify the errors and correct them.

### Questions
#### 1.
```python
def greet(name):
if name:
print(f"Hello, {name}!")
else:
print("Hello, world!")
```

#### 2.
```python
for i in range(5)
    print(i)
```

#### 3.
```python
fruits = ["apple", "banana", "cherry"]
print(fruits.lenght())
```

#### 4.
```python
def add_numbers(a, b):
    return a - b

result = add_numbers(5, 3)
print(result)
```

#### 5.
```python
person = {"name": "Alice", "age": "twenty-five"}
print("Name: " + person["name"] + ", Age: " + person["age"])
```

#### 6.
```python
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] *
print(numbers)
```

#### 7.
```python
def calculate_area(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area

print(calculate_area("5"))
```

#### 8.
```python
def find_max(numbers):
    max_num = float('-inf')
    for num in numbers:
        if num > max:
            max_num = num
    return max_num

print(find_max([1, 2, 3, 4, 5]))
```

#### 9.
```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError
        return "Division by zero is not allowed"

print(divide(10, 0))
```

#### 10.
```python
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

print(read_file("non_existent_file.txt"))
```