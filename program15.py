#practice question 1

movies = []  # Creating an empty list to store movie names

mov1 = input("Enter first movie name: ")
mov2 = input("Enter second movie name: ")
mov3 = input("Enter third movie name: ")

movies.append(mov1)  # Adding the first movie to the list
movies.append(mov2)  # Adding the second movie to the list 
movies.append(mov3)  # Adding the third movie to the list

print("Movies list:", movies)  # Printing the list of movies

#practice question 2

list1 = [1, 2, 1]  # Creating a list with 3 elements
list2 = [1, 2, 3]  # Creating another list with 3 elements

copy_list1 = list1.copy()  # Creating a copy of list1
copy_list1.reverse()  # Reversing the order of the copied list

if (copy_list1 == list2):  # Checking if the reversed copy of list1 is equal to list2
    print("The lists are palindromes.")
else:
    print("The lists are not palindromes.")