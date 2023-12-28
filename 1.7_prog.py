def calculate_factorial(n):

    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

# Input a number from the user
user_number = int(input("Enter a number: "))

# Check if the entered number is non-negative
if user_number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate and print the factorial
    factorial = calculate_factorial(user_number)
    print(f"The factorial of {user_number} is: {factorial}")
