#1
# it_company = ('Google', 'Amazon', 'Microsoft')
# list = list(it_company)
# list.append('Tesla')
# list_2 = tuple(list)
# print(list_2)

# 2
# text = ('Experienced', 'programmers', 'in', 'any', 'other', 'language', 'can', 'pick', 'up', 'Python',
#  'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'Amazon','clean', 'syntax', 'and', 'indentation', 
#  'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3',
#  'overview')
# print(text.index('Amazon'))

# 3
# text = ('Experienced', 'programmers', 'Google','in', 'any', 'Google', 'other', 'language', 'can', 'pick', 'up', 'Python', 'very', 
# 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and', 'indentation')
# text_1 = list(text)
# text_1[2] = 'Apple'
# text_2 = tuple(text_1)
# print(text_2)

# 4
# text = ('Experienced', 'programmers', 'in', 'any', 'Apple', 'other', 'language', 'can', 'pick', 'up', 'Python', 'very', 
# 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syn', 'Microsoft','tax', 'and', 'indentation')
# print(text[4:20])

# 5
# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language', 'can', 'pick', 'up', 'Python',
#  'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and', 'indentation', 
#  'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3',
#  'overview')
# print(text_tuple.count('Python'))

# 6
# text = ('Experienced', 'programmers', 'in', 'any', 'other', 'language', 'can', 'pick', 'up', 'Python', 'very', 
# 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and', 'indentation')
# text_1 = list(text)
# del text_1 [3:9]
# text_2 = ['Amazon', 'Google', 'Microsoft', 'Tesla', 'Android']
# text_1.extend(text_2)
# tuple = tuple(text_1)
# for i in text_1:
#     print(i)

#7
# a = []
# for i in range(1,101):
#     a.append(i)
# print(a)

# 8
# numbers = list(range(1,1001))
# min_numbers = min(numbers)
# max_numbers = max(numbers)
# sum_numbers = sum(numbers)
# print(numbers)
# print(min_numbers)
# print(max_numbers)
# print(sum_numbers)

# 9
# numbers = []
# for numbers in range(1,498):
#     if numbers % 2 == 0:
#         print(numbers)


# 10

# while True:
#         num1 = float(input("Введите первое число: "))
#         num2 = float(input("Введите второе число: "))
#         user = input("Выберите операцию (+, -, *, /) или 'Exit' для выхода: ")
#         if user == 'Exit':
#             break 
#         if user == '+':
#             print(num1 + num2)
#         elif user == '-':
#             print(num1 - num2)
#         elif user == '*':
#             print(num1 * num2)
#         elif user == '/':
#             print(num1 / num2)
#         else:
#             print("Error")

