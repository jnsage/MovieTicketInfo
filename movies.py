import csv
import pandas

#import the csv as a dataframe
movie_csv = pandas.read_csv('MovieBoardsDigital.csv')


# Look up a movie in the data frame
def movie_lookup():
    while True:
        movie_check = input("Enter a movie to see if Jared has seen it. Press 'Q' to Quit\n")
        if movie_check.lower() == 'q':
            break
        elif movie_check.casefold() in movie_csv['Title'].values:
            print(f"Jared has seen {movie_check}\n")       
        else:
            print(f"Jared hasn't seen {movie_check}.\n")    
    
movie_lookup()

print('\nThank you for checking in! Have a nice day')



# movie_dict = movie_csv.values()

# for items in movie_dict:
#     print(items)
    

# import csv as dictionary and print movie name
# with open('MovieBoardsDigital.csv', newline='') as csv_file:
#     movie_file = csv.DictReader(csv_file)
#     for row in movie_file:
#         print(row['Title'])
