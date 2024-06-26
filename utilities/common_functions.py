import os

def get_parent_framework_path():
    current_path = os.getcwd()
    get_parent = os.path.dirname(current_path)
#incase test run azure pipeline test machine
    # if "\\ET-catolog\\Hpone\\src\\test\\hponeauto" not in get_parent:
    #     return os.path.join(current_path, 'ET-catolog', 'Hpone', 'src', 'test', 'hponeauto')
    return get_parent

print(get_parent_framework_path())