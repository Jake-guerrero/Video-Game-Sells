# Video Game Sales
<br/>


## **Getting the Project to Run**

1. Make sure to have a version of Python3 installed on your computer. Use pip install -- update pip if you have not done so already.
2. After you have downloaded Python, clone the repository from GitHub.
3. Within your cloned repository, it is best practice to setup a virtual enviroment(venv). This allows you to install any project requirements without interfering with what you currently have installed. To set up the venv, from within the cloned repo folder navigate to the file path line. Here you will type "cmd" into the file path to bring up the commnad terminal. From there run, "py -m venv env". This will create a folder named "env" within your repo folder. This will house the python venv. Once you have that created, you will need to activate it. Run ".\env\Scripts\activate" from the command terminal. You will know your venv is active when you see (env) ahead of your directory path. Now your venv is ready to use.
4. From within that directory pip install the requirements.txt file by running "pip install -r requirements.txt". This will make sure you have the necessary pacages to run the program. For this program, we will be using these libraries:
* Numpy
* Pandas
* Matplotlib Pyplot
5. Now you have installed the packages and you are in the directory, you can run the program directly from the command terminal by running "Vide Games.py".
6. Once you are finished with the program, make sure you deactivate your venv. Run "deactivate" from the command terminal with the project directory.
<br/>

## **Requirements Met**
<br/>

This project incorporates the following Code Louisville requirements:
1. Read two data files.
2. Clean your data and perform a pandas merge with your two data sets, then calculate some new values based on the new data set.
3. Make 3 matplotlib or seaborn visualizations to display your data.
4. Build a custom data dictionary and include it either in your README.
5. Annotate your code with markdown cells in Jupyter Notebook.
Also includes instructions on how to set up virtual environment set up to run the project.

| Title | Genre | Publisher |
|:--------:|:--------:|:--------:|
|  The title of the game   |  The genre the games story is based off of.  |  The people who made the game. |

| Platform | Year/release_date | NA_Sales |
|:--------:|:--------:|:--------:|
|  The console the game was made to be played on.   |  The year/day the game was released.   |  The amount of copies sold in North America   |