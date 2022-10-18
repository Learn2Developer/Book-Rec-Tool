# Book Recommendation Tool
import random
import csv
import datetime


def try_parsing_date(text):
    for fmt in ("%m/%d/%y", "%Y-%m-%d", "%d.%m.%Y", "%d/%m/%y", "%Y", ""):
        try:
            return datetime.datetime.strptime(text, fmt)
        except ValueError:
            pass
    raise ValueError("no valid date format found")


search_list = []
file = open("Best_Books_Ever.csv")

type(file)

csvreader = csv.reader(file)
header = []
header = next(csvreader)
# print(header)

rows = []
for row in csvreader:
    rows.append(row)


# classics = [genre_search("Classics")]
# print(classics)

# Book list create functions
books_dict = {}
books_list = []
for n in range(len(rows) - 1):
    books_dict["book_name"] = rows[n][1]
    books_dict["author"] = rows[n][3]
    books_dict["rating"] = rows[n][4]
    books_dict["description"] = rows[n][5]
    books_dict["language"] = rows[n][6]
    genres = []
    genre_str = rows[n][8]
    genre_str = genre_str.strip(" ")
    genre_str = genre_str[2:-2]
    genre_list = genre_str.split("', '")
    for each in genre_list:
        genres.append(each)
    books_dict["genres"] = genres
    books_dict["pages"] = rows[n][12]
    books_dict["year"] = rows[n][15]
    books_dict["num_ratings"] = rows[n][17]
    books_dict["liked_percent"] = rows[n][19]
    books_list.append(books_dict)
    books_dict = {}
genre_list = books_list

# Language Functions
def language_list():
    languages = []
    for n in range(len(rows) - 1):
        languages.append(rows[n][6])
    return languages


def default_lang():
    default_lang = "English"
    return default_lang


def languages_sorted():
    set_of_langs = set(language_list())
    set_of_langs = sorted(set_of_langs)
    return set_of_langs


def popular_langs():
    popular_langs = {}
    lang_list = language_list()
    sorted_languages = languages_sorted()
    for lang in sorted_languages:
        popular_langs[lang] = lang_list.count(lang)
    return popular_langs.items()


def language():
    for n in range(len(rows) - 1):
        if "Jap" in rows[n][6]:
            print(rows[n][1])


# Rating Function
def min_rating(length_list_complete):
    rating_choice = float(
        input(
            "What is the minimum rating for a book that you would read? (decimal between 0.0-5.0): "
        )
    )
    while type(rating_choice) != "float" and (rating_choice > 5 or rating_choice < 0):
        rating_choice = input("Please enter a decimal between 0.0 and 5.0: ")
    rating_list = []
    for book in length_list_complete:
        if float(book["rating"]) > rating_choice:
            rating_list.append(book)

    return rating_list


# Year Function
def year_search(genre_list):
    year = input(
        "How recent was the book published? (type year of oldest disreable result): "
    )
    while year not in "0123456789":
        year = input("Please type a year: ")
        pass


# Genre Functions
def genres():
    genres = []
    for n in range(len(rows) - 1):
        genre_str = rows[n][8]
        genre_str = genre_str.strip(" ")
        genre_str = genre_str[2:-2]
        genre_list = genre_str.split("', '")
        for each in genre_list:
            genres.append(each)
    genres = set(genres)
    genres = sorted(genres)
    return genres


def genre_search(genre, genre_list):
    genre_search_list = []
    for n in range(len(genre_list) - 1):
        if genre in genre_list[n]["genres"] and genre_list[n]["language"] == "English":
            genre_search_list.append(genre_list[n])
    return genre_search_list


def genre_choice_search(genre_choice, genre_list):
    while genre_choice not in genres:
        if genre_choice == "help":
            print(genres)
        genre_choice = input(
            "Please choose a genre or type 'help' for a full list of options: "
        )
    print("\nShowing books in category: {}\n".format(genre_choice))
    genre_list_new = genre_search(genre_choice, genre_list)
    for genre in genre_list_new:
        print(genre["book_name"])

    genre_search_again = input(
        "Would you like to add another genre to the search? (y/n): "
    )
    while genre_search_again not in "yn":
        genre_search_again = input("I'm sorry, please choose yes or no. (y/n): ")

    if genre_search_again == "y":
        # print(genre_list_new)
        genre_choice_new = input(
            "What other genre would you list to add? (type help for a full list of genres): "
        )
        genre_choice_search(genre_choice_new, genre_list_new)

    return genre_list_new


# Book Summary Function
def book_summary(book_list):
    summary_choice = input(
        "Which book would you like to read the summary for? (Please type the book name): "
    )
    for book in book_list:
        if summary_choice == book["book_name"]:
            print("\n" + book["description"] + "\n")

    summary_again = input("Would you like to see the summary for another book? (y/n): ")
    while summary_again not in "yn":
        summary_again = input("Please choose y or n: ")
    if summary_again == "y":
        book_summary(book_list)


# Book Length Function
def book_length(list_choice):
    length_list = []
    length_choice = input(
        "How long would you like the book to be? \nAny, Short, Medium, Long, or Epic? (a/s/m/l/e): "
    )
    while length_choice not in "asmle":
        length_choice = input(
            "Sorry, please choose a book length. Any, Short, Medium, Long, or Epic? (a/s/m/l/e): "
        )

    if length_choice == "a":
        return list_choice
    elif length_choice == "s":
        for book in list_choice:
            if book["pages"] is None or book["pages"] == "":
                print(book["book_name"] + " pages col is None or ''.")
                length_list.append(book)
            elif int(book["pages"]) < 300:
                print(book["book_name"] + " is less than 300 Pages.")
                length_list.append(book)
    elif length_choice == "m":
        for book in list_choice:
            if book["pages"] is None or book["pages"] == "":
                print(book["book_name"] + " pages col is None or ''.")
                length_list.append(book)
            elif int(book["pages"]) >= 300 and int(book["pages"]) < 500:
                print(book["book_name"] + " is between 300 and 500 Pages.")
                length_list.append(book)
    elif length_choice == "l":
        for book in list_choice:
            if book["pages"] is None or book["pages"] == "":
                print(book["book_name"] + " pages col is None or ''.")
                length_list.append(book)
            elif int(book["pages"]) >= 500 and int(book["pages"]) < 700:
                print(book["book_name"] + " is between 500 and 700 pages.")
                length_list.append(book)
    elif length_choice == "e":
        for book in list_choice:
            if book["pages"] is None or book["pages"] == "":
                print(book["book_name"] + " pages col is None or ''.")
                length_list.append(book)
            elif int(book["pages"]) >= 700:
                print(book["book_name"] + " is over 700 pages.")
                length_list.append(book)
    return length_list


genres = genres()
# print(random.choice(genres))

print("Hello and welcome to BookRec 0.1v!\n")
genre_choice = input(
    "First off, what genre would you like to search for? (type help for a full list of genres): "
)
genre_list_complete = genre_choice_search(genre_choice, genre_list)

length_list_complete = book_length(genre_list_complete)
rating_list_complete = min_rating(length_list_complete)
for book in rating_list_complete:
    print(book["book_name"])
book_summary(rating_list_complete)
