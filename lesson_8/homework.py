# 1

last_names = ['Adamyan', 'Allen', 'Brooks', 'Davidson', 'Sargsyan', 'Jenkins']
armenian_last_names = []

while last_names:
    last_name = last_names.pop()
    length = len(last_name)
    last_letters = last_name[length - 3:]
    if last_letters == 'yan':
        armenian_last_names.append(last_name)
print(armenian_last_names)

# 2

long_word = 'arevachachapaylatakum'

count = 0
for letter in long_word:
    if letter == 'a':
        count += 1
print(count)

# 3

alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = list(range(1, len(alpabet) * 2, 2))
print(dict(zip(alpabet, numbers)))

# 4

factorial = 1
number = 1

while number < 11:
    factorial *= number
    number += 1

print(factorial)

# 5

alpabet_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reversed_alpabet = alpabet_2[:: -1]

print(reversed_alpabet)


# Research

"""
enumerate() - counteri tex karanq ogtagorcenq, key value a pahum , orinak unenq list [a, b, c] , 
enumarate([a, b, c]) anenq kveradardzni {0: a, 1: b, 2: c}, for i mejel nuyny key value a veradardznum 

"""