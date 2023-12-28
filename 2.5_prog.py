def compare_dictionaries(dict1, dict2):

    return dict1 == dict2

# Example dictionaries
dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'a': 1, 'b': 2, 'c': 3}

# Compare dictionaries using the function
result = compare_dictionaries(dict_a, dict_b)

# Display the result
if result:
    print("The dictionaries are equal.")
else:
    print("The dictionaries are not equal.")
