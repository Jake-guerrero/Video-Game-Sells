# Video Game Sales

## **Getting the Project to Run**

1. Make sure to have a version of Python3 installed on your computer. Use pip install -- update pip if you have not done so already.
2. After you have downloaded Python, clone the repository from GitHub.
3. Within your cloned repository, it is best practice to setup a virtual enviroment(venv). This allows you to install any project requirements without interfering with what you currently have installed. To set up the venv, from within the cloned repo folder navigate to the file path line. Here you will type "cmd" into the file path to bring up the commnad terminal. From there run, "py -m venv env". This will create a folder named "env" within your repo folder. This will house the python venv. Once you have that created, you will need to activate it. Run ".\env\Scripts\activate" from the command terminal. You will know your venv is active when you see (env) ahead of your directory path. Now your venv is ready to use.
4. From within that directory pip install the requirements.txt file by running "pip install -r requirements.txt". This will make sure you have the necessary pacages to run the program. For this program, we will be using these libraries:
* Numpy
* Pandas
* Matplotlib Pyplot
5. Now you have installed the packages and you are in the directory, you can run the program directly from the command terminal by running "Vide Games.ipynb".
6. Once you are finished with the program, make sure you deactivate your venv. Run "deactivate" from the command terminal with the project directory.