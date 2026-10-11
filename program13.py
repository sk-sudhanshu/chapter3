#list methods

list1 = [1, 3, 4, 2, 5]
list1.append(6)  # Adding an element to the end of the list
print(list1)

list1.sort()  # Sorting the list in ascending order
print(list1)

list1.sort(reverse=True)  # Sorting the list in descending order
print(list1)

list1.reverse()  # Reversing the order of the list
print(list1)

list1.insert(2, 10)  # Inserting an element at index 2
print(list1)

list1.remove(3)  # Removing the first occurrence of the element 3
print(list1)

list1.pop(4)  # Removing the element at index 4 from the list
print(list1)