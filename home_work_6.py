# # homework
# # 1
# def season(num1):
#     if num1 == 12 or num1 <= 2:
#         print('зима')
#     elif num1 <=5:
#         print('Весна')
#     elif num1 <=8:
#         print('Лето')
#     elif num1 <=11:
#         print('осень')
#     else:
#         print("введено неправельное число")

# season()


# Задача 2
# def bank(a, years):
#     persent = 0.10
#     for i in range(years):
#         a *= (1 + persent) 
#     print(a)
# bank(5000, 3)


# 3
# def list(list_1,list_2):
#     a = list_1 + list_2
#     print(sum(a))
#     print(sum(a)/10)

# list_1 = [1212,323,323,323,565]
# list_2 = [233,45,576867,78979,989]

# list(list_1,list_2)

# 4
# def a(numbers):
#     for i in range(1,100):
#         print(f'{numbers}:0')

# a('numbers')

# 5
# def text(list):
#     for i in list ['i']:

#         list = ['hallo', 'staderen', 'islam','irak','immunitet']

# text(list)


#Доп задача номер 1
# def abu(list):
#     list1 = []
#     for item in list:
#         if 'A' not in item and 'a' not in item and 'I' not in item and 'i' not in item:
#             list1.append(item)
#     return list1
# list2 = ["Apple", "orange", "Cherry", "Grapes", "Kawin"]
# list3 = abu(list2)
# print(list3)




# доп задача2
# def reverse_number(n):
#     reversed_n = int(str(n)[::-1])
#     return reversed_n


# n = 27
# reversed_n = reverse_number(n)
# print(f"Перевернутое число: {reversed_n}")

# 3 доп задача
# def chat_bot():
#     while True:
#         user = input("задайте вопрос:  ")
#         if user.find("?")>0:
#             print("Конечно")
#         elif user.find("!")>0:
#             print("успокойся")
#         elif user == "":
#             print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#         else:
#             print("ну и что")


# chat_bot()





