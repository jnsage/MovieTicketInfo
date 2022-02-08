import csv
import pandas

#import the csv as a dataframe
movie_csv = pandas.read_csv('MovieBoardsDigital.csv')

# initialize empty list and nested dictionary
# year_list = []
# nested = {'Y': None, 'N': None}
        
# group number of times I did or didn't see a movie with April by Year
# year_count = movie_csv.groupby(['Year', 'Saw with April'])[['Title']].count()
# print(year_count)
    
#add # of years to an empty list
# for year in movie_csv['Year'].unique():
    # year_list.append(year)

# add unique years as dictionary key with nested dict as keys
# year_dict = dict.fromkeys(year_list, nested)
# print(year_dict)
menu = {1 : 'Look up a movie', 2 : "See the last movie watched" }
print(menu)

# Look up a movie in the data frame
def movie_lookup():
    while True:
        movie_check = input("Enter a movie to see if Jared has seen it. Enter 'B' to go back to the main menu\n")
        if movie_check.lower() == 'B':
            break
        elif movie_check in movie_csv['Title'].values():
            print(f"Jared has seen {movie_check}.\n")
        else:
            print(f"Jared hasn't seen {movie_check}\n")    
    

 # Sort csv by date and look up last title and last year
def most_recent():
    sorted_by_date = movie_csv.sort_values('Date')
    recent_movie = sorted_by_date['Title'].iloc[-1]
    recent_year = sorted_by_date['Year'].iloc[-1]
    print(f"The last movie Jared saw was {recent_movie} in {recent_year}")


while True:
    menu_choice = input("Enter an Option 1 or 2\n")
    if menu_choice == '1':
        movie_lookup()
    elif menu_choice == '2':
        most_recent()
    if menu_choice.lower() == 'q':
        break
    else:
        print("please enter option 1-2 or enter Q to quit")

        

print("\nThank you for checking in! Have a nice day")




