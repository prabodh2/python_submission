def create_tuple_list_with_cube(input_list):

    tuple_list = [(num, num**3) for num in input_list]
    return tuple_list

# Input list of numbers
input_list = [2, 3, 4, 5, 6, 7, 8, 9]

# Call the function to create the list of tuples with cubes
result_list = create_tuple_list_with_cube(input_list)

# Display the result
print("List of Tuples with Number and its Cube:")
for item in result_list:
    print(item)
