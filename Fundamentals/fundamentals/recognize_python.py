num1 = 42 # variable declaration
num2 = 2.3 # variable declaration
boolean = True # Data type primative boolean
string = 'Hello World' # Data type primative string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Data type list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Data type dictionary
fruit = ('blueberry', 'strawberry', 'banana') # Data type tuple
print(type(fruit)) # Data type tuple
print(pizza_toppings[1]) # Data type list
pizza_toppings.append('Mushrooms') # Data type list
print(person['name']) # Data type dictionary
person['name'] = 'George' # Data type dictionary
person['eye_color'] = 'blue' # Data type diciionary
print(fruit[2]) # Data type tuple

if num1 > 45: # conditional statement
    print("It's greater") # print statment
else: # conditional satatment
    print("It's lower") # print statement

if len(string) < 5: # conditional statement
    print("It's a short word!")
elif len(string) > 15: # conditional statement
    print("It's a long word!")
else: # conditional statement
    print("Just right!")

for x in range(5): # for loop
    print(x) # print statement
for x in range(2,5): # for loop
    print(x) # print statement
for x in range(2,10,3): # for loop
    print(x) # print statement
x = 0 # variable declaration
while(x < 5): # while loop
    print(x) # print statment
    x += 1 # increment

pizza_toppings.pop() # Data type list
pizza_toppings.pop(1)  # Data type list
print(person) # Data type dictionary
person.pop('eye_color') # Data type dictionary
print(person) # print statment

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # conditional statement
        continue  # continue statement
    print('After 1st if statement') # print statment
    if topping == 'Olives': # conditional statment
        break # break statement

def print_hello_ten_times(): # fuction
    for num in range(10): # for loop
        print('Hello') # print statemnt

print_hello_ten_times() # fucntion call

def print_hello_x_times(x): # function
    for num in range(x): # for loop
        print('Hello') # print statment

print_hello_x_times(4) # function call

def print_hello_x_or_ten_times(x = 10): # function
    for num in range(x): # for loop
        print('Hello') # print statment

print_hello_x_or_ten_times() # fucntion call
print_hello_x_or_ten_times(4) # function call


""" # define multi-line string literals, docstrings are used in python to document code
Bonus section 
"""

# print(num3)  ## This line is commented out. If it were active, it would print the value of the variable num3, but as it's commented, it does nothing.

# num3 = 72  ## This is another commented line. If executed, it would assign the value 72 to the variable num3.

# fruit[0] = 'cranberry'    ## This line, also commented, would set the first element of the list fruit to the string 'cranberry'.
                            ## However, for this to work, the list fruit must already exist and contain at least one element.

# print(person['favorite_team'])  ## This commented line would print the value associated with the key 'favorite_team' from the dictionary person.

# print(pizza_toppings[7])  ## This line woudl print the 8th element of the list pizza_toppings. However, since there are only 5 element in the list, it would cause an error.
                            ## pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Data type list

#   print(boolean)  ## This line is commented out. If it were active, it would print the value of the variable boolean. 
                    ## However, there is an indentation error, as the print statement is indented with two spaced intead of four.

# fruit.append('raspberry') ## This line is commented out. If it were active, it would append the string 'raspberry' to the list fruits.
                            ## 

# fruit.pop(1) ## This line is commented out. If it were active, it would remove the second element of the list fruit.