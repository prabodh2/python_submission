def get_unique_elements(input_list):
    # Use a set to store unique elements
    unique_elements_set = set(input_list)
    
    # Convert the set back to a list to maintain the order
    unique_elements_list = list(unique_elements_set)
    
    return unique_elements_list

# Example usage:
input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
result = get_unique_elements(input_list)

print("Original List:", input_list)
print("List with Distinct Elements:", result)
