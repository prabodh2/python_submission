# Original list
original_list = [1, 2, 3]

# i. By using + operator
extended_list_1 = original_list + [4, 5, 6]

# ii. By using append()
extension_list = [7, 8, 9]
extended_list_2 = original_list.copy() 
extended_list_2.append(extension_list)

# iii. By using extend()
extended_list_3 = original_list.copy() 
extended_list_3.extend(extension_list)

# Print the results
print("i. Extended List using + operator:", extended_list_1)
print("ii. Extended List using append():", extended_list_2)
print("iii. Extended List using extend():", extended_list_3)
