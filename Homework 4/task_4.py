# 1.	 Выведите числа в диапазоне от 50 до 60.
# list1 = []
# for i in range(50, 60):
#  list1.append(i)
# print(list1)


# 2.	Вводится список чисел с клавиатуры.
# Нужно выводить элементы с чётными индексами.
# Пример:
# входные данные: 1, 2, 3, 4, 5, 6, 7, 8
# выходные данные: 1, 3, 5, 7
# list1 = [int(input("Введите числа: ")) for i in range(8)]
# list2 = []
# for i in list1:
#     if list1.index(i) % 2 == 0:
#        list2.append(i)
# print(list2)
# 3.	Вводится строка с клавиатуры.
# Если в ней  есть повторение слов, то выведите "Yes",
# # в противном случае "No"
# stroka = input("Введите строку: ")
# str1 =stroka.split()
# for i in str1:
#     if i == str1.find():  # не могу сделать
#      print('Yes')
#     else:
#      print('no')
# 4.	Вводится список чисел с клавиатуры.
# Необходимо вывести положительные числа.
# Подсказка: использовать for и if
# list1 = [int(input("Введите числа: ")) for i in range(5)]
# list2 = []
# for i in list1:
#     if i > 0:
#        list2.append(i)
# print(f'положительные числа: {list2}')

# 5.Вводится строка с пробелами.
# Разделите строку на слова и затем нужно вывести максимально по длине слово.
stroka = input("Введите строку: ")
max_word = ''
for word in stroka.split():
  if len(word) > len(max_word):
   max_word = word
   print(max_word)