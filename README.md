# Movie Ticket Info Project

 Since 2012, I've into a Google Sheets file. This project is about taking a look at a couple aspects of this information for my own curiousity, but can also tell the user a little bit about me (in data form!). This project has 4 menu options, each of which uses data from a CSV snapshot of a truncated Google Sheets file. The CSV is converted into a Pandas dataframe for manipulation and analysis. 
 

# Data in MovieBoardsDigital.csv 
## Data used in Movie Ticket Info Project:
- Year - The year in which a movie was seen. 
- Title - The title of the movie seen.
- Date - The date (ex. 1/1/2012) on which the movie was seen.
- Time - The start time of the movie

## Data not currently used
- Theater - The name of the theater the movie was seen in.
- Day of the Week - The day of the week (ex. Monday) the movie was seen on.
- Saw with April - Was my wife at the movie (Y) or not (N)

# Necessary Packages/Files
- pandas v1.4.0
- matplotlib v 3.5.1
- MovieBoardsDigital.csv from [https://github.com/jnsage/movies]
 

# Project Menu Option Descriptions
## Option 1 - Movie Lookup
- Requires user input of a movie title. 
- If the input is in the dataframe, project will return a postive message.
- If the input is not in the dataframe, project will return a negative message.
- Searches by exact spelling and punctuation but not casing.
    - 'Spiderman: No Way Home' will be found. 'Spider man No Way Home' will not be found.
    - 'Lincoln' and 'LiNColN' will both be found.

## Option 2 - Most Recent Movie
- Does not require user input.
- Returns last indexed item in the 'Title' column of the dataframe and # of days ago it was seen.
- As data is static, returns same movie title everytime, though the day could change.

## Option 3 - Number of Movies Watched in a Year
- Requires user input of a year format 'xxxx' from 2012-2021.
- If year is in 'Year' column of dataframe, returns # of movies seen that year.
- If year not in 'Year' column of dataframe or is not in correct format, returns an invalid input message.

## Option 4 - Movies by Start Time
- Does not require user input.
- Returns bar chart of number of movies seen against start times.
- As data is static, bar chart should look the same each time.

# Requirements
- Category 1
    - Implements a master loop console application. User can enter commangs to choose options, exit select options, and exit program
    - Option 2 calculates and displays data based on an external factor (the day the option is called)
- Category 2
    - This program reads data from an external CSV file.
- Category 3
    - This program visualizes data in a chart in option 4.
- Category 4
    - This program utilizes a virtual environment and lists dependencies in a requirement.txt file.


