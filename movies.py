import pandas as pd
import matplotlib.pyplot as plt
import logging
import random 

# Configure Log file
logging.basicConfig(filename='InputLog.log', format='%(funcName)s %(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

# Import MovieBoardsDigital.csv as a DataFrame. Replace the values in the 'Date' and 'Time' columns with a datetime objects.
movie_csv = pd.read_csv('MovieBoardsDigital.csv', parse_dates=['Date','Time'])

# Create new DataFrame where values are sorted by the Date column. Dates and times are 
sorted_by_date = movie_csv.sort_values(['Date','Time'])
sorted_by_date['Date Seen'] = sorted_by_date['Date'].dt.date
sorted_by_date['Show Time'] = sorted_by_date['Time'].dt.time

# Create dictionary to be used to create a menu for user input.
menu_options = {1 : 'Movie Lookup', 2 : "Most Recent Movie", 3 : "Number of Movies Watched in a Year",
                4 : 'Movies by Start Time', 5 : 'Suggest a Movie', 6 : 'Random Ticket'}

# common variable for menu prompt
back = "'B' to go back to the main menu.\n"



# Format and print the menu options.
def menu():
    menu_values = []
    for item in menu_options.values():
        menu_values.append(len(item)) 

    max_value_length = (max(menu_values) + 10)
    header = '=' * max_value_length
    print(header) 

    for key in menu_options:
        x = max_value_length - len(menu_options[key]) - 3
        print(key,"." * (x),menu_options[key])    

    print(header)
    

def info_by_title(movie_check):
    movie_lower = movie_check.lower()

    # Find index key for input and return values of some other columns with that same index key
    input_index = pd.Index(sorted_by_date['Title'].str.lower()).get_loc(movie_lower)
    index_values = sorted_by_date.drop(['Year', 'Time', 'Date', 'Saw with April'], axis=1).iloc[input_index]
    print(f"\nJared has ticket info for '{movie_check}'.\nHere are the deets:\n\n{index_values.to_string(index=False)}\n")


# Function to look up a user input in the 'Title' column of the DataFrame. 
def movie_lookup():
    
    while True:
        movie_check = input(f"\nEnter a movie title to check for ticket info or {back}")
        movie_lower = movie_check.lower()

        if movie_lower == 'b':
            break
        elif movie_lower in movie_csv['Title'].str.lower().values:
            info_by_title(movie_check)
            logging.info(f'Valid   - {movie_check}')
        else:
            print(f"\nThere is no ticket info for '{movie_check}'.")       
            logging.info(f'Invalid - {movie_check}')



 # Function that looks up and returns the last value in 'Title' and 'Year' columns from the 'sorted_by_date' DataFrame. 
def most_recent():
    recent_movie = sorted_by_date['Title'].iloc[-1]
    most_recent_date = sorted_by_date['Date'].iloc[-1]

    #Days between current date and date of last movie seen
    num_days_ago = pd.Timestamp.today() - most_recent_date
    print(f"\nThe most recent movie on record was'{recent_movie}'. Seen {num_days_ago.days} days ago on {most_recent_date.date()} at {sorted_by_date['Theater'].iloc[-1]}. \n")



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
        year_input = input(f"\nEnter a year 2012-2021 or {back}")
        if year_input in by_year_dict:
            print(f"\nJared saw {by_year_dict[year_input]} movies in {year_input}")
            logging.info(f'{year_input}')
        elif year_input.lower() == 'b':
            break
        elif year_input not in by_year_dict:
            print(f"\nInformation for {year_input} could not be found.")


      
# Produce a chart to show how many movies were show in a 3 hour block
def by_time_chart():

    # Resample time column into 3 hour blocks starting with 00:00 AM
    resampled_csv = movie_csv.resample('3H', on='Time').count()
    
    time_chart_x = ['12a-2:59a', '3a-5:59a', '6a-8:59a', '9a-11:59a', '12p-2:59p', '3p-5:59p', '6p-8:59p', '9p-11:59p']
    time_chart_y = []    

    for value in resampled_csv['Time']:
        time_chart_y.append(value)
    
    print('\nPlease close all charts to continue.\n')

    # Plot bar chart of # of movies seen by time
    plt.figure(figsize=(10.5,5))
    plt.bar_label(plt.bar(time_chart_x,time_chart_y, label='# Of Movies', color='#FFA500', edgecolor='000000'))
    plt.xlabel('Show Time Window')
    plt.ylabel('# of Movies')
    plt.title('# of Movies Watched by Show Time')         
    plt.show()

         

# Function that logs user input of suggestion
def movie_suggestion():
    while True:
        suggestion = input(f"\nEnter a movie suggestion or {back}")
        suggestion_lower = suggestion.lower()
        if suggestion_lower == 'b':
            break
        elif suggestion_lower in movie_csv['Title'].str.lower().values:
            print(f"We've already seen '{suggestion}'")
        else:
            logging.info(f'{suggestion}')
            print("Thank's for the suggestion!")



def movie_random():
      
    movie_check = random.choice(sorted_by_date['Title'])
    info_by_title(movie_check)



# Run the main menu
def main():
    print("\n\n\nLet's all go to the lobby!")
    while True:     
        menu() 
        menu_choice = input(f"Enter an option 1-{list(menu_options.keys())[-1]} or 'Q' to quit.\n")
        if menu_choice == '1':
            movie_lookup()
        elif menu_choice == '2':
            most_recent()
        elif menu_choice == '3':
            movie_by_year()
        elif menu_choice == '4':
            by_time_chart()
        elif menu_choice == '5':
            movie_suggestion()
        elif menu_choice == '6':
            movie_random()
        elif menu_choice.lower() == 'q':
            print("\nSee you real soon!\n")
            break
        else:
            print(f"\n{menu_choice} was not a valid option. Enter an option 1-4 or 'Q' to quit.\n")
            
        
        
if __name__ == "__main__":
    main()      





