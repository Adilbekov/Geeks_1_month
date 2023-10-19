#Задача 1
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)

#Задача 2
# numbers = {'num_1' : 1, 'num_2' : 2, 'num_3' : 3, 'num_100' : 100}
# for key in numbers:
#     numbers[key] *= 5
# print(numbers)

#Задача 3
# student = {'name' : 'Askhat', 'age' : 17}
# student['age'] *= 2
# print(student)

#Задача 4
# student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
# student['age'] = 16
# print(student)

#Задача 5
# student = {'name' : 'Askhat', 'age' : 17}
# student.pop('age')
# print(student)

#Задача 6
# student = {'name' : 'Askhat'}
# student.setdefault('address', 'Западный Анар')
# print(student)

#Задача 7
# students = {'Иван','Мария','Андрей','Елена'}
# print(sorted(students))

#Задача 8
# students = {'Иван':4,'Мария':5,'Андрей':3,'Елена':2}
# print(max(students))

#Задача 9
# dict1 = {'a': 10,'b': 20,'c': 30}
# dict2 = {'b': 5,'c': 15,'d': 25}
# dict3 = {}
# for key, value in dict1.items():
#     dict3[key] = dict3.get(key, 0) + value
# for key, value in dict2.items():
#     dict3[key] = dict3.get(key, 0) + value
# print(dict3)

#Задача 10
# students = [{'имя': 'Иван', 'оценки': [5, 5, 2]}, {'имя': 'Мария', 'оценки': [2, 4, 3]}, {'имя': 'Андрей', 'оценки': [3, 5, 5]}, {'имя': 'Елена', 'оценки': [5, 5, 5]}]
# for student in students:
#     name = student['имя']
#     scores = student['оценки']
#     average_score = sum(scores) / len(scores)
#     print(f"{name}: {average_score}")

#Задача 11
# numbers_dict = {
#     'a': 10,
#     'b': 20,
#     'c': 30,
#     'd': 40
# }

# average_value = sum(numbers_dict.values()) / len(numbers_dict)

# closest_key = None
# closest_difference = float('inf')

# for key, value in numbers_dict.items():
#     difference = abs(value - average_value)
#     if difference < closest_difference:
#         closest_key = key
#         closest_difference = difference

# print(f"Ключ с наиближайшим значением к среднему: {closest_key} (Значение: {numbers_dict[closest_key]})")


#Задача 12
# products = [{'название': 'яблоки', 'цена': 15},{'название': 'бананы', 'цена': 20},{'название': 'апельсины', 'цена': 12},{'название': 'киви', 'цена': 15}]
# total_sum = sum(product['цена'] for product in products)
# print(total_sum)

# Задача 13
# country_capital = {'Россия': 'Москва','США': 'Вашингтон, D.C.','Франция': 'Париж','Германия': 'Берлин','Китай': 'Пекин'}
# country = input("Введите название страны: ")
# capital = input("Введите название столицы: ")
# country_capital.setdefault(country, capital)
# print(country_capital)  

#Задача 14
# students = [
#     {'имя': 'Иван', 'возраст': 22, 'оценки': [85, 90, 78]},
#     {'имя': 'Мария', 'возраст': 17, 'оценки': [92, 88, 95]},
#     {'имя': 'Андрей', 'возраст': 15, 'оценки': [78, 82, 80]},
#     {'имя': 'Елена', 'возраст': 22, 'оценки': [95, 91, 89]}
# ]
# for student in students:
#     marks = max(student["оценки"])
#     if student['возраст'] > 18:
#         print(f"Имя студента: {student['имя']}, максимальный балл: {marks}")


#Доп Задача
#Задача 7
# user = {}
# user1 = input("Придумайте пароль: ")
# user2 = input("Подтверждение: ")
# user.setdefault(user1)
# if len(user1) < 8 :
#     print("Короткий пароль!")
# elif user1 == '12345678':
#     print("Простой пароль!")
# elif user2 != user1:
#     print("Различаются.")
# else:
#     print("Ok", user, "Пароль создан")