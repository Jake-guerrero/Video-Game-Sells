# Video Game Sales
<br/>


This project delves into video game sales, addressing three main questions:
1. How many physical copies of games were sold in 2015?
2. Which publisher had the highest sales?
3. What is the most popular genre in video games total in the dataset?
Using two datasets sourced from Kaggle, I will analyze these questions to create a comprehensive overview of video game sales.

## **Getting the Project to Run**

1. Install Python3: Ensure you have Python3 insalled on your computer. Use '<strong>pip install --upgrade pip</strong>' to update pip if neccessary in the terminal.
2. Clone the Respository: Download or clone the repository from Github to a directory of your choice.
* Find and click on the green "<strong>Code</strong>" button at the top of the repository page, copy the URL, and run the following command in your terminal: "<strong>git clone [URL]</strong>. Replace '<strong>[URL]</strong> with the URL you copied.
3. Set Up a Virtual Environment:
* Navigate to the cloned repository folder using your file explore.
* Open a command terminal by typing 'cmd' into the file path line. On macOS, type the command '<strong>cd</strong>'
* Create a virtual enviroment by running: '<strong>py -m venv env</strong>'. This creates a folder named 'env' within your repository to house the virtual environment.
* Activate the virtual environment by running: '<strong>.\env\Scripts\activate</strong>' (on Windows) or '<strong>source env/bin/activate</strong>' (on macOS/Linux). You will see '<strong>(env)</strong>' preceding your directory path, indicating that the virtual environment is active.
4. Install Project Dependencies: Ensure you are in the project directory and install the required packages by running: '<strong>pip install -r requirements.txt</strong>'. This will install the neccessary libraries for the project, which includes:
* '<strong>numpy</strong>'
* '<strong>pandas</strong>'
* '<strong>matplotlib</strong>'
5. Run the Program: Execute the program by typing: '<strong>python vgproject.py</strong>' in the command terminal. If you are using Python3, execute the program by typing: '<strong>python3 vgproject.py</strong>'.
* If you are not in the video games directory, use the '<strong>cd</strong>' command to go into the Video Game Sales directory.
* When the code is run through powershell, execute the program by typing: <strong>python .\vgproject.py</strong>'.
6. Deactivate the Virtual Environment: After you are finished with the program, deactivate the virutal environemnt by running: '<strong>deactivate</strong>' in the command terminal.

After running the code, three visualizations will appear:
1. <strong>Top Five Games Sold (2015)</strong>: This visual displays the top five games sold in millions for the year 2015.
2. <strong>Top Five Publishers by Game Count</strong>: This visual shows the top five publishers (Activision, Warner Bros. Interactive Entertainment, Take-Two Interactive, Bethesda Softworks, and Electronic Arts) and the percentage of total games each studio has produced.
3. <strong>Total Games by Genre (2015)</strong>: This visual illustrates the number of games made for each genre in 2015.

To navigate through the visuals, close each window using the X button in the top-left or top-right corner of each visuals.

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