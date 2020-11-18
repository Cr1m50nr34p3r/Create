import sys,os
from os import path 
import git_command
import subprocess
##### Change these values
# author name
full_name = "Akshat Garg"
# author email
email="akshatgarg789@gmail.com"
###########################################################
code = "C:/Program Files/Microsoft VS Code/Code.exe"
name=sys.argv[1]
git_command.init_repo(name)
print("creating README.md")
with open('README.md','w') as readme:
    readme.write(f'# {name}')
print("creating setup.py")
with open('setup.py','w') as setup:
    #change py_modules to a list containing name of python files
    setup.write(f"""from distutils.core import setup
setup(
    name= "{name.lower()}",
    version = '1.0.0',
    py_modules = [],
    author='{full_name}',
    author_email='{email}'
)""")
git_command.create_repo(name)
print("opening vscode")
subprocess.Popen([code,'.'],cwd=f"C:/Users/aksha/Desktop/Coding/Projects/{name}")
