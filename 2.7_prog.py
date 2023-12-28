# Original list
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# i. Print Complete list
print("i. Complete List:", a)

# ii. Print 4th element of list
print("ii. 4th Element:", a[3])

# iii. Print list from 0th to 4th index.
print("iii. List from 0th to 4th Index:", a[:5])

# iv. Print list -7th to 3rd element
print("iv. List -7th to 3rd Element:", a[-7:3])

# v. Appending an element to list.
a.append(110)
print("v. Appended List:", a)

# vi. Sorting the elements of list.
a.sort()
print("vi. Sorted List:", a)

# vii. Popping an element.
popped_element = a.pop()
print("vii. Popped Element:", popped_element)
print("    Updated List:", a)

# viii. Removing Specified element.
specified_element = 50
a.remove(specified_element)
print("viii. Removed Element:", specified_element)
print("     Updated List:", a)

# ix. Entering an element at specified index.
index_to_insert = 2
element_to_insert = 25
a.insert(index_to_insert, element_to_insert)
print("ix. Inserted Element at Index {}: {}".format(index_to_insert, element_to_insert))
print("    Updated List:", a)

# x. Counting the occurrence of a specified element.
element_to_count = 30
count = a.count(element_to_count)
print("x. Count of {}: {}".format(element_to_count, count))

# xi. Extending list.
extension_list = [120, 130, 140]
a.extend(extension_list)
print("xi. Extended List:", a)

# xii. Reversing the list.
a.reverse()
print("xii. Reversed List:", a)
