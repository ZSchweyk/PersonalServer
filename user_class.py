from os import listdir, system
from os.path import isfile, isdir, join
from directory_class import Directory


class User:
    def __init__(self, email_address: str):
        self.email_address = email_address
        if not isdir("/home/pi/UserFiles/" + self.email_address):
            system("mkdir /home/pi/UserFiles/" + self.email_address)
        self.directory = Directory("/home/pi/UserFiles/" + self.email_address)

    def add(self):
        pass

    def remove(self):
        pass