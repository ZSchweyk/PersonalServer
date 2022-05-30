from os import listdir
from os.path import isfile, isdir, join

class Directory:
    def __init__(self, path):
        self.path = path

    def get_children(self):
        dict_to_return = {"folders": [], "files": []}
        for item in listdir(self.path):
            if isdir(item):
                dict_to_return["folders"].append(item)
            elif isfile(item):
                dict_to_return["files"].append(item)
        return dict_to_return

    def enter(self, child):
        full_path = join(self.path, child)
        if child in listdir(self.path) and isdir(full_path):
            return Directory(full_path)
        raise Exception("Not a directory")

    def __repr__(self):
        return "<Directory " + self.path + ">"

    def __str__(self):
        return "<Directory " + self.path + ">"



d = Directory("/home/pi/Documents")
print(d.get_children())

# new_d = d.new_directory("Zeyn")
# print(new_d)
#
# print(new_d.get_children())
