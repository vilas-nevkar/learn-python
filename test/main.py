import builtins
import requests
#
# for i in dir(builtins):
#     print(i)

resp = requests.get('https://www.programiz.com/python-programming/methods/built-in/hasattr')
print(dir(resp))
if hasattr(resp, 'status_code'):
    print(type(resp.status_code))


class Student:

    def age(self):
        pass

s = Student()

print(s.__doc__)
print(getattr(s, 'age'))