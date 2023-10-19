# Homework
# 1

# list = "Этот текст содержит много слов и пробелов"
# print(list[::-1])


# 2

# my_list = ['яблоко','банан','вишня','яблоко','банан']
# print(set(my_list))

# 3
# text = "Цена товара: $19.99"
# a = text.index("$")
# b = text[a + 1:]
# c = float(b)
# d = c * 2
# print(d)

#4
# name = 'Эрбол'
# age = 16
# city = 'osh'
# print(f' Привет меня зовут {name} , мне  {age} лет, я живу в городе {city} ')

# 5

# name =str("Этот текст содержит несколько важных слов")
# if "важных" in name:
#     print("слово 'важных' найдено")
# else:
#     print("слово 'важных' не найдено")

#6
a = "2023-09-03"
b = a[:4]
c = a[5:7]
d = a[8:]
print(b)
print(c)
print(d)

# доп задача

text = """Advertising companies say advertising is necessary and important. 
It informs people about new products. Advertising hoardings in the street 
make our environment colourful. And adverts on TV are often funny. 
Sometimes they are mini-dramas and we wait for the next programme in the 
mini-drama. Advertising can educate, too. Adverts tell us about new, 
healthy products. And adverts in magazines give us ideas for how to look 
prettier, be fashionable and be successful. Without advertising, life is 
boring and colourless.
But some consumers argue that advertising is a bad thing. 
They say that advertising is bad for children. Adverts make children 
‘pester’ their parents buy things for them. Advertisers know we love our 
children and want to give them everything. So they use children’s 
‘pester power’ to sell their products. Finally, consumers say, if there is 
advertising there must be rules. Some adverts advertise unhealthy things like 
cigarettes and make people waste their money.
"""
print(text.count('s'))
print(text.count('t'))