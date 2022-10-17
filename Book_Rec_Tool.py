# Book Recommendation Tool
import random
import csv
import datetime


def try_parsing_date(text):
    for fmt in ("%m/%d/%y", "%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%Y", ""):
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
    try:
        books_dict["year"] = try_parsing_date(rows[n][15])
    except ValueError:
        books_dict["year"] = try_parsing_date(rows[n][14])
    print(books_dict["year"])
    books_dict["num_ratings"] = rows[n][17]
    books_dict["liked_percent"] = rows[n][19]
    books_list.append(books_dict)
    books_dict = {}


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


def year_search(genre_list):
    year = input(
        "How recent was the book published? (type year of oldest disreable result): "
    )
    while year not in "0123456789":
        year = input("Please type a year: ")


# print(languages_sorted())

# print(popular_langs())


# Think of questions to narrow list of books down...
# Like, what genres are you interested in?
# Give them a list of genres!


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


def genre_search(genre, genre_list=None):
    genre_search_list = []
    if genre_list == None:
        for n in range(len(rows) - 1):
            if genre in books_list[n]["genres"] and (
                books_list[n]["language"] == default_lang()
                or books_list[n]["language"] == ""
            ):
                genre_search_list.append(books_list[n])
    else:
        genre_search_list = []
        for n in range(len(genre_list) - 1):
            if genre in genre_list[n]["genres"]:
                genre_search_list.append(genre_list[n])

    return genre_search_list


genres = genres()
# print(random.choice(genres))


def genre_choice_search(genre_choice, genre_list=None):
    while genre_choice not in genres:
        if genre_choice == "help":
            print(genres)
        genre_choice = input(
            "Please choose a genre or type 'help' for a full list of options: "
        )
    print("\nShowing books in category: {}\n".format(genre_choice))
    if genre_list == None:
        print("Genre list is None")
        genre_list = genre_search(genre_choice)
        for genre in genre_list:
            print(genre["book_name"])
    else:
        print("Genre list already exists!")
        genre_list = genre_search(genre_choice, genre_list)
        for genre in genre_list:
            print(genre["book_name"])

    genre_search_again = input(
        "Would you like to add another genre to the search? (y/n): "
    )
    while genre_search_again not in "yn":
        genre_search_again = input("I'm sorry, please choose yes or no. (y/n): ")

    if genre_search_again == "y":
        print(genre_list)
        genre_choice_new = input(
            "What other genre would you list to add? (type help for a full list of genres): "
        )
        genre_choice_search(genre_choice_new, genre_list)


for n in range(len(books_list) - 1):
    print(books_list[n]["year"])

print("Hello and welcome to BookRec 0.1v!\n")
genre_choice = input(
    "First off, what genre would you like to search for? (type help for a full list of genres): "
)
genre_choice_search(genre_choice)
