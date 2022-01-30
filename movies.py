import csv
import pandas

movie_csv = pandas.read_csv('MovieBoardsDigital.csv')

while True:
    movie_check = input("Enter a movie to see if Jared has seen it. Press 'Q' to Quit\n")
    if movie_check == 'Q':
        break
    elif movie_check in movie_csv['Title'].values:
        print(f"Jared has seen {movie_check}")       
    else:
        print(f"Jared hasn't seen {movie_check}.")
    


print('Thank you for checking in! Have a nice day')



# movie_dict = movie_csv.values()

# for items in movie_dict:
#     print(items)
    

# import csv as dictionary and print movie name
# with open('MovieBoardsDigital.csv', newline='') as csv_file:
#     movie_file = csv.DictReader(csv_file)
#     for row in movie_file:
#         print(row['Title'])
