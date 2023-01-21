import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
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
        if key in file1.keys() and file2[key] != file1[key] or key not in file1.keys():
            diff[f" + {key}"] = value_2     
    sort_diff = sorted(diff.items(), key=lambda x: x[0][2:])
    return str(json.dumps(dict(sort_diff), indent=4)).replace('"', '')
