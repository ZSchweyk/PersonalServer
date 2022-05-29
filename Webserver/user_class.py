import os



class User:
    def __init__(self, email_address: str):
        self.email_address = email_address

        os.system("mkdir /home/pi/UserFiles/" + self.email_address)