# Movie Ticket Info Project

 I see a lot of movies in theaters. Since 2012, I've logged the information from the ticket stubs of every movie into a Google Sheets file. This project reads the data from the Google Sheets URL and converts it into a Pandas dataframe for manipulation and analysis. 

# Data used in Movie Ticket Info Project:
- Year - The year in which a movie was seen. 
- Title - The title of the movie seen.
- Theater - Name of the theater at which the movie was seen
- Day of the Week - Day on which the movie was seen. Ex. Monday
- Date - The year/month/day of which the movie was seen.
- Time - The start time of the movie. 

# System Requirements
- Python v3.10.1
- pandas v1.4.0
- matplotlib v3.5.1
- Active internet connection
  
   
# Instructions
1) Save movies.py to a directory on your local machine.
2) From the command line, navigate to that directory.
2) Create and activate a virtual environment in the directory.
3) Install system requirements: https://pip.pypa.io/en/stable/user_guide/#requirements-files
4) Run 'python movie.py' from the command line.
 

#  Menu Choice Descriptions
## Movie Lookup
- User inputs a movie title, if the title is present in the dataframe, function returns a postive message. If the input is not present, the function returns a negative message.
- Searches by exact spelling and punctuation but not casing.
    - 'Spiderman: No Way Home' will be found. 'Spider man No Way Home' will not be found.
    - 'Lincoln' and 'LiNColN' will both be found.

## Most Recent Movie
- Returns the last movie seen by date/start time from the dataframe. Also returns the number of days ago it was seen. As the data in this project is static, function returns the same movie title everytime. 

## Number of Movies Watched in a Year
- User inputs a year with format 'xxxx' from within range 2012-Current Year. If year exists in the dataframe, returns the number of movies seen that year.
- If input is a year before 2012 or input is not in correct format, function returns an invalid input message.
- If input is the current year but there is no data, returns a corresponding message. 

## Movies by Start Time
- Returns a bar chart of number of movies seen against start times. 

## Movie Suggestions
- User inputs a title suggestion. If the title is not present in the dataframe, function appends the title to an INFO log. If the title is already present, the user is alerted and the title is not logged.

## Random Ticket
- Returns the ticket info for a randomly selected movie in the dataframe.

# Fufilled Requirements
- Category 1
    - Implements a master loop console application. User can enter commands to choose options, exit select options, and exit program
    - Option 2 calculates and displays data based on an external factor (the day the option is called)
    - Option 3 creates lists and a dictionary, and then the dictionary is searched with user input as the key, outputs value back to the user.
    - Option 4 creates lists used to populate chart.
- Category 2
    - This program reads data from an external Google Sheets file in CSV format.
- Category 3
    - Option 1 visualizes data in tabular form.
    - Option 4 visualizes data in a bar chart.
- Category 4
    - This program utilizes a virtual environment and lists dependencies in a requirement.txt file.
    - Movies.py has accompanying test module, Test_movies.py. Test_movies.py includes 4 unit tests and tests the concept of Option 1.
    - Options 1, 3, and 5 utilize INFO logging to track user inputs. 



