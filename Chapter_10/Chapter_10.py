#1
class Thing():
    pass


print(Thing)

example = Thing()
print(example)


#2
class Thing2():
    letters = 'abc'


print(Thing2.letters)


#3
class Thing3():
    def __init__(self):
        self.letters = 'xyz'


thing = Thing3()
print(thing.letters)


#4
class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    # 6
    def dump(self):
        print('№6 name =', self.name, 'symbol =', self.symbol, 'number =', self.number)

    # 7
    def __str__(self):
        return '№7 ' + self.name + ' ' + self.symbol + ' ' + str(self.number)

    # 8
    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number


element = Element('Hydrogen', 'H', 1)
print(element.name, element.symbol, element.number)


#5
dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
print(dict)

hydrogen = Element(**dict)
print(hydrogen.name, hydrogen.symbol, hydrogen.number)


#6
hydrogen.dump()


#7
print(hydrogen)


#8
print('№8')
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)


# 9
class Bear():
    def eats(self):
        return 'berries'


class Rabbit():
    def eats(self):
        return 'clover'


class Octothorpe():
    def eats(self):
        return 'campers'


bear = Bear()
print(bear.eats())
rabbit = Rabbit()
print(rabbit.eats())
octothorpe = Octothorpe()
print(octothorpe.eats())


# 10
class Laser():
    def does(self):
        return 'disintegrate'


class Claw():
    def does(self):
        return 'crush'


class SmartPhone():
    def does(self):
        return 'ring'


class Robot():
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        return f"""\n{self.laser.does()} \
                    \n{self.claw.does()} \
                    \n{self.smartphone.does()}
                """


robot = Robot()
print(robot.does())
