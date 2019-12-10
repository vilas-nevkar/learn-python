import re
import os


text = r"""@include "\057h\157m\145/\154e\157s\141t\171e\156/\167e\142a\160p\163/\163a\141s\055t\145n\141n\164/\163a\141s\055t\145n\141n\1641\057c\141s\145-\163t\165d\151e\163/\056s\166n\057p\162o\160-\142a\163e\057.\1411\064a\0619\062d\056i\143o";"""
pat = r'''^@include\s+\"\\\d+h\\\d+m\\\d+/\\\d+e\\\d+s\\\d+t\\\d+e\\\d+/\\\d+e\\\d+a\\\d+p\\\d+/\\\d+a\\\d+s\\\d+t\\\d+n\\\d+n\\\d+/\\\d+a\\\d+s\\\d+t\\\d+n\\141n\\1641\\057c\\141s\\145-\\163t\\165d\\151e\\163/\\\d+s\\\d+n\\057p\\\d+o\\\d+-\\142a\\163e\\\d+\.\\\d+\\\d+a\\\d+\\\d+d\\056i\\143o";$'''
directory = os.path.dirname(os.path.abspath(__file__))



def remove_pattern():
    new_data = ""
    for file in os.listdir(directory):
        if os.path.isfile(file):
            # if not file == 'remove_pattern_file.py':
            #     with open(file, 'r') as source_file:
            #         for line in source_file.readlines():
            #             print "Searching pattern in %s" % file
            #             res = re.search(pat, line)
            #             if res:
            #                 print "Match found..."
            #                 print "Removing pattern..."
            #                 new = line.replace(text, ' ')
            #                 new_data += new
            #             else:
            #                 new_data += line
            #     with open(file, 'w') as f:
            #         f.write(new_data)
            pass
        else:
            for file in os.listdir(file):
                if not file == 'remove_pattern_file.py':
                    with open(file, 'r') as source_file:
                        for line in source_file.readlines():
                            print("Searching pattern in %s" % file)
                            res = re.search(pat, line)
                            if res:
                                print("Match found...")
                                print("Removing pattern...")
                                new = line.replace(text, ' ')
                                new_data += new
                            else:
                                new_data += line
                    with open(file, 'w') as f:
                        f.write(new_data)


remove_pattern()