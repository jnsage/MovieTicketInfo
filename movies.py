import pandas as pd



# Import MovieBoardsDigital.csv as a DataFrame. Replace the values in the 'Date' column with a datetime object.

movie_csv = pd.read_csv('MovieBoardsDigital.csv', parse_dates=['Date'])


# Create new DataFrame where values are sorted by the Date column. This will be used later in 'most_recent()' and 'movie_by_year()' functions.
sorted_by_date = movie_csv.sort_values('Date')


# Create dictionary to be used to create a menu for user input.
menu = {1 : 'Movie Check', 2 : "Most Recent Movie", 3 : "Number of movies watched in a year"}


# Function to look up a user input in the 'Title' column of the DataFrame. Returns affirmative messaging if input is in 'Title'.
# Returns negative statement if input is not in 'Title'
def movie_lookup():
   
    while True:
        movie_check = input("Enter a movie to check if Jared saw it in theaters.\nEnter 'B' to go back to the main menu\n")
        if movie_check.lower() == 'b':
            break
        elif movie_check.lower() in movie_csv['Title'].str.lower().values:
            print(f"Jared has seen {movie_check}\n")
        else:
            print(f"Jared hasn't seen {movie_check}\n")    
    

 # Function that looks up and returns the last value in 'Title' and 'Year' columns from the 'sorted_by_date' DataFrame. 
 # No user input required. Should only return one value.
def most_recent():
    recent_movie = sorted_by_date['Title'].iloc[-1]
    recent_date = sorted_by_date['Date'].iloc[-1]

    #Days between current date and date of last movie seen
    num_days_ago = pd.Timestamp.today() - recent_date
    
    print(f"The last movie Jared saw was {recent_movie}. He saw it {num_days_ago.days} days ago on {recent_date.date()}. \n")

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
        year_input = input("Enter a year between 2012 and 2021.\nEnter 'B' to go back to the main menu\n")
        if year_input in by_year_dict:
            print(f"Jared saw {by_year_dict[year_input]} movies in {year_input}\n")
        elif year_input.lower() == 'b':
            break
        elif year_input not in by_year_dict:
            print(f"{year_input} can't be found. Enter a year between 2012 and 2021.\nEnter 'B' to go back to the main\n")
      
# Function for the main menu seen by the user.
def main():
    while True:
        print(f"{menu}\n")
        menu_choice = input("Enter an option 1-3. Enter Q to quit\n")
        if menu_choice == '1':
            movie_lookup()
        elif menu_choice == '2':
            most_recent()
        elif menu_choice == '3':
            movie_by_year()
        elif menu_choice.lower() == 'q':
            break
        else:
            print(f'{menu_choice} is not a valid option.\n')
        

main()       

print("\nThank you for checking in! Have a nice day")




