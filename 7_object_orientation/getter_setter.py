
# non pythonic implementation


class Geek:
    def __init__(self, age=0):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value


anurag = Geek(30)
print(anurag.get_age())
anurag.set_age(50)
print(anurag.get_age())
vilas = Geek(40)
print(vilas.get_age())
vilas.set_age(41)
print(vilas.get_age())


class PropertyGeek:

    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value


pg = PropertyGeek(12)
print(pg.age)
pg.age = 15
print(pg.age)


class Robot:
    def __init__(self, name, build_year, lk=0.5, lp=0.5):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
            return "I feel miserable"
        elif s <= 0:
            return "I feel bad!"
        elif s <= 0.5:
            return "Could be worse!"
        elif s <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"


x = Robot("Marvin", 1979, 0.2, 0.4)
y = Robot("Caliban", 1993, -0.4, 0.3)
print(x.condition)
print(y.condition)