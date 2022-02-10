import csv
import pandas

#import the csv as a dataframe
movie_csv = pandas.read_csv('MovieBoardsDigital.csv')
movie_csv['Date'] = pandas.to_datetime(movie_csv['Date'])
sorted_by_date = movie_csv.sort_values('Date')


menu = {1 : 'Movie Check', 2 : "Most Recent Movie", 3 : "Movies Watched by Year"}

# Look up a movie in the data frame
def movie_lookup():
    while True:
        movie_check = input("Enter a movie to see if Jared has seen it. Enter 'B' to go back to the main menu\n")
        if movie_check.lower() == 'b':
            break
        elif movie_check in movie_csv['Title'].values:
            print(f"Jared has seen {movie_check}.\n")
        else:
            print(f"Jared hasn't seen {movie_check}\n")    
    

 # Convert Date column to date time abd sort csv by date. Return last entry of title and year.
def most_recent():
    recent_movie = sorted_by_date['Title'].iloc[-1]
    recent_year = sorted_by_date['Year'].iloc[-1]
    print(f"The last movie Jared saw was {recent_movie} in {recent_year}\n")

def movie_by_year():

    # initialize empty lists and a dictionary
    year_count = []
    movie_count = []
    by_year_dict = {}
    
    # add years from year column to list 1, add value counts from year to list 2.
    # convert year to string for input retrieval
    for item in sorted_by_date['Year'].unique():
        year_count.append(item)
    for value in sorted_by_date['Year'].value_counts(sort=False):
        movie_count.append(value)
    print(sorted_by_date['Year'].value_counts(sort=False))
   
   
    # populate dictionary using 2 lists with year as the key and count as the value
    by_year_dict = dict(zip(year_count, movie_count))


    # have user enter a year, return count if present
    while True: 
        year_input = input("Enter a year between 2012 and 2021. Enter 'B' to go back to the main menu\n")
        if year_input in by_year_dict:
            print(f"Jared saw {by_year_dict[year_input]} movies in {year_input}\n")
        elif year_input.lower() == 'b':
            break
        elif year_input not in by_year_dict:
            print("That's not a valid year. Enter a year between 2012 and 2021. Enter 'B' to go back to the main\n")
        else:
            print("Enter another year between 2012 and 2021. Enter 'B' to go back to the main menu\n")
    


while True:
    print(f"{menu}\n")
    menu_choice = input("Please enter option an option 1-3. Enter Q to quit\n")
    if menu_choice == '1':
        movie_lookup()
    elif menu_choice == '2':
        most_recent()
    elif menu_choice == '3':
        movie_by_year()
    elif menu_choice.lower() == 'q':
        break
    else:
        continue

        

print("\nThank you for checking in! Have a nice day")




