import pandas as pd
import numpy as np  
import matplotlib as mpl
import matplotlib.pyplot as plt


# Import MovieBoardsDigital.csv as a DataFrame. Replace the values in the 'Date' and 'Time' columns with a datetime objects.

movie_csv = pd.read_csv('MovieBoardsDigital.csv', parse_dates=['Date','Time'])

# Create new DataFrame where values are sorted by the Date column. This will be used later in 'most_recent()' and 'movie_by_year()' functions.
sorted_by_date = movie_csv.sort_values('Date')


# Create dictionary to be used to create a menu for user input.
menu_options = {1 : 'Movie Check', 2 : "Most Recent Movie", 3 : "Number of Movies Watched in a Year", 4 : 'Movies by Start Time'}
def menu():
    menu_values = []
    for item in menu_options.values():
        menu_values.append(len(item)) 

    max_value_length = max(menu_values) + 10
    print('='*max_value_length)

    for key in menu_options:
        x = max_value_length - len(menu_options[key])
        print(key,"."*(x-3),menu_options[key])    

    print('='*max_value_length)

# Function to look up a user input in the 'Title' column of the DataFrame. Returns affirmative messaging if input is in 'Title'.
# Returns negative statement if input is not in 'Title'
def movie_lookup():
   
    while True:
        movie_check = input("\nEnter a movie title to see if Jared saw it in theaters or 'B' to go back to the main menu.\n")
        if movie_check.lower() == 'b':
            break
        elif movie_check.lower() in movie_csv['Title'].str.lower().values:
            print(f"\nJared has seen {movie_check}")
        else:
            print(f"\nJared hasn't seen {movie_check}")    
    

 # Function that looks up and returns the last value in 'Title' and 'Year' columns from the 'sorted_by_date' DataFrame. 
 # No user input required. Should only return one value.
def most_recent():
    recent_movie = sorted_by_date['Title'].iloc[-1]
    recent_date = sorted_by_date['Date'].iloc[-1]

    #Days between current date and date of last movie seen
    num_days_ago = pd.Timestamp.today() - recent_date
    
    print(f"\nThe last movie Jared saw was {recent_movie}. He saw it {num_days_ago.days} days ago on {recent_date.date()}. \n")

# Function to look up how many movies Jared has seen in a year. Arguement for the year is input by the user.
def movie_by_year():

    # Initialize 2 empty lists and a dictionary.
    year_count = []
    movie_count = []
    by_year_dict = {}
    
    # Add unique values from 'Year' column to 'year_count' list. Add value counts from 'Year' to 'movie_count' list.
    # Convert unique values from 'Year' to string. 
    for item in sorted_by_date['Year'].unique():
        year_count.append(str(item))

    # Sort=False to make sure values counts are returned in the corresponding order as the unique values from 'Year'
    for value in sorted_by_date['Year'].value_counts(sort=False):
        movie_count.append(value)
      
   
    # Populate dictionary using 'year_count' as the keys and 'movie_count' as the values.
    by_year_dict = dict(zip(year_count, movie_count))

    # User inputs a year. If input is a key in 'by_year_dict', return the value. If not a key, then return negative message and restart loop.
    while True: 
        year_input = input("\nEnter a year 2012-2021 or 'B' to go back to the main menu.\n")
        if year_input in by_year_dict:
            print(f"\nJared saw {by_year_dict[year_input]} movies in {year_input}")
        elif year_input.lower() == 'b':
            break
        elif year_input not in by_year_dict:
            print(f"\nInformation for {year_input} could not be found.")
      
# Produce a chart to show how many movies were show in a 3 hour block
def by_time_chart():
    
    # Resample time column into 3 hour blocks starting with 00:00 AM
    resampled_csv = movie_csv.resample('3H', on='Time').count()
    
    # Make new lists that will become x and y values for chart

    time_chart_x = ['12a-2:59a', '3a-5:59a', '6a-8:59a', '9a-11:59a', '12p-2:59p', '3p-5:59p', '6p-8:59p', '9p-11:59p' ]
    time_chart_y = []    

    for value in resampled_csv['Time']:
        time_chart_y.append(value)
    
    print('\nPlease close all charts to continue.')
    
    # Plot bar chart of # of movies seen by time
    plt.figure(figsize=(10.5,5))
    plt.bar_label(plt.bar(time_chart_x,time_chart_y, label='# Of Movies', color='#FFA500', edgecolor='000000'))
    plt.xlabel('Start Time Window')
    plt.ylabel('# of Movies')
    plt.title('# of Movies Watched by Start Time')         
    plt.show()

    
# Function for the main menu seen by qthe user.

def main():
    while True:       
        menu() 
        menu_choice = input("Enter an option 1-4 or 'Q' to quit.\n")
        if menu_choice == '1':
            movie_lookup()
        elif menu_choice == '2':
            most_recent()
        elif menu_choice == '3':
            movie_by_year()
        elif menu_choice == '4':
            by_time_chart()
        elif menu_choice.lower() == 'q':
            break
        else:
            print(f"{menu_choice} was not a valid option. Enter an option 1-4 or 'Q' to quit. ")
        

main()       

print("\nThank you for checking in! Have a nice day")




