def print_natural_numbers_and_sum(n):

    sum_of_numbers = 0
    print(f"The first {n} natural numbers are:")
    for i in range(1, n + 1):
        print(i, end=" ")
        sum_of_numbers += i
    print(f"\nSum of the first {n} natural numbers is: {sum_of_numbers}")

# Input the value of n from the user
n = int(input("Enter the value of n: "))

# Call the function to print natural numbers and their sum
print_natural_numbers_and_sum(n)
