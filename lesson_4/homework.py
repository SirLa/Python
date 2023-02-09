# 1
# copyn mi levela copy anum, deepcopyn nested itemnernela copy anum,
# deep copy i jamanak nested itemnery vor poxenq originaly chi poxvi

# 2

x = [1, 2, 5, [8, 9, 10]]
copy = x[3][0:3]
y = x[0:3]
y.append(copy)
x[3][1] = 5
print(y, x)

# 3
# vorovhetev arrayi id n chenq poxum, change chi tenum

tup = ('Erk', 'Ereq', 'Choreq', 'Hing', 'Urb', ['Shb'])
tup[5].append('kiraki')
print(tup)

# 4

personal_info = ('My name', 'My last name', 'My father name')
name, last_name, patronymic = personal_info
print(name, last_name, patronymic)

# 5

users_tuple = ("Lilit", "Aren", "Janna", "Samvel (Sam)", "Gohar", "Armen", "Luiza")
users_list = list(users_tuple)
users_list[2] = 'text'
users_tuple = tuple(users_list)
print(users_tuple)

# 6

users_list = [
    "Lilit", "Aren", "Janna", "Samvel (Sam)", "Gohar", "Armen", "Luiza",
    [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21]]
]
formatted_users_list_items = tuple(users_list[0:7])
del users_list[0:6]

users_list[0] = formatted_users_list_items

zip_user_list = zip(users_list[0], users_list[1][0], users_list[1][1], users_list[1][2])

print(list(zip_user_list))

# Research

# zip() function veradardznuma hajordakanutyun, vortex hamapatasxanabar amen itemy karumes kapes
