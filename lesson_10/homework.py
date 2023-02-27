# 1
my_name = 'name'


def f1():
    global my_name
    my_name = 'Siri'


f1()
print(my_name)

# 2

users = ["Lilit", "Aren", "Janna", "Samvel", "Gohar", "Armen", "Luiza", "Janna", "Armen", "Lilit", "Armen"]
long_word = 'dzaynaskavarakavacharanoc'
last_names = ("Watson", "Richards", "Richardson", "Saunders", "Watson", "Young", "Saunders")


def find_repeated_values(sequence):
    if isinstance(sequence, int):
        return 'please send sequence object'
    unique_items = set()
    repeated_items = set()

    for item in sequence:
        if item not in unique_items:
            unique_items.add(item)
        elif item not in repeated_items:
            repeated_items.add(item)
    return repeated_items


print(find_repeated_values(users))


# 3

def return_sum_of_digits(number):
    list_of_digits = [int(i) for i in str(number)]
    sum_of_digits = 0
    for digit in list_of_digits:
        sum_of_digits += digit
    return sum_of_digits


print(return_sum_of_digits(12345))


# 4


def is_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def return_list_of_primes():
    list_of_primes = set()
    for number in range(2, 100):
        if is_prime(number):
            list_of_primes.add(number)

    return list_of_primes


print(return_list_of_primes())


# 5

def fibonacci(n):
    a = 0
    b = 1
    c = a + b
    if n <= 0:
        return 'normal tiv gri ay anasun'
    elif n == 1:
        return a
    else:
        for i in range(2, n):
            a = b
            b = c
            c = a + b
        return c


# Research

"""
Python Function Annotations - functioni parametrery taluc karum enq type y nshenq

*args
function in parametrner vor tanq args ov karanq vercnenq sax
**kwargs
named parametrnery nstuma functioni mej vorpes dict (key: value)
"""