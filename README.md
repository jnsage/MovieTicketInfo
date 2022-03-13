# Movie Ticket Info Project

 I see a lot of movies in theaters. Since 2012, I've logged the information from the ticket stubs of every movie into a Google Sheets file. This project uses data from a CSV snapshot of the movie ticket info from 2012-2021. The CSV is converted into a Pandas dataframe for manipulation and analysis. 

# Data used in Movie Ticket Info Project:
- Year - The year in which a movie was seen. 
- Title - The title of the movie seen.
- Theater - Name of the theater at which the movie was seen
- Day of the Week - Day on which the movie was seen. Ex. Monday
- Date - The year/month/day of which the movie was seen.
- Time - The start time of the movie. 

# System Requirements
- Python v 3.10.1
    - logging package
    - unittest package
- pandas v1.4.0
- matplotlib v3.5.1
- MovieBoardsDigital.csv from [https://github.com/jnsage/movies]

# Instructions
1) Save movies.py and MovieBoardsDigital.csv to the same directory on your local machine.
2) From the command line, navigate to that directory.
3) Pip install -r requirements.txt. Virtual environment recommended.
3) Run python movie.py from the command line.
 

#  Menu Options
## Option 1 - Movie Lookup
- User inputs a movie title, if the title is present in the dataframe, function returns a postive message. If the input is not present, the function returns a negative message.
- Searches by exact spelling and punctuation but not casing.
    - 'Spiderman: No Way Home' will be found. 'Spider man No Way Home' will not be found.
    - 'Lincoln' and 'LiNColN' will both be found.

## Option 2 - Most Recent Movie
- Returns the last movie seen by date/start time from the dataframe. Also returns the number of days ago it was seen. As the data in this project is static, function returns the same movie title everytime. 

## Option 3 - Number of Movies Watched in a Year
- User inputs a year with format 'xxxx' from the range 2012-2021. If year is present in the dataframe, returns the number of movies seen that year.
- If the year is not present in the dataframe or is not in correct format, function returns an invalid input message.

## Option 4 - Movies by Start Time
- Returns bar chart of number of movies seen against start times. 

## Option 5 - Movie Suggestions
- User inputs a title suggestion. If the title is not present in the dataframe, function appends the title to an INFO log. If the title is already in the dataframe, the user is alerted and the title is not logged.

# Fufilled Requirements
- Category 1
    - Implements a master loop console application. User can enter commands to choose options, exit select options, and exit program
    - Option 2 calculates and displays data based on an external factor (the day the option is called)
    - Option 3 creates lists and a dictionary, and then the dictionary is searched with user input as the key, outputs value back to the user.
    - Option 4 creates lists used to populate chart.
- Category 2
    - This program reads data from an external CSV file.
- Category 3
    - Option 1 visualizes data in tabular form.
    - Option 4 visualizes data in a bar chart.
- Category 4
    - This program utilizes a virtual environment and lists dependencies in a requirement.txt file.
    - Movies.py has accompanying test module, Test_movies.py. Test_movies.py includes 4 unit tests and tests the concept of Option 1 
    - Options 1, 3, and 5 utilize INFO logging to track user inputs. 



