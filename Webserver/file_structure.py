from os import listdir
from os.path import isfile, isdir, join

class Tree:
    def __init__(self, path):
        self.path = path

    def get_children(self):
        return listdir(self.path)

    def new_tree(self, child):
        full_path = join(self.path, child)
        if isdir(full_path):
            return Tree(full_path)