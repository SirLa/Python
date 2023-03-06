# 5

import sys

user_info = ["Lilit", "Aren", "Janna", "Samvel", "Gohar", "Armen", "Luiza"]
if sys.argv[1] == 'set':
    print(list(user_info))
elif sys.argv[1] == 'list':
    print(list(user_info))
elif sys.argv[1] == 'tuple':
    print(tuple(user_info))
else:
    print("the argument is wrong")

