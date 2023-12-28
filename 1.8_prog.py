def print_pattern(rows):

    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

# Input the number of rows from the user
num_rows = int(input("Enter the number of rows: "))

# Call the function to print the pattern
print_pattern(num_rows)
