# Задача №1.
#
# Исходные данные:
# - скрипт task1, который содержит реализацию классов Tank, TankCommander, TankGunner и
# код для проверки результата
#
# Необходимо:
# 1. Реализовать всю необходимую логику так, чтобы скрипт task1 выводил:
#     >>> Test passed. Amazing job!
#
# Желательно:
# 1. Привести альтернативные способы решения задачи.
#
# Примечание:
# - НЕЛЬЗЯ менять реализацию приведенных в исходных данных классов и проверочного кода.
# - Нет ограничений по реализации классов Tankman и Vehicle, а также вспомогательной логики.

class Tank:
    def __init__(self):
        pass

class TankCommander(Tank):
    def __init__(self):
        super().__init__()
        pass

class TankGunner(Tank):
    def __init__(self):
        super().__init__()
        pass

class Vehicle:
    def __init__(self):
        pass


class Tankman:
    pass


def test_task1():
    tankman = Tankman()
    vehicle = Vehicle()

    if isinstance(tankman, Tank) and isinstance(vehicle, Vehicle):
        print("Test passed. Amazing job!")
    else:
        print("Test failed. Keep trying!")

if __name__ == "__main__":
    test_task1()
