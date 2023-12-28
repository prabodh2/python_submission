# Define a sample list
my_list = [1, 2, 3, 4, 5]

# Method 1: Using reverse method
print("Traversing in reverse order using reverse method:")
reversed_list_method1 = my_list.copy()  # Create a copy to avoid modifying the original list
reversed_list_method1.reverse()
for item in reversed_list_method1:
    print(item, end=" ")
print()

# Method 2: Using slicing
print("Traversing in reverse order using slicing:")
reversed_list_method2 = my_list[::-1]
for item in reversed_list_method2:
    print(item, end=" ")
print()
