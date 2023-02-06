# 1

users_list = ['Vardan', 'Vazgen', 'Jarviz']
print(users_list[0], users_list[1], users_list[2])
users_list[1] = 'Oxxxy'
print(users_list)

# 2

x = [1,2,3,4,5,6]
z = [7,8,9,10,11]

print(len(x + z))

# 3

"""len() - veradardznuma erkarutyuny
   help() - infoa talis
   sum()
"""

# 4 commentic hanel stugeluc

# amount = int(input("how many words do you want to type?"))
# word = input("write a word")
# print(amount * word)

# 5

# users_list_isxodniy = ["Vazgen", "Chris Tacker", "Nikola Tesla"]
# new_user_list = users_list_isxodniy[:]
# new_user = new_user_list.append(input("write user nam you want to add"))
#
# print(users_list_isxodniy, new_user_list)

# 6

# users_list = ["Vazgen", "Chris Tacker", "Nikola Tesla"]

# user_to_remove = input(f"Your users is {users_list} who do you want to remove?")
# users_list.remove(user_to_remove)
# print(f"User {user_to_remove.upper()} is removed, your users are {users_list}")


# 7

#numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# couple_numbers = numbers_list[::-2]
# print(sum(couple_numbers))


# Research

#  1. list-ի որ մեթոդով կարող ենք գտնել տրված արժեքի index-ը: - index()
#print(numbers_list.index(9))


# 2. Ինչ է անում del արտահատությունը ու ինչով է տարբերվում remove()-ից:

# del
"""The del is a keyword in Python.
   An indexError is thrown if the index doesn’t exist in the Python list.
   The del works on index.
   The del deletes an element at a specified index number.
   The del is simple deletion.
"""

# remove
"""
   The remove(0) is a built-in method in Python.
   The valueError is thrown if the value doesn’t exist in the Python list.
   The remove() works on value.
   It removes the first matching value from the Python List.
   The remove() searches the list to find the item.
"""
