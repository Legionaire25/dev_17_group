# class Point:
#     color = 'red'
#     circle = 2
#     x = 1
#     y =2
#
#     def __init__(self):
#         print('вызов ___init___')
#         self.x = 0
#         self.y = 0
#
#     def __del__(self):
#         print(f'удаление экземпляра {self}')
#
#
#     # def set_coords(self, x, y):
#     #     self.x = x
#     #     self.y = y
#
#     # def get_coords(self):
#     #     return self.x, self.y
#
# point = Point()
# print(point.__dict__)
# # point.set_coords(1, 2)
# # print(point.get_coords())
# # print(point.__dict__)
# print(Point.__dict__)

# new -> объект класса -> init

# class Point:
#
#
#     def __new__(cls, *args, **kwargs):
#         print(f'вызов для {cls}')
#         return super().__new__(cls)
#
#     def __init__(self):
#         print('вызов ___init___')
#         self.x = 0
#         self.y = 0
#
# point = Point(1, 2)
# print(point)

class Counter:

    def __init__(self):
        self.__counter = 0

    def __init__(self, *args, **kwargs):
        print('__call__')
        self.__counter += 1
        return self.__counter

c = Counter()
c2 = Counter()
c()
c()
c()
result = c()
c2()
c2()
result2 = c2
print(result2)
print(result)