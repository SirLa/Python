# 1

"""
Ինչ տարբերություններ կան list comprehension-ի և generator-ի մեջ:

-list comprehension y uxxaki for -ov list sarqelu karch dzeva
-generator-y functiona vory veradardznuma iterable object vori vra karum enq next kanchenq,
generatorum el return y yeald ov enq anum, vory mi arjec veradardznuma hajordakanutyunic,
u spasuma hajordin nextov kancheluc hajordna veradardznum

husov em shat chem tuftel, alareci googlem

"""

# 2

"""
Ինչպես կարող ենք իմանալ function-ը generator է թե ոչ:

- nextov kanchenq
- returni texy yield petqa grac lini
"""


# 3

def fin(n):
    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a + b


ln = int(input('How long? '))
print(next(fin(ln)))



