def is_perfect_number(num):
    # Check for positive integers
    if num <= 0:
        return False
    
    # Find proper divisors and calculate their sum
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    # Check if the number is perfect
    return divisors_sum == num

# Example usage:
number_to_check = int(input("Enter a number to check for perfection: "))

if is_perfect_number(number_to_check):
    print(f"{number_to_check} is a perfect number.")
else:
    print(f"{number_to_check} is not a perfect number.")
