class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # self.gotmarks = self.name + ' obtained ' + self.marks + ' marks'

    @property
    def gotmarks(self):
        return self.name + ' obtained ' + self.marks + ' marks'

    @gotmarks.setter
    def gotmarks(self, sentence):
        name, rand, marks = sentence.split(' ')
        self.name = name
        self.marks = marks


st = Student("Jaki", "25")

print(st.name)
print(st.marks)
print(st.gotmarks)

st.name = "Anusha"
print(st.name)
print(st.gotmarks)

st.gotmarks = 'Anurag got 60'
print(st.gotmarks)
print(st.name)
print(st.marks)


######################################################################################

class Student:

    name = 'Anurag'
    age = 30
    school = 'Schoollllll'

    @property
    def display(self):
        print("My name is {} and I am {} years old".format(self.name, self.school))

    @display.setter
    def display(self):
        if self.age == 30:
            self.school = 'Anurag'
        else:
            self.school = 'Abha'


s = Student()
print(s.name)
print(s.age)
s.display
s.age = 60
s.display


########################################################################################


class Person():

    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    @property
    def fullname(self):
        return self.first + ' '+ self.last

    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split()
        self.first = firstname
        self.last = lastname

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

# Init a Person
person = Person('selva', 'prabhakaran')
print(person.fullname)  #> selva prabhakaran
print(person.first)  #> selva
print(person.last)  #> prabhakaran

# Setting fullname calls the setter method and updates person.first and person.last
person.fullname = 'velu pillai'

# Print the changed values of `first` and `last`
print(person.fullname) #> velu pillai
print(person.first)  #> pillai
print(person.last)  #> pillai


# deleter
# Init a Person
person = Person('selva', 'prabhakaran')
print(person.fullname)  #> selva prabhakaran

# Deleting fullname calls the deleter method, which erases self.first and self.last
del person.fullname

# Print the changed values of `first` and `last`
print(person.first)  #> None
print(person.last)  #> None

######################################################################################

import datetime

class Model():

    first_name = 'Anurag'
    last_name = 'Gundappa'
    clock_in = datetime.datetime.time()
    clock_out = datetime.datetime.time()
    total = datetime.datetime.time()
    # full = '{} {}'.format(first_name, last_name)

    @property
    def full(self):
        print('{} {}'.format(self.first_name, self.last_name))

    @full.setter
    def full(self, name):
        first_name, last_name = name.split()
        self.first_name = first_name
        self.last_name = last_name


m = Model()
print(m.first_name)
print(m.last_name)
print(m.full)

m.first_name = 'Aartu'
print(m.first_name)
print(m.last_name)
m.full = 'Abha gundappa'

print(m.first_name)
print(m.last_name)
print(m.clock_in)
print(m.clock_out)
m.full

