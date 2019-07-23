
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)

    def method2(self):
        pass

    @staticmethod
    def sq(a):
        return a * a

    def method3(self):
        ans = self.sq(23)
        return ans

    @classmethod
    def sample(cls):
        pass


def adder(a, b):
    return a + b


if __name__ == '__main__':
    print('This module is now executing on its own ')
    print(__name__)
    ########

else:
    print("This module is now imported and executed")
    print(__name__)