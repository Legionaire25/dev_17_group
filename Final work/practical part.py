# Практическая часть:
# 1) Требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
# Для этого создайте класс TriangleChecker, принимающий только положительные числа.
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# Ура, можно построить треугольник!
# С отрицательными числами ничего не выйдет!
# Жаль, но из этого треугольник не сделать.

# class TriangleChecker:
#     def __init__(self, a, b, c):
#         if a <= 0 or b <= 0 or c <= 0:
#             raise ValueError("С отрицательными числами ничего не выйдет!")
#
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
#             return "Ура, можно построить треугольник!"
#         else:
#             return "Жаль, но из этого треугольник не сделать"
#
# triangle_checker1 = TriangleChecker(3, 4, 5)
# print(triangle_checker1.is_triangle())  # Ура, можно построить треугольник!
#
# triangle_checker2 = TriangleChecker(1, 2, 5)
# print(triangle_checker2.is_triangle())  # Жаль, но из этого треугольник не сделать
#
# try:
#     triangle_checker3 = TriangleChecker(-1, 2, 3)
# except ValueError as e:
#     print(e)  # С отрицательными числами ничего не выйдет!
#
# 2) Задача
# Есть Помидор со следующими характеристиками:
# 1. Индекс
# 2. Стадия зрелости(стадии: Отсутствует, Цветение, Зеленый, Красный)
# Помидор может:
# 1. Расти (переходить на следующую стадию созревания)
# 2. Предоставлять информацию о своей зрелости
# Есть Куст с помидорами, который:
# 1. Содержит список томатов, которые на ней растут
# И может:
# 1. Расти вместе с томатами
# 2. Предоставлять информацию о зрелости всех томатов
# 3. Предоставлять урожай
# И также есть Садовник, который имеет:
# 1. Имя
# 2. Растение, за которым он ухаживает
# И может:
# 1. Ухаживать за растением
# 2. Собирать с него урожай
# Задание:
#  Класс Tomato
# 1. Создайте класс Tomato
# 2. Создайте статический атрибут states, который будет содержать все стадии созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два приватных атрибута:
#  1) _index - передается параметром и 2) _state - принимает первое значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра количество томатов
# и на его основе будет создавать список объектов класса Tomato. Данный список будет храниться внутри атрибута tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая
# Класс Gardener
# 1. Создайте класс Gardener
# 2.Создайте метод __init__(), внутри которого будут определены два атрибута:
#  1) name - передается параметром, является публичным и 2) _plant - принимает объект класса TomatoBush, является приватным
# 3.Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
# 4.Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай.
# Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.
# Тесты (main)
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай

# class Tomato:
#     states = {0: "Отсутствует", 1: "Цветение", 2: "Зеленый", 3: "Красный"}
#
#     def __init__(self, index):
#         self._index = index
#         self._state = 0
#
#     def grow(self):
#         if self._state < 3:
#             self._state += 1
#
#     def is_ripe(self):
#         if self._state == 3:
#             return True
#         return False
#
#
# class TomatoBush:
#     def __init__(self, num):
#         self.tomatoes = [Tomato(i) for i in range(0, num)]
#
#     def grow_all(self):
#         for tomato in self.tomatoes:
#             tomato.grow()
#
#     def all_are_ripe(self):
#         return all([tomato.is_ripe() for tomato in self.tomatoes])
#
#     def give_away_all(self):
#         self.tomatoes = []
#
#
# class Gardener:
#     def __init__(self, name, plant):
#         self.name = name
#         self._plant = plant
#
#     def work(self):
#         self._plant.grow_all()
#
#     def harvest(self):
#         if self._plant.all_are_ripe():
#             self._plant.give_away_all()
#         else:
#             print("Томаты еще не дозрели!")
#
#     @staticmethod
#     def knowledge_base():
#         print("Справка по садоводству")
#
#
#
# Gardener.knowledge_base()
# bush = TomatoBush(4)
# gardener = Gardener("Bob", bush)
# gardener.work()
# gardener.harvest()
# gardener.work()
# gardener.harvest()

# 3) Создайте систему управления банковскими счетами, которая позволяет создавать,
# управлять и выполнять операции с банковскими счетами различных клиентов.
# 1. Реализуйте класс Client, представляющий клиента банка.
# Класс должен иметь атрибуты name (имя клиента) и id (уникальный идентификатор клиента).
# 2. Реализуйте класс BankAccount, представляющий банковский счет.
# Класс должен иметь атрибуты account_number (номер счета),
# balance (баланс счета) и client (объект типа Client, которому принадлежит счет).
# Класс также должен иметь методы deposit(amount) и withdraw(amount),
# которые позволяют пополнить или снять деньги со счета.
# 3. Реализуйте класс Bank, представляющий банк. Класс должен иметь атрибут accounts,
# который является словарем, где ключами являются номера счетов, а значениями - объекты типа BankAccount.
# Класс также должен иметь методы create_account(client, initial_balance) для создания нового счета
# и get_account(account_number) для получения счета по его номеру.
# 4. Добавьте в класс Bank методы для выполнения переводов между счетами
# (transfer(sender_account, receiver_account, amount)),
# а также для получения общего баланса клиента (get_total_balance(client)),
# который включает сумму денег на всех его счетах.
# 5. Реализуйте обработку ошибок, например, недостаточно средств на счете при снятии денег
# или отсутствие счета при переводе.
#
# class Client:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
# class BankAccount:
#     def __init__(self, account_number, client):
#         self.account_number = account_number
#         self.balance = 0
#         self.client = client
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         else:
#             raise ValueError("Сумма должна быть положительной")
#
#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#             else:
#                 raise ValueError("Недостаточно средств на счете")
#         else:
#             raise ValueError("Сумма должна быть положительной")
#
# class Bank:
#     def __init__(self):
#         self.accounts = {}
#
#     def create_account(self, client, initial_balance):
#         account = BankAccount(len(self.accounts) + 1, client)
#         account.deposit(initial_balance)
#         self.accounts[account.account_number] = account
#         return account
#
#     def get_account(self, account_number):
#         if account_number in self.accounts:
#             return self.accounts[account_number]
#         else:
#             raise ValueError("Счет не найден")
#
#     def transfer(self, sender_account, receiver_account, amount):
#         sender = self.get_account(sender_account)
#         receiver = self.get_account(receiver_account)
#         sender.withdraw(amount)
#         receiver.deposit(amount)
#
#     def get_total_balance(self, client):
#         total_balance = 0
#         for account in self.accounts.values():
#             if account.client.id == client.id:
#                 total_balance += account.balance
#         return total_balance
#
# bank = Bank()
#
# client1 = Client("Alex Sun", 1)
# client2 = Client("Vasya Krug", 2)
#
# account1 = bank.create_account(client1, 1000)
# account2 = bank.create_account(client2, 500)
#
# account1.deposit(500)
# account2.withdraw(200)
#
# bank.transfer(account1.account_number, account2.account_number, 300)
#
# total_balance_client1 = bank.get_total_balance(client1)
# total_balance_client2 = bank.get_total_balance(client2)
#
# print("Общий баланс для клиента 1:", total_balance_client1)
# print("Общий баланс для клиента 2:", total_balance_client2)
#
# 4) Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
# По умолчанию name = Ivan, age = 18, groupNumber = 10A.
# Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber.
# Метод getName нужен для получения данных об имени конкретного студента,
# метод getAge нужен для получения данных о возрасте конкретного студента,
# vетод setGroupNumberнужен для получения данных о номере группы конкретного студента.
# Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию,
# метод setGroupNumber позволяет изменить номер группы установленный по умолчанию.
# В программе необходимо создать пять экземпляров класса Student, установить им разные имена,
# возраст и номер группы.

# class Student:
#     def __init__(self, name="Ivan", age=18, groupNumber="10A"):
#         self.name = name
#         self.age = age
#         self.groupNumber = groupNumber
#
#     def getName(self):
#         return self.name
#
#     def getAge(self):
#         return self.age
#
#     def getGroupNumber(self):
#         return self.groupNumber
#
#     def setNameAge(self, name, age):
#         self.name = name
#         self.age = age
#
#     def setGroupNumber(self, groupNumber):
#         self.groupNumber = groupNumber
#
# students = [Student() for _ in range(5)]
#
# for i, student in enumerate(students):
#     student.setNameAge(f"Student{i+1}", 18+i)
#     student.setGroupNumber(f"{i+1}A")
#
# for student in students:
#     print(f"Name: {student.getName()}, Age: {student.getAge()}, Group Number: {student.getGroupNumber()}")


# 5)
# Создайте простую веб-страницу для представления вашего любимого книжного произведения.
# Используйте HTML для структуры и оформления текста.
# Создайте базовую структуру HTML-страницы:
# Добавьте теги <html>, <head> и <body>.
# В <head> укажите заголовок страницы с названием вашего любимого произведения.
# Разделите текст на следующие секции:
# Введение: краткое описание произведения и его автора.
# Основная часть: извлеките несколько цитат или ключевых моментов из книги.
# Заключение: поделитесь своими мыслями о произведении.
# Используйте различные HTML-теги для оформления текста:
#
# Заголовки <h1>, <h2>, <h3> для разделов.
# Параграфы <p> для текста.
# Выделите ключевые фразы с помощью тега <strong> или <em>.
# Добавьте изображение обложки книги:
#
# Используйте тег <img> для вставки изображения.
# Укажите атрибут src для пути к изображению.
# Добавьте ссылку на страницу автора или на официальный сайт произведения:
#
# Используйте тег <a> для создания ссылки.
# Укажите атрибут href для указания URL.
# #
#
# 6) Вы идете в путешествие, надо подсчитать сколько у денег у каждого студента.
# Класс студен описан следующим образом:
# class Student:
# def __init__(self, name, money):
# 	self.name = name
# 	self.money = money
#

# class Student:
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#
# students = [
#     Student("Студент 1", 100),
#     Student("Студент 2", 200),
#     Student("Студент 3", 150),
#     Student("Студент 4", 180),
#     Student("Студент 5", 210),
# ]
#

# for student in students:
#     print(f"{student.name} имеет {student.money} денег.")

#
# 7) Создайте класс Students, содержащий поля: фамилия и инициалы, номер группы,
# успеваемость (список из пяти элементов).
# Создать класс School:
# Добавить возможно для добавления студентов в школу
# Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6.
# Добавить возможность вывода учеников заданной группы
# Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7)



# 8) Создайте класс Робот
# создайте 2 типа оружия: меч, автомат
# Создайте 2 типа амуниции: броня, шлем
# Добавьте оружию и амуниции свои характеристики(например урон, прочность)
# Создайте своего робота с каким либо оружием
# (может быть несколько и брони может быть несколько. Также может быть ничего)
# Выведите весь арсенал робота на экран

# class Weapon:
#     def __init__(self, name, damage):
#         self.name = name
#         self.damage = damage
#
# class Armor:
#     def __init__(self, name, durability):
#         self.name = name
#         self.durability = durability
#
# class Robot:
#     def __init__(self, name):
#         self.name = name
#         self.weapons = []
#         self.armors = []
#
#     def add_weapon(self, weapon):
#         self.weapons.append(weapon)
#
#     def add_armor(self, armor):
#         self.armors.append(armor)
#
#     def show_arsenal(self):
#         print(f"Арсенал робота {self.name}:")
#         print("Оружие:")
#         for weapon in self.weapons:
#             print(f"  {weapon.name} (Урон: {weapon.damage})")
#         print("Броня:")
#         for armor in self.armors:
#             print(f"  {armor.name} (Прочность: {armor.durability})")
#
#
#
# robot = Robot("Lyntik")
#
# sword = Weapon("Меч", 50)
# gun = Weapon("Автомат", 100)
#
# armor = Armor("Броня", 200)
# helmet = Armor("Шлем", 100)
#
# robot.add_weapon(sword)
# robot.add_weapon(gun)
# robot.add_armor(armor)
# robot.add_armor(helmet)
#
# robot.show_arsenal()


# 9) Создать 4 фрукта.
# Апельсин, яблоко, мандарин, банан
# У всех фруктов есть сорт, список витаминов, цена, имя
# У апельсина, мандарина, банана есть метод очистить
# У яблока метод порезать
# У банана есть характеристика: кол-во калия
# Создать 4 объекта фрукта и использовать все доступные методы и характеристики
# При вызове метода очистить, должно писаться имя фрукта
# Например:
# apple = Apple("sort", [a,b,c], 120, "apple")
# apple.clear()
# >>"apple очищен"


# class Fruit:
#     def __init__(self, sort, vitamins, price, name):
#         self.sort = sort
#         self.vitamins = vitamins
#         self.price = price
#         self.name = name
#
# class Orange(Fruit):
#     def clear(self):
#         print(f"{self.name} очищен")
#
# class Apple(Fruit):
#     def cut(self):
#         print(f"{self.name} порезан")
#
# class Mandarin(Fruit):
#     def clear(self):
#         print(f"{self.name} очищен")
#
# class Banana(Fruit):
#     def __init__(self, sort, vitamins, price, name, potassium):
#         super().__init__(sort, vitamins, price, name)
#         self.potassium = potassium
#
#     def clear(self):
#         print(f"{self.name} очищен")
#
# orange = Orange("sort1", ["A", "B", "C"], 100, "orange")
# apple = Apple("sort2", ["A", "D", "E"], 120, "apple")
# mandarin = Mandarin("sort3", ["A", "B", "C", "E"], 80, "mandarin")
# banana = Banana("sort4", ["B", "C", "K"], 150, "banana", 450)
#
# orange.clear()
# apple.cut()
# mandarin.clear()
# banana.clear()
#
# print(f"Количество калия в банане: {banana.potassium}")
