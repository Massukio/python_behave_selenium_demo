# python_behave_template
Selenium webdriver , python , behave

# Website
This repository is part of all tutorials on [ Selenium Framework ](http://www.seleniumframework.com)  

# Usage  
1. If you do not know how to use git, click "Download zip" option at right corner  
2. For Git users, git clone  
3. Install Python 2.7 or higher. Follow this [ Install Python ](http://www.seleniumframework.com/python-basic/what-is-python/)  
4. Install behave. Follow this [ Install behave ] (http://www.seleniumframework.com/python-basic/what-is-behave/) 
5. Complete installing Selenium webdriver components **Pending notes**
6. Open a shell/command prompt and from the root folder run "behave features --no-capture"  
7. Run behave with "-v" gives verbose log. For example running headless using phantomjs with -v creates ghostdriver.log  


# Pycharm Community Edition
To run the Behave features in Pycharm, you need to setup Run/Debug configurations first:
1. Script: put dot (.) in here [this way PyCharm recognizes the configuration as valid and doesn't show red cross mark]
2. Working Directory points to the dirctory where .feature file is
3. Interpreter options: -m behave
Reference: https://stackoverflow.com/questions/15860074/pycharm-how-to-run-behave-exe

Or you can just run features in command line:
>> behave [params] [*.feature]

If command lines aren't colored, read this issue and resolution:
https://github.com/Microsoft/WSL/issues/1173
