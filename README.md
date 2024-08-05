# Video Game Sales
<br/>


## **Getting the Project to Run**

1. Install Python3: Ensure you have Python3 insalled on your computer. Use 'pip install --upgrade pip' to update pip if neccessary.
2. Clone the Respository: Download or clone the repository from Github to a place you can find it specifically.
3. Set Up a Virtual Environment:
* Navigate to the cloned repository folder using your file explore.
* Open a command terminal by typing 'cmd' into the file path line.
* Create a virtual enviroment by running: 'py -m venv env'. This creates a folder named 'env' within your repository to house the virtual environment.
* Activate the virtual environment by running: '.\env\Scripts\activate' (on Windows) or 'source env/bin/activate (on macOS/Linux). You will see '(env)' preceding your directory path, indicating that the virtual environment is active.
4. Install Project Dependencies: Ensure you are in the project directory and install the required packages by running: 'pip install -r requirements.txt'. This will install the neccessary libraries for the project, which includes:
* 'numpy'
* 'pandas'
* 'matplotlib'
5. Run the Program: Execute the program by typing: 'python vgproject.py' in the command terminal.
6. Deactivate the Virtual Environment: After you are finished with the program, deactivate the virutal environemnt by running: 'deactivate' in the command terminal.
<br/>

## **Requirements Met**
<br/>

This project incorporates the following Code Louisville requirements:
1. Read two data files: The project reads two data files.
2. Data Cleaning and Merging: Clean the data and perform a pandas merge on the datasets, then calculate new values based on the merged data.
3. Visualizations: Create three visualizations using 'matplotlib' or 'seaborn' to display the data.
4. Data Dictionary: Build a custom data dictionary and include it in your README file.
5. Code Annotation: Annotate your code with markdown cells in a Jupyter Notebook.

| Title | Genre | Publisher |
|:--------:|:--------:|:--------:|
|  The title of the game   |  The genre the game's story  |  The entity responsible for creating the game |

| Platform | Year/release_date | NA_Sales |
|:--------:|:--------:|:--------:|
|  The console the game is designed for   |  The year orday the game was released   |  The number of copies sold in North America   |