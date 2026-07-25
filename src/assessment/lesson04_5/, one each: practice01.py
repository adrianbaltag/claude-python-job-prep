# OUT:   what comes back + what kind of thing (string / number / list / dict)
# IN:    what I must be given
# STEPS: 1.
#        2.
#        3.

"""
    1. Count names
A function that takes a list of names and gives back how many there are.

2. Apply a discount
A function that takes a price and a discount percentage, and gives back the final price.

3. Long words only
A function that takes a list of words and gives back only the words longer than 4 letters.

4. Describe a person
A function that takes a dictionary like {"name": "Ana", "age": 30} and gives back a sentence describing them.

5. Just the names
A function that takes a list of dictionaries — people, each with a name and an age — and gives back a list of only the names.
"""


# # 1
# def count_names(my_list):

#     size = len(my_list)

#     return size


# names = [
#     "Emma",
#     "Liam",
#     "Olivia",
#     "Noah",
#     "Ava",
#     "Ethan",
#     "Sophia",
#     "Mason",
#     "Isabella",
#     "William",
# ]
# total = count_names(names)
# print(total)


# # 2
# def discount(price, discount):
#     my_price = float(price)
#     my_discount = float(discount)
#     discount_amount = my_price * (my_discount / 100)
#     final_price = my_price - discount_amount
#     return final_price


# my_item = discount(100, 25)
# print(my_item)


# # 3
# def long_word(list):

#     long_list = []
#     for i in list:
#         if len(i) > 4:
#             long_list.append(i)

#     return long_list


# names = [
#     "Emma",
#     "Liam",
#     "Olivia",
#     "Noah",
#     "Ava",
#     "Ethan",
#     "Sophia",
#     "Mason",
#     "Isabella",
#     "William",
# ]
# result = long_word(names)
# print("I got back:", result)


# 4
def decribe_a_person(dict):
    # dict = {"a_name": "Ana", "a_age": 30}
    person = f"Her name is {dict['a_name']} with an age of {dict['a_age']} years old"
    return person


my_dict = {"a_name": "Ana", "a_age": 30}
a_person = decribe_a_person(my_dict)
print(a_person)


# 5
def people_names(my_dict):

    list_name = []
    for n in my_dict:
        list_name.append(n["name"])
    return list_name
    # return f"the name is {'name'} and age is {'age'}"


people = [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 34},
    {"name": "Charlie", "age": 22},
    {"name": "Diana", "age": 41},
]
names = people_names(people)
print(names[3])
