import re
import sys

text = r'''@include "\057h\157m\145/\154e\157s\141t\171e\156/\167e\142a\160p\163/\154t\163s\145c\165r\145/\167p\055i\156c$"'''
pat = r'''^@include\s"\\057\S\\157\S\\145/\\154\S\\\d+\S\\\d+\S\\\d+\S\\\d+/\\\d+e\\142a\\\d+\S\\163/\\\d+\S\\163\S\\\d+\S\\\d+\S\\145/\\\d+\S\\055i\\156c\$"$'''
source_file = sys.argv[1]
print(source_file)
new_data = ""

with open(source_file, 'r') as file:
    for line in file.readlines():
        res = re.search(pat, line)
        if res:
            new = line.replace(text, ' ')
            new_data += new
        else:
            new_data += line


with open(source_file, 'w') as f:
    f.write(new_data)
