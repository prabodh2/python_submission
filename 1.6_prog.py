def is_armstrong_number(number):

    num_str = str(number)
    order = len(num_str)
    sum_of_cubes = sum(int(digit) ** order for digit in num_str)
    return sum_of_cubes == number

# Input a number from the user
user_number = int(input("Enter a number: "))

# Check if the entered number is an Armstrong number
if is_armstrong_number(user_number):
    print(f"{user_number} is an Armstrong number.")
else:
    print(f"{user_number} is not an Armstrong number.")
