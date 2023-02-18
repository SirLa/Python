# 1

users = [[]]

if users:
    print('users exist')
else:
    print('users not found')

# ktpi 'users not found, vorovhetev uxexs archicha'

# 2

pythonists = ["Bush", "Jarvis", "Oxxi", "Buffon", "Vardan"]
my_name = 'Siri'
if my_name in pythonists:
    print(my_name)
else:
    pythonists.append(my_name)
    print(pythonists, my_name)

# 3

# x = 0
# while x < 21:
#     if x % 2 == 0:
#         print(x)
#     x = x + 1

# 4

y = 20

while y > 0:
    y = y - 1
    if y == 17:
        continue
    print(f"{y}-{y*y}")

# 5

counter = 0
n = 3

while n < 50:
    if n % 3 == 0:
        print(n)
        counter += 1
    n += 1
    if counter == 10:
        break

# Research

"""
 Ինչպես է աշխատում else-ը while-ի հետ
 while else - erb vor while i paymany darnuma false verjum mtnuma else-i mej, 
 break return aneluc el chi mtni, errori jamanakel chi mtni
"""