from os import listdir
from os.path import isfile, isdir, join

class Directory:
    def __init__(self, path):
        self.path = path

    def get_children(self):
        return listdir(self.path)

    def new_directory(self, child):
        full_path = join(self.path, child)
        if isdir(full_path):
            return Directory(full_path)

    def __str__(self):
        return "Directory(" + self.path + ")"



d = Directory("/home/pi/Documents")
print(d.get_children())

new_d = d.new_directory("Zeyn")
print(new_d)

print(new_d.get_children())
