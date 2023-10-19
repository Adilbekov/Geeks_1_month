# 
# 1 HW
# age = int(input('Введите число: '))
# if age <18:
#     print('Вы не соверщенолетний!!! \n чык ал жактан!!')
# elif age >18:
#     print('вы совершенолетний \n коро бер')
# elif age > 18 and age < 65:
#     print('сен уже карып баштапсын')
# elif age > 65 and age < 100:
#     print('карып бутупсун')
# else: 
#     print("Error")

#   2HW


# nam1 = float(input('введите второе число: '))
# nam2= float(input('введите первое чиcло: ')) 
# nam3 = float(input('введите третее число: '))

# min_num = min(nam1, nam2, nam3)
# print(min_num)

    #    3HW

# my_spisok = ['Osh','Bishkek','Talas','Karacha','Kaganat','Nisan','Mers','Golf','Chui','alma Ata','BMW','Karalma','alma Ata', 'q']
# spisok = my_spisok[2:8]
# print(spisok)


#  4HW
# my_list = ['q','w','r','t','y','u','i', 'a','s','d']
# del my_list[2]
# del my_list[7]

# new_list = ['z','x','c','v','b']
# print(my_list + new_list)

# 5hw

# new_file = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# new_file.remove(2)
# new_file.remove(16)
# print(new_file)


# 6

# numbers = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8, 909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,4,52,3]
# sorted_as = sorted(numbers)
# # print(sorted_as)

# # 7

# reversed_numbers = sorted_as[::-1]
# print(reversed_numbers)


# 8

# print(numbers.count(2))
# print(numbers.count(5))
# print(numbers.count(3))

# 9

# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(sum(list) / len(list))


# numbers = [1,2,3,4,5,6,7,8,9,10,]
# print(min(numbers))


# print(max(numbers))



# print(sum(numbers))


# list = ["q","w", "e",'f','fg','fvf','fbf','fbgfb','fbgb','fggbbgb']
# list[3], list[7] = list[7], list[3]
# print(list)

list = list(range(1,21,2))
print(list)
