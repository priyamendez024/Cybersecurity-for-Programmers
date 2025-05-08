import subprocess, shlex

def safe_list_dir(user_path):
    safe_path = shlex.quote(user_path)
    subprocess.run(["ls", safe_path], check=True)

path = input("Enter directory path: ")
safe_list_dir(path)