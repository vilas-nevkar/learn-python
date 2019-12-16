import re

"""
. = any character and NOT string
^ = start of string
$ = end of string
+ = one or more
* = zero or more
[] = Used to indicate a set of characters. In a set: single character in list
[^] = single character NOT in list
[a-z0-9] = The set of characters can include a range
\d == [0-9] =  whole numbers only 0-9 
[a-z] = alphabets in small notation
() = to focus on group
(?P<name>) = named group having particular name
(?P<=) = 
(?:...) = 
"""

pat = re.compile('^\d+$')
pat = '^\d+[a-z]?$'
pat = '^[a-zA-Z0-9]+@[a-z]+.[a-z]+$'
pat = '\d'
# pat = '\w*'

mobile = '9975753003'
email = 'anurag@gmail.com'
s = 'My 2 favourite numbers are 7 and 10'

print(pat)
print(type(pat))

# re.match
m = re.match(pat, mobile)
m = re.match(pat, email)
print(m)
# group is function of match object on success which gives matched exp
# print(m.group())

# re.findall returns a list of matched characters
m = re.findall(pat, s)

# re.search searches for only first occurrence
m = re.search(pat, s)
print(type(m))
print(m)

