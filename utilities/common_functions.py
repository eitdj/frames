import os


def get_parent_framework_path():
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    #incase test run azure pipeline test machine
    if "\\reports" not in parent_path:
        return os.path.join(current_path,'reports')
    return parent_path


print(get_parent_framework_path())
