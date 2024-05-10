# Python script to demonstrate various list and dictionary operations.

## Section 1: Update Values in Dictionaries and Lists
# Instructions: Update the values in various data structures as described below.

# List containing lists
x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15  # Update the value 10 in the second inner list to 15

# List of dictionaries for student records
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = 'Bryant'  # Change last name of the first student

# Dictionary with list values for sports directory
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'  # Update the first soccer player

# List containing a dictionary
z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30  # Update the y value from 20 to 30

## Section 2: Iterate Through a List of Dictionaries
# Instructions: Define a function to iterate through a list of dictionaries and print each key-value pair.

def iterateDictionary(some_list):
    for dictionary in some_list:
        print(f"first_name - {dictionary['first_name']}, last_name - {dictionary['last_name']}")

# Example use
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
iterateDictionary(students)

## Section 3: Get Values From a List of Dictionaries
# Instructions: Create a function that prints values from a specific key in a list of dictionaries.

def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])

# Example uses
iterateDictionary2('first_name', students)  # Output first names
iterateDictionary2('last_name', students)   # Output last names

## Section 4: Iterate Through a Dictionary with List Values
# Instructions: Define a function to print the size of each list in a dictionary, followed by its contents.

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key.upper()}")
        for item in value:
            print(item)

# Example use
bootcamp = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(bootcamp)
