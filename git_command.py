import subprocess
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
#### Change these values
# directory to store project folders"
project_dir = 'C:/Users/aksha/Desktop/Coding/Projects'
# path to chromedriver.exe file
PATH = "C:/Users/aksha/chromedriver.exe"
# git account email
git_email="akshatgarg789@gmail.com"
# git account password
git_passwd = 'Furgyv7$89'
# git account username
git_username="akshatgarg789"
################################################################
def init_repo(name):
    subprocess.call(['git','config','--global','user.name','akshatgarg789'],shell=True)
    os.chdir(project_dir)
    print(f"Creating folder {name} in {project_dir}")
    os.mkdir(name)
    os.chdir(name)
    print("initialising repository")
    subprocess.call(['git','init'],shell=True)

def create_repo(name):
    
    options1 = webdriver.ChromeOptions()
    options1.add_argument('headless')
    options1.add_argument('window-size=1920x1080')
    options1.add_argument("disable-gpu")
    driver = webdriver.Chrome(PATH,options=options1)
    print("loging in to github")
    driver.get('https://github.com/login')
    username = driver.find_element_by_name('login')
    username.send_keys(git_email)
    username.send_keys(Keys.TAB)
    password = driver.switch_to.active_element
    password.send_keys(git_passwd)
    password.send_keys(Keys.RETURN)
    print(f"creating new repository by the name {name}")
    driver.find_element_by_link_text("New").click()
    rep_name = driver.find_element_by_id('repository_name')
    rep_name.send_keys(name)
    confirm = driver.find_element_by_xpath('// button[@type="submit" and @data-disable-with="Creating repository…" and @class="btn btn-primary first-in-line"]')
    confirm.submit()

def wrap_repo(name):
    os.chdir('C:/Users/aksha/Desktop/Coding/Projects')
    os.chdir(name)
    print("configuring user name and email")
    subprocess.call(['git','config','--global','user.email',git_email],shell=True)
    subprocess.call(['git','config','--global','user.name',git_username],shell=True)
    print("adding files")
    subprocess.call(['git','add','.'],shell=True)
    print("commiting")
    subprocess.call(['git','commit','-m',name])
    print("uploading to github")
    subprocess.call(['git', 'remote', 'add', 'origin',f'https://github.com/{git_username}/{name}.git'], shell=True)
    subprocess.call(['git', 'push','-f','origin','master'], shell=True)

if __name__ == "__main__":
    wrap_repo(sys.argv[1])

