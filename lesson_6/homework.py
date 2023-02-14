# 1

# x = {1,2,4,5,6}
# y = {5,6,7,8,9}
#
# print(y.union(x))
# print(x.difference(y))

# 2
#
# hatum = set(list(x.intersection(y)))
# print(x.difference(hatum))

# 3

# r - bacuma u karduma filey defaultov

# 4

file_1 = open("file_1.txt", "w")
file_1.write("11 lal asaksj asj ")
file_2 = open("file_2.txt", "w")
file_2.write("22 sakskals asajsk ")
file_1.write("texttext")
file_2.write("textttt")
file_1.close()
file_2.close()

# file_name = input("Which files do you want to read?")
# with open(file_name) as file:
#     df = file.read()
#     print(df)


# 5

list_users = [
    {
      'first_name': 'Jorj',
      'last_name': 'Bush',
      'age': 55
    },

    {
      'first_name': 'James',
      'last_name': 'Bond',
      'age': 100
    }
]

user_data = open("user_info.txt", "w")
user_data.write(
    f"user1: first_name = {list_users[0]['first_name']}, last_name = {list_users[0]['last_name']}, age = {list_users[0]['age']}\n"
    f"user2: first_name = {list_users[1]['first_name']}, last_name = {list_users[1]['last_name']}, age = {list_users[1]['age']}"
)
user_data.close()

# research

# isdisjoint() - ete 2 set lriv yndhanur ban unen false a veradardznum, hakarak depqum true
# remove()-ի ու discard()-ի տարբերությունը - remove-y ete chka et itemy errora qcum, discardy error chi qcum
