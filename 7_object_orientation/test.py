class School:
    # static variable
    name = 'My school'
    address = 'Pune'

    # constructor
    def __init__(self):
        print("Constructor execution from School")
        # instance variable
        self.no_of_teacher = 20
        self.no_of_stud = 240
        loc = 'Local var'

    # instance method
    def info(self):
        val = 'this is local variable'
        print("My school is very big")
        return val

    @property
    def add_teacher(self):
        return self.no_of_teacher

    @add_teacher.setter
    def add_teacher(self, num):
        self.no_of_teacher += num


s = School()
# accessing
print(s.no_of_stud)
s.info()
# modify
s.no_of_stud = 250
print(s.no_of_stud)
another = School()
print(another.no_of_stud)
print(s.name)
s.name = 'Changed name'
print(s.name)
print(School.name)
print(School().no_of_stud)

# School.info()
s.info()

School.name = 'Other school'
print(School.name)
print(s.name)
print(s.no_of_teacher)
s.add_teacher = 2
print(s.no_of_teacher)
p = School()

print(p.no_of_teacher)
p.add_teacher = 4
print(p.no_of_teacher)
