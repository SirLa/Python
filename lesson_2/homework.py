# 1. inch type kveradardzni  1 + 2.0 +3:: Float (floati het gorc aneluc typey floata linum)

expression_1 = 1 + 2.0 + 3
print(type(expression_1))

# 2. pakagic

expression_2 = 2 * (3 + 4)
print(expression_2)

# 3. kloracnel 2.555 stanal 2.56

num = 2.555
print(round(num, 2))

# 4.

text = "Hello world"
print(text[6:], text[:5])

# 5.

text_1 = "text_1"
digit_1 = 1990
text_2 = "text_3"


print("Lorem Ipsum is %s dummy text of the printing and typesetting industry. " \
              "Lorem Ipsum has been the industry's standard dummy text ever since the %ds, " \
              "when an unknown printer took a %s of type and scrambled it to make a type specimen book." % (text_1, digit_1, text_2))


print("Lorem Ipsum is {0} dummy text of the printing and typesetting industry. "
      "Lorem Ipsum has been the industry's standard dummy text ever since the {1}s, "
      "when an unknown printer took a {2} of type and scrambled it to make a type specimen book.".format(text_1, digit_1, text_2))

print(f"Lorem Ipsum is {text_1} dummy text of the printing and typesetting industry. "
      f"Lorem Ipsum has been the industry's standard dummy text ever since the {digit_1}s, "
      f"when an unknown printer took a {text_2} of type and scrambled it to make a type specimen book.")

# 6

digit_2 = 97
item_1 = digit_2 % 10
item_2 = (digit_2 - item_1) // 10
print(item_1, item_2)

# 7

num_1 = 123

d_1 = num_1 % 10
d_2 = ((num_1 - d_1) // 10) % 10
d_3 = (num_1 - ((10 * d_2) + d_1)) // 100

print(d_1, d_2, d_3)

# research

str = "text"
print(str[len(str) - 1:])


# method of builtins.str instance
#     Return a copy of the string with leading and trailing whitespace removed.
#
#     If chars is given and not None, remove characters in chars instead.
# (END)

# Փորձեք հասկանալ ինչ են անում """-ը, օրինակ """some long text"""

# You can assign a multiline string to a variable by using three quotes:
