# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(c):
    return c + 273.15

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(k):
    return k - 273.15

valid_scales = {"1": "Celsius", "2": "Fahrenheit", "3": "Kelvin", "C": "Celsius", "F": "Fahrenheit", "K": "Kelvin"}

while True:
    temp = float(input("Enter the temperature: "))
    scale_from = input("Convert from (1: Celsius, 2: Fahrenheit, 3: Kelvin, or C/F/K): ").strip().upper()
    scale_to = input("Convert to (1: Celsius, 2: Fahrenheit, 3: Kelvin, or C/F/K): ").strip().upper()

    if scale_from not in valid_scales or scale_to not in valid_scales:
        print("Invalid temperature scale. Please choose from 1 (Celsius), 2 (Fahrenheit), 4 (Kelvin), or C/F/K.")
    else:
        scale_from = valid_scales[scale_from]
        scale_to = valid_scales[scale_to]

        if scale_from == "Celsius" and scale_to == "Fahrenheit":
            result = celsius_to_fahrenheit(temp)
            print(f"{temp} Celsius is {round(result, 2)} Fahrenheit")
        elif scale_from == "Fahrenheit" and scale_to == "Celsius":
            result = fahrenheit_to_celsius(temp)
            print(f"{temp} Fahrenheit is {round(result, 2)} Celsius")
        elif scale_from == "Celsius" and scale_to == "Kelvin":
            result = celsius_to_kelvin(temp)
            print(f"{temp} Celsius is {round(result, 2)} Kelvin")
        elif scale_from == "Kelvin" and scale_to == "Celsius":
            result = kelvin_to_celsius(temp)
            print(f"{temp} Kelvin is {round(result, 2)} Celsius")
        else:
            print("This conversion is not supported.")

    if input("Convert another? (yes/no): ").strip().lower() == "no":
        break
