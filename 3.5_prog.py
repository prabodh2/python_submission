def count_upper_lower(string):
    # Initialize counters
    upper_count = 0
    lower_count = 0
    
    # Iterate through each character in the string
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    # Return the counts
    return upper_count, lower_count

# Example usage:
string_test = 'Today is My Best Day'
upper, lower = count_upper_lower(string_test)

print(f"Original String: '{string_test}'")
print(f"Number of Upper-case Letters: {upper}")
print(f"Number of Lower-case Letters: {lower}")
