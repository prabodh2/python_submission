# my_module.py

def add_numbers(num1, num2):
    return num1 + num2


# main_script.py

# Import the created module
import my_module

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Use the function from the imported module
result = my_module.add_numbers(num1, num2)

# Display the result
print(f"The sum of {num1} and {num2} is: {result}")
