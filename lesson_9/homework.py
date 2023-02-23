# 1

def print_name(name, last_name, age):
    print(f"Hello my name is {name} my last name is {last_name}, I am {age} years old")


print_name('siri', 'aslanyan', 23)


# 2

def change_chars(text, old_char, new_char):
    new_text = ''
    for char in text:
        if char == old_char:
            char = new_char
        new_text += char
    print(new_text)


change_chars('lasvegas', 'a', 'b')


# 3

def create_file(file_name='text.txt', list_of_texts=[]):
    file = open(file_name, 'w')
    for line in list_of_texts:
        file.write(f"{line}\n")
    file.close()


create_file('file.txt', ['lalala', 'nanana', 'kakakak'])


# 4

def is_number_prime(number):
    if number > 1:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True
    else:
        return False


print(is_number_prime(7))


# Research
# tes orinaky, 3 chakerti mej gracy helpi jamanak docunetationa darnum u cuyca talis
def add(a, b):
    """
    Sum up two integers
    Arguments:
        a: an integer
        b: an integer
    Returns:
        The sum of the two integer arguments
    """
    return a + b


help(add)
