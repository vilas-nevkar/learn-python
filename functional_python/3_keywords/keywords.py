import keyword

"""
The following list shows the Python 3_keywords. 
These are reserved words and you cannot use them as constant or variable or any other identifier names. 
All the Python 3_keywords contain lowercase letters only except True, False, None.

These 
"""

for key in keyword.kwlist:
    print(key)

print(len(keyword.kwlist))

print(dir(keyword))