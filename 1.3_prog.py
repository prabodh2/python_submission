def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input a number from the user
user_number = int(input("Enter a number: "))

# Call the function to check if the number is even or odd
result = check_even_odd(user_number)

# Display the result
print(f"The number {user_number} is {result}.")
