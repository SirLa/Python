import functools

# 1

items = ['abcba', 'abcbca', 'abcbt', '121', '123454321', '5551555', 'abcd']


def is_palindrome(item):
    reversed_item = ''
    for i in item:
        reversed_item = i + reversed_item
    return reversed_item == item


def filter_palindromes(list_of_items):
    return list(filter(is_palindrome, list_of_items))


print(filter_palindromes(items))


# 2

def my_map(func, list_of_items):
    new_list_of_items = []
    for i in list_of_items:
        new_list_of_items.append(func(i))
    return iter(new_list_of_items)


print(list(my_map(lambda item: len(item), items)))

# gitem vor mi ban sxal em arel bayc chgitem inchy, zip y voobshe vortex petqa ogtagorceinq, u googlov urish dzever arac, erevi baner kain cheinq ancel, chjokeci


# 3

number_list = [1, 2, 5, 70, 4, 8, 50, 44]


def find_biggest_number(l_o_n):
    biggest_number = 0
    for i in l_o_n:
        if i > biggest_number:
            biggest_number = i
    return biggest_number


# print(find_biggest_number(number_list))


def find_biggest_number_with_reduce(l_o_n):
    return functools.reduce(lambda x, y: x if x > y else y, l_o_n)


print(find_biggest_number_with_reduce(number_list))
