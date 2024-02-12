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
