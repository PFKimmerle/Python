# Python script demonstrating various list operations and function definitions.

## 1. Countdown Function
# Instructions: Create a function that accepts a number and returns a list counting down from that number to zero.
def countdown(n):
    return list(range(n, -1, -1))

## 2. Print and Return Function
# Instructions: Create a function that receives a list with two numbers. It should print the first value and return the second.
def print_and_return(lst):
    print(lst[0])
    return lst[1]

## 3. First Plus Length Function
# Instructions: Create a function that accepts a list and returns the sum of the first element in the list plus the list's length.
def first_plus_length(lst):
    return lst[0] + len(lst)

## 4. Values Greater than Second Function
# Instructions: Create a function that accepts a list and creates a new list containing only the values from the original list that are greater than its second value. Print the count of these values and return the new list. If the list has less than 2 elements, return False.
def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    else:
        new_lst = [i for i in lst if i > lst[1]]
        print(len(new_lst))
        return new_lst

## 5. This Length, That Value Function
# Instructions: Write a function that accepts two integers: size (for the length of the list) and value (each element's value). The function should create and return a list of the specified size where every element is the specified value.
def length_and_value(size, value):
    return [value] * size

