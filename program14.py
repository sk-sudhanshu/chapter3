#tuples in python
#tuples are immutable, meaning their values cannot be changed after creation

tuple1 = (2, 4, 3, 1, 5)  # Creating a tuple with 5 elements
print(tuple1)
print(type(tuple1))  # Checking the type of the tuple
print(tuple1[1:3])  # Accessing elements from index 1 to 2 of the tuple


#tuples methods

tuple2 = (1, 2, 3, 4, 5, 1, 2, 3)  # Creating a tuple with duplicate elements
print(tuple2.count(1))  # Counting the occurrences of the element 1 in the tuple

print(tuple2.index(3))  # Finding the index of the first occurrence of the element 3 in the tuple