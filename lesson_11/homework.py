# 1.1

def get_user_info():
    with open("db.txt") as f:
        data = []
        for line in f:
            data.append(line.strip().split(','))

        data_keys = data.pop(0)

        finalData = []

        for i in data:
            finalData.append(dict(zip(data_keys, i)))

        return finalData


# print(get_user_info())


# 1.2

def update_user_info(user_info, **kwargs):
    user_info.append(kwargs)
    return user_info


updated_user_info = update_user_info(
    get_user_info(),
    first_name='test',
    last_name='testyan',
    age='17',
    profession='testirovshik',
    country='testashen',
    favorite_film='the tester',
    favorite_singer='testing band',
    favorite_chips='teys'
)


# 1.3

def write_updated_user_info_in_file(user_info):
    keys = user_info[0].keys()
    lines = ','.join(keys) + '\n'

    for i in user_info:
        line = ','.join(i.values()) + '\n'
        lines += line

    with open("db.txt", 'w') as f:
        f.write(str(lines))


# write_updated_user_info_in_file(updated_user_info)

# 2

number = [[[[[10]]]]]


def find_number(n):
    if not isinstance(n, list):
        return n
    else:
        return find_number(n[0])


print(find_number(number))


# 3


# chstugel, petqa andradarnam

def sum_numbers(n, sum_of_numbers=0):
    if not isinstance(n, list):
        sum_of_numbers += n
    else:
        sum_numbers(n[0], sum_of_numbers)

    return sum_of_numbers




numbers = [1, 2, [3, 4], [5, 6, [10, 19]]]
print(sum_numbers(numbers))


# Research

"""
lambda functions - ananun functiona, mi toxova linum
"""
