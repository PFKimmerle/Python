# Python script demonstrating basic functions and common pitfalls in function execution.

## 1. Function that returns a fixed value
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# Output: 5

## 2. Attempt to call an undefined function
# This will raise a NameError because the function is not defined before calling.
def number_of_military_branches():
    return 5
# Uncomment the line below to see the NameError
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

## 3. Function with unreachable return statement
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# Output: 5

## 4. Another function with unreachable code after return
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# Output: 5

## 5. Function that prints but does not return a value
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# Output: 5 and None

## 6. Adding results of functions that do not return values
def add(b,c):
    print(b+c)
# This will raise a TypeError because the add function prints but does not return a value
# Uncomment the line below to see the TypeError
# print(add(1,2) + add(2,3))

## 7. Function that concatenates string representations of integers
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# Output: 25

## 8. Function with multiple return paths and print statement
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
print(number_of_oceans_or_fingers_or_continents())
# Output: 100 and 10

## 9. Function with conditional returns and testing with different parameters
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b < c:
        return 7
    else:
        return 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Output: 7, 14, and 21

## 10. Function with a single effective return statement
def addition(b, c):
    return b + c
    return 10
print(addition(3,5))
# Output: 8

## 11. Exploring variable scope and printing before and after function calls
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# Output: 500, 500, 300, 500

## 12. Similar to above, with function return but no assignment
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# Output: 500, 500, 300, 500

## 13. Function modifies global variable through assignment after function call
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b = foobar()
print(b)
# Output: 500, 500, 300, 300

## 14. Sequence of function calls within another function
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# Output: 1, 3, 2

## 15. Function calls with return values influencing outer scope
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# Output: 1, 3, 5, 10
