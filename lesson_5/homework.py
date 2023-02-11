# 1

user = {
    'name': 'Jarviz',
    'age': '100',
    'professions': ['robot', 'dancer'],
    'test_result': [14, 5, 8, 99, 12, 2, 3, 5, 4]
}

user['professions'][1] = 'text'
user['test_result'].sort(reverse=True)
#print(user['professions'], user['test_result'])

# 2

fruits = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# print(sum(fruits.values()))
fruits['dzmeruk'] = 10
# print(fruits)

# 3

user_list = [
    {'first_name': '', 'last_name': '', 'age': '', 'phone': {'brend': '', 'number': '', 'is_5g': ''}},  # user 1
    {'first_name': '', 'last_name': '', 'age': '', 'phone': {'brend': '', 'number': '', 'is_5g': ''}}  # user 2
]

user_list[0]['first_name'] = 'Bill'
user_list[0]['last_name'] = 'Gates'
user_list[0]['age'] = 39
user_list[0]['phone']['brend'] = 'Samsung'
user_list[0]['phone']['number'] = '(206) 709-3100'
user_list[0]['phone']['is_5g'] = True
user_list[0]['car'] = {'car': {'model': 'Chevrolet Suburban', 'type': 'Luxus', 'max_speed': '232 km/h'}}

user_list[1]['first_name'] = 'Siri'
user_list[1]['last_name'] = 'jobs'
user_list[1]['age'] = 28
user_list[1]['phone']['brend'] = 'Iphone'
user_list[1]['phone']['number'] = '(93) 08-17-27'
user_list[1]['phone']['is_5g'] = False
user_list[1]['car'] = {'car': {'model': 'Mazda 3', 'type': 'chumus', 'max_speed': '180 km/h'}}

#print(user_list[0]['phone']['is_5g'], user_list[1]['phone']['is_5g'])

x = (user_list[0]['age'] > 18 and user_list[0]['phone']['is_5g']) or \
    ('bill' not in user_list[0]['first_name'] and 'gates' not in user_list[1]['last_name'])
y = (user_list[1]['age'] > 18 and user_list[0]['phone']['is_5g']) or \
    ('bill' not in user_list[1]['first_name'] and 'gates' not in user_list[1]['last_name'])
#print('chipavorvac e', x, y)

# 4

# zip()-ի և այլ անհրաժեշտ գործիքների միջոցով ստացեք dict որի key-րը կլինեն ձեր անվան առաջին տառերը իսկ
# 	   value-ները հակառակ տառերը, օրինակ ՝ jarvis {'j':'s', 'a':'i', 'r':'v', 'v':'r', 'i':'a', 's':'j'}

my_name = 'Siranush'
reversed_name = my_name[::-1]

zip_name_list = zip(my_name, reversed_name)

print(dict(zip_name_list))

"""
Research

  1. setDefault()
    - dictionary-i methoda, veradardznuma et key n ete ka ete chka avelacnuma
  2. fromkeys()
    - dictionary-i methoda, tvac arjeqnerov sarquma dictionary
  3. Փորձեք կիրառել մեր անցած ֆունկցիաները dict-ի համար և գրեք արդյունքներիը
    - zip - kapuma key ery,
    - len -veradardznuma itemneri qanaky,
    - sum - chi kareli kanchel es typei vra,
    - copy - nuyn dzev ashxatuma, mi level copy a anum
    - sorted - key ery sorta anum
"""