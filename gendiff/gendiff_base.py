import json
from os.path import normpath


#fn = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
#fj = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}


def json_to_py(file_path1, file_path2):
    file_path1 = normpath(file_path1)
    file_path2 = normpath(file_path2)
    f1 = json.loads(open(file_path1))
    f2 = json.loads(open(file_path2))
    print(generate_diff(f1, f2))

def generate_diff(file1, file2):
    diff = {}
    for key in file1.keys():
        value_1 = file1[key]
        if key not in file2.keys():
            diff[f" - {key}"] = value_1
        elif value_1 == file2[key]:
            diff[f"   {key}"] = value_1
        else:
            diff[f" - {key}"] = value_1
    
    for key in file2.keys():
        value_2 = file2[key]
        if key in file1.keys() and file2[key] != file1[key]:
            diff[f" + {key}"] = value_2
        elif key not in file1.keys():
            diff[f"   {key}"] = value_2
    sort_diff = sorted(diff.items(), key=lambda x: x[0][2:])
    return str(json.dumps(sort_diff, indent=2).replace('"', ''))
