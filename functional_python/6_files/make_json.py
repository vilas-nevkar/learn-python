import re
import json


output_dict = dict()
ser_func_pattern = re.compile(r"""(?P<success>(?P<key>Hyperverge Response)\s\|\s(?P<value>\{"success.*"}"}))""")
file_name = "doc_service_logs.logs"
with open(file_name, 'r') as log_file:
    content = log_file.readlines()
    for line in content:
        res = re.search(ser_func_pattern, line)
        if res:
            success = {res.groupdict()['key']: res.groupdict()['value']}
            print(success)
            output_dict.update(success)

result = json.dumps(output_dict, indent=4, sort_keys=True)
print(result)
