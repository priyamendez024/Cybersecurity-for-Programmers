import os

def list_dir(user_path):
    command = "ls " + user_path
    os.system(command)

path = input("Enter directory path: ")
list_dir(path)