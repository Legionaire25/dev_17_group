# def avg(ranks):
#     assert len(ranks) != 0 'expected len list not zero'
#     return sum(ranks) / len(ranks)
#
# my_list = []
# new_list = [1, 2, 3]
# print(f'среднее значение: {avg(my_list)}')

# 1) Написать функцию, которая будет заполнять список степенями числа 2 (от 2^1 до 2^n). n - целое число.
#
# def number_in_powers(n):
#     power= [2 ** i for i in range(1, n + 1)]
#     return power
# n = 0
# while n != 5:
#      n = int(input('Введите целое число :'))
# result = number_in_powers(n)
# print(result)
# assert result == [2, 4, 8, 16, 32]
# print("Тест пройден")



# 2) """Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys()""" Сделать проверку assert

# original_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# def add_length_to_keys(dictionary):
#     new_dict = {}
#     for key in dictionary.keys():
#         new_key = f"{key}{len(key)}"
#         new_dict[new_key] = dictionary[key]
#     return new_dict
# result_dict = add_length_to_keys(original_dict)
#
#
#
# print(result_dict)

# 3)"""Ввести строку. Если длина строки больше 10 то создать новую строку с 3 восклицательными
# знаками и
# вывести на экран. Если у нас меньше чем 10 то вывести второй символ строки""" Сделать проверку assert

# user_input = input("Введите строку: ")
#
# if len(user_input) > 10:
#     new_string = user_input + "!!!"
#     print("Новая строка:", new_string)
# else:
#     second_char = user_input[1]
#     print("Второй символ строки:", second_char)
#
# assert len(user_input) <= 10 or new_string == user_input + "!!!", "Ошибка в создании новой строки"
# assert len(user_input) > 10 or second_char == user_input[1], "Ошибка в извлечении второго символа"
#
# print("Тест пройдены!")

# 4) Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

# 5) Напишите программу, которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a;b],
# которые кратны числу 3. В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [−5;12].
# Всего чисел, делящихся на 3, на этом отрезке 6: − 3 , 0 , 3 , 6 , 9 , 12. Их среднее арифметическое равно 4.5.
