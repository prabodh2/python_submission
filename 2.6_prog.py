def create_cube_dict(start, end):

    cube_dict = {num: num**3 for num in range(start, end + 1) if num % 2 != 0}
    return cube_dict

# Input the range from the user
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

# Call the function to create the dictionary
result_dict = create_cube_dict(start_range, end_range)

# Display the result
print("Dictionary of Cubes of Odd Numbers:")
print(result_dict)
