# Create
## Prerequisites
1. Install <a href="https://chromedriver.chromium.org/">chrome web driver</a> 
2. python modules <a href="https://pypi.org/project/subprocess.run/">subprocess</a>,<a href="https://pypi.org/project/selenium/">Selenium</a>
## How to Install
1. Clone this repo by typing `git clone http://github.com/akshatgarg789/Create`
2. Change into the directory by typing `cd Create`
3. open the `.py` files with your preferred text editor
4. in git_command.py and create.py change the values given under `# Change these values`

<b>NOTE:   Don't change `line 22` in create.py</b>

5. Now install it as a module by typing `python setup.py sdist`
6. then type `python setup.py install`
## How to use
1. simply go to terminal and type `python -m create <project name>`
2. you will have a project created by the name of `project name` in your `project_folder`
3. After you have written your code go to `setup.py` and change the python modules on `line 21` according to your project
4. Change the README.md file according to your project
4.  Now go to terminal and type `python -m github_command <project name>`
### That's it your coding project is now uploaded to github